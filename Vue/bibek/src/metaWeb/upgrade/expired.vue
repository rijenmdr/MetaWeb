<template>
  <div class="modalCustom">
    <div tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">Alert</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">Dear {{name}} !!!!</div>
          <div class="modal-body">Your one month standard plan has been expired. Would you like to renew your plan again ??</div>
          <div class="modal-footer">
            <button @click="no" type="button" class="btn btn-danger">No</button>
            <button @click="yes" type="button" class="btn btn-success">Yes</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      name: this.$store.getters.getUser
    };
  },
  methods: {
    yes() {
      this.$router.push("/upgradetopro");
    },
    no() {
      this.$router.push("/dashboard");
    }
  }
};
</script>
<style scoped>
.modalCustom {
}
</style>