import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../metaWeb/home/home";
import Portfolio from "../components/portfolio/Portfolio";
import Books from "../components/NewBooks/books";
import Login from "../components/oldbooks/login";
import Try from "../components/Auth/login";
import LoginMain from '../metaWeb/auth/login'
import SignUpMain from '../metaWeb/auth/signup'
import Dashboard from '../metaWeb/dashboard/dashboard'

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path:'/login',
    component:LoginMain
  },
  {
    path:'/signup',
    component:SignUpMain
  },
  {
    path:'/dashboard',
    component:Dashboard
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
