<template>
  <div class="register-container">
    <h2>Register</h2>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" v-model="email" required />
        <!-- <span v-if="error" style="color: red;">{{ error }}</span> -->
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div class="mb-2 flex items-center text-sm">
        <el-radio-group v-model="userType" class="ml-4">
          <el-radio value="normal" size="large" >Normal User</el-radio>
          <el-radio value="premium" size="large" >Premium User</el-radio>
        </el-radio-group>
      </div>
      <div v-if="userType === 'premium'" class="form-group">
        <label for="inviteCode">Invite Code</label>
        <input type="text" id="inviteCode" v-model="inviteCode" required />
      </div>
      <button type="submit">Register</button>
    </form>
    <div class="login-link">
      <router-link to="/login">Already have an account? Click to login</router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import qs from 'qs';
import { mapActions } from 'vuex';
import { ElMessage } from 'element-plus';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      userType: 'normal', // Default user type is normal
      inviteCode: '',
      error: ''
    };
  },
  methods: {
    ...mapActions(['login']),
    validateEmail() {
      const invalidChars = /[!#$%^&*()+|~=`{}[\]:";'<>?,\/]/;
      if (invalidChars.test(this.email)) {
        this.error = '邮箱包含非法字符';
      } else {
        this.error = '';
      }
    },
    validatePassword(password) {
      const minLength = 6;
      const hasUpperCase = /[A-Z]/.test(password);
      const hasLowerCase = /[a-z]/.test(password);
      const hasNumber = /[0-9]/.test(password);
      const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);

      return password.length >= minLength &&
            !hasSpecialChar && // Ensure no special characters
            ((hasUpperCase && hasLowerCase) ||
              (hasUpperCase && hasNumber) ||
              (hasLowerCase && hasNumber));
    },

    handleRegister() {
            this.validateEmail();
            console.log(this.error);
            if (this.error==="邮箱包含非法字符") {
              ElMessage.error({
                message: "邮箱包含非法字符",
                duration: 1500
              });
              return;
            }
            if (!this.validatePassword(this.password)) {
              ElMessage.error({
                message: "密码长度必须至少为6位，且包含大小写字母和数字中的至少两种",
                duration: 1500
              });
              return;
            }

            let postData = qs.stringify({
                username: this.username,
                email: this.email,
                password: this.password,
                userType: this.userType,
                inviteCode: this.inviteCode
            })
            // this.showTips(this.user.username)
            axios.post(
                "/register", postData,
                {
                    headers: {'Content-Type':'application/x-www-form-urlencoded'}
                })
                .then(res => {
                    console.log(res.status);
                    if (res.status === 200 && res.data=="success") {
                      ElMessage.success({
                        message: "注册成功",
                        duration: 1500
                      });
                        this.$router.push("/login")
                    } 
                })
                .catch(error => {
                  if (error.response && error.response.status === 401) {
                    ElMessage.error({
                      message: "邀请码错误",
                      duration: 1500
                    });
                  }
                  else if (error.response.status === 400){
                    ElMessage.error({
                      message: "用户名已占用，请选择其他用户名",
                      duration: 1500
                    });
                  }
                  else {
                    ElMessage.error({
                      message: "注册失败",
                      duration: 1500
                    });
                  }
                });
        }
  }
};
</script>

<style scoped>
.error-message {
  position: absolute;
  bottom: -1.5em; /* Adjust based on your needs */
  left: 0;
  color: red;
  visibility: hidden; /* Hide by default */
}

.error-message:empty {
  visibility: hidden; /* Hide if empty */
}

.error-message:not(:empty) {
  visibility: visible; /* Show if not empty */
}
.register-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: calc(50vh - 60px); /* Full viewport height minus some space for top and bottom */
  max-width: 400px;
  margin: 130px auto; /* Center horizontally and give top/bottom margins */
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
input[type="email"],
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
  margin: 10px 0;
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

.login-link {
  text-align: center;
  margin-top: 20px;
}

.login-link a {
  color: #2f90b9;
  text-decoration: none;
}

.login-link a:hover {
  text-decoration: underline;
}

@media (max-width: 600px) {
  .register-container {
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
