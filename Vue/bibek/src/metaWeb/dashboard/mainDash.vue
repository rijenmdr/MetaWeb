<template>
  <section id="posts">
    <div class="container mainDash">
      <div class="row">
        <div class="col-md-9">
          <div class="card">
            <div class="card-header">
              <h4>Your Websites :</h4>
            </div>
            <table class="table table-striped">
              <thead class="thead-dark">
                <tr>
                  <th>Shop Id</th>
                  <th>Name of Site</th>
                  <th>Date Created</th>
                  <th>Edit</th>
                  <th>View</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="site in sites">
                  <th>{{site.id}}</th>
                  <th>{{site.nameOfSiteH}}</th>
                  <th>{{site.created_date}}</th>
                  <th>
                    <div @click="edit(site.id)" class="btn btn-secondary">
                      <i class="fas fa-edit"></i>Edit
                    </div>
                  </th>
                  <th>
                    <div @click="view(site.id)" class="btn btn-secondary">
                      View
                      <i class="fas fa-angle-double-right"></i>
                    </div>
                  </th>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div class="col-md-3">
          <div class="card text-center bg-primary text-white mb-3">
            <div class="card-body">
              <h3>My Website</h3>
              <h4 class="display-4">
                <i class="fas fa-pencil-alt"></i>
                {{number}}
              </h4>
              <router-link class="btn btn-outline-light btn-sm" to="/createWebsite">Create</router-link>
            </div>
          </div>
          <div class="card text-center bg-success text-white mb-3">
            <div class="card-body">
              <h3>Delete Website</h3>
              <h4 class="display-4">
                <i class="fas fa-trash"></i>
              </h4>
              <router-link to="/dashboard/delete" class="btn btn-outline-light btn-sm">Delete</router-link>
            </div>
          </div>
          <div class="card text-center bg-warning text-white mb-3">
            <div class="card-body">
              <h3>Customer Feedback</h3>
              <h4 class="display-4">
                <i class="fas fa-folder"></i>
                3
              </h4>
              <a href="user.html" class="btn btn-outline-light btn-sm">See more</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      sites: "",
      number:''
    };
  },
  async created() {
    let JWTToken = localStorage.getItem("token");
    if (!JWTToken) {
      JWTToken = this.$store.getters.getToken;
    }
    let user = this.$store.getters.getUser;
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
        this.number=res.data.data.length;
      });
  },
  methods: {
    view(id) {
      this.$router.push("/userWebsite/" + id);
    },
    edit(id) {
      this.$router.push("/editWebsite/" + id);
    }
  }
};
</script>
<style scoped>
.mainDash {
  margin-top: 5vh;
}
</style>