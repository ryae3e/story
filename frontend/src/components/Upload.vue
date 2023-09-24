<template>
  <div>
    <h2>Upload MP3</h2>
    <input type="file" @change="handleFileUpload"/>
    <button @click="submitFile">Submit</button>
  </div>
</template>

<script>
import api from '../services/api.js';

export default {
  data() {
    return {
      file: ''
    }
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    submitFile() {
      let formData = new FormData();
      formData.append('file', this.file);

      api.post('/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(() => {
        console.log('File uploaded successfully');
      }).catch(err => {
        console.error(err);
      });
    }
  }
}
</script>

<style scoped>
h2 {
  margin-bottom: 15px;
}

input[type="file"] {
  margin-bottom: 15px;
}
</style>