import { defineStore } from "pinia";
import { ref } from "vue";

export const useFivePapersStore = defineStore("five-papers", () => {
  const fivePapers = ref([]);
  return { fivePapers };
});
