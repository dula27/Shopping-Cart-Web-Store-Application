var cart = [];
function storeOrder(){
    var a = document.getElementById("itemID").value;
    var b = document.getElementById("buy").value;
    var c = document.getElementById("price").value;
    var order = {
        pid: a,
        qty: b,
        price: c
    };
    cart.push(order);
    var string = JSON.stringify(cart);
    sessionStorage.setItem("cart", string);
    var cartValue = sessionStorage.getItem( "cart" );
    var cartObj = JSON.parse( cartValue );
    for (var i in cart) {
        console.log("row " + i);
    }
}