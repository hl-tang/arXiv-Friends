<script setup lang="ts">
import TopBar from "../components/TopBar.vue";
import PaperRow from "../components/PaperRow.vue";

import { storeToRefs } from 'pinia'
import { useIsLoggedInStore } from '../stores/isLoggedIn'
const { username } = storeToRefs(useIsLoggedInStore())

import { useOmitAbstractStore } from '../stores/omitAbstract'
const { omitAbstract } = storeToRefs(useOmitAbstractStore())

import StarBoxIcon from "vue-material-design-icons/StarBox.vue";
import HistoryIcon from "vue-material-design-icons/History.vue";


import { useI18n } from 'vue-i18n'
const { t } = useI18n()

import { useDark } from '@vueuse/core'
const isDark = useDark()

import { ref } from 'vue';
const like_cnt = ref(0);
const history_cnt = ref(0);

import axios from 'axios';

const fetchFavoritesCnt = () => {
  axios.get('/api/likelist_cnt/')
    .then(res => {
      console.log("like_cnt: ", res.data)
      like_cnt.value = res.data
    })
    .catch((err) => {
      console.log(err)
    });
};
fetchFavoritesCnt();  // 进入页面后第一次叩くapi


const currentTab = ref('favorites'); // 当前显示的标签页（'favorites' 或 'history'）

const likedPapers = ref([]);
const historyPapers = ref([]);

const fetchFavoritesPapers = () => {
  axios.get('/api/like/')
    .then(res => {
      // console.log("response data: ", res.data)
      likedPapers.value = res.data
      console.log("likedPapers: ", likedPapers.value);
    })
    .catch((err) => {
      console.log(err)
    });
};
fetchFavoritesPapers();


const renewFavorites = () => {
  // 不设置0.5s延迟访问的话，可能PaperRow那里delete请求数据库还没做完，导致这里显示有问题
  setTimeout(() => {
    fetchFavoritesPapers();
  }, 500);
  setTimeout(() => {
    fetchFavoritesCnt();
  }, 500);
}


</script>

<template>
  <TopBar />

  <div class="pt-[100px] 2xl:pl-[400px] lg:pl-[280px] lg:pr-0 pr-2 w-[calc(100%-90px)] max-w-[1800px] 2xl:mx-auto">
    <div class="flex w-[calc(100vw-230px)]">
      <img class="max-w-[100px]  max-h-[100px] rounded-full" src="../assets/default_avatar.png">

      <div class="ml-5 w-full">
        <div class="text-[30px] font-bold truncate">
          {{ username }}
        </div>
        <!-- <div class="text-[18px] truncate">email</div> -->
        <v-btn variant="tonal" class="mt-2">
          Edit Profile
        </v-btn>
      </div>
    </div>

    <div class="min-h-screen flex flex-col p-4">
      <!-- Tabs Section -->
      <div class="w-full max-w-md">
        <div class="flex justify-around items-center border-b-4 "
          :class="isDark ? 'border-gray-700' : 'border-gray-300'">
          <el-badge :value="like_cnt" class="item" :offset="[-12, 3]">
            <button @click="currentTab = 'favorites'"
              :class="currentTab === 'favorites' ? 'border-b-4 border-blue-500 text-blue-400' : 'text-gray-600'"
              class="flex items-center py-2 px-4 focus:outline-none">
              <star-box-icon :size="25" :fillColor="currentTab === 'favorites' ? '#2acaea' : '#636363'" />
              收藏
            </button>
          </el-badge>

          <el-badge :value="history_cnt" class="item" :offset="[-12, 3]">
            <button @click="currentTab = 'history'"
              :class="currentTab === 'history' ? 'border-b-4 border-blue-500 text-blue-400' : 'text-gray-600'"
              class="flex items-center py-2 px-4 focus:outline-none">
              <history-icon :size="25" :fillColor="currentTab === 'history' ? '#2acaea' : '#636363'" />
              浏览历史
            </button>
          </el-badge>

          <div class="flex  items-center justify-center space-x-2">
            <v-switch v-model="omitAbstract" color="red-darken-3" label="" value="red-darken-3" hide-details></v-switch>
            <span>{{ t('showAbstract') }}</span>
          </div>
        </div>

        <!-- Content Section -->
        <div class="mt-4">
          <div v-if="currentTab === 'favorites'">
            <!-- 收藏内容 -->
            <p>这里显示收藏的内容...</p>

            <!-- 父组件(MyPage.vue)通过emit监听事件cancel-like-at-my-page，然后触发函数renewFavorites -->
            <div v-for="paper in likedPapers" :key="paper.paper_id" class="flex items-center space-x-3">
              <PaperRow :paper_id="paper.paper_id" :title_en="paper.title_en" :title_ja="paper.title_ja"
                :content_en="paper.content_en" :pdf_url="paper.pdf_url" :published="paper.published"
                :authors="paper.authors" :categories="paper.categories"
                @cancel-like-at-my-page="renewFavorites" />
            </div>

          </div>
          <div v-else-if="currentTab === 'history'">
            <!-- 浏览历史内容 -->
            <p>这里显示浏览历史的内容...</p>
          </div>
        </div>
      </div>
    </div>

  </div>


</template>

<style scoped></style>