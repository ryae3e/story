<template>
  <div class="entry-page">
    <h1>{{ date }}</h1>
    <Upload />
    <TranscribeButton />
    <TextEntry />
    <div class="entry-content">
      <p v-if="text">{{ text }}</p>
      <audio v-if="audio" controls :src="audio"></audio>
    </div>
  </div>
</template>

<script>
import Upload from './Upload.vue';
import TranscribeButton from './TranscribeButton.vue';
import TextEntry from './TextEntry.vue';
import api from '../services/api.js';

export default {
  name: 'EntryPage',
  components: {
    Upload,
    TranscribeButton,
    TextEntry
  },
  data() {
    return {
      date: '',
      text: '',
      audio: ''
    };
  },
  async created() {
    this.date = this.$route.params.date;
    const response = await api.getEntry(this.date);
    this.text = response.data.text;
    this.audio = response.data.audio;
  }
};
</script>

<style scoped>
.entry-page {
  padding: 20px;
}
.entry-content {
  margin-top: 20px;
}
</style>