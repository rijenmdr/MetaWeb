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
              </div>
              <div class="card-body">
                <form @submit.prevent="signUp">
                  <div class="form-group">
                    <label for="name">Username</label>
                    <input type="text" class="form-control" v-model="username" />
                  </div>
                  <div class="form-group">
                    <label for="name">Email</label>
                    <input type="email" class="form-control" v-model="email" />
                  </div>
                  <div class="form-group">
                    <label for="name">password</label>
                    <input type="password" class="form-control" v-model="password1" />
                  </div>
                  <div class="form-group">
                    <label for="name">Confirm Password</label>
                    <input type="password" class="form-control" v-model="password2" />
                  </div>
                  <input type="submit" value="Register" class="btn btn-success btn-block" />
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
export default {
  components: {
    Footer,
    Header
  },
  data() {
    return {
      username: null,
      email: null,
      password1: null,
      password2: null
    };
  },
  methods:{
            async signUp(){
                await this.$store.dispatch('signUp',{
                    username:this.username,
                    password1:this.password1,
                    password2:this.password2,
                    email:this.email
                })
                this.$router.push('/dashboard')
            }
        }
};
</script>
