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
        <img :src="following.avatar" class="user-avatar" alt="User Avatar" @click="ToOther(following.id)">
        <div class="user-details">
          <div class="user-name">{{ following.name }}</div>
          <div class="user-stats">{{ following.followers }} 粉丝 · {{ following.posts }} 发帖</div>
        </div>
        <el-button type="danger" size="large" round @click="handleClick(following.id)" class="custom-danger-button">
          {{ following.buttonText }}
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
const followings = ref([]);

const exitPage = () => {
  router.go(-1);
};

const ToOther = (id: number) => {
  router.push({ path: "/other", query: { id: id } });
};

const followUser = async (followingId) => {
  if (store.state.user_id === followingId) {
    ElMessage.error('您不能关注自己。');
    return;
  }
  try {
    const response = await axios.post('/api/follow', {
      user_id: store.state.user_id,
      following_id: followingId
    });
    if (response.status === 200) {
      ElMessage.success('关注成功！');
      updateFollowingState(followingId);
    }
  } catch (error) {
    ElMessage.error('关注失败，请稍后再试。');
  }
};

const unfollowUser = async (followingId) => {
  try {
    const response = await axios.post('/api/unfollow', {
      follower_id: store.state.user_id,
      followed_id: followingId
    });
    if (response.status === 200) {
      ElMessage.success('取消关注成功！');
      // 更新 followings 数组，移除已取消关注的用户
      followings.value = followings.value.filter(f => f.id !== followingId);
      updateFollowingState(followingId);
    }
  } catch (error) {
    ElMessage.error('取消关注失败，请稍后再试。');
  }
};

const updateFollowingState = async (followingId) => {
  const index = followings.value.findIndex(f => f.id === followingId);
  if (index !== -1) {
    const statusDetails = await checkFollowStatus(followingId);
    followings.value[index].isFollowed = statusDetails.isFollowed;
    followings.value[index].status = statusDetails.status;
    followings.value[index].buttonText = createButtonLabel(followings.value[index]);
  }
};

const createButtonLabel = (following) => {
  if (following.status === 1) {
    return '互相关注';
  } else if (following.isFollowed) {
    return '已关注';
  } else {
    return '关注';
  }
};

const handleClick = async (followingId) => {
  const index = followings.value.findIndex(f => f.id === followingId);
  if (index !== -1) {
    if (followings.value[index].isFollowed || followings.value[index].status === 1) {
      try {
        await ElMessageBox.confirm('您确定要取消关注吗？', {
          confirmButtonText: '确认',
          cancelButtonText: '取消',
          customClass: 'custom-message-box' // 使用自定义样式
        });
        await unfollowUser(followingId);
      } catch (error) {
        ElMessage.info('已取消操作');
      }
    } else {
      await followUser(followingId);
    }
  }
};

const checkFollowStatus = async (followingId) => {
  try {
    const response = await axios.get(`/api/check-follow/${userId}/${followingId}`);
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
    const response = await axios.get(`/api/followings/${userId}`);
    followings.value = response.data.followings.map(following => reactive({
      ...following,
      ...checkFollowStatus(following.id),
      buttonText: 'Loading...'  // Initial placeholder text
    }));
    followings.value.forEach(async (following, index) => {
      const statusDetails = await checkFollowStatus(following.id);
      followings.value[index].isFollowed = statusDetails.isFollowed;
      followings.value[index].status = statusDetails.status;
      followings.value[index].buttonText = createButtonLabel(following);
    });
  } catch (error) {
    ElMessage.error('Failed to load followings');
    console.error('Error loading followings:', error);
  }
});


</script>


<style>

.el-message-box .custom-message-box {
  background-color: #f3f4f6; /* 浅灰色背景 */
  color: #606266; /* 深灰色文字 */
  border-radius: 30px; /* 设置圆角 */
  width: 600px; /* 设置宽度 */
  height:400px;
  max-width: 90%; /* 确保宽度不超过90% */
  min-height: 300px; /* 设置最小高度 */
}

/* 修改取消按钮的样式 */
.el-message-box__btns .el-button {
  background-color: #d3d4d6; /* 灰色背景 */
  border-color: #d3d4d6; /* 灰色边框 */
  height:30px;
  width:90px;
  margin-right: 15px; /* 右边距，设置取消按钮和确认按钮之间的距离 */
}

/* 修改确认按钮的样式 */
.el-message-box__btns .el-button--primary {
  background-color: #000B42; /* 深蓝背景 */
  border-color: #000B42; /* 蓝色边框 */
  height:30px;
  width:90px;
  margin-left: 15px; /* 左边距，也可以用来调整距离 */
}

.el-message-box__btns {
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  padding: 10px; /* 添加一些内边距 */
}

.el-message-box__message p {
  font-size: 18px; /* 设置字体大小为18px */
  text-align: center; /* 文字居中显示 */
  color: #333; /* 设置字体颜色，可根据需要修改 */
}

.el-message-box__header.show-close {
    height:20px;
}

.el-message-box__container {
    align-items: center;
    display: flex;
    gap: 12px;
    justify-content: center; /* 水平居中 */
    align-items: center; /* 垂直居中 */
    height:50px;

}

.follow-container {
  background-color: white;
  border-radius: 20px;
  padding: 32px;
  max-width: 800px;
  margin: auto;
  margin-top: 100px;
  position: relative;
}

.custom-danger-button {
  background-color: #DE124A !important; /* 自定义背景颜色 */
  color: white !important; /* 自定义文字颜色 */
  border-color: #DE124A !important; /* 自定义边框颜色，确保一致性 */
}

.custom-danger-button:hover {
  background-color: #de1248d1 !important; /* 悬停时的背景颜色，更浅的蓝色 */
  border-color: #de1248d1 !important; /* 悬停时的边框颜色 */
}


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
  cursor: pointer;
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
