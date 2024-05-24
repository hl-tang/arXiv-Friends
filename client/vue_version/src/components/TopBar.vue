<script setup lang="ts">
import { ref } from "vue";
const searchContent = ref("")

import MagnifyIcon from "vue-material-design-icons/Magnify.vue";

import { useRouter } from "vue-router";
const router = useRouter()
const jumpSearchResult = () => {
  router.push({ path: '/search', query: { search_content: searchContent.value } })
}

import TranslateIcon from "vue-material-design-icons/Translate.vue";
import { useI18n } from 'vue-i18n'
const { locale, t } = useI18n()
function changeLanguage(lang: string) {
  locale.value = lang
}

import { Switch } from "vue-dark-switch"
import { useDark, useToggle } from '@vueuse/core'
const isDark = useDark()
const toggleDark = useToggle(isDark)

let showMenu = ref(false)
import AccountIcon from "vue-material-design-icons/Account.vue";
import LogoutVariantIcon from "vue-material-design-icons/LogoutVariant.vue";

import { storeToRefs } from 'pinia'
import { useIsLoggedInStore } from '../stores/isLoggedIn'
const { isLoggedIn, username } = storeToRefs(useIsLoggedInStore())

/* const sessionid = ref("");
sessionid.value = $cookies.get("sessionid");
console.log(sessionid.value);
console.log($cookies.get("sessionid"));
console.log($cookies.get("cookie")); */

import axios from 'axios';
const logout = async () => {
  axios.get('/api/logout/')
    .then(res => {
      isLoggedIn.value = false;
      console.log("Response Data:", res.data);
    })
  router.push('/loginregister');
};

console.log(isLoggedIn.value);

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
          <button
            class="w-9 h-9 flex items-center justify-center rounded-full border bg-gray-300 hover:bg-gray-400 hover:ring-2"
            @click="jumpSearchResult">
            <MagnifyIcon fillColor="#636363" />
          </button>
        </div>
      </div>

      <div class="flex items-center justify-end gap-3 min-w-[275px] max-w-[350px] w-full">
        <!-- switch multi language -->
        <el-dropdown trigger="hover">
          <TranslateIcon :size="30" fillColor="#ffcbcb"/>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="changeLanguage('en')">English</el-dropdown-item>
              <el-dropdown-item @click="changeLanguage('ja')">日本語</el-dropdown-item>
              <el-dropdown-item @click="changeLanguage('zh-cn')">中文</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>

        <!-- dark mode -->
        <div class="flex items-center mr-5">
          <Switch />
          <button @click="toggleDark()" class="mr-1">
            <span class="text-slate-100">{{ isDark ? 'Dark' : 'Light' }}</span>
          </button>
        </div>

        <div v-if="!isLoggedIn" class="flex items-center">
          <router-link to="/loginregister">
            <button
              class="flex items-center bg-red-600 hover:bg-red-400 text-white font-semibold border rounded-md px-3 py-[6px] ring-2 ring-gray-300 hover:ring-4 hover:ring-red-300">
              <span class="mx-2 font-medium ">{{ t('login') }}</span>
            </button>
          </router-link>

        </div>

        <div v-else class="flex items-center">
          <div class="relative">
            <button class="mt-1" @click="showMenu = !showMenu">
              <img class="rounded-full" width="45" src="../assets/default_avatar.png">
              <!-- :src="$userStore.image"> -->
            </button>


            <div v-if="showMenu" id="PopupMenu"
              class="absolute bg-white rounded-lg py-1 w-[140px] shadow-xl border top-[55px] -right-5">
              <router-link :to="{ name: 'MyPage', query: { username: username } }" @click="showMenu = false"
                class="flex items-center justify-start py-3 px-2 hover:bg-gray-100 cursor-pointer">
                <!-- <StarOutlineIcon :size="17" fillColor="#636363" class="ml-4" /> -->
                <AccountIcon :size="25" fillColor="#636363" />
                <span class="pl-2 font-semibold text-sm text-gray-700">MyPage</span>
              </router-link>

              <div @click="logout"
                class="flex items-center justify-start py-3 px-1.5 hover:bg-gray-100 border-t cursor-pointer">
                <LogoutVariantIcon :size="25" fillColor="#636363" />
                <span class="pl-2 font-semibold text-sm">Log out</span>
              </div>

            </div>

          </div>
        </div>


      </div>

    </div>

  </div>

</template>

<style scoped></style>