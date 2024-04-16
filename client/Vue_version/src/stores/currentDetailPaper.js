import { defineStore } from "pinia";
import { ref } from "vue";

export const useCurrentDetailPaperStore = defineStore(
  "current-detail-paper",
  () => {
    // const currentDetailPaper = ref(); //() 是不行的，会有画面が真っ白になるバグ 血痛的教训；但意外""似乎work
    const currentDetailPaper = ref([]);
    return { currentDetailPaper };
  }
);
