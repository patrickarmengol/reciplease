import { createApp } from 'vue';
import App from './App.vue';

import './assets/main.css';

Vue.prototype.$apiUrl = process.env.VUE_APP_API_URL || 'http://0.0.0.0/5000';

createApp(App).mount('#app')
