<template>
  <div class="main-content" id="panel">
    <!-- Header -->
    <!-- Header -->
    <div class="header bg-primary pb-6">
      <div class="container-fluid">
        <div class="header-body">
          <div class="row align-items-center bibek">
            <div class="col-lg-7 col-7"></div>
            <div class="col-lg-5 col-7 mt-3">
              <!-- <h6 class="h5 text-white d-inline-block ml-5">Welcome {{user}}</h6> -->
              <nav class="d-none d-md-inline-block ml-md-5 float-right">
                <button
                  type="button"
                  class="btn btn-white btn-sm buttonCustom"
                  data-toggle="modal"
                  data-target="#exampleModalCenter"
                >
                  <i class="fa fa-sign-out" aria-hidden="true"></i>Logout
                </button>
              </nav>
              <nav class="d-none d-md-inline-block ml-md-5 float-right">
                <div
              
                  class="btn text-white btn-sm buttonCustom"
                 
                >
                  <i class="fa fa-user" aria-hidden="true"></i> Welcome {{user}}
                </div>
              </nav>
            </div>
          </div>
          <!-- Modal -->
          <div
            class="modal fade"
            id="exampleModalCenter"
            tabindex="-1"
            role="dialog"
            aria-labelledby="exampleModalCenterTitle"
            aria-hidden="true"
          >
            <div class="modal-dialog modal-dialog-centered" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLongTitle">Alert</h5>
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div class="modal-body">You will be logged out of this session !!!</div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                  <button
                    @click="logout"
                    type="button"
                    data-dismiss="modal"
                    class="btn btn-primary"
                  >Continue</button>
                </div>
              </div>
            </div>
          </div>
          <!-- Card stats -->
          <div class="row">
            <div class="col-xl-3 col-md-6">
              <div class="card card-stats">
                <!-- Card body -->
                <div class="card-body">
                  <div class="row">
                    <div class="col">
                      <h5 class="card-title text-uppercase text-muted mb-0">Total Web Visits</h5>
                      <span class="h2 font-weight-bold mb-0">900</span>
                    </div>
                    <div class="col-auto">
                      <div class="icon icon-shape bg-gradient-red text-white rounded-circle shadow">
                        <i class="ni ni-active-40"></i>
                      </div>
                    </div>
                  </div>
                  <p class="mt-3 mb-0 text-sm">
                    <span class="text-success mr-2">
                      <i class="fa fa-arrow-up"></i> 3.48%
                    </span>
                    <span class="text-nowrap">Since last month</span>
                  </p>
                </div>
              </div>
            </div>
            <div class="col-xl-3 col-md-6">
              <div class="card card-stats">
                <!-- Card body -->
                <div class="card-body">
                  <div class="row">
                    <div class="col">
                      <h5 class="card-title text-uppercase text-muted mb-0">Feedback</h5>
                      <span class="h2 font-weight-bold mb-0">2</span>
                    </div>
                    <div class="col-auto">
                      <div
                        class="icon icon-shape bg-gradient-orange text-white rounded-circle shadow"
                      >
                        <i class="ni ni-chart-pie-35"></i>
                      </div>
                    </div>
                  </div>
                  <p class="mt-3 mb-0 text-sm">
                    <span class="text-success mr-2">
                      <i class="fa fa-arrow-up"></i> 3.48%
                    </span>
                    <span class="text-nowrap">Since last month</span>
                  </p>
                </div>
              </div>
            </div>
            <div class="col-xl-3 col-md-6">
              <div class="card card-stats">
                <!-- Card body -->
                <div class="card-body">
                  <div class="row">
                    <div class="col">
                      <h5 class="card-title text-uppercase text-muted mb-0">Total Websites</h5>
                      <span class="h2 font-weight-bold mb-0">{{number}}</span>
                    </div>
                    <div class="col-auto">
                      <div
                        class="icon icon-shape bg-gradient-info text-white rounded-circle shadow"
                      >
                        <i class="ni ni-chart-bar-32"></i>
                      </div>
                    </div>
                  </div>
                  <p class="mt-3 mb-0 text-sm">
                    <span class="text-success mr-2">
                      <i class="fa fa-arrow-up"></i> 3.48%
                    </span>
                    <span class="text-nowrap">Since last month</span>
                  </p>
                </div>
              </div>
            </div>
            <div class="col-xl-3 col-md-6">
              <div class="card card-stats">
                <!-- Card body -->
                <div class="card-body">
                  <div class="row">
                    <div class="col">
                      <h5 class="card-title text-uppercase text-muted mb-0">Remaining Days</h5>
                      <span v-if="paidUserInfo" class="h2 font-weight-bold mb-0">{{remainingDays}}</span>
                      <span v-else class="h2 font-weight-bold mb-0">000</span>
                    </div>
                    <div class="col-auto">
                      <div
                        class="icon icon-shape bg-gradient-green text-white rounded-circle shadow"
                      >
                        <i class="ni ni-money-coins"></i>
                      </div>
                    </div>
                  </div>
                  <p v-if="paidUserInfo" class="mt-3 mb-0 text-sm">
                    <span class="text-success mr-2">
                      <i class="fa fa-arrow-up"></i> Upgraded On :
                    </span>
                    <span class="text-nowrap">{{created_year}}/{{created_month}}/{{created_day}}</span>
                  </p>
                  <p v-else class="mt-3 mb-0 text-sm">
                    <span class="text-nowrap text-danger text1">Please Upgrade to Standard plan</span>
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Page content -->
    <div class="container-fluid mt--6">
      <div class="row">
        <div class="col-xl-12">
          <div class="card">
            <div class="card-header border-0">
              <div class="row align-items-center">
                <div class="col">
                  <h3 class="mb-0">Your Websites</h3>
                </div>
                <div class="col text-right">
                  <a href="#!" class="btn btn-sm btn-primary">See all</a>
                </div>
              </div>
            </div>
            <div class="table-responsive">
              <!-- Projects table -->
              <table class="table align-items-center table-flush">
                <thead class="thead-light">
                  <tr>
                    <th scope="col">Shop Id</th>
                    <th scope="col">Name of Site</th>
                    <th scope="col">Date Created</th>
                    <th scope="col">Edit</th>
                    <th scope="col">Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="site in sites">
                    <th scope="row">{{site.id}}</th>
                    <td>{{site.nameOfSiteH}}</td>
                    <td>{{site.created_date}}</td>
                    <td>
                      <div @click="edit(site.id)" class="btn btn-secondary">
                        <i class="fas fa-edit"></i> Edit
                      </div>
                    </td>
                    <td>
                      <div @click="view(site.id)" class="btn btn-secondary">
                        View
                        <i class="fas fa-angle-double-right"></i>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
      <!-- Footer -->
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      sites: "",
      number: "",
      user: this.$store.getters.getUser || localStorage.getItem("user"),
      paidUserInfo: null,
      remainingDays: "",
      created_year: "",
      created_month: "",
      created_day: ""
    };
  },
  async created() {
    setTimeout(() => {
      let paidUserInfo = this.$store.getters.getPaidUserInfo;
      if (paidUserInfo.length == 0) {
        this.paidUserInfo = null;
      } else this.paidUserInfo = paidUserInfo;
      if (this.paidUserInfo.length > 0) {
        let Ttime = this.$store.getters.getPaidUserInfo[0].created_date;
        let time = new Date(Ttime);
        this.created_year = time.getFullYear();
        this.created_month = time.getMonth();
        this.created_day = time.getDate();
        let d = new Date();
        let difference = (d.getTime() - time.getTime()) / 1000;
        let days = difference / 86400;
        this.remainingDays = 30 - Math.floor(days);
        // this.remainingDays = 30 - 30;
        if (this.remainingDays == 0) {
          if (this.$store.getters.getPaidUser == "present") {
            this.$store.dispatch("removePaidUser");
            this.$store.dispatch("setAlert");
            this.$router.push("/dateExpired");
          }
        } else {
          this.$store.dispatch("setRemainingDays", this.remainingDays);
        }
      }
    }, 300);
    let JWTToken = localStorage.getItem("token");
    if (!JWTToken) {
      JWTToken = this.$store.getters.getToken;
    }
    let user = localStorage.getItem("user");
    if (!user) {
      user = this.$store.getters.getUser;
    }

    await axios
      .post(
        "http://localhost:8000/api/dashboard",
        {
          user: user
        },
        {
          headers: {
            Authorization: `Token ${JWTToken}`
          }
        }
      )
      .then(res => {
        this.sites = res.data.data;
        this.number = res.data.data.length;
      });
  },
  methods: {
    view(id) {
      this.$router.push("/userWebsite/" + id);
    },
    edit(id) {
      this.$router.push("/editWebsite/" + id);
    },
    logout() {
      this.$store.dispatch("logout");
      this.$router.push("/");
    }
  }
};
</script>
<style scoped>
.mainDash {
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
</style>