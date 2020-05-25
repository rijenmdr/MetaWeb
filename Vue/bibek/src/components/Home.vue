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
       <!-- Home icon section -->
       <section id="home-icons" class="py-5">
           <div class="container">
               <div class="row">
                   <div class="col-md-4 mb-4 text-center">
                       <i class="fas fa-cog fa-3x mb-2"></i>
                       <h3>Turning Gears</h3>
                       <p class="lead">
                           Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis,
                           aperiam.
                       </p>
                   </div>
                   <div class="col-md-4 mb-4 text-center">
                       <i class="fas fa-cloud fa-3x mb-2"></i>
                       <h3>Sending Data</h3>
                       <p class="lead">
                           Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis,
                           aperiam.
                       </p>
                   </div>
                   <div class="col-md-4 mb-4 text-center">
                       <i class="fas fa-cart-plus fa-3x mb-2"></i>
                       <h3>Making Money</h3>
                       <p class="lead">
                           Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis,
                           aperiam.
                       </p>
                   </div>
               </div>
           </div>
       </section>
       <!-- Home heading section -->
       <section id="home-heading" class="p-5">
           <div class="dark-overlay">
               <div class="row">
                   <div class="col">
                       <div class="container pt-5">
                           <h1>Are You ready to get Started ?</h1>
                           <p class="lead d-none d-md-block">
                               Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est,
                               iusto?
                           </p>
                       </div>
                   </div>
               </div>
           </div>
       </section>
       <!-- info section -->
       <section id="info" class="py-3">
           <div class="container">
               <div class="row">
                   <div class="col-md-6 align-self-center">
                       <h3>What next ?</h3>
                       <p>
                           Lorem ipsum dolor sit amet consectetur adipisicing elit.
                           Aspernatur ipsum in, amet vitae iure iste totam expedita
                           voluptatibus pariatur numquam odit veniam eligendi vel nostrum.
                       </p>
                       <a href="about.html" class="btn btn-outline-success btn-lg"
                       >Learn More</a
                       >
                   </div>
                   <div class="col-md-6">
                       <img src="" class="img-fluid" alt="" />
                   </div>
               </div>
           </div>
       </section>
       <!-- Video play -->
       <section id="video-play">
           <div class="dark-overlay">
               <div class="row">
                   <div class="col">
                       <div class="container p-5">
                           <a
                                   href="#"
                                   class="video"
                                   data-video="http://www.youtube.com/embed/1I-3vJSC-Vo"
                                   data-toggle="modal"
                                   data-target="#videoModal"
                           >
                               <i class="fas fa-play fa-3x"></i>
                           </a>
                           <h1>See what we do</h1>
                       </div>
                   </div>
               </div>
           </div>
       </section>
       <!-- Photo Gallery -->
       <section id="gallery" class="py-5">
           <div class="container">
               <h1 class="text-center">Photo Gallery</h1>
               <p class="text-center">Checkout our photos</p>
               <div class="row mb-4">
                   <div class="col-md-4">
                       <a
                               href="http://source.unsplash.com/random/560x560"
                               data-toggle="lightbox"
                               data-gallery="img-gallery"
                               data-height="560"
                               data-width="560"
                       >
                           <img
                                   src="http://source.unsplash.com/random/560x560"
                                   alt=""
                                   class="img-fluid"
                           />
                       </a>
                   </div>

                   <div class="col-md-4">
                       <a
                               href="http://source.unsplash.com/random/561x561"
                               data-toggle="lightbox"
                               data-gallery="img-gallery"
                               data-height="561"
                               data-width="561"
                       >
                           <img
                                   src="http://source.unsplash.com/random/561x561"
                                   alt=""
                                   class="img-fluid"
                           />
                       </a>
                   </div>

                   <div class="col-md-4">
                       <a
                               href="http://source.unsplash.com/random/562x562"
                               data-toggle="lightbox"
                               data-gallery="img-gallery"
                               data-height="562"
                               data-width="562"
                       >
                           <img
                                   src="http://source.unsplash.com/random/562x562"
                                   alt=""
                                   class="img-fluid"
                           />
                       </a>
                   </div>
               </div>

               <div class="row mb-4">
                   <div class="col-md-4">
                       <a
                               href="http://source.unsplash.com/random/563x563"
                               data-toggle="lightbox"
                               data-gallery="img-gallery"
                               data-height="563"
                               data-width="563"
                       >
                           <img
                                   src="http://source.unsplash.com/random/563x563"
                                   alt=""
                                   class="img-fluid"
                           />
                       </a>
                   </div>

                   <div class="col-md-4">
                       <a
                               href="http://source.unsplash.com/random/564x564"
                               data-toggle="lightbox"
                               data-gallery="img-gallery"
                               data-height="564"
                               data-width="564"
                       >
                           <img
                                   src="http://source.unsplash.com/random/564x564"
                                   alt=""
                                   class="img-fluid"
                           />
                       </a>
                   </div>

                   <div class="col-md-4">
                       <a
                               href="http://source.unsplash.com/random/565x565"
                               data-toggle="lightbox"
                               data-gallery="img-gallery"
                               data-height="565"
                               data-width="565"
                       >
                           <img
                                   src="http://source.unsplash.com/random/565x565"
                                   alt=""
                                   class="img-fluid"
                           />
                       </a>
                   </div>
               </div>

               <div class="row mb-4">
                   <div class="col-md-4">
                       <a
                               href="http://source.unsplash.com/random/560x560"
                               data-toggle="lightbox"
                               data-gallery="img-gallery"
                               data-height="560"
                               data-width="560"
                       >
                           <img
                                   src="http://source.unsplash.com/random/560x560"
                                   alt=""
                                   class="img-fluid"
                           />
                       </a>
                   </div>

                   <div class="col-md-4">
                       <a
                               href="http://source.unsplash.com/random/561x561"
                               data-toggle="lightbox"
                               data-gallery="img-gallery"
                               data-height="561"
                               data-width="561"
                       >
                           <img
                                   src="http://source.unsplash.com/random/561x561"
                                   alt=""
                                   class="img-fluid"
                           />
                       </a>
                   </div>

                   <div class="col-md-4">
                       <a
                               href="http://source.unsplash.com/random/562x562"
                               data-toggle="lightbox"
                               data-gallery="img-gallery"
                               data-height="562"
                               data-width="562"
                       >
                           <img
                                   src="http://source.unsplash.com/random/562x562"
                                   alt=""
                                   class="img-fluid"
                           />
                       </a>
                   </div>
               </div>
           </div>
       </section>
       <!-- News Letter -->
       <section id="newsletter" class="text-center p-5 bg-dark text-white">
           <div class="container">
               <div class="row">
                   <div class="col">
                       <h1>Sign Up For Our Newsletter</h1>
                       <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consequatur atque omnis quam repudiandae maiores quasi, pariatur quibusdam commodi? Ipsa, tempora!</p>
                       <form class="form-inline justify-content-center">
                           <input type="text" class="form-control mb-2 mr-2" placeholder="Enter name">
                           <input type="email" class="form-control mb-2 mr-2" placeholder="Enter email">
                           <button class="btn btn-success mb-2">Submit</button>

                       </form>
                   </div>
               </div>
           </div>
       </section>
       <!-- Footer -->
       <section id="main-footer" class="text-center p-4">
           <div class="container">
               <div class="row">
                   <div class="col">
                       <p>Copyright&copy;<span id="year"></span>Books</p>
                   </div>
               </div>
           </div>
       </section>
       <!-- Video modal -->
       <div class="modal fade" id="videoModal">
           <div class="modal-dialog">
               <div class="modal-content">
                   <div class="modal-body">
                       <button class="close" data-dismiss="modal">
                           <span>&times;</span>
                       </button>
                       <iframe
                               src=""
                               frameborder="0"
                               height="350"
                               width="100%"
                               allowfullscreen
                       ></iframe>
                   </div>
               </div>
           </div>
       </div>
   </div>
</template>