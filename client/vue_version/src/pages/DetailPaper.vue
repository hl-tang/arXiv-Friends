<script setup lang="ts">
import TopBar from "../components/TopBar.vue";

import { ref } from "vue"
const tab = ref("null") //vuetify的tab

import { storeToRefs } from 'pinia'
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


import { useI18n } from 'vue-i18n'
const { t } = useI18n()

import { useDark } from '@vueuse/core'
const isDark = useDark()

import AccountSchoolIcon from "vue-material-design-icons/AccountSchool.vue";
import CalendarClockIcon from "vue-material-design-icons/CalendarClock.vue";
import ChartPieIcon from "vue-material-design-icons/ChartPie.vue";
import FileDownloadIcon from "vue-material-design-icons/FileDownload.vue";

function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toISOString().slice(0, 10);
}

const loading = ref(true);
const res_data = ref({});
import axios from 'axios'
axios.post('/api/simplify', {
  "paper_id": choosed_paper_id.value,
  "content_en": choosed_content_en.value
})
  .then(res => {
    loading.value = false;
    // console.log("Response Data:", res.data);
    res_data.value = res.data;
    console.log("Response Data:", res_data.value);

    if (res_data.value.msg === "tourist access can only access 3 times in 24h") {
      alert(res_data.value.msg);
    }
  })
  .catch((err) => {
    console.log(err)
  })

const notes = ref("");

const postNotes = () => {
  console.log("notes: " + notes.value);

}

</script>

<template>
  <TopBar />
  <div class="pt-[70px]">
    <div class="min-h-screen flex flex-col">
      <!-- 标题展示框 -->
      <header class="bg-zinc-600 text-rose-300 p-4 text-center">
        <h1 class="text-3xl font-bold">{{ choosed_title_en }}</h1>
        <h1 class="font-semibold text-2xl">{{ choosed_title_ja }}</h1>
      </header>

      <!-- 主内容区域 -->
      <div class="flex">
        <!-- 左半部分 -->
        <div class="w-2/3 p-4">
          <!-- <p class="text-lg">左半部分内容</p> -->

          <div v-if="loading">
            <!-- <el-skeleton :rows="30" animated /> -->
            <v-skeleton-loader color="#ffcbcb" type="article"></v-skeleton-loader>
            <v-skeleton-loader color="#ffcbcb" type="article"></v-skeleton-loader>
            <div v-for="(item, index) in [1, 2, 3]" :key="index">
              <!-- <span>{{ index }}</span> -->
              <v-skeleton-loader color="#ffcbcb" type="article"></v-skeleton-loader>
            </div>
          </div>

          <div v-else class="mx-8 my-4">
            <v-card :color="isDark ? 'grey-darken-4' : 'white'">
              <v-tabs v-model="tab" color="red-lighten-1" bg-color="grey-darken-2" align-tabs="center">
                <v-tab value="1">English Abstract</v-tab>
                <v-tab value="2">翻訳された要旨</v-tab>
                <v-tab value="3">簡易化された要旨</v-tab>
              </v-tabs>

              <v-card-text>
                <v-window v-model="tab">
                  <v-window-item value="1">
                    <div class="mt-3 text-lg mx-6 indent-8">
                      {{ choosed_content_en }}
                    </div>
                  </v-window-item>

                  <v-window-item value="2">
                    <div class="mt-3 text-lg mx-6 indent-8">
                      {{ res_data.content_ja }}
                    </div>
                  </v-window-item>

                  <v-window-item value="3" class="mt-3 text-lg mx-6 indent-8">
                    {{ res_data.content_plain }}
                  </v-window-item>
                </v-window>
              </v-card-text>
            </v-card>
          </div>

        </div>

        <!-- 右半部分 -->
        <div class="w-1/3 flex flex-col space-y-6 mx-8 my-4">
          <!-- 右上部分 -->
          <div class="flex-1 mt-4 bg-gray-300 text-black p-4 space-y-4">
            <!-- <p class="text-lg">右上部分内容</p> -->
            <div class="">
              <span class="flex">
                <AccountSchoolIcon :size="25" fillColor="#636363" />
                <span class="ml-1 mr-4">{{ t('authors') }}:</span>
              </span>
              <!-- {{ choosedPaperInfoStore.Authors }} -->
              <!-- bug:最后一个item会显示, -->
              <span v-for="(name, index) in choosed_authors" :key="name" class="ml-2">
                {{ name }}<span v-if="index < choosed_authors.length - 1">,</span>
              </span>
            </div>

            <div class="flex items-center">
              <CalendarClockIcon :size="25" fillColor="#636363" />
              <span class="ml-1 mr-4">{{ t('published') }}:</span>
              <!-- {{ choosedPaperInfoStore.Published }} -->
              <span class="date">{{ formatDate(choosed_published) }}</span>
            </div>

            <div class="flex">
              <ChartPieIcon :size="25" fillColor="#636363" />
              <span class="ml-1 mr-4">{{ t('categories') }}:</span>
              <!-- {{ choosedPaperInfoStore.Categories }} -->
              <!-- bug:最后一个item会显示, -->
              <span v-for="Category in choosed_categories" :key="Category" class="mr-2 ">
                {{ Category }},
              </span>
            </div>

            <div class="flex">
              <FileDownloadIcon :size="25" fillColor="#636363" />
              <span class="ml-1 mr-4">{{ t('download') }}:</span>
              <a :href="choosed_pdf_url" target="_blank"
                class="underline decoration-dashed decoration-pink-600">[pdf]</a>
            </div>
          </div>
          <!-- 右下部分 -->
          <div class="flex flex-col bg-gray-400 p-4">
            <!-- <p class="text-lg">右下部分内容</p> -->
            <v-textarea label="Input your notes here:" variant="outlined" v-model="notes"
              placeholder="Notes"></v-textarea>

            <button
              class="bg-red-600 text-gray-300 font-semibold py-2 px-4 w-32 rounded-md hover:bg-red-700 hover:text-gray-100"
              @click="postNotes">
              Submit
            </button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
.date {
  font-size: 14px;
  color: #645e5e;
}
</style>