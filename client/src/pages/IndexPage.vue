<template>
  <q-page class="flex items-center justify-center column">
    <div>
      <h2 class="text-center">Login</h2>
      <h6 class="text-center">Select an account to analyze</h6>
    </div>
    <vk-authorization />
  </q-page>
</template>

<script setup>
import VkAuthorization from 'src/components/VkAuthorization.vue';
</script>

<style scoped>
</style>
