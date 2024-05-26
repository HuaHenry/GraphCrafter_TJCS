import Vue from 'vue';
import Vuex from 'vuex';

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
    }
  },
  getters: {
    isLoggedIn: state => state.isLoggedIn
  }
});
