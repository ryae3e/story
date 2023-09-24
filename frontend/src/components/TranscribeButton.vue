<template>
  <button @click="transcribe" :disabled="isTranscribing">Transcribe</button>
</template>

<script>
import api from '../services/api.js';

export default {
  data() {
    return {
      isTranscribing: false,
    };
  },
  methods: {
    async transcribe() {
      this.isTranscribing = true;
      try {
        await api.transcribeAudio(this.$route.params.date);
        this.$emit('transcriptionComplete');
      } catch (error) {
        console.error('Error transcribing audio:', error);
      } finally {
        this.isTranscribing = false;
      }
    },
  },
};
</script>

<style scoped>
button {
  margin-top: 10px;
}
</style>