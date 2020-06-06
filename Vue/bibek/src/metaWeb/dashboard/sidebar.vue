<template>
  <nav
    class="sidenav navbar navbar-vertical fixed-left navbar-expand-xs navbar-light bg-white"
    id="sidenav-main"
  >
    <div class="scrollbar-inner">
      <!-- Brand -->
      <div class="sidenav-header align-items-center">
        <router-link class="navbar-brand mr-lg-5 logo" to="/">
          Meta
          <span class="text1">web</span>
        </router-link>
      </div>
      <div class="navbar-inner">
        <!-- Collapse -->
        <div class="collapse navbar-collapse" id="sidenav-collapse-main">
          <!-- Nav items -->
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link to="/dashboard" class="nav-link">
                <i class="ni ni-tv-2 text-primary"></i>
                <span class="nav-link-text">Dashboard</span>
              </router-link>
            </li>

           

            <li v-if="number<=1 || paidUser" class="nav-item">
              <router-link to="/dashboard/createWebsite" class="nav-link">
                <i class="fas fa-edit text-success"></i>
                <span class="nav-link-text">Create</span>
              </router-link>
            </li>
            <li v-else class="nav-item">
              <router-link v-if="!paidUser" to="/upgradetopro" class="nav-link">
                <i class="fas fa-edit text-success"></i>
                <span  class="nav-link-text">Upgrate to Create</span>
              </router-link>
            </li>

            <li class="nav-item">
              <router-link to="/dashboard/delete" class="nav-link">
                <i class="fas fa-trash text-danger"></i>
                <span class="nav-link-text">Delete</span>
              </router-link>
            </li>

            <li class="nav-item">
              <router-link to="/dashboard/feedback" class="nav-link">
                <i class="ni ni-bullet-list-67 text-default"></i>
                <span class="nav-link-text">Feedbacks</span>
              </router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="profile.html">
                <i class="ni ni-single-02 text-yellow"></i>
                <span class="nav-link-text">Profile</span>
              </a>
            </li>
            <li v-if="!paidUser" class="nav-item">
              <router-link class="nav-link" to="/upgradetopro">
                <i class="ni ni-send text-dark"></i>
                <span class="nav-link-text">Upgrade</span>
              </router-link>
            </li>
            <li v-if="paidUser" class="nav-item" data-toggle="modal" data-target="#modalProUser">
              <router-link to="/dashboard/protemplates" class="nav-link">
                <i class="fa fa-pencil-square text-primary" aria-hidden="true"></i>
                <span class="nav-link-text">Pro Template</span>
              </router-link>
            </li>

            <li v-if="paidUser" class="nav-item">
              <router-link class="nav-link" to="/upgradetopro">
                <i class="fa fa-product-hunt text-success" aria-hidden="true"></i>
                <span class="nav-link-text">Custom Templates</span>
              </router-link>
            </li>
          </ul>
          <!-- Divider -->
          <hr class="my-3" />
        </div>
      </div>
    </div>
  </nav>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      paidUser: ""
    };
  },
  props: ["number"],
  methods: {
    logout() {
      this.$store.dispatch("logout");
      this.$router.push("/");
    }
  },
  created() {
    setTimeout(() => {
      console.log(this.$store.getters.getPaidUser);
      this.paidUser = this.$store.getters.getPaidUser;
    }, 1000);
  }
};
</script>
<style  scoped>
a:hover {
  text-decoration: none;
}
@import url("https://fonts.googleapis.com/css2?family=Cabin:wght@700&display=swap");
.logo {
  font-size: 22px;
  font-family: "Cabin", sans-serif;
}
.text1 {
  color: #d3b001;
}
</style>
