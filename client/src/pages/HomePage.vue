<template>
    <q-page class="flex items-center justify-center column">
        <div>
            <h2 class="text-center">PsyNetVK</h2>
            <information/>
            <!-- <h2 class="text-center">MindMapVK</h2>
            <h2 class="text-center">VKMentalInsight</h2> -->
        </div>
    </q-page>
</template>
  
<script setup>
import { onMounted } from 'vue'
import Information from 'src/components/Information.vue'
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
  