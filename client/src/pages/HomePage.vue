<template>
    <q-page class="flex items-center justify-center column">
        <div>
            <h2 class="text-center">PsyNetVK</h2>
            <!-- <h2 class="text-center">MindMapVK</h2>
            <h2 class="text-center">VKMentalInsight</h2> -->
        </div>
    </q-page>
</template>
  
<script setup>
import { onMounted } from 'vue'
import axios from 'axios'

// обработка параметров после загрузки компонента
onMounted(() => {
    const urlParams = new URLSearchParams(window.location.hash)
    const payload = urlParams.get('payload')
    console.log('Payload:', payload)

    if (payload) {
        // отправляем payload на бэкенд
        sendPayloadToBackend(payload);
    }
});

const sendPayloadToBackend = async (payload) => {
    try {
        const response = await axios.post('http://localhost:8000/callback', payload)
        console.log('Backend response:', response.data)
    } catch (error) {
        console.error('Error sending payload to backend:', error)
    }
}
</script>
  
<style scoped></style>
  