import { createStore } from 'vuex';
import router from '@/router';  // 确保路径正确

export default createStore({
  state() {
    const user_id = localStorage.getItem('user');
    return {
      isLoggedIn: !!user_id,  // 如果 user_id 存在则设置为 true
      user_id: user_id        // 直接使用 localStorage 中的 user_id
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
    login({ commit }, user_id) {
      localStorage.setItem('user', user_id); // 假设 user_id 是传递给 login action 的
      commit('setLoginState', true);
      commit('setCurUserID', user_id);
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