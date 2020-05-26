<template>
  <div>
    <Header :nameOfSite="nameOfSite" id="1"/>
    <header id="page-header">
      <div class="container">
        <div class="row">
          <div class="col-md-6 m-auto text-center">
            <h1>Contact Us</h1>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus, alias!</p>
          </div>
        </div>
      </div>
    </header>
    <!-- Contact -->
    <section id="contact" class="py-3">
      <div class="container">
        <div class="row">
          <div class="col-md-4">
            <div class="card p-4">
              <div class="card-body">
                <h4>{{titleC}}</h4>
                <p>{{descriptionC}}</p>
                <h4>Adderess</h4>
                <p>{{addressC}}</p>
                <h4>Email</h4>
                <p>{{emailC}}</p>
                <h4>Phone</h4>
                <p>{{phoneC}}</p>
              </div>
            </div>
          </div>
          <div class="col-md-8">
            <div class="card p-4">
              <div class="card-body">
                <h3 class="text-center">Please fill the form to contact us</h3>
                <hr class="bg-warning" />
                <div class="row">
                  <div class="col-md-6">
                    <div class="form-group">
                      <input type="text" name placeholder="First Name" id class="form-control" />
                    </div>
                  </div>

                  <div class="col-md-6">
                    <div class="form-group">
                      <input type="text" name placeholder="Last Name" id class="form-control" />
                    </div>
                  </div>

                  <div class="col-md-6">
                    <div class="form-group">
                      <input type="text" name placeholder="Email" id class="form-control" />
                    </div>
                  </div>

                  <div class="col-md-6">
                    <div class="form-group">
                      <input type="text" name placeholder="Address" id class="form-control" />
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-12">
                    <div class="form-group">
                      <textarea rows="5" class="form-control" placeholder="Enter Message"></textarea>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-12">
                    <div class="form-group">
                      <input
                        type="submit"
                        value="Submit"
                        class="form-control btn btn-outline-success"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- Staff -->
   
  </div>
</template>
<script>
import Header from "./componentHead";
export default {
  components: {
    Header
  },
  data() {
    return {
      nameOfSite: this.$store.getters.getWebsite.nameOfSiteH,
      titleC: this.$store.getters.getWebsite.titleC,
      descriptionC: this.$store.getters.getWebsite.descriptionC,
      emailC: this.$store.getters.getWebsite.emailC,
      phoneC: this.$store.getters.getWebsite.phoneC,
      addressC: this.$store.getters.getWebsite.addressC
    };
  }
};
</script>