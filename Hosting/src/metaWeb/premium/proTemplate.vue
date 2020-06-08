<template>
  <div class="main-content" id="panel">
    <div class="header bg-primary pb-6"></div>
    <div class="card card-stats mt-5 col-md-11 ml-5">
      <!-- Card body -->
      <div class="card-body">
        <div class="row">
          <div class="col">
            <h5 class="card-title text-uppercase text-muted mb-0">Template for personal portfolio</h5>
            <span
              class="h4 font-weight-bold mb-0"
            >This templates is used to make the personal port-folio</span>
          </div>
          <div @click="portfolio" class="col-auto">
            <div class="icon icon-shape bg-gradient-orange text-white rounded-circle shadow">
              <i class="fas fa-arrow-right"></i>
            </div>
          </div>
        </div>
        <p class="mt-3 mb-0 text-sm">
          <span class="text-success mr-2">
            <i class="fa fa-edit text-primary"></i> Created By:
          </span>
          <span class="text-nowrap">MetaWeb Team</span>
        </p>
      </div>
    </div>
    <div class="card card-stats mt-5 col-md-11 ml-5">
      <!-- Card body -->
      <div class="card-body">
        <div class="row">
          <div class="col">
            <h5 class="card-title text-uppercase text-muted mb-0">Template for Hotel Websites</h5>
            <span
              class="h4 font-weight-bold mb-0"
            >This templates is used to make the website for your hotel.It has various features that helps you to make your website looks astonishing</span>
          </div>
          <div @click="hotel" class="col-auto">
            <div class="icon icon-shape bg-gradient-orange text-white rounded-circle shadow">
              <i class="fas fa-arrow-right"></i>
            </div>
          </div>
        </div>
        <p class="mt-3 mb-0 text-sm">
          <span class="text-success mr-2">
            <i class="fa fa-edit text-primary"></i> Created By:
          </span>
          <span class="text-nowrap">MetaWeb Team</span>
        </p>
      </div>
    </div>
    <!-- Modal -->

    <div v-if="modal" class="modal-dialog modal-dialog-centered alertCustom" role="document" :class="{show:modal}">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLongTitle">Alert</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div
          class="modal-body"
        >You can only create one site. You already have site created with name "{{sitename}}"" and shopId: "{{shopId}}"</div>
        <div class="modal-footer">
          <button @click="cancel" type="button" class="btn btn-primary">Ok</button>
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
      modal: "",
      sitename: "",
      shopId: ""
    };
  },
  methods: {
    cancel(){
      this.$router.push("/dashboard");
    },
    portfolio() {
      this.$router.push("/dashboard/portfolio");
    },
    hotel() {
      let JWTToken = localStorage.getItem("token");
      if (!JWTToken) {
        JWTToken = this.$store.getters.getToken;
      }
      let user = localStorage.getItem("user");
      if (!user) {
        user = this.$store.getters.getUser;
      }

      axios
        .post(
          "https://bibeklama.pythonanywhere.com/api/get_hotels",
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
          if (res.data.data == 0) {
            this.$router.push("/dashboard/hotel");
          }
          this.modal = "true";
          this.sitename = res.data.data[0].name;
          this.shopId = res.data.data[0].id;
        })
        .catch(err => {
          this.$router.push("/dashboard/hotel");
        });
    }
  }
};
</script>
<style scoped>
.alertCustom {
  position: absolute;
  top: 0px;
  left: 35vw;
  width: 50vw;

  
}
.show{
  opacity: 1;
  z-index: 2;
  animation: show 0.5s;

  transform: scale(1);
}
@keyframes show {
  from{
    
transform: scale(0);
    opacity:0;
      z-index:-1;
  } to{
    
transform: scale(1);
    opacity: 1;
      z-index:2;
  }
}
</style>