<template>
    <q-page class="flex items-center justify-center column">
        <div>
            <HomeComponent/>
        </div>
    </q-page>
</template>
  
<script setup>
import { onMounted } from 'vue'
import HomeComponent from 'src/components/HomeComponent.vue'
import { sendPayloadToBackend} from 'src/api/analyses.ts'

// обработка параметров после загрузки компонента
onMounted(() => {
    const urlParams = new URLSearchParams(window.location.hash)
    const payload = urlParams.get('payload')
    console.log('Payload:', payload)

    if (payload) {
        // отправляем payload на бэкенд
        sendPayloadToBackend(payload);
    }
})
</script>
  
<style scoped></style>
  