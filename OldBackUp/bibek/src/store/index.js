import Vue from "vue";
import Vuex from "vuex";

import Auth from "./modules/auth";
import Dashboard from "./modules/dashboard";
import UserSite from "./modules/userSiteInfo";
import Notifications from "./modules/notifications";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    Auth,
    Dashboard,
    UserSite,
    Notifications,
  },
});
