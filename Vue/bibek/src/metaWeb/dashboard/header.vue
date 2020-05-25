<template>
    <div>
        <nav class="navbar navbar-expand-sm bg-dark navbar-dark p-0">
      <div class="container">
        <a href="../index.html" class="navbar-brand">meroStore</a>
        <button
          class="navbar-toggler"
          data-toggle="collapse"
          data-target="#collapseNavbar"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="collapseNavbar">
          <ul class="navbar-nav">
            <li class="nav-item px-2">
              <a class="nav-link active" href="index.html">
                Dashboard
              </a>
            </li>

            <li class="nav-item px-2">
              <a class="nav-link" href="posts.html">
                Posts
              </a>
            </li>

            <li class="nav-item px-2">
              <a class="nav-link" href="categories.html">
                Categories
              </a>
            </li>
            <li class="nav-item px-2">
              <a class="nav-link" href="users.html">
                Users
              </a>
            </li>
          </ul>

          <ul class="navbar-nav ml-auto">
            <li class="nav-item dropdown mr-3">
              <a
                href="#"
                class="nav-link dropdown-toggle"
                data-toggle="dropdown"
              >
                <i class="fas fa-user mr-1"></i>Welcome {{user}}
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
            <li class="nav-item"  @click="logout">
              <div class="nav-link">
                <i class="fas fa-user-times"></i> Logout
              </div>
            </li>
          </ul>
        </div>
      </div>
    </nav>
     <header id="main-header" class="py-2 bg-primary text-white">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <h1><i class="fas fa-cog"></i> Dashboard</h1>
          </div>
        </div>
      </div>
    </header>
    
    </div>
</template>
<script>
export default {
  data(){
    return{
      user:this.$store.getters.getUser
    }
  },
  methods:{
     logout(){
                this.$store.dispatch('logout')
                this.$router.push('/')
            }
  }
}
</script>