<template>
  <div>
    <div class="container mainDash">
      <div class="row">
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              <h4>FeedBacks :</h4>
            </div>
            <table class="table table-striped">
              <thead class="thead-dark">
                <tr>
                  <th>Visitor Id</th>
                  <th>First Name</th>
                  <th>Last Name</th>
                  <th>Email</th>

                  <th>Message</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="feed in feeds">
                  <th>{{feed.id}}</th>
                  <th>{{feed.first_name}}</th>
                  <th>{{feed.last_name}}</th>
                  <th>{{feed.email}}</th>
                  <th>{{feed.message}}</th>
                  <th>
                    <div @click="deleteFeed(feed.id)" class="btn btn-danger">
                      <i class="fas fa-trash"></i>
                    </div>
                  </th>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      feeds: ""
    };
  },
  created() {
    let shopid = this.$route.params.shopid;
    axios.get("http://localhost:8000/api/get_review/" + shopid).then(res => {
      this.feeds = res.data.feedback;
    });
  },
  methods: {
    deleteFeed(id) {
      axios
        .delete("http://localhost:8000/api/delete_feedback/" + id)
        .then(res => {
          let shopid = this.$route.params.shopid;
          axios
            .get("http://localhost:8000/api/get_review/" + shopid)
            .then(res => {
              this.feeds = res.data.feedback;
            });
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>