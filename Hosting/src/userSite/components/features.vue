<template>
  <section id="home-icons" class="py-5 features">
    <div class="container">
      <div class="row">
        <div class="col-md-4 mb-4 text-center">
          <i class="fas fa-cog fa-3x mb-2"></i>
          <h3 class="text">{{featureOneH}}</h3>
          <p class="lead">
            {{featureOneDesH}}
          </p>
        </div>
        <div class="col-md-4 mb-4 text-center">
          <i class="fas fa-cloud fa-3x mb-2"></i>
          <h3 class="text">{{featureTwoH}}</h3>
          <p class="lead">
            {{featureTwoDesH}}
          </p>
        </div>
        <div class="col-md-4 mb-4 text-center">
          <i class="fas fa-cart-plus fa-3x mb-2"></i>
          <h3 class="text">{{featureThreeH}}</h3>
          <p class="lead">
            {{featureThreeDesH}}
          </p>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  props: [
    "featureOneH",
    "featureTwoH",
    "featureThreeH",
    "featureOneDesH",
    "featureTwoDesH",
    "featureThreeDesH"
  ]
};
</script>
<style scoped>
.features {
  margin-top: -20vh;
}
.text{
  color: black;
}
</style>
