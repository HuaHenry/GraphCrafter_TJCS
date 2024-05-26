import { createStore } from 'vuex';

export default createStore({
  state() {
    return {
      isLoggedIn: false
    };
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