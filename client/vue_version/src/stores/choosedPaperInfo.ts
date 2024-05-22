import { defineStore } from "pinia";
import { ref } from "vue";
// PaperRow通过props从Home或SearchResult拿到论文数据，一旦点击了一个PaperRow组件就选择了这篇论文跳到简化页面
// PaperRow组件点击后就状态管理全局变量保存论文数据，在DetailPaper组件显示这些保存了的数据
export const useChoosedPaperInfoStore = defineStore(
  "choosed-paper-info",
  () => {
    const choosed_paper_id = ref("");
    const choosed_title_en = ref("");
    const choosed_title_ja = ref("");
    const choosed_authors = ref([]);
    const choosed_categories = ref([]);
    const choosed_published = ref("");
    const choosed_pdf_url = ref("");
    const choosed_content_en = ref("");

    return {
      choosed_paper_id,
      choosed_title_en,
      choosed_title_ja,
      choosed_authors,
      choosed_categories,
      choosed_published,
      choosed_pdf_url,
      choosed_content_en,
    };
  },
  {
    persist: true,
  }
);
