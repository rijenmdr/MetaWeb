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
                  <input type="text" class="form-control" v-model="category" placeholder="Category" />
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
                  <textarea
                    rows="3"
                    class="form-control"
                    v-model="featureOneDesH"
                    placeholder="feature description"
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
                  <textarea
                    rows="3"
                    class="form-control"
                    v-model="featureTwoDesH"
                    placeholder="feature description"
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
                <div class="form-group">
                  <textarea
                    rows="3"
                    class="form-control"
                    v-model="featureThreeDesH"
                    placeholder="feature description"
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
                    rows="10"
                    class="form-control"
                    v-model="whatWeDoA"
                    placeholder="What we do"
                  />
                </div>
              </div>
              <div class="card-header">
                <h4>Background Color</h4>
              </div>
              <div class="card-body">
                <div class="form-group">
                  <select v-model="backgroundColor" class="form-control form-control">
                    <option value="green">Green</option>
                    <option value="#30332E">Black</option>
                    <option value="#DECA04">Yellow</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-3 mx-auto">
            <div class="card">
              <div class="card-header">
                <h4>Service Page</h4>
              </div>
              <div class="card-body">
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="serviceOne"
                    placeholder="Service One"
                  />
                </div>

                <div class="form-group">
                  <textarea
                    rows="3"
                    class="form-control"
                    v-model="serviceOneDes"
                    placeholder="description of service one"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="serviceTwo"
                    placeholder="service two"
                  />
                </div>
                <div class="form-group">
                  <textarea
                    rows="3"
                    class="form-control"
                    v-model="serviceTwoDes"
                    placeholder="description two"
                  />
                </div>
                <div class="form-group">
                  <input
                    type="text"
                    class="form-control"
                    v-model="serviceThree"
                    placeholder="service three"
                  />
                </div>
                <div class="form-group">
                  <textarea
                    rows="3"
                    class="form-control"
                    v-model="serviceThreeDes"
                    placeholder="description of service three"
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
            <!-- <div>
              <img src="../../../assets/userWebsite/Home.png" height="250vh" width="350vw" />
            </div>
            <div>
              <img src="../../../assets/userWebsite/about.png" height="250vh" width="350vw" />
            </div>
            <div>
              <img src="../../../assets/userWebsite/contact.png" height="250vh" width="350vw" />
            </div>-->
            <!-- <div class="card-header">
              <h4>Images</h4>
            </div>
            <div class="form-group">
              <input type="file" @change="onFileChanged" class="form-control" multiple="multiple"/>
            </div>
            <div class="form-group">
              <input type="file" @change="onFileChanged(2)" class="form-control" />
            </div>
            <div class="form-group">
              <input type="file" @change="onFileChanged(3)" class="form-control" />
            </div>
            <div class="form-group">
              <input type="file" @change="onFileChanged(4)" class="form-control" />
            </div>
            <div class="form-group">
              <input type="file" @change="onFileChanged(5)" class="form-control" />
            </div>-->
          </div>
        </div>
      </div>
    </section>
    <div class="container">
      <div class="row">
        <div class="col-md-6"></div>
      </div>
    </div>
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
      addressC: "",
      featureOneDesH: "",
      featureTwoDesH: "",
      featureThreeDesH: "",
      serviceOne: "",
      serviceTwo: "",
      serviceOneDes: "",
      serviceTwoDes: "",
      serviceThree: "",
      serviceThreeDes: "",
      backgroundColor: ""
    };
  },
  created() {
    //yeslay 2 hrs khayo . default ma value bind  nahune bug raixa so created ma value change garayrw garayko

    this.backgroundColor = "green";
  },
  methods: {
    dashboard() {
      this.$router.push("/dashboard");
    },
    onFileChanged(event) {
      console.log(event.target.files[0]);
    },
    async createWebsite() {
      let JWTToken = localStorage.getItem("token");
      if (!JWTToken) {
        JWTToken = this.$store.getters.getToken;
      }
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
            user: this.$store.getters.getUser,
            featureOneDesH: this.featureOneDesH,
            featureTwoDesH: this.featureTwoDesH,
            featureThreeDesH: this.featureThreeDesH,
            serviceOne: this.serviceOne,
            serviceTwo: this.serviceTwo,
            serviceThree: this.serviceThree,
            serviceOneDes: this.serviceOneDes,
            serviceTwoDes: this.serviceTwoDes,
            serviceThreeDes: this.serviceThreeDes,
            backgroundColor: this.backgroundColor
          },
          {
            headers: {
              Authorization: `Token ${JWTToken}`
            }
          }
        )
        .then(res => {
          this.$store.dispatch("addNotifications", {
            type: "success",
            message: "This is the view of your new website"
          });
          this.$store.dispatch("setId", res.data.website.id);
          this.$router.push("/userWebsite/" + res.data.website.id);
        })
        .catch(err => {
          console.log("err")
          console.log(err);
        });
    }
  }
};
</script>