// main.js — reconstructed from app_9ada4703.js (webpack module "56d7")
// Vue 2.6.11 SPA. Third-party libs live in chunk-vendors_30de09e7.js.

import Vue from "vue";
import VueCookie from "vue-cookie";       // webpack module 00e7  -> this.$cookie
import BootstrapVue from "bootstrap-vue";  // webpack module 5f5b
import VueRouter from "vue-router";        // webpack module 8c4f
import axios from "axios";                 // webpack module bc3a

import App from "./App.vue";
import Home from "./views/Home.vue";       // route "index"
import Detail from "./views/Detail.vue";   // route "detail"
import Login from "./views/Login.vue";     // route "login"
import Report from "./views/Report.vue";   // route "report"

// core-js polyfills pulled in by webpack: c975 d3b7 e260 e6cf cca6 a79d 3ca3 ddb0 2b3d
// App.vue scoped styles: modules 034f / 85ec (empty in this build)

Vue.use(VueRouter);

const router = new VueRouter({
  routes: [
    { path: "/",           name: "index",  component: Home },
    { path: "/:id/detail", name: "detail", component: Detail },
    { path: "/login/",     name: "login",  component: Login },
    { path: "/report",     name: "report", component: Report },
  ],
});

Vue.config.productionTip = false;
Vue.use(VueCookie);
Vue.use(BootstrapVue);

// Shared axios client, exposed as this.$http on every component.
const http = axios.create({
  baseURL: "http://" + location.host + "/",
  timeout: 1000,
});

// Request interceptor:
//   - if the request URL contains "..", block it ("hack detected") — a path-
//     traversal guard done entirely client-side (trivially bypassable by
//     calling the API directly).
//   - otherwise attach the auth token from the cookie as a "token" header.
http.interceptors.request.use(
  function (config) {
    if (config.url.indexOf("..") > -1) {
      alert("hack detected");
      return Promise.reject();
    }
    config.headers["token"] = VueCookie.get("token");
    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);
Vue.prototype.$http = http;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
