<template>
  <div class="follow-container">
    <!-- Exit button -->
    <div class="close-circle" @click="exitPage">
      <Close style="width: 1.2em; height: 1.2em; color: rgba(51, 51, 51, 0.8)" />
    </div>
    <!-- Follower list -->
    <ul class="follower-list">
      <li v-for="follower in followers" :key="follower.id" class="follower-item">
        <img :src="follower.avatar" class="user-avatar" alt="User Avatar">
        <div class="user-details">
          <div class="user-name">{{ follower.name }}</div>
          <div class="user-stats">{{ follower.followers }} 粉丝 {{ follower.posts }} 帖子</div>
        </div>
        <el-button type="danger" size="large" round @click="handleClick(follower.id)">
          {{ follower.buttonText }}
        </el-button>
      </li>
    </ul>
  </div>
</template>


<script lang="ts" setup>
import { ref, onMounted, reactive } from 'vue';
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus';
import { Close } from '@element-plus/icons-vue';
import { useRouter } from 'vue-router';
import store from "../../store/index";

const router = useRouter();
const userId = store.state.user_id;
const followers = ref([]);

const exitPage = () => {
  router.go(-1);
};

const followUser = async (followerId) => {
  if (store.state.user_id === followerId) {
    ElMessage.error('您不能关注自己。');
    return;
  }
  try {
    const response = await axios.post('/api/follow', {
      follower_id: store.state.user_id,
      followed_id: followerId
    });
    if (response.status === 200) {
      ElMessage.success('关注成功！');
      updateFollowerState(followerId);
    }
  } catch (error) {
    ElMessage.error('关注失败，请稍后再试。');
  }
};

const unfollowUser = async (followerId) => {
  try {
    const response = await axios.post('/api/unfollow', {
      follower_id: store.state.user_id,
      followed_id: followerId
    });
    if (response.status === 200) {
      ElMessage.success('取消关注成功！');
      updateFollowerState(followerId);
    }
  } catch (error) {
    ElMessage.error('取消关注失败，请稍后再试。');
  }
};

const updateFollowerState = async (followerId) => {
  const index = followers.value.findIndex(f => f.id === followerId);
  if (index !== -1) {
    const { isFollowed, status } = await checkFollowStatus(followerId);
    followers.value[index].isFollowed = isFollowed;
    followers.value[index].status = status;
    followers.value[index].buttonText = createButtonLabel(followers.value[index]);
  }
};

const createButtonLabel = (follower) => {
  if (follower.status === 1) {
    return '互相关注';
  } else if (follower.isFollowed) {
    return '已关注';
  } else {
    return '关注';
  }
};

const handleClick = async (followerId) => {
  const index = followers.value.findIndex(f => f.id === followerId);
  if (index !== -1) {
    if (followers.value[index].isFollowed || followers.value[index].status === 1) {
      try {
        await ElMessageBox.confirm('您确定要取消关注吗？', '确认信息', {
          confirmButtonText: '确认',
          cancelButtonText: '取消',
          type: 'warning'
        });
        await unfollowUser(followerId);
      } catch (error) {
        ElMessage.info('已取消操作');
      }
    } else {
      await followUser(followerId);
    }
  }
};

const checkFollowStatus = async (followerId) => {
  try {
    const response = await axios.get(`/api/check-follow/${userId}/${followerId}`);
    return {
      isFollowed: response.data.isFollowed,
      status: response.data.status
    };
  } catch (error) {
    console.error('Error checking follow status:', error);
    return { isFollowed: false, status: 0 };
  }
};

onMounted(async () => {
  try {
    const response = await axios.get(`/api/followers/${userId}`);
    followers.value = response.data.followers.map(follower => reactive({
      ...follower,
      ...checkFollowStatus(follower.id),
      buttonText: 'Loading...'  // Initial placeholder text
    }));
    followers.value.forEach(async (follower, index) => {
      const statusDetails = await checkFollowStatus(follower.id);
      followers.value[index].isFollowed = statusDetails.isFollowed;
      followers.value[index].status = statusDetails.status;
      followers.value[index].buttonText = createButtonLabel(follower);
    });
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
