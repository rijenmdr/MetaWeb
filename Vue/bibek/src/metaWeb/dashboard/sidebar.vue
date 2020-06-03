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
            <li class="nav-item">
              <router-link to="/dashboard/createWebsite" class="nav-link">
                <i class="ni ni-planet text-orange"></i>
                <span class="nav-link-text">Create</span>
              </router-link>
            </li>
            <li class="nav-item">
              <router-link to="/dashboard/delete" class="nav-link">
                <i class="fas fa-trash"></i>
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
            <li class="nav-item">
              <router-link class="nav-link" to="/upgradetopro">
                <i class="ni ni-send text-dark"></i>
                <span class="nav-link-text">Upgrade</span>
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
export default {
  data() {
    return {
      user: this.$store.getters.getUser || localStorage.getItem("user")
    };
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
      this.$router.push("/");
    }
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
