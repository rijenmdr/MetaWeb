<template>
  <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
    <div class="container">
      <a href="index.html" class="navbar-brand">{{title}}</a>
      <button class="navbar-toggler" data-toggle="collapse" data-target="#navbarcollapse">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarcollapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <a href="index.html" class="nav-link">{{menu1}}</a>
          </li>
          <li class="nav-item">
            <a href="about.html" class="nav-link">{{menu2}}</a>
          </li>
          <li class="nav-item">
            <a href="services.html" class="nav-link">{{menu3}}</a>
          </li>
          <li class="nav-item">
            <a href="blog.html" class="nav-link">{{menu4}}</a>
          </li>
          <li class="nav-item">
            <a href="contact.html" class="nav-link">{{menu5}}</a>
          </li>
          <li class="nav-item">
            <a href="../index.html" class="nav-link">MeroStore Home</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      title: "this",
      menu1: "",
      menu2: "",
      menu3: "",
      menu4: "",
      menu5: ""
    };
  },
  created() {
    let JWTToken = localStorage.getItem("token");
    let id = this.$store.getters.getWebId;
    console.log(id);
    axios
      .get("http://localhost:8000/api/get_website/" + id, {
        headers: {
          Authorization: `Token ${JWTToken}`
        }
      })
      .then(res => {
        (this.title = res.data.book.title),
          (this.menu1 = res.data.book.menu1),
          (this.menu2 = res.data.book.menu2),
          (this.menu3 = res.data.book.menu3),
          (this.menu4 = res.data.book.menu4),
          (this.menu5 = res.data.book.menu5);
      });
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