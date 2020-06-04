import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../metaWeb/home/home";
import Login from "../metaWeb/auth/login/login";
import LoginMain from "../metaWeb/auth/login/loginMain";
import SignUpMain from "../metaWeb/auth/signup/signup";
import Dashboard from "../metaWeb/dashboard/dashboard";
import CreateWebsite from "../metaWeb/dashboard/functions/createWebsite";
import UserWebsite from "../userSite/userSite";
import UserWebsiteAbout from "../userSite/components/about";

import UserWebsiteServices from "../userSite/components/services";
import UserWebsiteContact from "../userSite/components/contact";
import DashboardMain from "../metaWeb/dashboard/mainDash";
import DashboardDelete from "../metaWeb/dashboard/functions/deleteWebsite";
import DashboardFeedback from "../metaWeb/dashboard/functions/feedbacks";
import DashboardFeed from "../metaWeb/dashboard/functions/feed";
import EditWebsite from "../metaWeb/dashboard/functions/editWebsite";
import Search from "../metaWeb/search/search";
import UpgradeToPro from "../metaWeb/upgrade/upgrade";

import forgotPasswordEmail from '../metaWeb/auth/forgetPassword/forgetPassword'
import NewPasswordEmail from '../metaWeb/auth/forgetPassword/newPassword'

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    component: Login,
    children: [
      { path: "", component: LoginMain },
      { path: "reset-password", component: forgotPasswordEmail },
      { path: "new-password/:email", component: NewPasswordEmail },
    ],
  },
  {
    path: "/signup",
    component: SignUpMain,
  },
  {
    path: "/search",
    component: Search,
  },
  {
    path: "/dashboard",
    component: Dashboard,
    children: [
      { path: "", component: DashboardMain },
      { path: "delete", component: DashboardDelete },
      { path: "/createWebsite", component: CreateWebsite },
      { path: "feedback", component: DashboardFeedback },
      { path: "feedback/:shopid", component: DashboardFeed },
      { path: "/editWebsite/:id", component: EditWebsite },
    ],
  },

  {
    path: "/userWebsite/about",
    component: UserWebsiteAbout,
  },
  {
    path: "/userWebsite/services",
    component: UserWebsiteServices,
  },
  {
    path: "/userWebsite/contact",
    component: UserWebsiteContact,
  },
  {
    path: "/userWebsite/:id",
    component: UserWebsite,
  },
  {
    path: "/upgradetopro",
    component: UpgradeToPro,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;