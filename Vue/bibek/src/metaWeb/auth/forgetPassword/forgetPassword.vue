<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-4"></div>
        <div class="col-md-4 main">
          <div class="card text-center mt-5">
            <div class="card-body">
              <h3>
                <i class="fa fa-lock fa-4x"></i>
              </h3>
              <div v-if="spinner" class="lds-roller">
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
              </div>
              <h2 class="text-center">Forgot Password?</h2>
              <p>You can reset your password here.Enter the email associated with your account.Email with verification token will be sent to your email.</p>
              <form @submit.prevent="submitDone">
                <div
                  class="input-group input-group-md mb-3 mt-3"
                  :class="{invalid:$v.email.$error}"
                >
                  <div class="input-group-prepend">
                    <span class="input-group-text">
                      <i class="fas fa-envelope"></i>
                    </span>
                  </div>
                  <input
                    @input="$v.email.$touch()"
                    v-model="email"
                    type="text"
                    class="form-control"
                    placeholder="Enter Your Email"
                  />
                </div>
                <div v-if="$v.email.$error" class="error">Enter valid email</div>
                <div class="error">{{error}}</div>

                <button
                  :disabled="$v.$invalid"
                  class="btn btn-block bg-success text-white btn-large button"
                >search</button>
              </form>
            </div>
          </div>
        </div>
        <div class="col-md-3"></div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { required, email } from "vuelidate/lib/validators";
export default {
  data() {
    return {
      email: "",
      error: "",
      spinner:false
    };
  },
  validations: {
    email: {
      required,
      email
    }
  },
  methods: {
    submitDone() {
      this.spinner = true
      axios
        .post("http://localhost:8000/api/password_reset/", {
          email: this.email
        })
        .then(res => {
          this.$router.push("/new-password/" + this.email);
        })
        .catch(err => {
          this.error = "This email in not associated with any account";
        });
    }
  }
};
</script>
<style scoped>
input:focus,
input.form-control:focus {
  outline: none !important;
  outline-width: 0 !important;
  box-shadow: none;
}
.invalid input {
  
  background-color: #ffc9aa;
}
.error {
  font-size: 12px;
  color: red;
  margin-bottom: 2px;
}
.lds-roller {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-roller div {
  animation: lds-roller 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
  transform-origin: 40px 40px;
}
.lds-roller div:after {
  content: " ";
  display: block;
  position: absolute;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: black;
  margin: -4px 0 0 -4px;
}
.lds-roller div:nth-child(1) {
  animation-delay: -0.036s;
}
.lds-roller div:nth-child(1):after {
  top: 63px;
  left: 63px;
}
.lds-roller div:nth-child(2) {
  animation-delay: -0.072s;
}
.lds-roller div:nth-child(2):after {
  top: 68px;
  left: 56px;
}
.lds-roller div:nth-child(3) {
  animation-delay: -0.108s;
}
.lds-roller div:nth-child(3):after {
  top: 71px;
  left: 48px;
}
.lds-roller div:nth-child(4) {
  animation-delay: -0.144s;
}
.lds-roller div:nth-child(4):after {
  top: 72px;
  left: 40px;
}
.lds-roller div:nth-child(5) {
  animation-delay: -0.18s;
}
.lds-roller div:nth-child(5):after {
  top: 71px;
  left: 32px;
}
.lds-roller div:nth-child(6) {
  animation-delay: -0.216s;
}
.lds-roller div:nth-child(6):after {
  top: 68px;
  left: 24px;
}
.lds-roller div:nth-child(7) {
  animation-delay: -0.252s;
}
.lds-roller div:nth-child(7):after {
  top: 63px;
  left: 17px;
}
.lds-roller div:nth-child(8) {
  animation-delay: -0.288s;
}
.lds-roller div:nth-child(8):after {
  top: 56px;
  left: 12px;
}
@keyframes lds-roller {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>