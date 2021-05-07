from flask import Flask, render_template,request,session
from datetime import date
import sqlite3
import mysql.connector

app = Flask('app', static_url_path='/static')
app.secret_key = b'mysecretkey'

@app.route('/')
def home():
	if session.get('username'):
		msg = 'welcome %s' % session['username']
	else:
		msg = "You need to login before you add to cart."
	return render_template("index.html",msg=msg)

@app.route('/logout')
def logout():
	session.clear()
	return render_template("login.html")

@app.route('/login',methods=['GET', 'POST'])
def login():
	mydb = mysql.connector.connect(
		host="****", #add host AWS ec2 instance
		user="****",
		password="****",
		database="shoppingCart"
	)
	app.secret_key = b'mysecretkey'
	c = mydb.cursor()
	if request.method == 'POST':
		# Modify this to select the username and password from the database and compare against what the user entered. 
		# Return the loggedin.html page with a custom error message if it doesnt match otherwise dispaly "Welcome <<USERNAME>>"

		# Retrieve the userID and password from the login form
		user = request.form["username"]
		password = request.form["password"]

		# Try to retrieve from the database with the associated credentials
		adr = (user,password,)
		c.execute('''SELECT * FROM people WHERE loginId = %s AND pass = %s''',adr)
		results = c.fetchone()
		
		# Check to see if the database returned a user or not
		if results is None:
			# Could add a return to home button in order to prevent having to reload the pages
			return "Invalid credentials"
		
		# Assume that the user is in the database - make a message that incorporates the userID
		session.clear()
		msg = "Welcome %s" % user
		session['username'] = user
		print(session['username'])
		return render_template('index.html',msg=msg)

	#Render the loggedin template.
	return render_template('login.html')

@app.route('/register',methods=['GET', 'POST'])
def register():
	c = mydb.cursor()
	if request.method == 'POST':
		## Modify this to connect to the database and insert a new users with fields from the form. 
		# Return the registered.html page to show success.
			
		# Retrieve all of the info from the registration form
		# A next step could be to error check to make sure that all of the fields have been entered
		name = request.form["Name"]
		email = request.form["Email"]
		user = request.form["Username"]
		password = request.form["Password"]
		session.clear()
		session['username'] = user
		# Insert the values into the database as a new user
		c.execute("""INSERT INTO people VALUES (%s, %s, %s, %s)""",[name,user,email,password])
		mydb.commit()

		return render_template('registered.html')

	## Otherwise return register page on get request
	return render_template('register.html')

@app.route('/search',methods=['GET', 'POST'])
def search():
	app.secret_key = b'mysecretkey'
	c = mydb.cursor()

	search = request.form["search"]
	likeSearch =  (('%' + search + '%'),)

	# Try to retrieve from the database with the associated credentials
	c.execute('''SELECT * FROM product WHERE pname LIKE %s''',likeSearch)
	results = c.fetchall()
	
	# Check to see if the database returned a user or not
	if results is None:
		# Could add a return to home button in order to prevent having to reload the pages
		return "No product matches your search term."
	
	# Assume that the user is in the database - make a message that incorporates the userID
	stock = results
	
	return render_template('search.html',stock=stock)

@app.route('/orders',methods=['GET', 'POST'])
def orders():
	app.secret_key = b'mysecretkey'
	c = mydb.cursor()

	# Try to retrieve from the database with the associated credentials
	c.execute('''SELECT * FROM orders WHERE loginID = %s''',(session['username'],))
	results = c.fetchall()
	
	# Check to see if the database returned a user or not
	if results is None:
		# Could add a return to home button in order to prevent having to reload the pages
		return "No order history."
	
	# Assume that the user is in the database - make a message that incorporates the userID
	stock = results
	
	return render_template('orders.html',stock=stock)

@app.route('/orderItem',methods=['GET', 'POST'])
def order_item():
	app.secret_key = b'mysecretkey'
	c = mydb.cursor()

	orderID = request.form['orderID']

	# Try to retrieve from the database with the associated credentials
	c.execute('''SELECT * FROM orderItems WHERE orderID = %s''',(orderID,))
	results = c.fetchall()
	
	# Check to see if the database returned a user or not
	if results is None:
		# Could add a return to home button in order to prevent having to reload the pages
		return "No such order exists."
	
	# Assume that the user is in the database - make a message that incorporates the userID
	stock = results
	
	return render_template('orderItem.html',stock=stock)

@app.route('/cart',methods=['GET', 'POST'])
def cart():
	app.secret_key = b'mysecretkey'
	c = mydb.cursor()
	
	if 'itemID' not in session: 
		session['itemID'] = []
		session['price'] = []
		session['pname'] = []
		session['qty'] = []

	if request.method == 'POST':
		itemID = request.form['itemID']
		qty = request.form['buy']
		price = request.form['price']
		pname = request.form['pname']
		
		itemID_list = session['itemID']
		itemID_list.append(itemID)
		session['itemID'] = itemID_list

		qty_list = session['qty']
		qty_list.append(qty)
		session['qty'] = qty_list

		pname_list = session['pname']
		pname_list.append(pname)
		session['pname'] = pname_list

		price_list = session['price']
		total_price = float(price) * float(qty)
		price_list.append(str(total_price))
		session['price'] = price_list

		print(session['price'])
		print(session['qty'])


		return render_template('cart.html',len=len(session['itemID'])\
		,qty=session['qty'],price=session['price'],\
		pname=session['pname'],pid=session['itemID'])
	
	return render_template('cart.html',len=len(session['itemID'])\
		,qty=session['qty'],price=session['price'],\
		pname=session['pname'],pid=session['itemID'])

@app.route('/del_cart',methods=['GET', 'POST'])
def del_cart():
	app.secret_key = b'mysecretkey'
	c = mydb.cursor()

	if request.method == 'POST':
		session['itemID'] = []
		session['price'] = []
		session['pname'] = []
		session['qty'] = []

	
	return render_template('cart.html',len=len(session['itemID'])\
		,qty=session['qty'],price=session['price'],\
		pname=session['pname'],pid=session['itemID'])

@app.route('/update',methods=['GET', 'POST'])
def update():
	app.secret_key = b'mysecretkey'
	c = mydb.cursor()
	len1 = len(session['itemID'])
	if request.method == 'POST':
		pid = session['itemID']
		qty = session['qty']
		price = session['price']
		date1 = date.today()
		orderID = 0
		orderItem = 0
		order_sum = 0
		for x in range(0,len1):
			order_sum += float(price[x])
		
		c.execute('''SELECT MAX(orderID) FROM orders''')
		result2 = c.fetchone()
		if result2 is not None:
			orderID = int(result2[0]) + 1
		c.execute("""INSERT INTO orders VALUES (%s, %s, %s, %s)"""\
				,[date1,orderID,session['username'],float(order_sum)])
		mydb.commit()
		for i in range(0,len1):
			c.execute('''SELECT MAX(orderItem) FROM orderItems''')
			result = c.fetchone()
			if result is None:
				orderItem = 0
			else:
				orderItem = int(result[0]) + 1
			c.execute("""INSERT INTO orderItems VALUES (%s, %s, %s, %s, %s)"""\
				,[int(orderItem),orderID,int(pid[i]),int(qty[i]),float(price[i])])
			mydb.commit()
			c.execute('''SELECT quantity FROM product WHERE pid = %s''',(pid[i],))
			result3 = c.fetchone()
			update_qty = int(result3[0]) - int(qty[i])
			c.execute('''UPDATE product SET quantity = %s WHERE pid = %s''',(update_qty,pid[i],))
			mydb.commit()
		session['itemID'] = []
		session['price'] = []
		session['qty'] = []

		c.execute('''SELECT * FROM orders WHERE loginID = %s''',(session['username'],))
		results = c.fetchall()
		
		return render_template('orders.html',stock=results)

@app.route('/bath',methods=['GET', 'POST'])
def bath():
	app.secret_key = b'mysecretkey'
	c = mydb.cursor()

	# Try to retrieve from the database with the associated credentials
	c.execute('''SELECT * FROM product WHERE cid = 6''')
	results = c.fetchall()
	
	# Check to see if the database returned a user or not
	if results is None:
		# Could add a return to home button in order to prevent having to reload the pages
		return "Sorry all products are out of stock."
	
	# Assume that the user is in the database - make a message that incorporates the userID
	stock = results
	
	return render_template('bath.html',stock=stock)

@app.route('/body',methods=['GET', 'POST'])
def body():
	app.secret_key = b'mysecretkey'
	c = mydb.cursor()

	# Try to retrieve from the database with the associated credentials
	c.execute('''SELECT * FROM product WHERE cid = 5''')
	results = c.fetchall()
	
	# Check to see if the database returned a user or not
	if results is None:
		# Could add a return to home button in order to prevent having to reload the pages
		return "Sorry all products are out of stock."
	
	# Assume that the user is in the database - make a message that incorporates the userID
	stock = results
	
	return render_template('body.html',stock=stock)

@app.route('/face',methods=['GET', 'POST'])
def face():
	app.secret_key = b'mysecretkey'
	c = mydb.cursor()

	# Try to retrieve from the database with the associated credentials
	c.execute('''SELECT * FROM product WHERE cid = 4''')
	results = c.fetchall()
	
	# Check to see if the database returned a user or not
	if results is None:
		# Could add a return to home button in order to prevent having to reload the pages
		return "Sorry all products are out of stock."
	
	# Assume that the user is in the database - make a message that incorporates the userID
	stock = results
	
	return render_template('face.html',stock=stock)

@app.route('/hair',methods=['GET', 'POST'])
def hair():
	app.secret_key = b'mysecretkey'
	c = mydb.cursor()

	# Try to retrieve from the database with the associated credentials
	c.execute('''SELECT * FROM product WHERE cid = 3''')
	results = c.fetchall()
	
	# Check to see if the database returned a user or not
	if results is None:
		# Could add a return to home button in order to prevent having to reload the pages
		return "Sorry all products are out of stock."
	
	# Assume that the user is in the database - make a message that incorporates the userID
	stock = results
	
	return render_template('hair.html',stock=stock)

@app.route('/makeup',methods=['GET', 'POST'])
def makeup():
	app.secret_key = b'mysecretkey'
	c = mydb.cursor()

	# Try to retrieve from the database with the associated credentials
	c.execute('''SELECT * FROM product WHERE cid = 2''')
	results = c.fetchall()
	
	# Check to see if the database returned a user or not
	if results is None:
		# Could add a return to home button in order to prevent having to reload the pages
		return "Sorry all products are out of stock."
	
	# Assume that the user is in the database - make a message that incorporates the userID
	stock = results
	
	return render_template('makeup.html',stock=stock)

@app.route('/frag',methods=['GET', 'POST'])
def frag():
	app.secret_key = b'mysecretkey'
	c = mydb.cursor()

	# Try to retrieve from the database with the associated credentials
	c.execute('''SELECT * FROM product WHERE cid = 1''')
	results = c.fetchall()
	
	# Check to see if the database returned a user or not
	if results is None:
		# Could add a return to home button in order to prevent having to reload the pages
		return "Sorry all products are out of stock."
	
	# Assume that the user is in the database - make a message that incorporates the userID
	stock = results
	
	return render_template('frag.html',stock=stock)

app.run(host='0.0.0.0', port=8080)
