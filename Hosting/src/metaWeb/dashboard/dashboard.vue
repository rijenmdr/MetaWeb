<template>
  <div class="main">
    <div class="div1">
      <Sidebar :number="number" />
    </div>
    <div class="div2">
      <router-view></router-view>
    </div>
    <div></div>
  </div>
</template>
<script>
import axios from "axios";

import MainDash from "./mainDash";
import Sidebar from "./sidebar";
export default {
  data() {
    return {
      number: ""
    };
  },
  components: {
    MainDash,
    Sidebar
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
        "https://bibeklama.pythonanywhere.com/api/dashboard",
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
        this.number = res.data.data.length || 0;
        console.log(this.number);
        axios
          .post(
            "https://bibeklama.pythonanywhere.com/api/search_paid_user",
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
<style scoped > .mainDash {
  margin-top: 5vh;
}
.bibek {
  border-bottom: 1px solid white;

  margin-bottom: 10px;
  padding-top: 10px;
  box-sizing: border-box;
}
.logout-button {
  cursor: pointer;
}
.buttonCustom {
  margin-top: -20px;
}
.text1 {
  font-size: 12px;
}
.premium {
  border: 1px solid #cacfc9;
  color: #67ee46;
  padding-left: 10px;
  box-sizing: border-box;
}
.main {
  display: flex;
}
.div1 {
  width: 20%;
}
</style>

