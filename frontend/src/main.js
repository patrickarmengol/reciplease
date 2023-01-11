import { createApp } from 'vue';
import App from './App.vue';

import './assets/main.css';


let app = createApp(App)
app.config.globalProperties.$apiUrl = import.meta.env.API_URL || 'http://0.0.0.0:5000';
app.mount('#app');