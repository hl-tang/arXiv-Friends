<script setup lang="ts">
import { ref } from "vue";
const searchContent = ref("")

import MagnifyIcon from "vue-material-design-icons/Magnify.vue";

import { useRouter } from "vue-router";
const router = useRouter()
const jumpSearchResult = () => {
  router.push({ path: '/search', query: { search_content: searchContent.value } })
}


import { useI18n } from 'vue-i18n'
const { locale, t } = useI18n()
function changeLanguage(lang: string) {
  locale.value = lang
}

</script>

<template>
  <div id="TopBar" class="fixed bg-neutral-700 mt-0.5 z-30 flex items-center w-full border-b h-[70px]">
    <div class="flex items-center justify-between w-full px-6 mx-auto">

      <router-link :to="{ name: 'Home' }">
        <img src="../assets/arxiv-logo-1-300x135.png" style="transform: scale(0.6);">
      </router-link>

      <div class="hidden md:flex items-center bg-[#F1F1F2] p-1 rounded-full max-w-[580px] w-full ">
        <input type="text"
          class="w-full pl-3 my-2 bg-transparent placeholder-[#838383] text-[15px] focus:outline-none text-black"
          v-model="searchContent" :placeholder="t('searchPapers')" @keyup.enter="jumpSearchResult">
        <div class="px-3 py-1 flex items-center border-l border-l-gray-300">
          <button class="w-9 h-9 flex items-center justify-center rounded-full border bg-gray-300 hover:bg-gray-400 hover:ring-2"
          @click="jumpSearchResult">
            <MagnifyIcon fillColor="#636363" />
          </button>
        </div>
      </div>

      



    </div>

  </div>

</template>

<style scoped></style>