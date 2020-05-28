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
    let data={
      token:this.$store.getters.getToken,
      user:this.$store.getters.getUser
    }
    await this.$store.dispatch("setUserSite",data);
  }
};
</script>