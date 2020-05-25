<template>
     <nav class="navbar navbar-expand-md navbar-light fixed-top py-4p" id="main-nav">
    <div class="container">
      <a href="#home" class="navbar-brand">
        <img src="../../assets/mlogo.png" width="50" height="50" alt="" />
        <h3 class="d-inline align-middle">etaWeb</h3>
      </a>
      <button class="navbar-toggler" data-toggle="collapse" data-target="#navbarCollapse">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav ml-auto">
         
          <li class="nav-item">
            <a href="#how-it-works" class="nav-link">How it works</a>
          </li>
          <li class="nav-item">
            <a href="#about" class="nav-link">About Us</a>
          </li>
          <li class="nav-item">
            <a href="#contact" class="nav-link">Contact</a>
          </li>
          <li class="nav-item">
           
            <router-link to="/login" class="nav-link">Login</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>