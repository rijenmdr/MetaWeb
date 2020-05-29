<template>
  <header id="home-section" class="landingView">
    <div class="primary-overlay dark-overlay mb-5 home">
      <div class="home-inner container home">
        <div class="row">
          <div class="col-lg-8 d-none d-lg-block mt-4">
            <h1 class="display-4">
              Build
              <strong>Website</strong> easily
              and
              <strong>reach more customers</strong>
            </h1>
            <div class="d-flex ml-5">
              <div class="p-2 slign-self-start">
                <i class="fas fa-check fa-2x"></i>
              </div>
              <div
                class="p-2 slign-self-end"
              >Website of websites : maintain your website in our website</div>
            </div>
            <div class="d-flex ml-5">
              <div class="p-2 slign-self-start">
                <i class="fas fa-check fa-2x"></i>
              </div>
              <div
                class="p-2 slign-self-end"
              >Platform for the shop owners to maintain their website easily</div>
            </div>
            <div class="d-flex ml-5">
              <div class="p-2 slign-self-start">
                <i class="fas fa-check fa-2x"></i>
              </div>
              <div class="p-2 slign-self-end">Get rid of high hosting and domain costs</div>
            </div>
            <div class="d-flex ml-5">
              <div class="p-2 slign-self-start">
                <i class="fas fa-check fa-2x"></i>
              </div>
              <div
                class="p-2 slign-self-end"
              >Create account and maintain your site and reach out more customers online</div>
            </div>
            <div class="d-flex ml-5">
              <div class="p-2 slign-self-start">
                <i class="fas fa-user fa-2x p-2"></i>
              </div>
              <router-link to="/signup">
                <div class="p-3 signUp">Sign Up Now</div>
              </router-link>
            </div>
          </div>
          <div class="col-lg-4 mt-4 mb-5">
            <div class="card formCenter text-center card-form mb-5">
              <div class="card-body">
                <h3>SEARCH FOR STORES</h3>
                <p>Enter the details of the shop around you and find their website easily</p>

                <div class="form-group">
                  <input type="text" class="form-control" placeholder="keywords" />
                </div>
                <div class="form-group">
                  <select v-model="val" class="form-control form-control">
                    <option value="paknajol">Paknajol</option>
                    <option value="kathnamdu">Kathmandu</option>
                    <option value="balaju">Balaju</option>
                  </select>
                </div>
                <div class="form-group">
                  <input
                    v-model="shopId"
                    type="number"
                    class="form-control form-control"
                    placeholder="shop no"
                  />
                </div>
                <div class="form-group">
                  <input type="text" class="form-control" placeholder="category" />
                </div>
                <div>
                  <div>
                    <div @click="search" class="btn btn-success btn-block">Search</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>
<script>
export default {
  data() {
    return {
      shopId: "",
      val: "this"
    };
  },
  created() {
    //yeslay 2 hrs khayo . default ma value bind  nahune bug raixa so created ma value change garayrw garayko 
    this.val = 'paknajol'
  },
  methods: {
    search() {
      console.log(this.val);
      // this.$router.push("/userWebsite/" + this.shopId);
  
    },
    select() {
      console.log("ayo");
    }
  }
};
</script>
<style scoped>
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