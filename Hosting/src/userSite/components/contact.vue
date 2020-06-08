<template>
  <div>
    <Header :nameOfSite="nameOfSite" id="4" :backgroundColor="backgroundColor" />
    <header id="page-header">
      <div class="container mt-2">
        <div class="row">
          <div class="col-md-6 m-auto text-center">
            <h1>Contact Us</h1>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus, alias!</p>
          </div>
        </div>
      </div>
    </header>
    <!-- Contact -->
    <section id="contact" class="py-3">
      <div class="container">
        <div class="row">
          <div class="col-md-4">
            <div class="card p-4">
              <div class="card-body">
                <h4>{{titleC}}</h4>
                <p>{{descriptionC}}</p>
                <h4>Adderess</h4>
                <p>{{addressC}}</p>
                <h4>Email</h4>
                <p>{{emailC}}</p>
                <h4>Phone</h4>
                <p>{{phoneC}}</p>
              </div>
            </div>
          </div>
          <div class="col-md-8">
            <div class="card p-4">
              <div class="card-body">
                <h3 class="text-center">Please fill the form to contact us</h3>

                <form @submit.prevent="submitFeedback">
                  <div class="row mt-4">
                    <div class="col-md-6">
                      <div class="form-group" :class="{invalid:$v.first_name.$error}">
                        <input
                          type="text"
                          @blur="$v.first_name.$touch()"
                          v-model="first_name"
                          name
                          placeholder="First Name"
                          id
                          class="form-control"
                        />
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group" :class="{invalid:$v.last_name.$error}">
                        <input
                          type="text"
                          @blur="$v.last_name.$touch()"
                          v-model="last_name"
                          name
                          placeholder="Last Name"
                          id
                          class="form-control"
                        />
                      </div>
                    </div>
                    <div class="col-md-6 mt-3">
                      <div class="form-group" :class="{invalid:$v.email.$error}">
                        <input
                          type="text"
                          @blur="$v.email.$touch()"
                          v-model="email"
                          name
                          placeholder="Email"
                          id
                          class="form-control"
                        />
                      </div>
                    </div>
                    <div class="col-md-6 mt-3">
                      <div class="form-group" :class="{invalid:$v.address.$error}">
                        <input
                          type="text"
                          @blur="$v.address.$touch()"
                          v-model="address"
                          name
                          placeholder="Address"
                          id
                          class="form-control"
                        />
                      </div>
                    </div>
                  </div>
                  <div class="row mt-3">
                    <div class="col-md-12">
                      <div class="form-group">
                        <textarea
                          v-model="message"
                          rows="5"
                          class="form-control"
                          placeholder="Enter Message"
                        ></textarea>
                      </div>
                    </div>
                  </div>
                  <div class="row mt-3">
                    <div class="col-md-12">
                      <div class="form-group">
                        <input
                          type="submit"
                          value="Submit"
                          class="form-control btn btn-outline-success bg-success text-white"
                        />
                      </div>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <Footer :backgroundColor="backgroundColor" />
  </div>
</template>
<script>
import axios from "axios";
import Header from "./componentHead";
import Footer from "./footer";
import host from '../../host.js'
import {
  required,
  email,
  maxLength,
  minLength,
  sameAs
} from "vuelidate/lib/validators";
export default {
  components: {
    Header,
    Footer
  },
  data() {
    return {
      user: "",
      first_name: "",
      last_name: "",
      email: "",
      address: "",
      message: "",
      shopId: "",
      done: "",

      nameOfSite: this.$store.getters.getWebsite.nameOfSiteH,
      titleC: this.$store.getters.getWebsite.titleC,
      descriptionC: this.$store.getters.getWebsite.descriptionC,
      emailC: this.$store.getters.getWebsite.emailC,
      phoneC: this.$store.getters.getWebsite.phoneC,
      addressC: this.$store.getters.getWebsite.addressC,
      backgroundColor: this.$store.getters.getWebsite.backgroundColor
    };
  },
  created() {
    // console.log(this.$store.getters.getWebsite.id);
  },
  validations: {
    email: {
      required,
      email
    },
    first_name: {
      required,
      minLength: minLength(2),
      maxLength: maxLength(15)
    },
    last_name: {
      required,
      minLength: minLength(2),
      maxLength: maxLength(15)
    },
    address: {
      required,
      minLength: minLength(2),
      maxLength: maxLength(15)
    }
  },
  methods: {
    submitFeedback() {
      axios
        .post(host.host+"/api/add_review", {
          user: this.$store.getters.getWebsite.user,
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
          address: this.address,
          message: this.message,
          shopId: this.$store.getters.getWebsite.id
        })
        .then(res => {
          this.done = "feedback Sent";
          (this.first_name = ""),
            (this.last_name = ""),
            (this.email = ""),
            (this.address = ""),
            (this.message = "");
          this.$store.dispatch("addNotifications", {
            type: "success",
            message: "Feedback sent successfully"
          });
          this.$router.push("/userWebsite/about");
        });
    }
  }
};
</script>
<style scoped>
.invalid input {
  border: 1px solid red;
}
</style>