import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../metaWeb/home/home";
import LoginMain from "../metaWeb/auth/login";
import SignUpMain from "../metaWeb/auth/signup";
import Dashboard from "../metaWeb/dashboard/dashboard";
import CreateWebsite from "../metaWeb/dashboard/functions/createWebsite";
import UserWebsite from "../userSite/userSite";
import UserWebsiteAbout from "../userSite/components/about";
import UserWebsiteLanding from "../userSite/components/landing";
import UserWebsiteContact from "../userSite/components/contact";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    component: LoginMain,
  },
  {
    path: "/signup",
    component: SignUpMain,
  },
  {
    path: "/dashboard",
    component: Dashboard,
  },
  {
    path: "/createWebsite",
    component: CreateWebsite,
  },
  
  {
    path: "/userWebsite/about",
    component: UserWebsiteAbout,
  },
  {
    path: "/userWebsite/contact",
    component: UserWebsiteContact,
  },
  {
    path: "/userWebsite/:id",
    component: UserWebsite,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
