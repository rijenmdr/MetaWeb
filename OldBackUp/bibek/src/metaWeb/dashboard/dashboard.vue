<template>
  <div>
    <Header />

    <router-view></router-view>

    <Footer />
  </div>
</template>
<script>
import axios from "axios";
import Header from "./header";
import Actions from "./actions";
import Footer from "../home/footer";
import MainDash from "./mainDash";
export default {
  components: {
    Header,
    Footer,
    Actions,
    MainDash
  },
  async created() {
    let token = this.$store.getters.getToken;
    if (!token) {
      token = localStorage.getItem("token");
    }
    let user = this.$store.getters.getUser;
    if (!user) {
      user = localStorage.getItem("user");
    }
    let data = {
      token: token,
      user: user
    };
    await this.$store.dispatch("setUserSite", data);
  }
};
</script>