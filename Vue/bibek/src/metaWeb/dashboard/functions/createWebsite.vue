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
                    v-model="nameOfSiteH"
                    placeholder="Name of Website"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="category"
                    placeholder="Category"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="headingOneH"
                    placeholder="heading one"
                  />
                </div>
                <div class="form-group">
                  <textarea
                    rows="3"
                    class="form-control"
                    v-model="descriptionOneH"
                    placeholder="description one"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="headingTwoH"
                    placeholder="heading two"
                  />
                </div>
                <div class="form-group">
                  <textarea
                    rows="3"
                    class="form-control"
                    v-model="descriptionTwoH"
                    placeholder="description two"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="headingThreeH"
                    placeholder="heading three"
                  />
                </div>
                <div class="form-group">
                  <textarea
                    rows="3"
                    class="form-control"
                    v-model="descriptionThreeH"
                    placeholder="description three"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="featureOneH"
                    placeholder="feature one"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="featureTwoH"
                    placeholder="feature two"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="featureThreeH"
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
                  <textarea
                    rows="3"
                    class="form-control"
                    v-model="introductionA"
                    placeholder="Introduction"
                  />
                </div>
                <div class="form-group">
                  <textarea
                    rows="15"
                    class="form-control"
                    v-model="whatWeDoA"
                    placeholder="What we do"
                  />
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
                  <input type="text" class="form-control" v-model="titleC" placeholder="title" />
                </div>
                <div class="form-group">
                  <textarea
                    rows="6"
                    class="form-control"
                    v-model="descriptionC"
                    placeholder="description"
                  />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="emailC" placeholder="email" />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="phoneC" placeholder="phone" />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" v-model="addressC" placeholder="address" />
                </div>

                <div class="form-group">
                  <button
                    @click="createWebsite"
                    class="btn bg-success text-white btn-block border-white"
                  >Create</button>
                </div>
                <div class="form-group">
                  <button
                    @click="dashboard"
                    class="btn bg-danger text-white btn-block border-white"
                  >Cancel</button>
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
      category: "",
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
    dashboard() {
      this.$router.push("/dashboard");
    },
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
            category: this.category,
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
          this.$router.push("/userWebsite/" + res.data.website.id);
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>