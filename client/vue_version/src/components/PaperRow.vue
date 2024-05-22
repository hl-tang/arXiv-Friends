<script setup lang="ts">
import { toRefs, ref } from "vue"

// PaperRow作为子组件被Home和SearchResult引用，Home和SearchResult通过axios从后端获得数据，传给PaperRow
const props = defineProps({
  paper_id: String,
  title_en: String,
  title_ja: String,
  authors: Array,
  published: String,
  content_en: String,
  pdf_url: String,
  categories: Array
})
const { paper_id, title_en, title_ja, authors, published, content_en, pdf_url, categories } = toRefs(props);

import { storeToRefs } from 'pinia'
import { useOmitAbstractStore } from '../stores/omitAbstract'
// const omitAbstractStore = useOmitAbstractStore()
const { omitAbstract } = storeToRefs(useOmitAbstractStore())

import { useChoosedPaperInfoStore } from '../stores/choosedPaperInfo'
const {
  choosed_paper_id,
  choosed_title_en,
  choosed_title_ja,
  choosed_authors,
  choosed_categories,
  choosed_published,
  choosed_pdf_url,
  choosed_content_en
} = storeToRefs(useChoosedPaperInfoStore());

import { useDark } from '@vueuse/core'
const isDark = useDark()

function formatDate(dateString: string) {
  const date = new Date(dateString);
  return date.toISOString().slice(0, 10);
}

import { useRoute, useRouter } from "vue-router"
const router = useRouter()

const jumpDetailPaper = () => {
  choosed_paper_id.value = paper_id.value;
  choosed_title_en.value = title_en.value;
  choosed_title_ja.value = title_ja.value;
  choosed_authors.value = authors.value;
  choosed_categories.value = categories.value;
  choosed_published.value = published.value;
  choosed_pdf_url.value = pdf_url.value;
  choosed_content_en.value = content_en.value;
  router.push('/detailpaper');
}

import FileLinkOutlineIcon from "vue-material-design-icons/FileLinkOutline.vue";

</script>

<template>
  <!-- PaperRow -->
  <!-- w-[1060px]不固定的话，有些paper会不知道为什么超级宽 -->
  <div class="w-[850px] my-2 overflow-hidden flex flex-col justify-between rounded-2xl shadow-2xl  hover:ring-2 ring-gray-500
        border-b hover:border-t hover:border-y-2 hover:border-x cursor-pointer"
    :class="[omitAbstract ? 'h-[260px]' : 'h-[160px]', isDark ? 'bg-neutral-700' : 'bg-neutral-200']"
    @click="jumpDetailPaper">

    <div class="mx-2 flex -mb-1">
      <div class="mr-2">{{ paper_id }}</div>

      <a :href="pdf_url" target="_blank" class="underline decoration-dashed decoration-pink-600">
        <file-link-outline-icon :size="25" fillColor="#636363" />
      </a>
    </div>

    <div class="flex flex-col justify-center items-center text-xl hover:italic bg-rose-500" @click="jumpDetailPaper">
      <div class="mr-3 font-bold text-gray-950">{{ title_en }}</div>
      <div class="font-semibold text-gray-800">{{ title_ja }}</div>
    </div>

    <!-- 需要频繁切换 v-show -->
    <div v-show="omitAbstract" class="px-6">
      <el-scrollbar height="90px">
        <p class="text-base font-semibold" :class="[isDark ? 'text-gray-200' : 'text-gray-700']">
          {{ content_en }}
        </p>
      </el-scrollbar>
    </div>

    <div class="ml-1 truncate">
      <span class="mr-2">Authors:</span>
      {{ authors.join(', ') }}
    </div>
    <div class="flex mx-2 -mt-3">
      <span class="mr-2">Submitted:</span>
      <p class="date pt-0.5">{{ formatDate(published) }}</p>
    </div>
  </div>
</template>

<style scoped>
.date {
  font-size: 14px;
}
</style>