import axios from 'axios';

const API_URL = process.env.VUE_APP_API_URL || 'http://localhost:5000/api';

const apiClient = axios.create({
  baseURL: API_URL,
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
});

export default {
  setAuthToken(token) {
    apiClient.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  },
  removeAuthToken() {
    delete apiClient.defaults.headers.common['Authorization'];
  },
  async login(credentials) {
    const response = await apiClient.post('/auth/login', credentials);
    return response.data;
  },
  async register(credentials) {
    const response = await apiClient.post('/auth/register', credentials);
    return response.data;
  },
  async uploadFile(date, file) {
    const formData = new FormData();
    formData.append('file', file);
    const response = await apiClient.post(`/entries/${date}/upload`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    return response.data;
  },
  async getEntries(date) {
    const response = await apiClient.get(`/entries/${date}`);
    return response.data;
  },
  async deleteEntry(date, filename) {
    const response = await apiClient.delete(`/entries/${date}/${filename}`);
    return response.data;
  },
  async transcribeAudio(date, filename) {
    const response = await apiClient.post(`/entries/${date}/${filename}/transcribe`);
    return response.data;
  },
  async getDashboardMetrics() {
    const response = await apiClient.get('/dashboard');
    return response.data;
  }
};