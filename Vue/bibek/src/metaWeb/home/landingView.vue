<template>
  <div class="section section-hero section-shaped">
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
          <div class="row align-items-center justify-content-center">
            <div class="col-lg-6 text-center">
              <p
                class="lead text-white"
              >Search for the stores around you Or create website and promote your business with us</p>
              <div class="col-lg-12 col-sm-6 d-flex mt-4">
                <div class="form-group has-success">
                  <input type="text" placeholder="Keywords" class="form-control is-valid" />
                </div>
                <div class="form-group has-success ml-3">
                  <input
                    v-model="shopId"
                    type="number"
                    placeholder="Shop Id"
                    class="form-control is-valid"
                  />
                </div>
              </div>
              <div class="btn-wrapper mt-5">
                <a
                  href="https://www.creative-tim.com/product/argon-design-system"
                  class="btn btn-lg btn-white btn-icon mb-3 mb-sm-0"
                >
                  <span class="btn-inner--icon">
                    <i class="fas fa-search"></i>
                  </span>
                  <span class="btn-inner--text">Search WEBSITE</span>
                </a>
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
        </div>
      </div>
    </div>
    <div class="separator separator-bottom separator-skew zindex-100">
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
    </div>
  </div>
</template>
<script>
export default {
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
        this.$router.push("/userWebsite/" + this.shopId);
      } else {
        this.$router.push(
          "/search?keywords=" +
            this.keywords +
            "&location=" +
            this.location +
            "&category=" +
            this.category
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
@import "../../assets/css/nucleo-icons.css";
@import "../../assets/css/argon-design-system.css?v=1.2.0";
.landingView {
  margin-top: 12vh;
}
.formCenter {
  background: #1b838f;
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