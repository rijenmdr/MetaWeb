<template>
  <div>
    <Header :nameOfSite="nameOfSite" :id="2" :backgroundColor="backgroundColor" />
    <header id="page-header">
      <div class="container">
        <div class="row">
          <div class="col-md-6 m-auto text-center">
            <h1 class="text">About Us</h1>
            <p>{{introduction}}</p>
          </div>
        </div>
      </div>
    </header>
    <!-- About section -->
    <section id="about" class="py-3">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <h1>What We Do</h1>
            <p>{{whatWeDoA}}</p>
          </div>
          <div class="col-md-6">
            <img
              src="https://source.unsplash.com/random/700x700/?technology"
              alt
              class="img-fluid rounded-circle d-none d-md-block about-img"
            />
          </div>
        </div>
      </div>
    </section>
    <!-- Icon Boxes -->
    <section id="icon-boxes" class="p-5">
      <div class="container">
        <div class="row mb-4">
          <div class="col-md-4">
            <div class="card bg-danger text-white text-center">
              <div class="card-body">
                <i class="fas fa-building fa-3x"></i>
                <h3>Sample heading</h3>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laboriosam ipsum non
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card bg-info text-white text-center">
              <div class="card-body">
                <i class="fas fa-bullhorn fa-3x"></i>
                <h3>Books</h3>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laboriosam ipsum non
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card bg-danger text-white text-center">
              <div class="card-body">
                <i class="fas fa-comments fa-3x"></i>
                <h3>Pasal</h3>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laboriosam ipsum non
              </div>
            </div>
          </div>
          <div class="col-md-4"></div>
          <div class="col-md-4"></div>
        </div>
        <div class="row mb-4">
          <div class="col-md-4">
            <div class="card bg-dark text-white text-center">
              <div class="card-body">
                <i class="fas fa-box fa-3x"></i>
                <h3>Sample heading</h3>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laboriosam ipsum non
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card bg-danger text-white text-center">
              <div class="card-body">
                <i class="fas fa-credit-card fa-3x"></i>
                <h3>Books</h3>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laboriosam ipsum non
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card bg-dark text-white text-center">
              <div class="card-body">
                <i class="fas fa-coffee fa-3x"></i>
                <h3>Pasal</h3>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laboriosam ipsum non
              </div>
            </div>
          </div>
          <div class="col-md-4"></div>
          <div class="col-md-4"></div>
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
      introduction: this.$store.getters.getWebsite.introductionA,
      whatWeDoA: this.$store.getters.getWebsite.whatWeDoA,
      nameOfSite: this.$store.getters.getWebsite.nameOfSiteH,
      backgroundColor: this.$store.getters.getWebsite.backgroundColor,
      id: this.$store.getters.getWebsite.id
    };
  }
};
</script>
<style scoped>
#page-header {
  height: 200px;
  background: url("../../assets/image1.jpg");
  background-position: 0 -300px;
  background-attachment: fixed;
  color: #fff;
  border-bottom: 1px #eee solid;
  padding-top: 50px;
}
.text {
  color: white;
}
</style>
    
