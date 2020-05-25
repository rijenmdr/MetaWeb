<template>
  <div>
    <section id="login">
      <div class="container mt-3 mb-3">
        <div class="row">
          <div class="col-md-3 mx-auto">
            <div class="card">
              <div class="card-header">
                <h4>Home Page</h4>
              </div>
              <div class="card-body">
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="title"
                    placeholder="Name of Website"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="description"
                    placeholder="heading one"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="username"
                    placeholder="description one"
                  />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="menus" placeholder="heading two" />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="menu1"
                    placeholder="description two"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="menu2"
                    placeholder="heading three"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="menu3"
                    placeholder="description three"
                  />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="menu4" placeholder="feature one" />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="menu5" placeholder="feature two" />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="menu5"
                    placeholder="Feature three"
                  />
                </div>
              </div>
            </div>
          </div>

          <div class="col-md-3 mx-auto">
            <div class="card">
              <div class="card-header">
                <h4>About Page</h4>
              </div>
              <div class="card-body">
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="title"
                    placeholder="Introduction"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="description"
                    placeholder="What we do"
                  />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="username" placeholder="title" />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="menus" placeholder="title" />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="menu1" placeholder="title" />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="menu2" placeholder="title" />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="menu3" placeholder="title" />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="menu4" placeholder="title" />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="menu5" placeholder="title" />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="menu5" placeholder="title" />
                </div>
              </div>
            </div>
          </div>

          <div class="col-md-3 mx-auto">
            <div class="card">
              <div class="card-header">
                <h4>Contact Page</h4>
              </div>
              <div class="card-body">
                <div class="form-group">
                  <input type="text" class="form-control" v-model="title" placeholder="title" />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="description"
                    placeholder="description"
                  />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="username" placeholder="email" />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="menus" placeholder="phone" />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="menu1" placeholder="address" />
                </div>

                <div class="form-group">
                  <button class="btn bg-success text-white btn-block border-white">Create</button>
                </div>
                <div class="form-group">
                  <button class="btn bg-danger text-white btn-block border-white">Cancel</button>
                </div>
              </div>
            </div>
          </div>

          <div class="col-md-3 mx-auto">
            <div>
              <img src="../../../assets/userWebsite/Home.png" height="250vh" width="350vw" />
            </div>
            <div>
              <img src="../../../assets/userWebsite/about.png" height="250vh" width="350vw" />
            </div>
            <div>
              <img src="../../../assets/userWebsite/contact.png" height="250vh" width="350vw" />
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      nameOfSiteH: "",
      headingOneH: "",
      descriptionOneH: "",
      headingTwoH: "",
      descriptionTwoH: "",
      headingThreeH: "",
      descriptionThreeH: "",
      featureOneH: "",
      featureTwoH: "",
      featureThreeH: "",
      introductionA: "",
      whatWeDoA: "",
      titleC: "",
      emailC: "",
      descriptionC: "",
      phoneC: "",
      addressC: ""
    };
  },
  methods: {
    async createWebsite() {
      let JWTToken = localStorage.getItem("token");
      if (!JWTToken) {
        JWTToken = this.$store.getters.getToken;
      }
      console.log(JWTToken);
      await axios
        .post(
          "http://localhost:8000/api/add_website",

          {
            nameOfSiteH: this.nameOfSiteH,
            headingOneH: this.headingOneH,
            descriptionOneH: this.descriptionOneH,
            headingTwoH: this.headingTwoH,
            descriptionTwoH: this.descriptionTwoH,
            headingThreeH: this.headingThreeH,
            descriptionThreeH: this.descriptionThreeH,
            featureOneH: this.featureOneH,
            featureTwoH: this.featureTwoH,
            featureThreeH: this.featureThreeH,
            introductionA: this.introductionA,
            whatWeDoA: this.whatWeDoA,
            titleC: this.titleC,
            emailC: this.emailC,
            descriptionC: this.descriptionC,
            phoneC: this.phoneC,
            addressC: this.addressC,
            user: this.$store.getters.getUser
          },
          {
            headers: {
              Authorization: `Token ${JWTToken}`
            }
          }
        )
        .then(res => {
          this.$store.dispatch("setId", res.data.website.id);
          this.$router.push("/userWebsite");
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>