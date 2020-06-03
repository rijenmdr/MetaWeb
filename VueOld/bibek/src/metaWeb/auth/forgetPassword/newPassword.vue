<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-4"></div>
        <div class="col-md-4 main">
          <div class="card text-center mt-5">
            <div class="card-body">
              <h3>
                <i class="fa fa-key fa-4x"></i>
              </h3>
              <h2 class="text-center">Enter new password</h2>
              <p>
                A email was sent to
                <span class="email">{{email}}</span>.Please enter the token provided. Password should be different from username.
              </p>
              <form @submit.prevent="submitDoneNew">
                <div
                  class="input-group input-group-md mb-3 mt-3"
                  :class="{invalid:$v.password.$error}"
                >
                  <div class="input-group-prepend">
                    <span class="input-group-text">
                      <i class="fas fa-user-lock"></i>
                    </span>
                  </div>
                  <input
                    @input="$v.password.$touch()"
                    v-model="password"
                    type="password"
                    class="form-control"
                    placeholder="Enter New Password"
                  />
                </div>
                <div class="input-group input-group-md mb-3 mt-3">
                  <div class="input-group-prepend">
                    <span class="input-group-text">
                      <i class="fas fa-key"></i>
                    </span>
                  </div>
                  <input v-model="token" type="text" class="form-control" placeholder="Enter Token" />
                </div>
                <div v-if="$v.password.$error" class="error">Enter valid email</div>
                <div class="error">{{error}}</div>

                <button
                  :disabled="$v.$invalid"
                  class="btn btn-block bg-success text-white btn-large button"
                >Submit</button>
              </form>
              <router-link to="/login/reset-password">
                <div class="again">Didn't receive email.Resend email again ?</div>
              </router-link>
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
import { required, minLength } from "vuelidate/lib/validators";
export default {
  data() {
    return {
      password: "",
      token: "",
      error: "",
      email: this.$route.params.email
    };
  },
  validations: {
    password: {
      required,
      minLength: minLength(8)
    }
  },
  methods: {
    submitDoneNew() {
      axios
        .post("http://localhost:8000/api/password_reset/confirm/", {
          password: this.password,
          token: this.token
        })
        .then(res => {
          this.$router.push("/login");
        })
        .catch(err => {
          this.error = "Invalid Token or password";
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
  border: 1px solid red;
  background-color: #ffc9aa;
}
.error {
  font-size: 12px;
  color: red;
  margin-bottom: 2px;
}
.email {
  color: blue;
}
.again {
  color: teal;
  font-size: 12px;
}
</style>