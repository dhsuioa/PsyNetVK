<template>
  <q-page class="flex items-center justify-center column">
        <div class="title">
          <!-- <span :class="`text-weight-medium ${$q.dark.isActive ? 'text-white' : 'text-accent'
            }`">PsyNet</span> -->
          <span :class="`text-weight-medium text-h2 text-accent`">PsyNet</span>
          <span :class="`text-weight-medium text-h2 text-primary`">Vk</span>
            <!-- <h2 class="text-center">MindMapVK</h2>
            <h2 class="text-center">VKMentalInsight</h2> -->
        </div>
        <vk-authorization />
    </q-page>
</template>

<script setup>
import VkAuthorization from 'src/components/VkAuthorization.vue';
</script>

<style scoped>

.title {
  margin-bottom: 20px
}
</style>