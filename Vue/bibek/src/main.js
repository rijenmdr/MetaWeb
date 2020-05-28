import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import VueResource from "vue-resource";
import Vuelidate from "vuelidate";

Vue.use(Vuelidate);
Vue.use(VueResource);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
