<template>
  <div>
    <div class="section section-hero section-shaped mt-0">
      <router-link class="navbar-brand mr-lg-5 logo" to="/">
        Meta
        <span class="text1">web</span>
      </router-link>
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
      <div class="container search-top">
        <div class="row">
          <div class="form-group has-success d-flex col-lg-3 col-12">
            <input type="text" v-model="keywords" class="form-control" />
          </div>
          <div class="form-group has-success d-flex col-lg-2 col-12">
            <input type="text" v-model="location" class="form-control" />
          </div>
          <div class="form-group ml-0 col-lg-2 col-12">
            <input v-model="shopId" type="number" placeholder="Shop Id" class="form-control" />
          </div>
          <div class="form-group ml-0 col-lg-2 col-12 ml-md-3">
            <button type="submit" class="btn btn-lg btn-white btn-icon mb-sm-0">
              <span class="btn-inner--icon">
                <i class="fas fa-search"></i>
              </span>
              <span class="btn-inner--text">Search WEBSITE</span>
            </button>
          </div>
          <div class="form-group ml-0 col-lg-2 col-12 ml-md-5">
            <div @click="search" class="btn btn-lg btn-github btn-icon mb-3 mb-sm-0">
              <span class="btn-inner--icon">
                <i class="fas fa-hand-point-right"></i>
              </span>
              <span class="btn-inner--text">
                <span class="text-warning">Shop Id</span> Search
              </span>
            </div>
          </div>
        </div>
        <div class="row search-result">
          <section class="section section-lg pt-lg-0 mt--200">
            <div class="container">
              <div class="row justify-content-center">
                <div class="col-lg-12">
                  <div class="row row-grid">
                    <div class="col-lg-4">
                      <card class="border-0" hover shadow body-classes="py-5">
                        <icon
                          name="fa fa-cutlery"
                          aria-hidden="true"
                          type="primary"
                          rounded
                          class="mb-4"
                        ></icon>
                        <h6 class="text-primary text-uppercase">Gyan Dai ko Khaja Ghar</h6>
                        <p
                          class="description mt-3"
                        >The best place in the town to get the best and delicious food. We offer you the best then the rest.</p>
                        <div>
                          <badge type="primary" rounded>9818445068</badge>
                          <badge type="primary" rounded>khajaghar@gmail.com</badge>
                          <badge type="primary" rounded>Balaju Kathmandu</badge>
                        </div>
                        <base-button tag="a" href="#" type="primary" class="mt-4">Visit Website</base-button>
                      </card>
                    </div>
                    <div class="col-lg-4">
                      <card class="border-0" hover shadow body-classes="py-5">
                        <icon name="fa fa-shopping-bag" type="success" rounded class="mb-4"></icon>
                        <h6 class="text-success text-uppercase">Laxmi Fancy Store</h6>
                        <p
                          class="description mt-3"
                        >All ladies and gents fancy clothes available under a roof. A warm welcome to all .</p>
                        <div>
                          <badge type="success" rounded>Paknajol</badge>
                          <badge type="success" rounded>9818446582</badge>
                          <badge type="success" rounded>laxmi@gmail.com</badge>
                        </div>
                        <base-button tag="a" href="#" type="success" class="mt-4">Visit Website</base-button>
                      </card>
                    </div>
                    <div class="col-lg-4">
                      <card class="border-0" hover shadow body-classes="py-5">
                        <icon name="fa fa-cutlery" type="warning" rounded class="mb-4"></icon>
                        <h6 class="text-warning text-uppercase">RK House</h6>
                        <p
                          class="description mt-3"
                        >The best newari hotel at thamel. Do visit us for the tipical newari cousines. A warm welcome to all.</p>
                        <div>
                          <badge type="warning" rounded>Thamel</badge>
                          <badge type="warning" rounded>rkghar@gmail.com</badge>
                          <badge type="warning" rounded>9840154754</badge>
                        </div>
                        <base-button tag="a" href="#" type="warning" class="mt-4">Visit Website</base-button>
                      </card>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
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
  </div>
</template>
<script>
export default {
  data() {
    return {
      keywords: this.$route.query.keywords,
      shopId: "",
      location: this.$route.query.location
    };
  },
  methods: {
    search() {
      if (this.shopId < 1000) {
        this.$router.push("/" + this.shopId);
      } else {
        this.$router.push("/userWebsite/" + this.shopId);
      }
    }
  }
};
</script>
<style scoped>
.search-top {
  margin-top: -15vh;
}
.search-result {
  margin-top: 40vh;
}
@import url("https://fonts.googleapis.com/css2?family=Cabin:wght@700&display=swap");
.logo {
  z-index: 1000;
  top: 11vh;
  left: 12.3vw;
  position: absolute;
  margin-top: -10vh;
  color: white;
  font-size: 22px;
  font-family: "Cabin", sans-serif;
}
.text1 {
  color: #d3b001;
}
</style>