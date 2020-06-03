<template>
  <div>
    <Sidebar/>
    <!-- Main content -->
    <router-view></router-view>
  </div>
</template>
<script>
import axios from "axios";
import Sidebar from "./sidebar";
import Actions from "./actions";
import Footer from "../home/footer";
import MainDash from "./mainDash";
export default {
  components: {
    Sidebar,
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
<style scoped>
@import "../../assets/assetsDash/css/argon.css?v=1.2.0";

</style>

