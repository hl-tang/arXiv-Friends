<script setup lang="ts">

</script>

<template>
  <div id="TopBar" class="fixed bg-neutral-700 mt-0.5 z-30 flex items-center w-full border-b h-[70px]">
    <div class="flex items-center justify-between w-full px-6 mx-auto">

      <router-link :to="{ name: 'Home' }">
        <img src="../assets/arxiv-logo-1-300x135.png" style="transform: scale(0.6);">
      </router-link>


    </div>

  </div>
  
</template>

<style scoped></style>