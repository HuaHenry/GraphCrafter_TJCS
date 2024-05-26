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
          <input type="radio" value="admin" v-model="userType" />
          Admin User
        </label>
      </div>
      <div v-if="userType === 'admin'" class="form-group">
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

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      userType: 'normal', // Default user type is normal
      inviteCode: ''
    };
  },
  methods: {
    ...mapActions(['login']),
    handleRegister() {
            let postData = qs.stringify({
                username: this.username,
                email: this.email,
                password: this.password,
                userType: this.userType,
                inviteCode: this.inviteCode
            })
            // this.showTips(this.user.username)
            axios.post(
                "http://127.0.0.1:5000/register", postData,
                {
                    headers: {'Content-Type':'application/x-www-form-urlencoded'}
                })
                .then(res => {
                    if (res.status === 200 && res.data=="success") {
                        //this.showTips("注册成功！", "success")
                        this.$router.push("/login")
                    } else if (res.data === 'error') {
                        //this.showTips("该用户名已被注册！", "danger")
                    }
                }).catch(() => {
                    //this.showTips("注册失败")
                })

        }

    // async handleRegister() {
    //   try {
    //     const response = await axios.post('http://127.0.0.1:5000/register', {
    //       username: this.username,
    //       email: this.email,
    //       password: this.password,
    //       userType: this.userType,
    //       inviteCode: this.inviteCode
    //     });
    //     alert(response.data.message);
    //   } catch (error) {
    //     alert(error.response.data.message || 'An error occurred');
    //   }
    // }
  }
};
</script>

<style scoped>
.register-container {
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
