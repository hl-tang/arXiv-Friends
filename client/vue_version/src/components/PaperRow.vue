<script setup lang="ts">
import { toRefs, ref, watch } from "vue"

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
import StarIcon from "vue-material-design-icons/Star.vue";

const isLiked = ref(false);
// 只有在mypage收藏一开始显示黄色星星
const route = useRoute();

if (route.path === '/mypage') {
  isLiked.value = true;
}
// console.log("isLike:", isLiked.value);

import axios from 'axios';

const emit = defineEmits(['cancel-like-at-my-page']);

import { useIsLoggedInStore } from '../stores/isLoggedIn'
const { isLoggedIn } = storeToRefs(useIsLoggedInStore())

const likeOrCancel = () => {
  if (isLoggedIn.value === false) {
    alert("please login");
    return;
  }

  // 发请求
  if (isLiked.value === false) {
    // 收藏
    axios.post('/api/like/', null, { // null作为请求体（body）占位符
      params: {
        paper_id: paper_id.value
      }
    }).then(res => {
      // console.log("Response Data:", res.data)
      if (res.data.msg) {
        alert(res.data.msg)
      }
    }).catch((err) => {
      console.log(err)
    });
  }
  else {
    // 取消
    axios.delete('/api/like/', {
      params: {
        paper_id: paper_id.value
      }
    }).then(res => {
      // Emit an event to notify the parent component
      emit('cancel-like-at-my-page');
    }).catch((err) => {
      console.log(err)
    });
  }
  // 真伪转换,写在第一句那判断条件就反过来了
  isLiked.value = !isLiked.value;
};


</script>

<template>
  <!-- PaperRow -->
  <!-- w-[1060px]不固定的话，有些paper会不知道为什么超级宽 -->
  <div class="flex space-x-10">

    <div class="w-[870px] my-2 overflow-hidden flex flex-col justify-between rounded-2xl shadow-2xl  hover:ring-2 ring-gray-500
        border-b hover:border-t hover:border-y-2 hover:border-x cursor-pointer"
      :class="[omitAbstract ? 'h-[265px]' : 'h-[170px]', isDark ? 'bg-neutral-700' : 'bg-neutral-200']"
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

    <!-- 把这个div去掉 button由于最外层的flex影响，长度拉满。 flex横向排列纵向拉满，flex-col反过来,所以加个div -->
    <div class="flex items-center">
      <button :class="['p-2 rounded-full', isLiked ? 'bg-yellow-500' : 'bg-gray-400', 'hover:p-2.5']"
        @click="likeOrCancel">
        <star-icon :size="30" :fillColor="isLiked ? '#ffff00' : '#666666'" />
      </button>
    </div>

  </div>

</template>

<style scoped>
.date {
  font-size: 14px;
}
</style>