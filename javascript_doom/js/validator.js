const emailbtn = document.getElementById('email');
const confbtn = document.getElementById('email_confirm');

confbtn.addEventListener('input', verificar);

function verificar() {
    let email = emailbtn.value;
    let conf = confbtn.value;
    if (email !== conf){
        errorText.style.display = 'block';
        confbtn.classList.add('error')
    } else{
        errorText.style.display = 'none';
        confbtn.classList.remove('error')
    }
}
