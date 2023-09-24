<template>
  <div class="text-entry">
    <h2>Journal Entry</h2>
    <textarea v-model="entryText" placeholder="Write your journal entry here..."></textarea>
    <button @click="saveEntry">Save Entry</button>
  </div>
</template>

<script>
import api from '../services/api.js';

export default {
  data() {
    return {
      entryText: '',
    };
  },
  methods: {
    async saveEntry() {
      try {
        const response = await api.post('/entries', { text: this.entryText });
        this.entryText = '';
        this.$emit('entrySaved', response.data);
      } catch (error) {
        console.error('Error saving entry:', error);
      }
    },
  },
};
</script>

<style scoped>
.text-entry {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.text-entry textarea {
  width: 80%;
  height: 200px;
  margin-bottom: 20px;
}

.text-entry button {
  width: 100px;
  height: 30px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

.text-entry button:hover {
  background-color: #45a049;
}
</style>