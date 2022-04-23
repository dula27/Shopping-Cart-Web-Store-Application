# Shopping Cart Web App

## Application Requirements
The website should be able to display products being sold in several categories. A user visiting your web store application can search for products (i.e., search for a specific item name and display that item) or display all items in a certain category. The website should display the available quantity for each product.

Only a logged in user can add products to a shopping cart and "buy" various quantities of products by checking out. To "buy" a product means to reduce the quantity from that product with the quantity that was "bought" (i.e. your database should be updated to reflect the reduction in quantity of items after purchase). 

A logged in user shopping cart can be viewed, edited, checked out or deleted. A logged in user can also see his/her orders history if there are any.

## Implementation
- Python Flask will be used for all the server side scripting.
- The cart should be implemented with Session variables. Hint: the session should be based on the user login.
  - This means the shopping cart should *not* be stored in your database.
- Check user input: do not allow me to buy -2 boxes of detergent or, 100 boxes if you only have 1 in stock.
- Keep minimum information about customers: username and password, first and last name. We are not interested in addresses at this point.
- For the base level you can use sqlite as your database, but to earn a perfect score you must use mysql hosted on Amazon Web Services
- For the base level you can use Repl.it to host your python web application, but to earn a perfect score you must run it on AWS.
- If you use AWS you will need to ensure that it is continuously running until we perform grading!
- Where details are not specified in the assignment, you should assume something "reasonable" that you think the client will expect.


- [X] Database schema and scripts to create and populate the tables.
  - [X] This must be kept in the `store_schema.sql` file.
  - [X] Credit will be given for either sqlite or MySQL database syntax.
- [X] Minimal web interface: web page does not look professional, minimal styling, no form checks.
- [X] The user can see all the products the store sells; minimum of 10 products.
- [X] The user can search for a specific item by name.
- [X] The user can see all the products in a specific category; minimum of 3 categories.
- [X] The user can login, but not create a new account.
  - [X] Users who are not in the DB can't login.
  - [X] Must include a sample user named `testuser` with password `testpass`
- [X] The logged in user can view, add to, edit, check out or delete the cart.
- [X] The database is updated when a user buys or checks out.
- [X] The store doesn't let a user buy negative amounts or more than is in the inventory.

- [X] A new user can sign up.
- [X] A logged in user can see his/her previous order history.
- [X] The front end is user friendly: website is easy and intuitive to navigate, no server error messages are presented to to user (if an error occurs, give a user friendly message).
- [X] Website style: products have pictures.

- [X] Database uses MySQL instead of sqlite and Flask web server runs in AWS
- [X] Implement client-side validation for input forms (e.g. quantity added to cart can't be negative) using Javascript.
- [X] The logged in user can sort its orders by date.(Pre sorted orders by date)
- [X] The logged in user can search for a product in his/her past orders.
- [X] Website inspires a professional look: has logo, product descriptions, etc.
