<template>
    <div id="building">
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
                <el-radio-group v-model="userType" class="ml-4">
                <el-radio value="user" size="large">User</el-radio>
                <el-radio value="admin" size="large">Admin</el-radio>
                </el-radio-group>
            </div>
            <button type="submit">Log In</button>
            </form>
            <div class="register-link">
            <router-link to="/register">Don't have an account? Click to register</router-link>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import qs from 'qs';
import {mapActions } from 'vuex';
import store from "../store/index";
import { ElMessage } from 'element-plus';

export default {
  data() {
    return {
      username: '',
      password: '',
      userType: 'user' // Default user type is user
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
        console.log(res.status);
        console.log(res.data.status);
        console.log(res.data.user_id);
        console.log(res.data.isAdmin);
        if (res.status === 200 && res.data.status === "success") {
          this.login({user_id: res.data.user_id,isAdmin:res.data.isAdmin});
          console.log("登录成功");
          store.commit("setCurUserID",res.data.user_id);
          store.commit("setAdminState",res.data.isAdmin);
          localStorage.setItem("user",res.data.user_id);
          localStorage.setItem('is_admin', res.data.isAdmin);
          ElMessage.success({
            message: "登录成功",
            duration: 1500
          });
          if(this.userType === "admin"){
            this.$router.push("/manager");
          }
          else{
            this.$router.push("/Demo");
          }
        }
        else if (res.data.status === 'error') {
              this.$message.error("登录失败");
              console.log("登录失败");
              return;
        }
        })
        .catch(error => {
          if (error.response)
          {
            if (error.response.status === 401) {
              ElMessage.error({
                message: "用户名或密码错误",
                duration: 1500
              });
            }
            else if (error.response.status === 402){
              ElMessage.error({
                message: "您不是系统管理员",
                duration: 1500
              });
            }
            else {
              ElMessage.error({
                message: "登录失败：未知错误",
                duration: 1500
              });
            }
          }
          else {
            ElMessage.error({
              message: error,
              duration: 1500
            });
          }
        });
    },
  }
};
</script>

<style scoped>

#building{
    /* background:url("https://bpic.588ku.com/back_our/20210902/bg/3eae21e778dae.png"); */
    background:url("https://bpic.588ku.com/video_listen/588ku_pic/21/06/07/8cf50ff21b08565c17c19ae00cf70805.jpg");
    width:100%;
    height:100%;
    position:fixed;
    background-size:100% 100%;
}

.login-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: calc(50vh - 60px); /* Full viewport height minus some space for top and bottom */
  max-width: 400px;
  margin: 150px auto; /* Center horizontally and give top/bottom margins */
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

/*input[type="radio"] {*/
/*  background: #666666;*/
/*  margin-right: 5px;*/
/*  transform: scale(0.5);*/
/*}*/

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
