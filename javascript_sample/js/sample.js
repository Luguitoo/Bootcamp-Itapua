
let compras = []

function calc(){
   //console.log(document.getElementById("product").value)
   let result = 0;
   for (let i = 0; i < compras.length; i++) {
    console.log(compras[i])
    result += compras[i].precio * compras[i].cant;
   }
   //alert(`Total de la orden: ${precio * cant}`)
   alert(`Total de la orden: ${result}`)
   compras = []
}
function add(){
    const precio = parseInt(document.getElementById("product").value)
    const cant = parseInt(document.getElementById("number").value)
    let compra = {
        precio: precio,
        cant: cant
    }
    compras.push(compra)
    console.log(compras)
}