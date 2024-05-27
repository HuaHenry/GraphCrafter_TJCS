<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div class="form-group user-type">
        <label class="radio-label">
          <input type="radio" value="normal" v-model="userType" checked />
          Normal User
        </label>
        <label class="radio-label">
          <input type="radio" value="premium" v-model="userType" />
          Premium User
        </label>
        <label class="radio-label">
          <input type="radio" value="admin" v-model="userType" />
          Admin User
        </label>
      </div>
      <button type="submit">Log In</button>
    </form>
    <div class="register-link">
      <router-link to="/register">Don't have an account? Click to register</router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import qs from 'qs';
import {mapActions } from 'vuex';
import store from "../store/index";

export default {
  data() {
    return {
      username: '',
      password: '',
      userType: 'normal' // Default user type is normal
    };
  },
  methods: {
    ...mapActions(['login']),
    handleLogin() {
            let postData = qs.stringify({
                username: this.username,
                password: this.password,
                userType: this.userType
            })
            axios.post("/login", postData,
            {
                headers: {'Content-Type':'application/x-www-form-urlencoded'}
            }
			).then(res => {
        if (res.status === 200 && res.data.status === "success") {
          this.login();
          console.log("登录成功");
          store.commit("setCurUserID",res.data.user_id);
          this.$router.push("/dashboard");
        }
        else if (res.data.status === 'error') {
             this.$message.error("登录失败");
          console.log("登录失败");
          return;
        }
                })
                .catch(() => {
                  console.log("登录失败");
                })
        },
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: calc(50vh - 60px); /* Full viewport height minus some space for top and bottom */
  max-width: 400px;
  margin: 30px auto; /* Center horizontally and give top/bottom margins */
  padding: 20px; /* Reduce padding */
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  font-family: 'Arial', sans-serif;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #666;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.user-type {
  display: flex;
  justify-content: space-around;
  margin: 20px 0;
}

.radio-label {
  font-weight: bold;
  color: #333;
  font-size: 0.9em;
}

input[type="radio"] {
  margin-right: 5px;
  transform: scale(0.5);
}

button {
  width: 100%;
  padding: 10px;
  background-color: #2f90b9;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #0056b3;
}

.register-link {
  text-align: center;
  margin-top: 20px;
}

.register-link a {
  color: #2f90b9;
  text-decoration: none;
}

.register-link a:hover {
  text-decoration: underline;
}

@media (max-width: 600px) {
  .login-container {
    padding: 15px;
  }

  h2 {
    font-size: 1.5em;
  }

  button {
    padding: 8px;
    font-size: 14px;
  }
}
</style>
