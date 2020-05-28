<template>
  <div class="deleteWebsite">
    <div class="container">
      <div class="row">
        <div class="col-md-3" v-for="(site,i) in userSite">
          <div class="card text-center bg-primary text-white mb-3">
            <div class="card-body">
              <h3>My Website {{i+1}}</h3>
              <h4>{{site.nameOfSiteH}}</h4>
              <h4>shop id: {{site.id}}</h4>
              <h34My Website {{i+1}}</h4>
              <h4 class="display-4">
                <i class="fas fa-pencil-alt"></i>
              </h4>
              <div class="btn btn-outline-light btn-sm" @click="deleteSite(site.id)">Delete</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      userSite: this.$store.getters.getUserSite
    };
  },
  methods:{
    
      async deleteSite(val){
         let JWTToken = localStorage.getItem("token");
         if (!JWTToken) {
         JWTToken = this.$store.getters.getToken;
         }
          await axios.delete('http://localhost:8000/api/delete_website/'+val,
           {
            headers: {
              Authorization: `Token ${JWTToken}`
            }
          })
          .then(res=>
          {
            this.$store.dispatch('setUserSite',{token:this.$store.getters.getToken,user:this.$store.getters.getUser})
             
          }
          )
          .catch(err=>{
            console.log(err)
          })
          this.$router.push('/dashboard')
      }
  }
};
</script>
<style scoped>
.deleteWebsite {
  margin-top: 10vh;
  margin-bottom: 10vh;
}
</style>