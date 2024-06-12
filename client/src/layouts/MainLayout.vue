<template>
  <q-layout view="hHh lpR fFf">
    <!-- <q-header elevated style="background-color: #FFFFFF"> -->
    <q-header style="background-color: #FFFFFF">
      <q-toolbar>
        <q-toolbar-title class="row">
          <!-- <span :class="`text-accent`">PsyNet</span>
          <span :class="`text-primary`">Vk</span> -->
          <div class="q-gutter-sm q-ml-sm" v-for="link in links">
            <q-btn
              :label="link.title"
              :to="link.to"
              color="dark"
              flat
            />
          </div>
        </q-toolbar-title>
        <q-space />
        <q-btn-dropdown outline label="@id" color="dark" dropdown-icon="false">
          <q-list class="text-negative">
            <q-item  clickable v-close-popup @click="onItemClick">
              <q-item-section>
                <q-item-label>
                  Выход
                </q-item-label>
              </q-item-section>
            </q-item>
          </q-list>
        </q-btn-dropdown>
      </q-toolbar>
    </q-header>

    <q-page-container style="background-color: #F5F5F5">
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script setup lang="ts">
const links = [
  { title: 'Главная', to: '/' },
  { title: 'Анализ', to: '/analysis' },
  { title: 'Результаты', to: '/results' }
]

</script>