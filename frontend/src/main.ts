import { createApp } from "vue";
import App from "./App.vue";
import store from "./store/index"
import router from "./router/index";
//vuetify用不了 已卸载
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";

const app = createApp(App);

app.use(router);
app.use(ElementPlus);
app.use(store);
app.mount("#app");


import axios from 'axios';

// 设置后端服务器的基准 URL
axios.defaults.baseURL = 'http://127.0.0.1:8080';
// axios.defaults.baseURL = 'http://123.60.90.34:3306';