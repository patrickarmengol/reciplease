import { createApp } from 'vue';
import App from './App.vue';

import './assets/main.css';


const app = createApp(App).mount('#app');
app.config.globalProperties.$apiUrl = process.env.API_URL || 'http://0.0.0.0/5000';
