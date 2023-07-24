
const form = document.getElementById('form');
form.addEventListener('submit', function(e) {
  const email = form.email.value;
  const conf = form.email_confirm.value;
  console.log(email, conf)
  if(email !== conf){
    e.preventDefault();
    const element = document.createElement("p")
    const msg = document.createTextNode("No coinciden los emails")
    element.classList.toggle("alert")
    element.appendChild(msg)
    form.appendChild(element)
    setTimeout(() => {
      element.style.display = "none"
    }, 3000);
  } else{
    form.submit();
  }
});
form.addEventListener('onchange', function(e) {
  const email = form.email.value;
  const conf = form.email_confirm.value;
  console.log(email, conf)
});