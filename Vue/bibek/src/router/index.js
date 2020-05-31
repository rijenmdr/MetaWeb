import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../metaWeb/home/home";
import LoginMain from "../metaWeb/auth/login";
import SignUpMain from "../metaWeb/auth/signup/signup";
import Dashboard from "../metaWeb/dashboard/dashboard";
import CreateWebsite from "../metaWeb/dashboard/functions/createWebsite";
import UserWebsite from "../userSite/userSite";
import UserWebsiteAbout from "../userSite/components/about";
import UserWebsiteLanding from "../userSite/components/landing";
import UserWebsiteServices from "../userSite/components/services";
import UserWebsiteContact from "../userSite/components/contact";
import DashboardMain from "../metaWeb/dashboard/mainDash";
import DashboardDelete from "../metaWeb/dashboard/functions/deleteWebsite";
import DashboardFeedback from "../metaWeb/dashboard/functions/feedbacks";
import DashboardFeed from "../metaWeb/dashboard/functions/feed";
import EditWebsite from "../metaWeb/dashboard/functions/editWebsite";
import Search from "../metaWeb/search/search"

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
    path: "/search",
    component: Search,
  },
  {
    path: "/dashboard",
    component: Dashboard,
    children: [
      { path: "", component: DashboardMain },
      { path: "delete", component: DashboardDelete },
      { path: "/createWebsite", component: CreateWebsite},
      { path: "feedback", component:DashboardFeedback},
      { path: "feedback/:shopid", component:DashboardFeed},
      { path: "/editWebsite/:id", component: EditWebsite},
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
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
