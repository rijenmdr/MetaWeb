<template>
  <div>
    <div class="container h-100 loginMain">
      <div class="d-flex justify-content-center h-100">
        <div class="user_card">
          <div class="d-flex justify-content-center">
            <div class="brand_logo_container">
              <img src="../../../assets/mlogo.png" class="brand_logo" alt="Logo" />
            </div>
          </div>

          <div class="d-flex justify-content-center form_container">
            <form @submit.prevent="login">
              <div class="input-group mb-3 error">{{error}}</div>
              <div class="input-group mb-3">
                <div class="input-group-append">
                  <span class="input-group-text">
                    <i class="fas fa-user"></i>
                  </span>
                </div>
                <input
                  type="text"
                  name
                  class="form-control input_user"
                  value
                  placeholder="username"
                  v-model="username"
                />
              </div>
              <div class="input-group mb-2">
                <div class="input-group-append">
                  <span class="input-group-text">
                    <i class="fas fa-key"></i>
                  </span>
                </div>
                <input
                  type="password"
                  name
                  class="form-control input_pass"
                  value
                  placeholder="password"
                  v-model="password"
                />
              </div>
              <div class="form-group">
                <div class="custom-control custom-checkbox">
                  <input
                    type="checkbox"
                    class="custom-control-input"
                    id="customControlInline"
                    v-model="remember"
                  />
                  <label class="custom-control-label" for="customControlInline">Remember me</label>
                </div>
              </div>
              <div class="d-flex justify-content-center mt-3 login_container">
                <button type="submit" name="button" class="btn login_btn">Login</button>
              </div>
            </form>
          </div>

          <div class="mt-4">
            <div class="d-flex justify-content-center links">
              Don't have an account?
              <router-link class="ml-2" to="/signup">Sign Up</router-link>
            </div>
            <div class="d-flex justify-content-center links">
              <router-link to="/login/reset-password">Forgot your password?</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      username: null,
      password: null,
      error: "",
      remember: ""
    };
  },

  methods: {
    async login() {
      await this.$store.dispatch("Login", {
        username: this.username,
        password: this.password,
        remember: this.remember
      });

      const error = this.$store.getters.getError;
      console.log(this.$store.getters.getUser);
      if (error) {
        this.error = "Username and Password didn't match";
      } else {
        this.$router.push("/dashboard");
      }
    }
  },
  created() {
    const token = localStorage.getItem("token");
    if (!token) {
      return;
    }
    const expirationDate = localStorage.getItem("expiresIn");
    const now = new Date();
    if (now >= expirationDate) {
      return;
    }
    this.$router.push("/dashboard");
  }
};
</script>


<style scoped>
a{
  color:#DAD9D2;
}
body,
html {
  margin: 0;
  padding: 0;
  height: 100%;
  background: #60a3bc !important;
}
.user_card {
  height: 400px;
  width: 350px;
  margin-top: auto;
  margin-bottom: auto;
  background: #51c2cf;
  position: relative;
  display: flex;
  justify-content: center;
  flex-direction: column;
  padding: 10px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  -webkit-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2),
    0 6px 20px 0 rgba(0, 0, 0, 0.19);
  -moz-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2),
    0 6px 20px 0 rgba(0, 0, 0, 0.19);
  border-radius: 5px;
}
.brand_logo_container {
  position: absolute;
  height: 170px;
  width: 170px;
  top: -75px;
  border-radius: 50%;
  background: #60a3bc;
  padding: 10px;
  text-align: center;
}
.brand_logo {
  height: 150px;
  width: 150px;
  border-radius: 50%;
  border: 2px solid white;
}
.form_container {
  margin-top: 100px;
}
.login_btn {
  width: 100%;
  background: #1b838f !important;
  color: white !important;
}
.login_btn:focus {
  box-shadow: none !important;
  outline: 0px !important;
}
.login_container {
  padding: 0 2rem;
}
.input-group-text {
  background: #1b838f !important;
  color: white !important;
  border: 0 !important;
  border-radius: 0.25rem 0 0 0.25rem !important;
}
.input_user,
.input_pass:focus {
  box-shadow: none !important;
  outline: 0px !important;
}
.custom-checkbox .custom-control-input:checked ~ .custom-control-label::before {
  background-color: #c0392b !important;
}
.loginMain {
  margin-top: 5vh;
}
.error {
  color: #963115;
}
</style>