import { createRouter, createWebHistory } from "vue-router";

import Home from "../pages/Home.vue";
import SearchResult from "../pages/SearchResult.vue";
import DetailPaper from "../pages/DetailPaper.vue";
import Profile from "../pages/Profile.vue";
// import Play from "../pages/Play.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/search",
    name: "SearchResult",
    component: SearchResult,
  },
  {
    path: "/detailpaper",
    name: "DetailPaper",
    component: DetailPaper,
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
  },
  /* {
    path: "/play",
    component: Play,
  }, */
];

const router = createRouter({
  // history: createWebHistory(process.env.BASE_URL),
  // vite不用process.env
  // 报错看developer tool的Console的error
  // https://vitejs.dev/guide/env-and-mode.html 写法看文档
  // 其实createWebHistory() 小括号里空着也行
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;