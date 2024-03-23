<template>
  <q-layout view="hHh lpR fFf">

    <!-- <q-header elevated style="background-color: #FFFFFF"> -->
    <q-header style="background-color: #FFFFFF">
      <q-toolbar>
        <q-toolbar-title >
          <span :class="` text-accent`">PsyNet</span>
          <span :class="`text-primary`">Vk</span>
        </q-toolbar-title>
        <q-space />
        <q-btn>asd</q-btn>
      </q-toolbar>
    </q-header>

    <q-page-container style="background-color: #F5F5F5">
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script setup lang="ts">

</script>