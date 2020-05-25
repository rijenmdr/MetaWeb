<template>
    <header id="home-section" class="landingView">
    <div class="primary-overlay dark-overlay mb-5 home">
      <div class="home-inner container home">
        <div class="row">
          <div class="col-lg-8 d-none d-lg-block mt-5">
            <h1 class="display-4">
              Build <strong> Website </strong> easily
              and<strong> reach more customers</strong>
            </h1>
            <div class="d-flex ml-5">
              <div class="p-2 slign-self-start">
                <i class="fas fa-check fa-2x"></i>
              </div>
              <div class="p-2 slign-self-end">
                Website of websites : maintain your website in our website 
               
              </div>
            </div>
            <div class="d-flex ml-5">
              <div class="p-2 slign-self-start">
                <i class="fas fa-check fa-2x"></i>
              </div>
              <div class="p-2 slign-self-end">
                Platform for the shop owners to maintain their website easily
              </div>
            </div>
            <div class="d-flex ml-5">
              <div class="p-2 slign-self-start">
                <i class="fas fa-check fa-2x"></i>
              </div>
              <div class="p-2 slign-self-end">
                Get rid of high hosting and domain costs
              </div>
            </div>
            <div class="d-flex ml-5">
              <div class="p-2 slign-self-start">
                <i class="fas fa-check fa-2x"></i>
              </div>
              <div class="p-2 slign-self-end">
                Create account and maintain your site and reach out more customers online
              </div>
            </div>
            <div class="sign-up-now mt-5">
              <router-link to="/signup" class="btn btn-outline-dark btn-lg text-white ml-5">
              
                <i class="fas fa-arrow-right"></i> Sign Up Now
              </router-link>
            </div>
          </div>
          <div class="col-lg-4 mt-5 mb-5">
            <!--form-->
            <div class="card formCenter text-center card-form ">
              <div class="card-body">
                <h3>SEARCH FOR STORES</h3>
                <p>Enter the details of the shop around you and find their website easily </p>
                <form action="/website/index.html">
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control form-control-lg"
                      placeholder="keywords"
                    />
                  </div>
                  <div class="form-group">
                    <input
                      type="email"
                      class="form-control form-control-lg"
                      placeholder="city"
                    />
                  </div>
                  <div class="form-group">
                    <input
                      type="number"
                      class="form-control form-control-lg"
                      placeholder="shop no"
                    />
                  </div>
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control form-control-lg"
                      placeholder="category"
                    />
                  </div>
                  <input
                    type="submit"
                    value="Search"
                    class="btn btn-outline-light btn-block"
                  />
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>
<style scoped>
    
  .landingView{
      margin-top: 12vh;
  }  
  .formCenter{
    background:#1b838f;
  }

</style>