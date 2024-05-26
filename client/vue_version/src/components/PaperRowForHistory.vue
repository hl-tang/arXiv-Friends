<script setup lang="ts">
import { toRefs, ref, watch } from "vue"

// PaperRow作为子组件被Home和SearchResult引用，Home和SearchResult通过axios从后端获得数据，传给PaperRow
// !!! History还要多传一个has_note的布尔变数 !!!
const props = defineProps({
  paper_id: String,
  title_en: String,
  title_ja: String,
  authors: Array,
  published: String,
  content_en: String,
  pdf_url: String,
  categories: Array,
  has_note: Boolean
})
const { paper_id, title_en, title_ja, authors, published, content_en, pdf_url, categories, has_note } = toRefs(props);

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
import NoteEditIcon from "vue-material-design-icons/NoteEdit.vue";
import TrashCanIcon from "vue-material-design-icons/TrashCan.vue";

const isHovered = ref(false);
const dialog = ref(false);

import axios from 'axios';
const emit = defineEmits(['delte-history-at-my-page', 'post-note-at-my-page']);

const notes = ref("");

const checkNotes = () => {
  dialog.value = true;

  axios.get('/api/notes/', {
    params: {
      paper_id: paper_id.value
    }
  })
    .then(res => {
      console.log("response data: ", res.data)
      // notes.value = res.data //小心notes = ref("")而不是ref({})
      notes.value = res.data.notes
      console.log("获取到的notes: ", notes.value);
    })
    .catch((err) => {
      console.log(err)
    })
};

const postNotes = () => {
  axios.post('/api/notes/', {
    "paper_id": paper_id.value,
    "notes": notes.value
  })
    .then(res => {
      // Emit an event to notify the parent component
      emit('post-note-at-my-page');
    });
  alert("post success")
  // Emit an event to notify the parent component
  //写在.then外面就不会等写入数据库之后再emit,从而导致MyPage renewHistoryEditNote时数据库还没更新而返回错的结果导致显示有问题
  // emit('post-note-at-my-page');
};


const deleteHistory = () => {
  axios.delete('/api/browse-history/', {
    params: {
      paper_id: paper_id.value
    }
  }).then(res => {
    // Emit an event to notify the parent component
    emit('delte-history-at-my-page');
  }).catch((err) => {
    console.log(err)
  });
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
      <!-- <button :class="['p-2 rounded-full', has_note ? 'bg-red-400 hover:bg-red-300' : 'bg-gray-400', 'hover:p-2.5']"
        @click="checkAndEditNote">
        <note-edit-icon :size="30" :fillColor="has_note ? '#000000' : '#666666'" />
      </button> -->

      <div class="text-center pa-4">

        <button :class="['p-2 rounded-full', has_note ? 'bg-red-400 hover:bg-red-300' : 'bg-gray-400', 'hover:p-2.5']"
          @click="checkNotes">
          <note-edit-icon :size="30" :fillColor="has_note ? '#000000' : '#666666'" />
        </button>

        <v-dialog v-model="dialog" width="450">

          <div class="flex flex-col bg-gray-400 p-4">
            <!-- <p class="text-lg">右下部分内容</p> -->
            <v-textarea label="Input your notes here:" variant="outlined" v-model="notes"
              placeholder="Notes"></v-textarea>

            <div class="flex justify-between">
              <button
                class="bg-red-600 text-gray-300 font-semibold py-2 px-4 w-30 rounded-md hover:bg-red-700 hover:text-gray-100"
                @click="postNotes">
                Submit
              </button>

              <button
                class="bg-red-600 text-gray-300 font-semibold py-2 px-4 w-30 rounded-md hover:bg-red-700 hover:text-gray-100"
                @click="dialog = false">
                Close
              </button>
            </div>
          </div>

        </v-dialog>
      </div>

    </div>

    <div class="flex items-center" @mouseover="isHovered = true" @mouseleave="isHovered = false">
      <button class="p-2 rounded-full bg-gray-400 hover:p-2.5 hover:bg-red-500" @click="deleteHistory">
        <trash-can-icon :size="30" :fillColor="isHovered ? '#000000' : '#666666'" />
      </button>
    </div>




  </div>

</template>

<style scoped>
.date {
  font-size: 14px;
}
</style>