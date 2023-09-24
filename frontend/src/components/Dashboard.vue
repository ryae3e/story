<template>
  <div class="dashboard">
    <h1>Dashboard</h1>
    <div class="metrics">
      <div class="metric">
        <h2>Total Entries</h2>
        <p>{{ totalEntries }}</p>
      </div>
      <div class="metric">
        <h2>Total Audio Files</h2>
        <p>{{ totalAudioFiles }}</p>
      </div>
      <div class="metric">
        <h2>Total Transcriptions</h2>
        <p>{{ totalTranscriptions }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../services/api.js'

export default {
  data() {
    return {
      totalEntries: 0,
      totalAudioFiles: 0,
      totalTranscriptions: 0
    }
  },
  created() {
    this.fetchMetrics()
  },
  methods: {
    async fetchMetrics() {
      try {
        const response = await api.get('/dashboard/metrics')
        this.totalEntries = response.data.totalEntries
        this.totalAudioFiles = response.data.totalAudioFiles
        this.totalTranscriptions = response.data.totalTranscriptions
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>

<style scoped>
.dashboard {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.metrics {
  display: flex;
  justify-content: space-between;
}

.metric {
  text-align: center;
}
</style>