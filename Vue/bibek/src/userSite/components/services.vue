<template>
  <div>
    <Header :nameOfSite="nameOfSite" :backgroundColor="backgroundColor" id="3" />
    <section id="services" class="py-5">
      <div class="container mb-5 mt-5">
        <div class="row">
          <div class="col-md-4">
            <div class="card text-center">
              <div class="card-header text-white bg-color">
                <h3 class="text">Service One</h3>
              </div>
              <div class="card-body">
                <h4 class="card-title">{{serviceOne}}</h4>
                <p>{{serviceOneDes}}</p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card text-center">
              <div class="card-header bg-color text-white">
                <h3 class="text">Service Two</h3>
              </div>
              <div class="card-body">
                <h4 class="card-title">{{serviceTwo}}</h4>
                <p>{{serviceTwoDes}}</p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card text-center">
              <div class="card-header bg-color text-white">
                <h3 class="text">Service Three</h3>
              </div>
              <div class="card-body">
                <h4 class="card-title">{{serviceThree}}</h4>
                <p>{{serviceThreeDes}}</p>
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
import Header from "./componentHead";
import Footer from "./footer";
export default {
  components: {
    Header,
    Footer
  },
  data() {
    return {
      serviceOne: this.$store.getters.getWebsite.serviceOne,
      serviceTwo: this.$store.getters.getWebsite.serviceTwo,
      serviceThree: this.$store.getters.getWebsite.serviceThree,
      serviceOneDes: this.$store.getters.getWebsite.serviceOneDes,
      serviceTwoDes: this.$store.getters.getWebsite.serviceTwoDes,
      serviceThreeDes: this.$store.getters.getWebsite.serviceThreeDes,
      backgroundColor: this.$store.getters.getWebsite.backgroundColor,
      nameOfSite: this.$store.getters.getWebsite.nameOfSiteH
    };
  }
};
</script>
<style scoped>
.bg-color {
  background: #787575;
}
.text {
  color: white;
}
</style>