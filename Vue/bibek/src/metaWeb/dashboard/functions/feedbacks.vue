<template>
  <div class="feedback">
    <div class="container">
      <div class="row">
        <div class="col-md-3" v-for="(site,i) in userSite">
          <div class="card text-center bg-success text-white mb-3">
            <div class="card-body">
              <h3>My Website {{i+1}}</h3>
              <h4>{{site.nameOfSiteH}}</h4>
              <h4>shop id: {{site.id}}</h4>
              <h4 class="display-4">
                <i class="fas fa-envelope"></i>
              </h4>
              <div class="btn btn-outline-light btn-sm" @click="feedback(site.id)">Show Feedbacks</div>
            </div>
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
      userSite: this.$store.getters.getUserSite
    };
  },
  created() {
    
    // console.log(this.$store.getters.getUserSite.length)
    // let length=this.$store.getters.getUserSite.length
    
    // axios.get("http://localhost:8000/api/get_review/" + shopid)
    // .then(res => {
    //     console.log(res)
    //     this.feeds = res.data.feedback;
    // });
  },
  methods: {
    feedback(val) {
      this.$router.push("/dashboard/feedback/" + val);
    }
  }
};
</script>
<style scoped>
.feedback{
  margin-top: 10vh;
  margin-bottom: 10vh;
}

</style>