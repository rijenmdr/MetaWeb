<template>
  <div class="main-content">
    <div>
      <div class="upgrade-top">
        <div>Upgrade to Standard plan</div>
        <div>
          <i class="far fa-money-bill-alt"></i>
        </div>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-md-5">
            <div class="col-md-12 offer">
              <div class="col-md-12">
                <div class="card text-center">
                  <div class="card-header titleBox text-white">
                    <h3>Standard Plan</h3>
                  </div>
                  <div class="card-body">
                    <h4 class="card-title">Rs 200/month</h4>
                    <p>Get the most out of your website, unlock premium features at the reasonable price. Grab the offer as soon as possible.</p>
                    <ul class="list-group">
                      <li class="list-group-item">
                        <i class="fas fa-check mr-3"></i>More Templates
                      </li>
                      <li class="list-group-item">
                        <i class="fas fa-check mr-3"></i>More Customization
                      </li>
                      <li class="list-group-item">
                        <i class="fas fa-check mr-3"></i>Email notifications
                      </li>
                      <li class="list-group-item">
                        <i class="fas fa-check mr-3"></i>Data Visualization
                      </li>
                      <li class="list-group-item">
                        <i class="fas fa-check mr-3"></i>And many more
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-7 mt-5">
            <h3>Payment Details</h3>
            <p
              class="lead"
            >we accept the following methods of payment.Please provide valid information. We are aware about your data security.</p>

            <div class="input-group input-group-lg mb-3 mt-5">
              <div class="input-group-prepend">
                <span class="input-group-text">
                  <i class="fas fa-user"></i>
                </span>
              </div>
              <input v-model="email" type="text" class="form-control" placeholder="Email Address" />
            </div>
            <div class="input-group input-group-lg mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text">
                  <i class="fas fa-user-lock"></i>
                </span>
              </div>
              <input
                v-model="password"
                type="email"
                class="form-control"
                placeholder="Enter Your Password"
              />
            </div>
            <div class="input-group input-group-lg mb-4 ml-5 mt-4">
              <label class="radio-inline">
                <input type="radio" name="optradio" checked /> e-sewa
              </label>
              <label class="radio-inline ml-5">
                <input type="radio" name="optradio" /> khalti
              </label>
              <label class="radio-inline ml-5">
                <input type="radio" name="optradio" /> IME pay
              </label>
            </div>
            <div class="input-group input-group-lg mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text">
                  <i class="fas fa-key"></i>
                </span>
              </div>
              <input v-model="password" type="email" class="form-control" placeholder="Card Number" />
            </div>
            <button @click="payDone"
              type="button"
              class="btn btn-block bg-success text-white button"
              data-toggle="modal"
              data-target="#exampleModalCenter"
            >Pay</button>
          </div>
        </div>
      </div>
    </div>
   
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      email: "",
      password: ""
    };
  },
  methods: {
    payDone() {
      let token = this.$store.getters.getToken;
      if (!token) {
        token = localStorage.getItem("token");
      }
      let user = this.$store.getters.getUser;
      if (!user) {
        user = localStorage.getItem("user");
      }
      axios
        .post(
          "https://bibeklama.pythonanywhere.com/api/set_paid_user",
          {
            username: user
          },
          {
            headers: {
              Authorization: `Token ${token}`
            }
          }
        )
        .then(res => {
          console.log(res);
          this.$router.push("/payment-confirm");
        });
    }
  }
};
</script>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap");
.upgrade-top {
  font-family: "Poppins", sans-serif;
  font-size: 2.7vw;
  padding-top: 3vh;
  height: 12vh;
  justify-content: space-around;

  display: flex;
  box-shadow: 0px 2px 4px 0px #d6d5c8;
}
.offer {
  margin-top: 5vh;
  border-radius: 20px;
}
input[type="radio"] {
  transform: scale(1.5);
}
.button {
  font-size: 20px;
}
.titleBox {
  background: #999898;
}
</style>
