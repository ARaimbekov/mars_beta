// main.js
import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import { createVuetify } from 'vuetify'; 
import 'vuetify/dist/vuetify.min.css'; 

const app = createApp(App);
const vuetify = createVuetify();

app.use(vuetify);
app.config.globalProperties.$axios = axios;

app.mount('#app', true);