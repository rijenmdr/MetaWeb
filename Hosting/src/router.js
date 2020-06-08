// import Vue from "vue";
// import Router from "vue-router";
// import AppHeader from "./layout/AppHeader";
// import AppFooter from "./layout/AppFooter";
// import Components from "./views/Components.vue";
// import Landing from "./views/Landing.vue";
// import Login from "./views/Login.vue";
// import Register from "./views/Register.vue";
// import Profile from "./views/Profile.vue";

// Vue.use(Router);

// export default new Router({
//   linkExactActiveClass: "active",
//   routes: [
//     {
//       path: "/",
//       name: "components",
//       components: {
//         header: AppHeader,
//         default: Components,
//         footer: AppFooter
//       }
//     },
//     {
//       path: "/landing",
//       name: "landing",
//       components: {
//         header: AppHeader,
//         default: Landing,
//         footer: AppFooter
//       }
//     },
//     {
//       path: "/login",
//       name: "login",
//       components: {
//         header: AppHeader,
//         default: Login,
//         footer: AppFooter
//       }
//     },
//     {
//       path: "/register",
//       name: "register",
//       components: {
//         header: AppHeader,
//         default: Register,
//         footer: AppFooter
//       }
//     },
//     {
//       path: "/profile",
//       name: "profile",
//       components: {
//         header: AppHeader,
//         default: Profile,
//         footer: AppFooter
//       }
//     }
//   ],
//   scrollBehavior: to => {
//     if (to.hash) {
//       return { selector: to.hash };
//     } else {
//       return { x: 0, y: 0 };
//     }
//   }
// });
import Vue from "vue";
import VueRouter from "vue-router";
import Home from "./metaWeb/home/home";
import Login from "./metaWeb/auth/login/login";
import LoginMain from "./metaWeb/auth/login/loginMain";
import SignUpMain from "./metaWeb/auth/signup/signup";
import Dashboard from "./metaWeb/dashboard/dashboard";
import DashboardMain from "./metaWeb/dashboard/mainDash";
import DashboardDelete from "./metaWeb/dashboard/functions/deleteWebsite";
import DashboardFeedback from "./metaWeb/dashboard/functions/feedbacks";
import CreateWebsite from "./metaWeb/dashboard/functions/createWebsite";
import ErrorHotel from "./metaWeb/premium/errorHotel";
import DashboardFeed from "./metaWeb/dashboard/functions/feed";
import EditWebsite from "./metaWeb/dashboard/functions/editWebsite";
import ProTemplate from "./metaWeb/premium/proTemplate";
import HotelTemplate from "./metaWeb/premium/hotel";
import PortfolioTemplate from "./metaWeb/premium/portfolio";
import UpgradeToPro from "./metaWeb/upgrade/upgrade";
import PaymentConfirm from "./metaWeb/upgrade/confirm";
import DashboardDeleteSuccess from "./metaWeb/dashboard/functions/deleteHelper/confirm";
import UserWebsite from "./userSite/userSite";
import UserWebsiteAbout from "./userSite/components/about";
import UserWebsiteServices from "./userSite/components/services";
import UserWebsiteContact from "./userSite/components/contact";
import Hotel from "./hotel/hotel";

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
    children: [{ path: "", component: LoginMain }],
  },
  {
    path: "/signup",
    component: SignUpMain,
  },
  {
    path: "/dashboard",
    component: Dashboard,
    children: [
      { path: "", component: DashboardMain },
      { path: "delete", component: DashboardDelete },
      { path: "error", component: ErrorHotel },
      { path: "createWebsite", component: CreateWebsite },
      { path: "feedback", component: DashboardFeedback },
      { path: "feedback/:shopid", component: DashboardFeed },
      { path: "/editWebsite/:id", component: EditWebsite },
      { path: "protemplates", component: ProTemplate },
      { path: "hotel", component: HotelTemplate },
      { path: "portfolio", component: PortfolioTemplate },
      { path: "/upgradetopro", component: UpgradeToPro },
    ],
  },
  { path: "/payment-confirm", component: PaymentConfirm },
  { path: "/deleteSuccess", component: DashboardDeleteSuccess },

  { path: "/userWebsite/about", component: UserWebsiteAbout },
  { path: "/userWebsite/services", component: UserWebsiteServices },
  { path: "/userWebsite/contact", component: UserWebsiteContact },
  { path: "/userWebsite/:id", component: UserWebsite },
  {
    path: "/:id",
    component: Hotel,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
