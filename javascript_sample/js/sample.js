let compras = [];

function calc() {
  const result = resultado();
  const envioValue = envio(result);
  alert(`Total de la orden: ${result}. Envío: ${envioValue}`);
  compras = [];
}

function resultado() {
  
  return compras.reduce((prev, compra)=>{
    return prev + compra.precio * compra.cant
  },0);
}

function envio(result) {
  let envio;
  if (result < 2000) {
    envio = 500;
  } else if (result >= 2000 && result < 3000) {
    envio = 250;
  } else {
    envio = 0;
  }
  return envio;
}

function add() {
  const precio = parseInt(document.getElementById("product").value);
  const cant = parseInt(document.getElementById("number").value);
  const productoExistente = compras.find((compra) => compra.precio === precio);

   if (productoExistente) {
    // Si el producto ya existe, simplemente aumentamos la cantidad
    productoExistente.cant += cant;
  } else {
    // Si no existe, lo agregamos al arreglo 'compras'
    let compra = {
      precio: precio,
      cant: cant,
    };
    compras.push(compra);
}
  subtotal = mostrar();
  alert(`${subtotal} Total: ${resultado()}`);
}

function mostrar() {
  return compras.map(compras => {
    return `${compras.precio}- ${compras.cant}`
  }).join("\n");
}