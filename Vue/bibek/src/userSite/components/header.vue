<template>
  <nav class="navbar navbar-expand-sm navbar-dark" :style="{backgroundColor:backgroundColor}">
    <div class="container">
      <div class="navbar-brand text">{{nameOfSite}}</div>
      <button class="navbar-toggler" data-toggle="collapse" data-target="#navbarcollapse">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarcollapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link to="/userWebsite/about" class="nav-link">{{menu2}}</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/userWebsite/services" class="nav-link">{{menu3}}</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/userWebsite/contact" class="nav-link">{{menu4}}</router-link>
          </li>
          <li class="nav-item">
            <a href="contact.html" class="nav-link">{{menu5}}</a>
          </li>
          <li class="nav-item">
            <router-link v-if="loggedin" to="/dashboard" class="nav-link">Dashboard</router-link>
            <a v-else href="/" class="nav-link">metaWeb</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
<script>
import axios from "axios";
export default {
  props: ["nameOfSite", "backgroundColor"],
  data() {
    return {
      title: "this",
      menu1: "Home",
      menu2: "About",
      menu3: "Services",
      menu4: "Contact",
      menu5: "",
      textColor: "red",
      loggedin: this.$store.getters.getToken
    };
  },
  created() {
    console.log(this.$store.getters.getWebsite.backgroundColor);
  }
};
</script>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Righteous&display=swap");
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
.navbarUser {
  background: yellow;
}
.text {
  color: white;
  font-family: "Righteous", cursive;
  font-size: 20px;
  cursor: pointer;
}
</style>