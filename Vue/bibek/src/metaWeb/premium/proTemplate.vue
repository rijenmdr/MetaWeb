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
  </div>
</template>
<script>
export default {
    methods:{
        portfolio(){
            this.$router.push('/dashboard/portfolio')
        },
        hotel(){
            this.$router.push('/dashboard/hotel')
        }
    }
}
</script>