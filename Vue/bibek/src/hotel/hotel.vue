<template>
  <div>
    <header class="top-navbar">
      <nav class="navbar navbar-expand-lg">
        <div class="container">
          <a class="navbar-brand" href="index.html">
            <img src="./images/logo.png" class="logo-image" alt />
          </a>
          <button
            class="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbars-rs-food"
            aria-controls="navbars-rs-food"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbars-rs-food">
            <ul class="navbar-nav ml-auto">
              <li class="nav-item home-icon">
                <a class="nav-link text" href="index.html">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link text" href="menu.html">Menu</a>
              </li>
              <li class="nav-item">
                <a class="nav-link text" href="about.html">About</a>
              </li>

              <li class="nav-item">
                <a class="nav-link text" href="contact.html">Contact</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
    <section id="showcase">
      <div id="myCarousel" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
          <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
          <li data-target="#myCarousel" data-slide-to="1"></li>
          <li data-target="#myCarousel" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
          <div class="carousel-item carousel-image-1 active">
            <img src="./images/slider-03.jpg" />
            <div class="container">
              <div class="carousel-caption d-none d-sm-block text-center title-box">
                <h1 class="title">Welcome To Yamifood Restaurant</h1>

                <p class="des">this</p>
              </div>
            </div>
          </div>

          <div class="carousel-item carousel-image-2">
            <img src="./images/slider-02.jpg" />
            <div class="container">
              <div class="carousel-caption d-none d-sm-block mb-5 title-box">
                <h1 class="title">this</h1>

                <p class="des">this</p>
              </div>
            </div>
          </div>

          <div class="carousel-item carousel-image-3">
            <img src="./images/slider-01.jpg" />
            <div class="container">
              <div class="carousel-caption d-none d-sm-block text-right title-box">
                <h1 class="title">this</h1>

                <p class="des">this</p>
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
    <div class="about-section-box">
      <div class="container">
        <div class="row">
          <div class="col-lg-6 col-md-6 col-sm-12">
            <img src="./images/about-img.jpg" alt class="img-fluid" />
          </div>
          <div class="col-lg-6 col-md-6 col-sm-12 text-center">
            <div class="inner-column">
              <h1>
                Welcome To
                <span>Yamifood Restaurant</span>
              </h1>
              <h4>Little Story</h4>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque auctor suscipit feugiat. Ut at pellentesque ante, sed convallis arcu. Nullam facilisis, eros in eleifend luctus, odio ante sodales augue, eget lacinia lectus erat et sem.</p>
              <p>Sed semper orci sit amet porta placerat. Etiam quis finibus eros. Sed aliquam metus lorem, a pellentesque tellus pretium a. Nulla placerat elit in justo vestibulum, et maximus sem pulvinar.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Start Gallery -->
    <div class="gallery-box">
      <div class="container-fluid">
        <div class="row">
          <div class="col-lg-12">
            <div class="heading-title text-center">
              <h2>Gallery</h2>
              <p>Lorem Ipsum is simply dummy text of the printing and typesetting</p>
            </div>
          </div>
        </div>
        <div class="tz-gallery">
          <div class="row">
            <div class="col-sm-12 col-md-4 col-lg-4">
              <a class="lightbox" href="images/gallery-img-01.jpg">
                <img class="img-fluid" src="./images/gallery-img-01.jpg" alt="Gallery Images" />
              </a>
            </div>
            <div class="col-sm-6 col-md-4 col-lg-4">
              <a class="lightbox" href="images/gallery-img-02.jpg">
                <img class="img-fluid" src="./images/gallery-img-02.jpg" alt="Gallery Images" />
              </a>
            </div>
            <div class="col-sm-6 col-md-4 col-lg-4">
              <a class="lightbox" href="images/gallery-img-03.jpg">
                <img class="img-fluid" src="./images/gallery-img-03.jpg" alt="Gallery Images" />
              </a>
            </div>
            <div class="col-sm-12 col-md-4 col-lg-4">
              <a class="lightbox" href="images/gallery-img-04.jpg">
                <img class="img-fluid" src="./images/gallery-img-04.jpg" alt="Gallery Images" />
              </a>
            </div>
            <div class="col-sm-6 col-md-4 col-lg-4">
              <a class="lightbox" href="images/gallery-img-05.jpg">
                <img class="img-fluid" src="./images/gallery-img-05.jpg" alt="Gallery Images" />
              </a>
            </div>
            <div class="col-sm-6 col-md-4 col-lg-4">
              <a class="lightbox" href="images/gallery-img-06.jpg">
                <img class="img-fluid" src="./images/gallery-img-06.jpg" alt="Gallery Images" />
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- End Gallery -->
    <!-- Start Contact info -->
    <div class="contact-imfo-box">
      <div class="container">
        <div class="row">
          <div class="col-md-4">
            <i class="fa fa-volume-control-phone"></i>
            <div class="overflow-hidden">
              <h4>Phone</h4>
              <p class="lead">+01 123-456-4590</p>
            </div>
          </div>
          <div class="col-md-4">
            <i class="fa fa-envelope"></i>
            <div class="overflow-hidden">
              <h4>Email</h4>
              <p class="lead">yourmail@gmail.com</p>
            </div>
          </div>
          <div class="col-md-4">
            <i class="fa fa-map-marker"></i>
            <div class="overflow-hidden">
              <h4>Location</h4>
              <p class="lead">800, Lorem Street, US</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- End Contact info -->

    <!-- Start Footer -->
    <footer class="footer-area bg-f">
      <div class="container">
        <div class="row">
          <div class="col-lg-3 col-md-6">
            <h3>About Us</h3>
            <p>Integer cursus scelerisque ipsum id efficitur. Donec a dui fringilla, gravida lorem ac, semper magna. Aenean rhoncus ac lectus a interdum. Vivamus semper posuere dui, at ornare turpis ultrices sit amet. Nulla cursus lorem ut nisi porta, ac eleifend arcu ultrices.</p>
          </div>
          <div class="col-lg-3 col-md-6">
            <h3>Opening hours</h3>
            <p>
              <span class="text-color">Monday:</span>Closed
            </p>
            <p>
              <span class="text-color">Tue-Wed :</span> 9:Am - 10PM
            </p>
            <p>
              <span class="text-color">Thu-Fri :</span> 9:Am - 10PM
            </p>
            <p>
              <span class="text-color">Sat-Sun :</span> 5:PM - 10PM
            </p>
          </div>
          <div class="col-lg-3 col-md-6">
            <h3>Contact</h3>
            <p class="lead">Ipsum Street, Lorem Tower, MO, Columbia, 508000</p>
            <p class="lead">
              <a href="#">+01 2000 800 9999</a>
            </p>
            <p>
              <a href="#">info@admin.com</a>
            </p>
          </div>
          <div class="col-lg-3 col-md-6">
            <h3>Subscribe</h3>
            <div class="subscribe_form">
              <form class="subscribe_form">
                <input
                  name="EMAIL"
                  id="subs-email"
                  class="form_input"
                  placeholder="Email Address..."
                  type="email"
                />
                <button type="submit" class="submit">SUBSCRIBE</button>
                <div class="clearfix"></div>
              </form>
            </div>
            <ul class="list-inline f-social">
              <li class="list-inline-item">
                <a href="#">
                  <i class="fa fa-facebook" aria-hidden="true"></i>
                </a>
              </li>
              <li class="list-inline-item">
                <a href="#">
                  <i class="fa fa-twitter" aria-hidden="true"></i>
                </a>
              </li>
              <li class="list-inline-item">
                <a href="#">
                  <i class="fa fa-linkedin" aria-hidden="true"></i>
                </a>
              </li>
              <li class="list-inline-item">
                <a href="#">
                  <i class="fa fa-google-plus" aria-hidden="true"></i>
                </a>
              </li>
              <li class="list-inline-item">
                <a href="#">
                  <i class="fa fa-instagram" aria-hidden="true"></i>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div class="copyright">
        <div class="container">
          <div class="row">
            <div class="col-lg-12">
              <p class="company-name">
                All Rights Reserved. &copy; 2018
                <a href="#">Yamifood Restaurant</a> Design By :
                <a href="https://html.design/">html design</a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </footer>
    <!-- End Footer -->
  </div>
</template>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins&display=swap");
@import url("https://fonts.googleapis.com/css?family=Athiti:400,500,600");
@import url("https://fonts.googleapis.com/css?family=Arbutus+Slab");
.navbar {
  background: white;
}
.text {
  font-family: "Athiti", sans-serif;
  font-size: 20px;
}
.title-box {
  position: absolute;
  top: 20vh;
}
.title {
  font-family: "Arbutus Slab", serif;
  font-size: 60px;
  color: white;
  font-weight: bold;
}
.carousel-item {
  height: 600px;
}
.carousel-image-1 {
  background-size: cover;
}
.carousel-image-2 {
  background-size: cover;
}
.carousel-image-3 {
  background-size: cover;
}
.carousel-control-next-icon,
.carousel-control-prev-icon {
  border: 3px solid white;
  border-radius: 50%;
  height: 10vh;
  width: 5vw;
  color: red;
  font-size: 40px;
}
.logo-image {
  height: 50px;
}
.home-icon {
  border-bottom: 1px solid black;
  padding-left: 12px;
}
.about-section-box {
  padding: 70px 0px;
}
.about-section-box .img-fluid {
  box-shadow: -10px -10px 0px #d0a772;
}
.inner-column {
}
.inner-column h1 {
  font-family: "Arbutus Slab", serif;
  font-size: 30px;
  color: #010101;
}
.inner-column h1 span {
  color: #d0a772;
}
.inner-column h4 {
  font-size: 16px;
  font-weight: 500;
}
.inner-column p {
  font-size: 18px;
}
.inner-column .btn-outline-new-white {
  color: #d0a772;
}
.inner-column .btn-outline-new-white:hover {
  color: #ffffff;
}
.footer-area {
  padding-top: 50px;
  padding-bottom: 0px;
}
.bg-f {
  background-image: url("./images/footer-bg.jpg");
  background-attachment: scroll;
  background-clip: initial;
  background-color: rgba(0, 0, 0, 0);
  background-origin: initial;
  background-position: center center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
}
.bg-f::before {
  background: #010101;
  content: "";
  height: 100%;
  left: 0;
  position: absolute;
  top: 0;
  width: 100%;
  z-index: 1;
  opacity: 0.8;
}

.footer-area .container {
  position: relative;
  z-index: 1;
}
.footer-area h3 {
  color: #ffffff;
  text-transform: uppercase;
  font-size: 24px;
  border-bottom: 1px dashed rgba(207, 166, 113, 0.5);
  margin-bottom: 10px;
}
.footer-area p {
  font-size: 15px;
  color: rgba(255, 255, 255, 0.8);
  margin: 0;
  padding-bottom: 10px;
}

.footer-area p.lead {
  font-size: 19px;
  color: #ffffff;
  margin-bottom: 15px;
}
.footer-area p.lead a {
  color: #ffffff;
  margin-bottom: 15px;
}
.footer-area p.lead a:hover {
  color: #d0a772;
}
.footer-area p a {
  font-size: 18px;
  color: #ffffff;
}
.footer-area p a:hover {
  color: #d0a772;
}

.subscribe_form {
  display: block;
  text-align: center;
  padding: 5px 0;
}

.subscribe_form .form_input {
  display: block;
  background-color: rgba(0, 0, 0, 0.7);
  color: #fff;
  border: none;
  font-size: 19px;
  line-height: 50px;
  padding: 0 10px;
  float: left;
  width: 100%;
  transition: all 0.5s ease-in-out;
}

.subscribe_form .submit {
  background-color: #d0a772;
  color: #fff;
  font-size: 16px;
  font-weight: 600;
  line-height: 50px;
  display: inline-block;
  padding: 0 10px;
  float: left;
  width: 100%;
  border: none;
  cursor: pointer;
  transition: all 0.5s ease-in-out;
}
.subscribe_form .submit:hover {
  background: #010101;
}

.f-social {
  padding-bottom: 10px;
  margin: 0px;
  margin-top: 20px;
}
.f-social li a {
  font-size: 25px;
  color: rgba(255, 255, 255, 0.9);
  margin-right: 10px;
}

.copyright {
  margin-top: 20px;
  position: relative;
  display: block;
  background-color: #010101;
  border-top: 1px dashed rgba(207, 166, 113);
  padding: 30px 0;
  z-index: 1;
}

.copyright .company-name {
  font-size: 16px;
  text-align: center;
}
.copyright .company-name a {
  font-size: 16px;
}
.contact-imfo-box {
  background: #d0a772;
  padding: 30px 0;
}

.overflow-hidden {
  overflow: hidden;
}

.contact-imfo-box i {
  display: block;
  float: left;
  width: 60px;
  height: 60px;
  line-height: 60px;
  text-align: center;
  background: #fff;
  color: #d0a772;
  font-size: 30px;
  -webkit-border-radius: 50%;
  -moz-border-radius: 50%;
  -ms-border-radius: 50%;
  border-radius: 50%;
  margin-right: 20px;
}
.contact-imfo-box h4 {
  margin: 0px;
  margin-top: 5px;
  color: #ffffff;
  font-size: 20px;
  padding: 0px;
  font-weight: 500;
  line-height: 24px;
}
.contact-imfo-box p {
  margin: 0px;
  color: #ffffff;
  font-weight: 300;
}
.gallery-box {
  padding: 70px 0px;
}
.tz-gallery {
  margin-top: 30px;
}
.tz-gallery .lightbox img {
  width: 100%;
  margin-bottom: 30px;
  transition: 0.2s ease-in-out;
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
}
.tz-gallery .lightbox img:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3);
}
</style>