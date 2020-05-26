<template>
  <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
    <div class="container">
      <a href="index.html" class="navbar-brand">{{nameOfSite}}</a>
      <button class="navbar-toggler" data-toggle="collapse" data-target="#navbarcollapse">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarcollapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link :to='home' class="nav-link">{{menu1}}</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/userWebsite/about" class="nav-link">{{menu2}}</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/userWebsite/contact" class="nav-link">{{menu3}}</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/userWebsite/about" class="nav-link">{{menu4}}</router-link>
          </li>
          <li class="nav-item">
            <a href="contact.html" class="nav-link">{{menu5}}</a>
          </li>
          <li class="nav-item">
            <a href="/" class="nav-link">metaWeb</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
<script>
import axios from "axios";
export default {
  props: ["nameOfSite"],
  data() {
    return {
      title: "this",
      menu1: "Home",
      menu2: "About",
      menu3: "Contact",
      menu4: "",
      menu5: "",
      home:this.$store.getters.getWebsite.id.toString()
    };
  },
  created(){
      console.log(this.$store.getters.getWebsite.id)
  }
};
</script>
<style scoped>
body {
  overflow-x: hidden;
}
.navbar .nav-link {
  font-size: 14px;
  text-transform: uppercase;
  padding-left: 1rem !important;
  padding-right: 1rem !important;
}
.navbar .nav-item.active {
  border-left: #444 3px solid;
}
</style>