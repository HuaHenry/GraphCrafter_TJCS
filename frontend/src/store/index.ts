import { createStore } from 'vuex';
import router from '@/router';  // 确保路径正确

export default createStore({
  state() {
    const user_id = localStorage.getItem('user');
    const is_admin = localStorage.getItem('is_admin') === 'true'; // 从 localStorage 读取管理员状态
    return {
      isLoggedIn: !!user_id,  // 如果 user_id 存在则设置为 true
      user_id: user_id,        // 直接使用 localStorage 中的 user_id
      isAdmin: is_admin        // 布尔值，如果用户是管理员则为 true
    };
  },
  mutations: {
    setLoginState(state, isLoggedIn) {
      state.isLoggedIn = isLoggedIn;
    },
    setCurUserID(state, id){
      state.user_id = id;
    },
    setAdminState(state, isAdmin) {
      state.isAdmin = isAdmin;  // 设置管理员状态
    }
  },
  actions: {
    login({ commit }, { user_id, isAdmin }) {
      localStorage.setItem('user', user_id); // 假设 user_id 是传递给 login action 的
      localStorage.setItem('is_admin', isAdmin); // 存储管理员状态
      commit('setLoginState', true);
      commit('setCurUserID', user_id);
      commit('setAdminState', isAdmin); // 提交管理员状态
    },
    logout({ commit }) {
      commit('setLoginState', false);
      commit('setCurUserID', null); // 注销时清除用户ID
      commit('setAdminState', false); // 注销时重置管理员状态
      localStorage.removeItem("user"); // 清除 localStorage 中的用户信息
      localStorage.removeItem("is_admin"); // 清除管理员状态
      router.push('/'); // 导航回登录页面
    }

  },
  getters: {
    isLoggedIn: state => state.isLoggedIn,
    userID:state => state.user_id,
    isAdmin: state => state.isAdmin // 添加一个 getter 来获取管理员状态
  }
});