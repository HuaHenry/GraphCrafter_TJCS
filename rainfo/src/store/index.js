import Vue from 'vue';
import Vuex from 'vuex';
import router from "../router/router";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isLoggedIn: false
  },
  mutations: {
    setLoginState(state, isLoggedIn) {
      state.isLoggedIn = isLoggedIn;
    }
  },
  actions: {
    login({ commit }) {
      commit('setLoginState', true);
    },
    logout({ commit }) {
      commit('setLoginState', false);
      commit('setCurUserID', null); // 注销时清除用户ID
      router.push('/login'); // 导航回登录页面
    }
  },
  getters: {
    isLoggedIn: state => state.isLoggedIn
  }
});
