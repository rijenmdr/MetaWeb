<template>
  <div>
    <Header />
    <div class="section section-hero section-shaped mt-0">
      <div class="shape shape-style-1 shape-primary">
        <span class="span-150"></span>
        <span class="span-50"></span>
        <span class="span-50"></span>
        <span class="span-75"></span>
        <span class="span-100"></span>
        <span class="span-75"></span>
        <span class="span-50"></span>
        <span class="span-100"></span>
        <span class="span-50"></span>
        <span class="span-100"></span>
      </div>
      <div class="page-header">
        <div class="container shape-container d-flex align-items-center py-lg">
          <div class="col px-0">
            <form @submit="search">
              <div class="row align-items-center justify-content-center">
                <div class="col-lg-8 text-center">
                  <p class="lead text-white">
                    Search for the
                    <span class="text1">stores</span> around you Or
                    <span class="text1">create website</span> and promote your business with us. All in here
                  </p>
                  <div class="col-lg-12 col-sm-12 d-inline d-md-flex mt-4">
                    <div class="form-group has-success d-flex col-lg-5 col-12">
                      <input
                        type="text"
                        v-model="keywords"
                        placeholder="Keywords"
                        class="form-control"
                      />
                    </div>
                    <div class="form-group has-success col-lg-5 col-12">
                      <input
                        type="text"
                        v-model="location"
                        placeholder="Location"
                        class="form-control"
                      />
                    </div>
                    <div class="form-group ml-0 col-lg-3 col-12">
                      <input
                        v-model="shopId"
                        type="number"
                        placeholder="Shop Id"
                        class="form-control"
                      />
                    </div>
                  </div>
                  <div class="btn-wrapper mt-5">
                    <button type="submit" class="btn btn-lg btn-white btn-icon mb-3 mb-sm-0">
                      <span class="btn-inner--icon">
                        <i class="fas fa-search"></i>
                      </span>
                      <span class="btn-inner--text">Search WEBSITE</span>
                    </button>
                    <div @click="search" class="btn btn-lg btn-github btn-icon mb-3 mb-sm-0">
                      <span class="btn-inner--icon">
                        <i class="fas fa-hand-point-right"></i>
                      </span>
                      <span class="btn-inner--text">
                        <span class="text-warning">Shop Id</span> Search
                      </span>
                    </div>
                  </div>
                  <div class="mt-5"></div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
      <!-- <div class="separator separator-bottom separator-skew">
      <svg
        x="0"
        y="0"
        viewBox="0 0 2560 100"
        preserveAspectRatio="none"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
      >
        <polygon class="fill-white" points="2560 0 2560 100 0 100" />
      </svg>
      </div>-->
    </div>
    <HowItWorks />
    <Premium />
    <OurTeam />
    <Contact />
    <Footer />
  </div>
</template>
<script>
import Header from "./header";
import HowItWorks from "./howItWorks";
import OurTeam from "./ourteam";
import Contact from "./contact";
import Footer from "./footer";
import Premium from "./premium";
export default {
  components: {
    Header,
    HowItWorks,
    OurTeam,
    Contact,
    Premium,
    Footer
  },
  data() {
    return {
      shopId: "",
      location: "",
      category: "",
      keywords: ""
    };
  },
  created() {
    //yeslay 2 hrs khayo . default ma value bind  nahune bug raixa so created ma value change garayrw garayko
    this.location = "location";
    this.category = "category";
  },
  methods: {
    search() {
      if (
        this.location == "location" &&
        this.category == "category" &&
        this.shopId != ""
      ) {
        if (this.shopId < 1000) {
          this.$router.push("/" + this.shopId);
        } else {
          this.$router.push("/userWebsite/" + this.shopId);
        }
      } else {
        this.$router.push(
          "/search?keywords=" + this.keywords + "&location=" + this.location
        );
      }
    },
    select() {
      console.log("ayo");
    }
  }
};
</script>
<style scoped>
.landingView {
  margin-top: 0vh;
}
.formCenter {
  background: #1b838f;
}
.text1 {
  color: #d3b001;
}
.signUp {
  color: white;
  font-size: 22px;
}
a:hover {
  text-decoration: none;
}
.signUp:hover {
  color: black;
  border: 1px solid red;
  font-size: 32px;
  text-decoration: none;
  transition: 0.5s;
  border-radius: 20px;
}
.buttonSearch {
  background: #63b839;
  width: 22vw;
  height: 7vh;
  color: white;
  border-radius: 10px;
  box-shadow: none;
  text-align: center;
  padding-top: 10px;
}
.buttonSearch:hover {
  opacity: 0.7;
}
</style>