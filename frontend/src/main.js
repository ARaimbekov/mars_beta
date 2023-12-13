import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';

const app = createApp(App);

// Внедрите axios во все экземпляры Vue
app.config.globalProperties.$axios = axios;

app.mount('#app');