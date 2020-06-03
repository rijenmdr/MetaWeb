<template>
  <nav
    id="navbar-main"
    class="navbar navbar-main navbar-expand-lg navbar-transparent navbar-light headroom"
  >
    <div class="container">
      <router-link class="navbar-brand mr-lg-5 logo" to="/">Meta<span class="text1">web</span></router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbar_global"
        aria-controls="navbar_global"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="navbar-collapse collapse" id="navbar_global">
        <div class="navbar-collapse-header">
          <div class="row">
            <div class="col-6 collapse-brand">
              <a href="./index.html">
                <img src="./assets/img/brand/blue.png" />
              </a>
            </div>
            <div class="col-6 collapse-close">
              <button
                type="button"
                class="navbar-toggler"
                data-toggle="collapse"
                data-target="#navbar_global"
                aria-controls="navbar_global"
                aria-expanded="false"
                aria-label="Toggle navigation"
              >
                <span></span>
                <span></span>
              </button>
            </div>
          </div>
        </div>
        <ul class="navbar-nav navbar-nav-hover align-items-lg-center">
          <li class="nav-item dropdown">
            <a href="#" class="nav-link" data-toggle="dropdown" role="button">
              <i class="ni ni-ui-04 d-lg-none"></i>
              <span class="nav-link-inner--text">why us ?</span>
            </a>
            <div class="dropdown-menu dropdown-menu-xl">
              <div class="dropdown-menu-inner">
                <a
                  href="https://demos.creative-tim.com/argon-design-system/docs/getting-started/overview.html"
                  class="media d-flex align-items-center"
                >
                  <div class="icon icon-shape bg-gradient-primary rounded-circle text-white">
                    <i class="ni ni-spaceship"></i>
                  </div>
                  <div class="media-body ml-3">
                    <h6 class="heading text-primary mb-md-1">Getting started</h6>
                    <p class="description d-none d-md-inline-block mb-0">Build websites on our site</p>
                  </div>
                </a>
                <a
                  href="https://demos.creative-tim.com/argon-design-system/docs/foundation/colors.html"
                  class="media d-flex align-items-center"
                >
                  <div class="icon icon-shape bg-gradient-success rounded-circle text-white">
                    <i class="ni ni-palette"></i>
                  </div>
                  <div class="media-body ml-3">
                    <h6 class="heading text-primary mb-md-1">Share Shop Ids</h6>
                    <p
                      class="description d-none d-md-inline-block mb-0"
                    >Share your shop id with customers so that they can get you online within our site</p>
                  </div>
                </a>
                <a
                  href="https://demos.creative-tim.com/argon-design-system/docs/components/alerts.html"
                  class="media d-flex align-items-center"
                >
                  <div class="icon icon-shape bg-gradient-warning rounded-circle text-white">
                    <i class="ni ni-ui-04"></i>
                  </div>
                  <div class="media-body ml-3">
                    <h5 class="heading text-warning mb-md-1">As an Invidual</h5>
                    <p
                      class="description d-none d-md-inline-block mb-0"
                    >You can get the information about the shops and their services around you</p>
                  </div>
                </a>
              </div>
            </div>
          </li>
        </ul>
        <ul class="navbar-nav align-items-lg-center ml-lg-auto">
          <li class="nav-item">
            <a
              class="nav-link nav-link-icon"
              href="https://www.facebook.com/"
              target="_blank"
              data-toggle="tooltip"
              title="Like us on Facebook"
            >
              <i class="fa fa-facebook-square"></i>
              <span class="nav-link-inner--text d-lg-none">Facebook</span>
            </a>
          </li>
          <li class="nav-item">
            <a
              class="nav-link nav-link-icon"
              href="https://www.instagram.com/"
              target="_blank"
              data-toggle="tooltip"
              title="Follow us on Instagram"
            >
              <i class="fa fa-instagram"></i>
              <span class="nav-link-inner--text d-lg-none">Instagram</span>
            </a>
          </li>
          <li class="nav-item">
            <a
              class="nav-link nav-link-icon"
              href="https://twitter.com/"
              target="_blank"
              data-toggle="tooltip"
              title="Follow us on Twitter"
            >
              <i class="fa fa-twitter-square"></i>
              <span class="nav-link-inner--text d-lg-none">Twitter</span>
            </a>
          </li>

          <li class="nav-item d-none d-lg-block ml-lg-4">
            <router-link to="/signup" class="btn btn-neutral btn-icon">
              <span class="btn-inner--icon">
                <i class="fas fa-user-plus"></i>
              </span>
              <span class="nav-link-inner--text"> Register</span>
            </router-link>
            <router-link to="/login" class="btn btn-neutral btn-icon">
              <span class="btn-inner--icon">
                <i class="fas fa-sign-in-alt"></i>
              </span>
              <span class="nav-link-inner--text"> Login</span>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
<style scoped>
@import "../../assets/css/nucleo-icons.css";
@import "../../assets/css/font-awesome.css";
@import "../../assets/css/argon-design-system.css?v=1.2.0";
@import url("https://fonts.googleapis.com/css2?family=Cabin:wght@700&display=swap");
.logo {
  font-size: 22px;
  font-family: 'Cabin', sans-serif;
}
.text1{
  color: #D3B001;
}
</style>