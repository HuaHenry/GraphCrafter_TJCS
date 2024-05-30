/*
 * @Author: LoveKamila 120189976+LoveKamila@users.noreply.github.com
 * @Date: 2024-05-06 15:40:08
 * @LastEditors: LoveKamila 120189976+LoveKamila@users.noreply.github.com
 * @LastEditTime: 2024-05-26 15:40:28
 * @FilePath: \rainfo\src\main.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
/*
 * @Author: LoveKamila 120189976+LoveKamila@users.noreply.github.com
 * @Date: 2024-05-06 15:40:08
 * @LastEditors: LoveKamila 120189976+LoveKamila@users.noreply.github.com
 * @LastEditTime: 2024-05-26 15:11:41
 * @FilePath: \rainfo\src\main.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router/router';
import VueScrollactive from 'vue-scrollactive';
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
import "hooper/dist/hooper.css";
import './assets/scss/style.scss'

import store from './store'; // 导入Vuex store

Vue.config.productionTip = false
Vue.use(VueScrollactive);


new Vue({
    vuetify,
    router,
    store,
    render: h => h(App),
}).$mount('#app')