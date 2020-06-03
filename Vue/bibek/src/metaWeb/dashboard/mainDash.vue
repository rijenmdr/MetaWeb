<template>
  <div class="main-content" id="panel">
    <!-- Header -->
    <!-- Header -->
    <div class="header bg-primary pb-6">
      <div class="container-fluid">
        <div class="header-body">
          <div class="row align-items-center bibek">
            <div class="col-lg-7 col-7"></div>
            <div class="col-lg-5 col-7">
              <h6 class="h4 text-white d-inline-block mb-0 mt">Welcome {{user}}</h6>
              <nav aria-label="breadcrumb" class="d-none d-md-inline-block ml-md-5">
                <ol
                  @click="logout"
                  class="breadcrumb breadcrumb-links breadcrumb-dark logout-button"
                >
                  <li class="breadcrumb-item active" aria-current="page">Logout</li>
                </ol>
              </nav>
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
                      <span class="h2 font-weight-bold mb-0">24</span>
                    </div>
                    <div class="col-auto">
                      <div
                        class="icon icon-shape bg-gradient-green text-white rounded-circle shadow"
                      >
                        <i class="ni ni-money-coins"></i>
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
      user: this.$store.getters.getUser || localStorage.getItem("user")
    };
  },
  async created() {
    let JWTToken = localStorage.getItem("token");
    if (!JWTToken) {
      JWTToken = this.$store.getters.getToken;
    }
    let user = localStorage.getItem("user");
    if (!user) {
      user = this.$store.getters.getUser;
    }
    console.log(user);
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
</style>