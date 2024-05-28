import { defineStore } from "pinia";
import { ref } from "vue";
// 在LoginRegister和TopBar以及PaperRow的星星用到
// 而且控制全局的是否登录判断
// 后端用Django的@login_required修饰的endpoint未登录访问直接报错404，未登录的报错由前端处理了直接弹出警告
export const useIsLoggedInStore = defineStore(
  "is-logged-in",
  () => {
    const isLoggedIn = ref(false);
    const username = ref("bbb");
    return { isLoggedIn, username };
  },
  {
    persist: true,
  }
);
