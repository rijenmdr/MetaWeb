<template>
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
              <h1 class="display-3">Heading one</h1>

              <p class="lead">
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Reprehenderit iste harum possimus sed. Provident fugit omnis
                ullam, labore necessitatibus quibusdam.
              </p>
              <a href="#" class="btn btn-danger btn-lg">Sign Up Now</a>
            </div>
          </div>
        </div>

        <div class="carousel-item carousel-image-2">
          <div class="container">
            <div class="carousel-caption d-none d-sm-block mb-5">
              <h1 class="display-3">Heading two</h1>

              <p class="lead">
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Reprehenderit iste harum possimus sed. Provident fugit omnis
                ullam, labore necessitatibus quibusdam.
              </p>
              <a href="#" class="btn btn-info btn-lg">Learn More</a>
            </div>
          </div>
        </div>

        <div class="carousel-item carousel-image-3">
          <div class="container">
            <div class="carousel-caption d-none d-sm-block text-right mb-5">
              <h1 class="display-3">Heading Three</h1>

              <p class="lead">
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Reprehenderit iste harum possimus sed. Provident fugit omnis
                ullam, labore necessitatibus quibusdam.
              </p>
              <a href="#" class="btn btn-success btn-lg">Play Now</a>
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
</template>
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