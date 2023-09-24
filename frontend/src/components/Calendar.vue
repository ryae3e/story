<template>
  <div class="calendar">
    <vue-calendar @date-clicked="goToDate" :attributes="datesWithEntries"></vue-calendar>
  </div>
</template>

<script>
import VueCalendar from 'vue2-simple-calendar'
import api from '../services/api'

export default {
  name: 'Calendar',
  components: {
    VueCalendar
  },
  data() {
    return {
      datesWithEntries: []
    }
  },
  methods: {
    async goToDate(date) {
      this.$router.push({ name: 'EntryPage', params: { date: date } })
    },
    async getDatesWithEntries() {
      try {
        const response = await api.get('/entries/dates')
        this.datesWithEntries = response.data.map(date => {
          return { 
            date: date, 
            customClass: 'entry-date' 
          }
        })
      } catch (error) {
        console.error(error)
      }
    }
  },
  created() {
    this.getDatesWithEntries()
  }
}
</script>

<style scoped>
.entry-date {
  background-color: #ffeb3b;
}
</style>