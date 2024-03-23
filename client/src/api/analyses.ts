import axios from 'axios'

export const sendPayloadToBackend = async (payload: string) => {
    try {
        const response = await axios.post('http://localhost:8000/callback', payload)
        console.log('Backend response:', response.data)
    } catch (error) {
        console.error('Error sending payload to backend:', error)
    }
}