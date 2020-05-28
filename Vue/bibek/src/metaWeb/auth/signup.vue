<template>
  <div>
    <Header />
    <section id="login">
      <div class="container mt-3 mb-3">
        <div class="row">
          <div class="col-md-6 mx-auto">
            <div class="card">
              <div class="card-header">
                <h4>Register Form</h4>
                <p class="error">{{error}}</p>
              </div>
              <div class="card-body">
                <form @submit.prevent="signUp">
                  <div class="form-group" :class="{invalid:$v.username.$error}">
                    <label for="name">Username</label>
                    <input
                      @blur="$v.username.$touch()"
                      type="text"
                      class="form-control"
                      v-model="username"
                    />
                  </div>
                  <div class="form-group" :class="{invalid:$v.email.$error}">
                    <label for="name">Email</label>
                    <input
                      type="email"
                      id="email"
                      class="form-control"
                      @blur="$v.email.$touch()"
                      v-model="email"
                    />
                    <!-- <div v-if="!$v.email.email">please provide valid email address</div> -->
                  </div>
                  <div class="form-group" :class="{invalid:$v.password1.$error}">
                    <label for="name">password</label>
                    <input
                      type="password"
                      @blur="$v.password1.$touch()"
                      class="form-control"
                      v-model="password1"
                    />
                  </div>
                  <div class="form-group" :class="{invalid:$v.password2.$error}">
                    <label for="name">Confirm Password</label>
                    <input
                      type="password"
                      @blur="$v.password2.$touch()"
                      class="form-control"
                      v-model="password2"
                    />
                  </div>
                  <button :disabled="$v.$invalid" type="submit"  class="btn btn-success btn-block">Register</button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <Footer />
  </div>
</template>
<script>
import Footer from "../../metaWeb/home/footer";
import Header from "./headerAuth";
import {
  required,
  email,
  maxLength,
  minLength,
  sameAs
} from "vuelidate/lib/validators";

export default {
  components: {
    Footer,
    Header
  },
  data() {
    return {
      username: "",
      email: "",
      password1: "",
      password2: "",
      error: ""
    };
  },
  validations: {
    email: {
      required,
      email
    },
    username: {
      required,
      maxLength: maxLength(10)
    },
    password1: {
      required,
      minLength: minLength(6)
    },
    password2: {
      sameAs: sameAs("password1")
    }
  },
  methods: {
    async signUp() {
      await this.$store.dispatch("signUp", {
        username: this.username,
        password1: this.password1,
        password2: this.password2,
        email: this.email
      });
      const error = this.$store.getters.getError;
      if (error) {
        this.error = "Username or email already exists";
      } else {
        this.$router.push("/dashboard");
      }
    }
  }
};
</script>
<style scoped>
.error {
  color: red;
  text-align: center;
}
.invalid label {
  color: red;
}
.invalid input {
  border: 1px solid red;
  background-color: #ffc9aa;
}
</style>
