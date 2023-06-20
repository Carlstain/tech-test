import { createApp } from 'vue'
import App from './App.vue'
import router from './router';
import store from './store';
import 'vuetify/styles';
import {createVuetify} from "vuetify";
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import axios from "axios";

axios.defaults.baseURL = new URL(`${import.meta.env.VITE_API_BASE_URL}`).href;

const app = createApp(App);

app.use(store)
app.use(router);

const vuetify= createVuetify({
    components,
    directives,
})

app.use(vuetify);

app.mount('#app');
