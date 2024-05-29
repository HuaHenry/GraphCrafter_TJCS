<template>
  <div class="follow-container">
    <!-- 退出按钮 -->
    <div class="close-circle">
      <div class="close close-mask-white" @click="exitPage">
        <Close style="width: 1.2em; height: 1.2em; color: rgba(51, 51, 51, 0.8)" />
      </div>
    </div>
    <!-- 粉丝列表 -->
    <ul class="follower-list">
      <li v-for="follower in followers" :key="follower.id" class="follower-item">
        <img :src="follower.avatar" class="user-avatar" alt="User Avatar">
        <div class="user-details">
          <div class="user-name">{{ follower.name }}</div>
          <div class="user-stats">{{ follower.followers }} 粉丝   {{ follower.posts }} 帖子 </div>
        </div>
        <button class="follow-button">回关</button>
      </li>
    </ul>
  </div>
</template>


<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { ElMessage } from 'element-plus';
import { Close } from '@element-plus/icons-vue';
import { useRouter } from 'vue-router';
import store from "../../store/index";

const router = useRouter();
const userId = store.state.user_id;
const followers = ref([]);  // Changed from followings to followers

const exitPage = () => {
  router.go(-1);
};

onMounted(async () => {
  try {
    const response = await axios.get(`/api/followers/${userId}`);  // Fetch followers
    followers.value = response.data.followers;  // Adjusted for followers
  } catch (error) {
    ElMessage.error('Failed to load followers');
    console.error('Error loading followers:', error);
  }
});
</script>


<style scoped>
.follow-container {
  background-color: white;
  border-radius: 20px;
  padding: 32px;
  max-width: 800px;
  margin: auto;
  margin-top: 100px;
  position: relative;
}

.close-circle {
  position: absolute;
  top: 0px;
  right: 0px;
  z-index: 100;
  cursor: pointer;
}

.close-mask-white {
  background-color: white;
  border-radius: 100%;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.close {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 40px;
  height: 40px;
}

.follower-list{
  list-style: none;
  padding: 0;
}

.follower-item {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
}

.user-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  margin-right: 16px;
}

.user-details {
  flex-grow: 1;
}

.user-name {
  font-weight: bold;
}

.user-stats {
  color: rgba(0, 0, 0, 0.6);
  font-size: 14px;
}

.follow-button {
  padding: 7px 14px;
  background-color: #ff4d4f;
  color: white;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  font-size: 14px; /* Adjusted font size to make text smaller */
}
</style>
