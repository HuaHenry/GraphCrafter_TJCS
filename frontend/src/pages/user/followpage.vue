<template>
  <div class="follow-container">
    <!-- Exit button -->
    <div class="close-circle">
      <div class="close close-mask-white" @click="exitPage">
        <Close style="width: 1.2em; height: 1.2em; color: rgba(51, 51, 51, 0.8)" />
      </div>
    </div>
    <!-- Following list -->
    <ul class="following-list">
      <li v-for="following in followings" :key="following.id" class="following-item">
        <img :src="following.avatar" class="user-avatar" alt="User Avatar">
        <div class="user-details">
          <div class="user-name">{{ following.name }}</div>
          <div class="user-stats">{{ following.followers }} 粉丝   {{ following.posts }} 发帖</div>
        </div>
        <button class="follow-button">已关注</button>
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
const followings = ref([]);

const exitPage = () => {
  router.go(-1);
};

onMounted(async () => {
  try {
    const response = await axios.get(`/api/followings/${userId}`);
    followings.value = response.data.followings;
  } catch (error) {
    ElMessage.error('Failed to load followings');
    console.error('Error loading followings:', error);
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
  top: -0px;
  left: -25px;
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

.following-list {
  list-style: none;
  padding: 0;
}

.user-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  margin-right: 16px;
}

/* .user-details {
  flex-grow: 1;
} */

.user-name {
  font-weight: bold;
}

.user-stats {
  color: rgba(0, 0, 0, 0.6);
  font-size: 14px;
}

.following-item {
  display: flex;
  align-items: center;
  justify-content: space-between; /* Keeps elements justified but can be adjusted */
  gap: 10px; /* Reduces the gap between elements in the flex container */
  margin-bottom: 16px;
}

.user-details {
  flex-grow: 1;
  margin-right: 0px; /* Adjust or remove if unnecessary */
}

.follow-button {
  padding: 7px 14px;
  background-color: #ff4d4f;
  color: white;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  font-size: 14px;
  margin-left: 5px;
}


</style>
