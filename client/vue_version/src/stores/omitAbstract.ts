import { defineStore } from "pinia";
import { ref } from "vue";
// 在PaperRow和Home以及SearchResult中用到的变量，用来控制PaperRow是否显示摘要
export const useOmitAbstractStore = defineStore("omit-abstract", () => {
  const omitAbstract = ref(true);
  return { omitAbstract };
});
