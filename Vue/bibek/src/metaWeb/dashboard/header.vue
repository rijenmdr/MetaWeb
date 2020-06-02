<template>
  <div>
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark p-0">
      <div class="container">
        <router-link to="/" class="navbar-brand">
          <img src="../../assets/mlogo.png" width="50" height="50" alt />
          <h3 class="d-inline align-middle">etaWeb</h3>
        </router-link>
        <button class="navbar-toggler" data-toggle="collapse" data-target="#collapseNavbar">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="collapseNavbar">
          <ul class="navbar-nav">
            <!-- <li class="nav-item px-2">
              <a class="nav-link active" href="index.html">
                Dashboard
              </a>
            </li>-->
          </ul>

          <ul class="navbar-nav ml-auto">
            <li class="nav-item dropdown mr-3">
              <a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown">
                <i class="fas fa-user mr-1"></i>
                Welcome {{user}}
              </a>
              <div class="dropdown-menu">
                <a href="profile.html" class="dropdown-item">
                  <i class="fas fa-user-circle"></i>Profile
                </a>
                <a href="settings.html" class="dropdown-item">
                  <i class="fas fa-cog"></i>Settings
                </a>
              </div>
            </li>
            <li class="nav-item" @click="logout">
              <div class="nav-link">Logout</div>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <header id="main-header" class="py-2 bg-primary text-white">
      <div class="container">
        <div class="row">
          <div class="col-md-9">
            <router-link to="/dashboard" class="text-white dashboard">
              <h1>
                <i class="fas fa-cog"></i> Dashboard
              </h1>
            </router-link>
          </div>
          <div class="col-md-3 mt-2">
            <router-link to="/upgradetopro" class="text-white dashboard">
              <h4>
                <i class="fas fa-shopping-cart"></i> Upgrade to Pro
              </h4>
            </router-link>
          </div>
        </div>
      </div>
    </header>
  </div>
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
</style>>

</style>