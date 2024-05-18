import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";

const app = createApp(App);

import router from "./router";
app.use(router);

import { createPinia } from "pinia";
const pinia = createPinia();
app.use(pinia);

import axios from "axios";
axios.defaults.baseURL = "http://127.0.0.1:8000";
// axios.defaults.baseURL = "http://192.168.122.150:8000";
// axios.defaults.baseURL = "http://47.245.14.48";

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
const vuetify = createVuetify({
  components,
  directives,
});
app.use(vuetify);

import i18n from "./i18n";
app.use(i18n);

app.mount("#app");
