<template>
   <section id="contact" class="bg-light py-5 contact">
    <div class="container contact">
      <div class="row">
        <div class="col-lg-9">
          <h3>Get In Touch</h3>
          <p class="lead">For any enquire , feel free to contact us !!</p>
          <form>
            <div class="input-group input-group-lg mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text">
                  <i class="fas fa-user"></i>
                </span>
              </div>
              <input type="text" class="form-control" placeholder="Enter name">
            </div>
            <div class="input-group input-group-lg mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text">
                  <i class="fas fa-envelope"></i>
                </span>
              </div>
              <input type="email" class="form-control" placeholder="Enter email">
            </div>
            <div class="input-group input-group-lg mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text">
                  <i class="fas fa-pencil-alt"></i>
                </span>
              </div>
              <textarea rows="5" class="form-control" placeholder="Enter your message"></textarea>
            </div>
            <input type="submit" value="submit" class="btn btn-block btn-large texttitle">
          </form>
        </div>
        <div class="col-lg-3 align-self-center">
          <img src="../../assets/mlogo.png" alt="" class="img-fluid">
        </div>
      </div>
    </div>
  </section>
</template>
<style scoped>
  .texttitle{
    color:white;
    background: #1b838f;
  }
  
</style>>