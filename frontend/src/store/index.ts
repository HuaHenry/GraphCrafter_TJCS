import { createStore } from 'vuex';
import router from '@/router';  // 确保路径正确

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
      commit('setCurUserID', null); // 注销时清除用户ID
      localStorage.removeItem("user"); // 清除 localStorage 中的用户信息
      router.push('/'); // 导航回登录页面
    }

  },
  getters: {
    isLoggedIn: state => state.isLoggedIn,
    userID:state => state.user_id
  }
});