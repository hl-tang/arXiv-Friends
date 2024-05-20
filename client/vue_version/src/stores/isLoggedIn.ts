import { defineStore } from "pinia";
import { ref } from "vue";
// 在LoginRegister和TopBar用到
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
