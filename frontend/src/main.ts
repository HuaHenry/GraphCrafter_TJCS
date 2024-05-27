import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import store from "./store/index"
//vuetify用不了 已卸载
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
import "hooper/dist/hooper.css";
import './assets/scss/style.scss'

const app = createApp(App);

import router from "./router/index";

import ElementPlus from "element-plus";
import "element-plus/dist/index.css";


app.use(router);
app.use(ElementPlus);
app.use(store);
app.mount("#app");


import axios from 'axios';

// 设置后端服务器的基准 URL
axios.defaults.baseURL = 'http://127.0.0.1:8080';