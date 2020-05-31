<template>
  <div>
    <section id="showcase">
      <div id="myCarousel" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
          <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
          <li data-target="#myCarousel" data-slide-to="1"></li>
          <li data-target="#myCarousel" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
          <div class="carousel-item carousel-image-1 active">
            <div class="container">
              <div class="carousel-caption d-none d-sm-block text-right mb-5">
                <h1 class="display-3">{{headingOneH}}</h1>

                <p class="lead">{{descriptionOneH}}</p>
              </div>
            </div>
          </div>

          <div class="carousel-item carousel-image-2">
            <div class="container">
              <div class="carousel-caption d-none d-sm-block mb-5">
                <h1 class="display-3">{{headingTwoH}}</h1>

                <p class="lead">{{descriptionTwoH}}</p>
              </div>
            </div>
          </div>

          <div class="carousel-item carousel-image-3">
            <div class="container">
              <div class="carousel-caption d-none d-sm-block text-right mb-5">
                <h1 class="display-3">{{headingThreeH}}</h1>

                <p class="lead">{{descriptionThreeH}}</p>
              </div>
            </div>
          </div>
        </div>
        <a href="#myCarousel" class="carousel-control-prev" data-slide="prev">
          <span class="carousel-control-prev-icon"></span>
        </a>
        <a href="#myCarousel" class="carousel-control-next" data-slide="prev">
          <span class="carousel-control-next-icon"></span>
        </a>
      </div>
    </section>
    <Features
      :featureOneH="featureOneH"
      :featureTwoH="featureTwoH"
      :featureThreeH="featureThreeH"
      :featureOneDesH="featureOneDesH"
      :featureTwoDesH="featureTwoDesH"
      :featureThreeDesH="featureThreeDesH"
    />
  </div>
</template>
<script>
import Features from "./features";
import Footer from "./footer";
export default {
  props: [
    "headingOneH",
    "headingTwoH",
    "headingThreeH",
    "descriptionOneH",
    "descriptionTwoH",
    "descriptionThreeH",
    "featureOneH",
    "featureTwoH",
    "featureThreeH",
    "featureOneDesH",
    "featureTwoDesH",
    "featureThreeDesH"
  ],
  components: {
    Features,
    Footer
  }
};
</script>
<style scoped>
.carousel-item {
  height: 450px;
}
.carousel-image-1 {
  background: url("../../assets/image1.jpg");
  background-size: cover;
}
.carousel-image-2 {
  background: url("../../assets/image2.jpg");
  background-size: cover;
}
.carousel-image-3 {
  background: url("../../assets/image3.jpg");
  background-size: cover;
}
</style>