import { createStore } from 'vuex';

export default createStore({
  state() {
    return {
      isLoggedIn: false,
      user_id:null
    };
  },
  mutations: {
    setLoginState(state, isLoggedIn) {
      state.isLoggedIn = isLoggedIn;
    },
    setCurUserID(state, id){
      state.user_id = id;
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
    isLoggedIn: state => state.isLoggedIn,
    userID:state => state.user_id
  }
});