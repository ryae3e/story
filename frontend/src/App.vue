<template>
  <div id="app">
    <header>
      <h1>Personal Journal</h1>
      <Authentication />
    </header>
    <main>
      <Calendar />
      <router-view />
    </main>
    <footer>
      <Dashboard />
    </footer>
  </div>
</template>

<script>
import Calendar from './components/Calendar.vue'
import Authentication from './components/Authentication.vue'
import Dashboard from './components/Dashboard.vue'

export default {
  name: 'App',
  components: {
    Calendar,
    Authentication,
    Dashboard
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>