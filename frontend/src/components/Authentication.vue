<template>
  <div class="authentication">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input type="text" v-model="username" placeholder="Username" required>
      <input type="password" v-model="password" placeholder="Password" required>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import api from '../services/api.js';

export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await api.login(this.username, this.password);
        this.$emit('login', response.data.token);
      } catch (error) {
        console.error('An error occurred:', error);
      }
    }
  }
};
</script>

<style scoped>
.authentication {
  width: 300px;
  margin: 0 auto;
}

form {
  display: flex;
  flex-direction: column;
}

input, button {
  margin-bottom: 10px;
}
</style>