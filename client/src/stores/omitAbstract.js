import { defineStore } from "pinia";
import { ref } from "vue";
// 在home和PaperRow都用到
export const useOmitAbstractStore = defineStore("omit-abstract", () => {
  const omitAbstract = ref(true);
  return { omitAbstract };
});
