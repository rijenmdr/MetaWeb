<template>
  <section class="section section-shaped section-lg mt-0 mb-0">
    <div class="shape shape-style-1 bg-gradient-default">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
    </div>
    <div class="container pt-lg-1">
      <div class="row justify-content-center">
        <div class="col-lg-5">
          <div class="card bg-secondary shadow border-0">
            <div class="card-header bg-white pb-5">
              <div class="text-muted text-center mb-3">
                <small>Sign in with</small>
              </div>
              <div class="btn-wrapper text-center">
                <a href="#" class="btn btn-neutral btn-icon">
                  <span class="btn-inner--icon">
                    <img src="../../../assets/github.svg" />
                  </span>
                  <span class="btn-inner--text">Github</span>
                </a>
                <a href="#" class="btn btn-neutral btn-icon">
                  <span class="btn-inner--icon">
                    <img src="../../../assets/google.svg" />
                  </span>
                  <span class="btn-inner--text">Google</span>
                </a>
              </div>
            </div>
            <div class="card-body px-lg-5 py-lg-4">
              <div v-if="!error" class="text-center text-muted mb-4">
                <small>Or sign in with credentials</small>
              </div>
              <div v-else class="text-center text-muted mb-4">
                <small class="error">{{error}}</small>
              </div>

              <form @submit.prevent="login">
                <div class="form-group mb-3">
                  <div class="input-group input-group-alternative">
                    <div class="input-group-prepend">
                      <span class="input-group-text">
                        <i class="ni ni-email-83"></i>
                      </span>
                    </div>
                    <input
                      v-model="username"
                      class="form-control"
                      placeholder="Username"
                      type="text"
                    />
                  </div>
                </div>
                <div class="form-group focused">
                  <div class="input-group input-group-alternative">
                    <div class="input-group-prepend">
                      <span class="input-group-text">
                        <i class="ni ni-lock-circle-open"></i>
                      </span>
                    </div>
                    <input
                      v-model="password"
                      class="form-control"
                      placeholder="Password"
                      type="password"
                    />
                  </div>
                </div>
                <!-- <div class="custom-control custom-control-alternative custom-checkbox">
                  <input class="custom-control-input" id=" customCheckLogin" type="checkbox" />
                  <label class="custom-control-label" for="customCheckLogin">
                    <span>Remember me</span>
                  </label>
                </div>-->
                <div class="custom-control custom-checkbox">
                  <input
                    v-model="remember"
                    class="custom-control-input"
                    id="customCheck2"
                    type="checkbox"
                  />
                  <label class="custom-control-label" for="customCheck2">
                    <span>Remember me</span>
                  </label>
                </div>
                <div class="text-center">
                  <button type="submit" class="btn btn-primary my-4">Sign in</button>
                </div>
              </form>
            </div>
          </div>
          <div class="row mt-3">
            <div class="col-6">
              <router-link to="/reset-password" class="text-light">
                <small>Forgot password?</small>
              </router-link>
            </div>
            <div class="col-6 text-right">
              <router-link to="/signup" class="text-light">
                <small>Create new account</small>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
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
.error {
  color: red;
}
</style>
