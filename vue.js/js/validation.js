// Registro de componentes
Vue.component('common-modal', {
    template: `
    <div class="modal_back">
      <div class="modal_body">
        <p class="modal_sign">Error.</p>
        <p class="alert_color">{{ message }}</p>
        <button @click="closeModal">close</button>
      </div>
    </div>`,
    props: {
        message: String,
    },
    methods: {
        closeModal(){
          this.$emit('close');
        }
    }
  })
  

//registro de objetos
const app = new Vue({
    el: '#app',
    data: {
      errorMessage: 'Correo electrónico no coincidente.',
      errorMessage2: 'Completa el campo de confirmacion de email.',
      formData: {
        name: '',
        email: '',
        emailConfirm: '',
        content: ''
      },
      regions: [
        "America",
        "Asia",
        "Sudamerica",
        "Africa"
      ],
      confirmView: false,
      modalView: false,
    },

    methods: {
        openCheckArea(){
            if (!this.validation) {
                this.showModal();
            } else{
                this.confirmView = true;
            } 
        },
        closeCheckArea() {
            this.confirmView = false;
          },
        showModal() {
            this.modalView = true;
          },
        hideModal() {
            this.modalView = false;
          },
    },
    computed: {
        validation: function() {
            return this.formData.email === '' || this.formData.emailConfirm === '' || this.formData.email === this.formData.emailConfirm
        },
        empty: function() {
            return this.formData.emailConfirm === '' && this.formData.email
        },
        errorClass: function() {
            return this.validation ? false : 'alert_bg';
          }
      },
  })
