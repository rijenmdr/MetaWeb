<template>
  <nav class="navbar navbar-expand-sm navbar-dark" :style="{backgroundColor:backgroundColor}">
    <div class="container">
      <a href="index.html" class="navbar-brand">{{nameOfSite}}</a>
      <button class="navbar-toggler" data-toggle="collapse" data-target="#navbarcollapse">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarcollapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link :to="home" class="nav-link">{{menu1}}</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/userWebsite/about" class="nav-link" :class="{active:id==2}">{{menu2}}</router-link>
          </li>
          <li class="nav-item">
            <router-link
              to="/userWebsite/services"
              class="nav-link"
              :class="{active:id==3}"
            >{{menu3}}</router-link>
          </li>
          <li class="nav-item">
            <router-link
              to="/userWebsite/contact"
              class="nav-link"
              :class="{active:id==4}"
            >{{menu4}}</router-link>
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
  props: ["nameOfSite", "id"],
  data() {
    return {
      title: "this",
      menu1: "Home",
      menu2: "About",
      menu3: "Services",
      menu4: "Contact",
      menu5: "",
      backgroundColor: this.$store.getters.getWebsite.backgroundColor,
      home: this.$store.getters.getWebsite.id.toString()
    };
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