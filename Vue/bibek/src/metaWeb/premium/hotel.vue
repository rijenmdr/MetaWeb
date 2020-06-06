<template>
  <div class="main-content" id="panel">
    <div class="header pb-6">
      <section id="login">
        <form @submit.prevent="submitFile">
          <div class="container mt-3 mb-3">
            <div class="row">
              <div class="col-md-3 mx-auto">
                <div class="card">
                  <div class="card-header">
                    <h5>Landing Page</h5>
                  </div>
                  <div class="card-body">
                    <div class="form-group" :class="{invalid:$v.name.$error}">
                      <input
                        @blur="$v.name.$touch()"
                        type="text"
                        class="form-control"
                        v-model="name"
                        placeholder="Name"
                      />

                      <div v-if="$v.name.$error" class="error">Please enter valid name of Hotel</div>
                      <div v-if="$v.name.$model" class="info">This will be name of Hotel</div>
                    </div>

                    <div class="form-group" :class="{invalid:$v.welcomeOne.$error}">
                      <input
                        @blur="$v.welcomeOne.$touch()"
                        type="text"
                        class="form-control"
                        v-model="welcomeOne"
                        placeholder="Welcome One"
                      />
                      <div v-if="$v.welcomeOne.$error" class="error">Please enter valid Welcome Note</div>
                      <div v-if="$v.welcomeOne.$model" class="info">This will be Welcome Note</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.welcomeOneDes.$error}">
                      <textarea
                        @blur="$v.welcomeOneDes.$touch()"
                        rows="3"
                        class="form-control"
                        v-model="welcomeOneDes"
                        placeholder="Description"
                      />
                      <div
                        v-if="$v.welcomeOneDes.$error"
                        class="error"
                      >Please enter valid Welcome Description</div>
                      <div
                        v-if="$v.welcomeOneDes.$model"
                        class="info"
                      >This will be Welcome Description</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.welcomeTwo.$error}">
                      <input
                        @blur="$v.welcomeTwo.$touch()"
                        type="text"
                        class="form-control"
                        v-model="welcomeTwo"
                        placeholder="Welcome Two"
                      />
                      <div v-if="$v.welcomeTwo.$error" class="error">Please enter valid Welcome Note</div>
                      <div v-if="$v.welcomeTwo.$model" class="info">This will be Welcome Note</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.welcomeTwoDes.$error}">
                      <textarea
                        @blur="$v.welcomeTwoDes.$touch()"
                        rows="3"
                        class="form-control"
                        v-model="welcomeTwoDes"
                        placeholder="description two"
                      />
                      <div
                        v-if="$v.welcomeTwoDes.$error"
                        class="error"
                      >Please enter valid Welcome Description</div>
                      <div
                        v-if="$v.welcomeTwoDes.$model"
                        class="info"
                      >This will be Welcome Description</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.photo_1.$error}">
                      <label>Welcome Image 1</label>
                      <input
                        @blur="$v.photo_1.$touch()"
                        type="file"
                        ref="photo_1"
                        class="form-control"
                        v-on:change="handleFileUpload()"
                      />
                      <div v-if="$v.photo_1.$error" class="error">Please enter valid Image File</div>
                      <div v-if="$v.photo_1.$model" class="info">This will be Landing Page Image</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.photo_2.$error}">
                      <label>Welcome Image Two</label>
                      <input
                        @blur="$v.welcomeTwo.$touch()"
                        type="file"
                        ref="photo_2"
                        class="form-control"
                        v-on:change="handleFileUpload()"
                      />
                      <div v-if="$v.photo_2.$error" class="error">Please enter valid Image File</div>
                      <div v-if="$v.photo_2.$model" class="info">This will be Landing Page Image</div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-md-3 mx-auto">
                <div class="card">
                  <div class="card-header">
                    <h5>About Page</h5>
                  </div>
                  <div class="card-body">
                    <div class="form-group" :class="{invalid:$v.about.$error}">
                      <textarea
                        @blur="$v.about.$touch()"
                        rows="10"
                        class="form-control"
                        v-model="about"
                        placeholder="About"
                      />
                      <div v-if="$v.about.$error" class="error">Please enter valid About</div>
                      <div v-if="$v.about.$model" class="info">This will be About info</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.photo_3.$error}">
                      <label>About Image</label>
                      <input
                        @blur="$v.photo_3.$touch()"
                        type="file"
                        ref="photo_3"
                        class="form-control"
                        v-on:change="handleFileUpload()"
                      />
                      <div v-if="$v.photo_3.$error" class="error">Please enter valid Image File</div>
                      <div v-if="$v.photo_3.$model" class="info">This will be About Photo</div>
                    </div>
                  </div>
                  <div class="card-header">
                    <h5>Background Color</h5>
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
                    <h5>Details</h5>
                  </div>
                  <div class="card-body">
                    <div class="form-group" :class="{invalid:$v.phone.$error}">
                      <input
                        @blur="$v.phone.$touch()"
                        type="number"
                        class="form-control"
                        v-model="phone"
                        placeholder="Phone"
                      />
                      <div v-if="$v.phone.$error" class="error">Please enter valid Phone</div>
                      <div v-if="$v.phone.$model" class="info">This will be Phone Number</div>
                    </div>

                    <div class="form-group" :class="{invalid:$v.email.$error}">
                      <input
                        @blur="$v.email.$touch()"
                        type="text"
                        class="form-control"
                        v-model="email"
                        placeholder="Email"
                      />
                      <div v-if="$v.email.$error" class="error">Please enter valid Email</div>
                      <div v-if="$v.email.$model" class="info">This will be Email Address</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.location.$error}">
                      <input
                        @blur="$v.location.$touch()"
                        type="text"
                        class="form-control"
                        v-model="location"
                        placeholder="location"
                      />
                      <div v-if="$v.location.$error" class="error">Please enter valid Location</div>
                      <div v-if="$v.location.$model" class="info">This will be Your Location</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.aboutFooter.$error}">
                      <textarea
                        @blur="$v.aboutFooter.$touch()"
                        rows="3"
                        class="form-control"
                        v-model="aboutFooter"
                        placeholder="about footer"
                      />
                      <div v-if="$v.aboutFooter.$error" class="error">Please enter valid About</div>
                      <div v-if="$v.aboutFooter.$model" class="info">This will be About at Footer</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.openingHours.$error}">
                      <input
                        @blur="$v.openingHours.$touch()"
                        type="text"
                        class="form-control"
                        v-model="openingHours"
                        placeholder="Opening Hours"
                      />
                      <div v-if="$v.openingHours.$error" class="error">Please enter valid info</div>
                      <div v-if="$v.openingHours.$model" class="info">This will be opening time</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.fbLink.$error}">
                      <input
                        @blur="$v.fbLink.$touch()"
                        type="text"
                        class="form-control"
                        v-model="fbLink"
                        placeholder="facebook link"
                      />
                      <div v-if="$v.fbLink.$error" class="error">Please enter valid fb-link</div>
                      <div v-if="$v.fbLink.$model" class="info">This will be fb link</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.instaLink.$error}">
                      <input
                        @blur="$v.instaLink.$touch()"
                        type="text"
                        class="form-control"
                        v-model="instaLink"
                        placeholder="Instagram Link"
                      />
                      <div v-if="$v.instaLink.$error" class="error">Please enter valid insta-link</div>
                      <div v-if="$v.instaLink.$model" class="info">This will be instagram link</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.youtubeLink.$error}">
                      <input
                        @blur="$v.youtubeLink.$touch()"
                        type="text"
                        class="form-control"
                        v-model="youtubeLink"
                        placeholder="Youtube Link"
                      />
                      <div
                        v-if="$v.youtubeLink.$error"
                        class="error"
                      >Please enter valid youtube-link</div>
                      <div v-if="$v.youtubeLink.$model" class="info">This will be Youtube link</div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-md-3 mx-auto">
                <div class="card">
                  <div class="card-header">
                    <h5>Images</h5>
                  </div>
                  <div class="card-body">
                    <div class="form-group" :class="{invalid:$v.galleryDes.$error}">
                      <input
                        @blur="$v.galleryDes.$touch()"
                        type="text"
                        class="form-control"
                        v-model="galleryDes"
                        placeholder="Gallery Description"
                      />
                      <div v-if="$v.galleryDes.$error" class="error">Please enter valid Image Des</div>
                      <div v-if="$v.galleryDes.$model" class="info">This will be Gallery Des</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.photo_4.$error}">
                      <label>Gallery Photo 1</label>
                      <input
                        @blur="$v.photo_4.$touch()"
                        type="file"
                        ref="photo_4"
                        class="form-control"
                        v-on:change="handleFileUpload()"
                      />
                      <div v-if="$v.photo_4.$error" class="error">Please enter valid Image File</div>
                      <div v-if="$v.photo_4.$model" class="info">This will be Gallery Image</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.photo_5.$error}">
                      <label>Gallery Photo 2</label>
                      <input
                        @blur="$v.photo_5.$touch()"
                        type="file"
                        ref="photo_5"
                        class="form-control"
                        v-on:change="handleFileUpload()"
                      />
                      <div v-if="$v.photo_5.$error" class="error">Please enter valid Image File</div>
                      <div v-if="$v.photo_5.$model" class="info">This will be Gallery Image</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.photo_6.$error}">
                      <label>Gallery Photo 3</label>
                      <input
                        @blur="$v.photo_6.$touch()"
                        type="file"
                        ref="photo_6"
                        class="form-control"
                        v-on:change="handleFileUpload()"
                      />
                      <div v-if="$v.photo_6.$error" class="error">Please enter valid Image File</div>
                      <div v-if="$v.photo_6.$model" class="info">This will be Gallery Image</div>
                    </div>
                    <div class="form-group" :class="{invalid:$v.photo_7.$error}">
                      <label>Gallery Photo 4</label>
                      <input
                        @blur="$v.photo_7.$touch()"
                        type="file"
                        ref="photo_7"
                        class="form-control"
                        v-on:change="handleFileUpload()"
                      />
                      <div v-if="$v.photo_7.$error" class="error">Please enter valid Image File</div>
                      <div v-if="$v.photo_7.$model" class="info">This will be Gallery Image</div>
                    </div>

                    <div class="form-group" :class="{invalid:$v.youtubeLink.$error}">
                      <button
                        :disabled="$v.$invalid"
                        type="submit"
                        class="btn bg-success text-white btn-block border-white"
                      >Create</button>
                    </div>
                    <div class="form-group" :class="{invalid:$v.youtubeLink.$error}">
                      <button
                        @click="dashboard"
                        class="btn bg-danger text-white btn-block border-white"
                      >Cancel</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </form>
      </section>
    </div>
  </div>
</template>
<script>
import {
  required,
  email,
  maxLength,
  minLength,
  sameAs
} from "vuelidate/lib/validators";
import axios from "axios";
export default {
  data() {
    return {
      name: "",
      category: "hotel",
      welcomeOne: "",
      welcomeOneDes: "",
      welcomeTwo: "",
      welcomeTwoDes: "",
      about: "",
      backgroundColor: "",
      galleryDes: "",
      phone: "",
      email: "",
      location: "",
      aboutFooter: "",
      openingHours: "",
      fbLink: "",
      instaLink: "",
      youtubeLink: "",
      photo_1: "",
      photo_2: "",
      photo_3: "",
      photo_4: "",
      photo_5: "",
      photo_6: "",
      photo_7: ""
    };
  },
  validations: {
    email: {
      required,
      email
    },
    name: { required },
    welcomeOne: { required },
    welcomeOneDes: { required },
    welcomeTwo: { required },
    welcomeTwoDes: { required },
    photo_1: { required },
    photo_2: { required },
    photo_3: { required },
    about: { required },
    phone: { required },
    location: { required },
    aboutFooter: { required },
    openingHours: { required },
    fbLink: { required },
    instaLink: { required },
    youtubeLink: { required },
    galleryDes: { required },
    photo_4: { required },
    photo_5: { required },
    photo_6: { required },
    photo_7: { required }
  },
  created() {
    //yeslay 2 hrs khayo . default ma value bind  nahune bug raixa so created ma value change garayrw garayko
    this.backgroundColor = "green";
  },
  methods: {
    dashboard() {
      this.$router.push("/dashboard");
    },
    handleFileUpload() {
      this.photo_1 = this.$refs.photo_1.files[0];
      this.photo_2 = this.$refs.photo_2.files[0];
      this.photo_3 = this.$refs.photo_3.files[0];
      this.photo_4 = this.$refs.photo_4.files[0];
      this.photo_5 = this.$refs.photo_5.files[0];
      this.photo_6 = this.$refs.photo_6.files[0];
      this.photo_7 = this.$refs.photo_7.files[0];
    },

    submitFile() {
      console.log(this.photo_1);
      let formData = new FormData();
      formData.append("user", this.$store.getters.getUser);
      formData.append("name", this.name);
      formData.append("category", this.category);
      formData.append("welcomeOne", this.welcomeOne);
      formData.append("welcomeOneDes", this.welcomeOneDes);
      formData.append("welcomeTwo", this.welcomeTwo);
      formData.append("welcomeTwoDes", this.welcomeTwoDes);
      formData.append("about", this.about);
      formData.append("galleryDes", this.galleryDes);
      formData.append("phone", this.phone);
      formData.append("email", this.email);
      formData.append("location", this.location);
      formData.append("aboutFooter", this.aboutFooter);
      formData.append("openingHours", this.openingHours);
      formData.append("fbLink", this.fbLink);
      formData.append("instaLink", this.instaLink);
      formData.append("youtubeLink", this.youtubeLink);
      formData.append("backgroundColor", this.backgroundColor);
      formData.append("photo_1", this.photo_1);
      formData.append("photo_2", this.photo_2);
      formData.append("photo_3", this.photo_3);
      formData.append("photo_4", this.photo_4);
      formData.append("photo_5", this.photo_5);
      formData.append("photo_6", this.photo_6);
      formData.append("photo_7", this.photo_7);

      axios
        .post("http://localhost:8000/api/add_hotel", formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(res => {
          console.log(res);
          this.$store.dispatch("addNotifications", {
            type: "success",
            message: "This is the view of your new website"
          });
        })
        .catch(function() {
          console.log("FAILURE!!");
        });
    }
  }
};
</script>
<style scoped>
.invalid input {
  border: 1px solid red;
}

.invalid textarea {
  border: 1px solid red;
}
@import url("https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap");
.error {
  font-size: 15px;
  text-align: center;
  color: #f04104;
  font-family: "Patrick Hand", cursive;
}
.info {
  font-size: 15px;
  text-align: center;
  color: #32f004;
  font-family: "Patrick Hand", cursive;
}
</style>