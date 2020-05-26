<template>
    <div>
        <Header :nameOfSite="nameOfSite" :id="1"/>
        <header id="page-header">
        <div class="container">
            <div class="row">
                <div class="col-md-6 m-auto text-center">
                    <h1>About Us</h1>
                    <p>{{introduction}}</p>
                </div>
            </div>
        </div>
    </header>
    <!-- About section -->
    <section id="about" class="py-3">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <h1>What We Do</h1>
                    <p>{{whatWeDoA}}</p>
                  
                    
                </div>
                <div class="col-md-6">
                    <img src="https://source.unsplash.com/random/700x700/?technology" alt="" class="img-fluid rounded-circle d-none d-md-block about-img">
                </div>
            </div>
        </div>
    </section>
    <!-- Icon Boxes -->
    <section id="icon-boxes" class="p-5">
        <div class="container">
            <div class="row mb-4">
                <div class="col-md-4">
                    <div class="card bg-danger text-white text-center">
                        <div class="card-body">
                            <i class="fas fa-building fa-3x"></i>
                            <h3>Sample heading</h3>
                            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laboriosam ipsum non 
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card bg-info text-white text-center">
                        <div class="card-body">
                            <i class="fas fa-bullhorn fa-3x"></i>
                            <h3>Books</h3>
                            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laboriosam ipsum non 
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card bg-danger text-white text-center">
                        <div class="card-body">
                            <i class="fas fa-comments fa-3x"></i>
                            <h3>Pasal</h3>
                            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laboriosam ipsum non 
                        </div>
                    </div>
                </div>
                <div class="col-md-4"></div>
                <div class="col-md-4"></div>
            </div>
            <div class="row mb-4">
                <div class="col-md-4">
                    <div class="card bg-dark text-white text-center">
                        <div class="card-body">
                            <i class="fas fa-box fa-3x"></i>
                            <h3>Sample heading</h3>
                            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laboriosam ipsum non 
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card bg-danger text-white text-center">
                        <div class="card-body">
                            <i class="fas fa-credit-card fa-3x"></i>
                            <h3>Books</h3>
                            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laboriosam ipsum non 
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card bg-dark text-white text-center">
                        <div class="card-body">
                            <i class="fas fa-coffee fa-3x"></i>
                            <h3>Pasal</h3>
                            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laboriosam ipsum non 
                        </div>
                    </div>
                </div>
                <div class="col-md-4"></div>
                <div class="col-md-4"></div>
            </div>
        </div>
    </section>
    <!-- Testimonials -->
    <section id="testimonials" class="p-4 bg-dark text-white">
        <div class="container">
            <h2 class="text-center">testimonials</h2>
            <div class="row text-center">
                <div class="col">
                    <div class="slider">
                        <div>
                            <blockquote class="blockquote">
                                <p class="mb-0">Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus, laboriosam.</p>
                                <footer class="blockquote-footer">Bibek lama From 
                                    <cite title="company1"> company1</cite>
                                </footer>
                            </blockquote>
                        </div>

                        <div>
                            <blockquote class="blockquote">
                                <p class="mb-0">Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus, laboriosam.</p>
                                <footer class="blockquote-footer">Pooja From 
                                    <cite title="company2"> company1</cite>
                                </footer>
                            </blockquote>
                        </div>

                        <div>
                            <blockquote class="blockquote">
                                <p class="mb-0">Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur aperiam, enim repellendus est quae provident laboriosam commodi veritatis, quos reprehenderit vitae totam incidunt accusamus! Sequi, </laboriosam></p>
                                <footer class="blockquote-footer">Laxmi Manandhar From 
                                    <cite title="company3"> company1</cite>
                                </footer>
                            </blockquote>
                        </div>

                    </div>
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
    
    </div>
</template>
<script>
import Header from './componentHead'
export default {
    components:{
        Header
    },
    data(){
        return{
            introduction:this.$store.getters.getWebsite.introductionA,
            whatWeDoA:this.$store.getters.getWebsite.whatWeDoA,
            nameOfSite: this.$store.getters.getWebsite.nameOfSiteH,
            id: this.$store.getters.getWebsite.id
        }
    }
}
</script>
<style scoped>
    #page-header{
    height: 200px;
    background: url('../../assets/image1.jpg');
    background-position:0 -300px;
    background-attachment: fixed;
    color: #fff;
    border-bottom:1px #eee solid;
    padding-top: 50px;
}
</style>>
    
</style>