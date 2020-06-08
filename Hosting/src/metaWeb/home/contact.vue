<template>
  <section id="contact" class="bg-light py-5 contact">
    <div class="container contact">
      <div class="row">
        <div class="col-lg-9">
          <h3>Get In Touch</h3>
          <p class="lead">For any enquire , feel free to contact us !!</p>
          <form @submit.prevent="submitFeedBack">
            <div class="form-group input-group-lg mb-3" :class="{invalid:$v.name.$error}">
              <div class="input-group mb-4">
                <div class="input-group-prepend">
                  <span class="input-group-text">
                    <i class="fas fa-user"></i>
                  </span>
                </div>
                <input
                  @blur="$v.name.$touch()"
                  v-model="name"
                  type="text"
                  class="form-control"
                  placeholder="Enter name"
                />
              </div>
            </div>
            <div class="form-group input-group-lg mb-3" :class="{invalid:$v.email.$error}">
              <div class="input-group mb-4">
                <div class="input-group-prepend">
                  <span class="input-group-text">
                    <i class="fas fa-envelope"></i>
                  </span>
                </div>
                <input
                  @blur="$v.email.$touch()"
                  v-model="email"
                  type="email"
                  class="form-control"
                  placeholder="Enter email"
                />
              </div>
            </div>
            <div class="input-group input-group-lg mb-3" :class="{invalid:$v.message.$error}">
              <div class="input-group-prepend">
                <span class="input-group-text">
                  <i class="fas fa-pencil-alt"></i>
                </span>
              </div>
              <textarea
                v-model="message"
                @blur="$v.message.$touch()"
                rows="5"
                class="form-control"
                placeholder="Enter your message"
              ></textarea>
            </div>
            <input type="submit" value="submit" class="btn btn-block btn-large texttitle" />
          </form>
        </div>
        <div class="col-lg-3 align-self-center">
          <img src="../../assets/mlogo.png" alt class="img-fluid" />
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import axios from "axios";
import {
  required,
  maxLength,
  email,
  minLength
} from "vuelidate/lib/validators";
export default {
  data() {
    return {
      name: "",
      email: "",
      message: ""
    };
  },
  validations: {
    name: {
      required,
      maxLength: maxLength(15)
    },
    email: {
      required,
      email
    },
    message: {
      minLength: minLength(1)
    }
  },
  methods: {
    submitFeedBack() {
      axios
        .post("https://bibeklama.pythonanywhere.com/api/add_message", {
          name: this.name,
          email: this.email,
          message: this.message
        })
        .then(res => {
          this.message = "";
          this.email = "";
          this.name = "";
          this.$router.push("/success");
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>
<style scoped>
.texttitle {
  color: white;
  background: #1b838f;
}
.invalid input,
.invalid textarea {
  border: 1px solid red;
}
</style>>