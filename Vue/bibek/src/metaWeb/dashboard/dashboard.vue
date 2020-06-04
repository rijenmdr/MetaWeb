<template>
  <div>
    <Sidebar :number="number" />
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
  data() {
    return {
      number: ""
    };
  },
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
    await axios
      .post(
        "http://localhost:8000/api/dashboard",
        {
          user: user
        },
        {
          headers: {
            Authorization: `Token ${token}`
          }
        }
      )
      .then(res => {
        this.number = res.data.data.length;
        axios
          .post(
            "http://localhost:8000/api/search_paid_user",
            {
              username: user
            },
            {
              headers: {
                Authorization: `Token ${token}`
              }
            }
          )
          .then(res => {
            if (res.data.paidUser.length > 0) {
              if (this.$store.getters.getAlert) {
                this.$store.dispatch("setPaidUser", res.data.paidUser);
              }
            }
          })
          .catch(err => {
            console.log("error");
            console.log(err);
          });
      });
  }
};
</script>
<style scoped>
@import "../../assets/assetsDash/css/argon.css?v=1.2.0";
</style>

