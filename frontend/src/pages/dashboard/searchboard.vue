<template>
  <div class="feeds-page">
    <div class="channel-container">
      <div class="scroll-container channel-scroll-container">
        <div class="content-container">
          <div class="channel" :class="{ active: activeChannel === '帖子' }" @click="activeChannel = '帖子'; fetchSearchResults()">帖子</div>
          <div class="channel" :class="{ active: activeChannel === '用户' }" @click="activeChannel = '用户'; fetchSearchResults()">用户</div>
        </div>
      </div>
    </div>
    <div class="loading-container"></div>
    <div class="feeds-container">
      <!-- 仅在用户视图中显示用户 -->
      <div v-if="activeChannel === '用户'">
        <ul class="user-list">
          <li v-for="user in list" :key="user.id" class="user-item">
            <img :src="user.photo" class="user-avatar" alt="User photo" @click="toOther(user.id)">
            <div class="user-details">
              <div class="user-name">{{ user.name }}</div>
              <div class="user-stats">{{ user.followers }} 粉丝 · {{ user.posts }} 发帖</div>
            </div>
            <el-button :type="user.is_followed ? 'danger' : 'primary'" size="large" round @click="handleUserClick(user.id)">
              {{ user.buttonText }}
            </el-button>

          </li>
        </ul>
      </div>
      <!-- 显示帖子的视图保留原样 -->
      <Waterfall v-else :list="list" :width="242" :hasAroundGutter="false" style="max-width: 1260px">
      <template #item="{item}">
        <div class="card">
          <LazyImg :url="item.pictures" style="border-radius: 8px"  @click="toMain(item.ids)" />
          <div class="footer">
            <a class="title"><span>{{ item.titles }}</span></a>
            <div class="author-wrapper">
              <a class="author">
                <img class="author-avatar" :src="item.avatars" />
                <span class="name">{{ item.authors }}</span>
              </a>
              <span class="like-wrapper like-active">
                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16" style="width: 1em; height: 1em">
                  <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
                </svg>
                <!-- <Search  /> -->
                <span class="count">{{ item.likes }}</span>
              </span>
            </div>
          </div>
        </div>
      </template>
    </Waterfall>
    </div>

    <div class="feeds-loading"></div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import { LazyImg, Waterfall } from "vue-waterfall-plugin-next";
import "vue-waterfall-plugin-next/dist/style.css";
import store from "../../store/index";
import { ElMessage, ElMessageBox } from 'element-plus';

const route = useRoute();
const router = useRouter();

const list = ref([]);
const activeChannel = ref('帖子'); // 初始频道设为“推荐”
const curuserId = store.state.user_id;  // 从 Vuex store 获取当前用户 ID
// 获取搜索结果
const fetchSearchResults = async () => {
    const query = route.query.query;

    if (!query) {
        list.value = [];
        return;
    }
    try {
        let url = '/api/posts/search';
        if (activeChannel.value === '用户') {
            url = '/api/users/search';
        }
        const response = await axios.get(url, { params: { query, userId: curuserId} });
        if (activeChannel.value === '用户') {
            list.value = response.data.users.map(user => ({
                id: user.id,
                name: user.name,
                photo: user.photo,
                followers: user.followers,
                posts: user.posts,
                is_followed: user.is_followed,
                is_follower: user.is_follower,
                buttonText: createButtonLabel(user)

            }));
        } else {
            list.value = response.data.posts.map(post => ({
                ids: post.id,
                pictures: post.picture1,
                titles: post.title,
                authors: post.author,
                avatars: post.avatar,
                likes: post.likes
            }));
        }
    } catch (error) {
        console.error('Error fetching search results:', error);
    }
};


// 监视路由查询参数的变化
watch(() => route.query.query, () => {
    fetchSearchResults();
});
onMounted(fetchSearchResults);

const toMain = (id: number) => {
  router.push({ path: "/main", query: { id: id } });
};

const toOther = (id) => {
  router.push({ path: "/other", query: { id } });
};

const followUser = async (followingId) => {
  console.log(store.state.user_id); // 查看 Vuex store 的当前状态
  console.log(followingId); // 查看 Vuex store 的当前状态

  if (store.state.user_id == followingId) {
    ElMessage.error('您不能关注自己。');
    return;
  }
  try {

    const response = await axios.post('/api/follow', {
      follower_id: store.state.user_id,
      followed_id: followingId
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
      updateFollowingState(followingId);
    }
  } catch (error) {
    ElMessage.error('取消关注失败，请稍后再试。');
  }
};
const checkFollowStatus = async (followingId) => {
  try {
    const response = await axios.get(`/api/check-follow/${store.state.user_id}/${followingId}`);
    return {
      isFollowed: response.data.isFollowed,
      status: response.data.status
    };
  } catch (error) {
    console.error('Error checking follow status:', error);
    return { isFollowed: false, status: 0 };
  }
};

const updateFollowingState = async (followingId) => {
  const index = list.value.findIndex(f => f.id === followingId);
  if (index !== -1) {
    const statusDetails = await checkFollowStatus(followingId);
    list.value[index].is_followed = statusDetails.isFollowed;
    list.value[index].is_follower = statusDetails.status;
    list.value[index].buttonText = createButtonLabel(list.value[index]);
  }
};

const createButtonLabel = (user) => {
  let label: string; // 默认标签
  if (user.is_follower  && user.is_followed ) {
    label = '互相关注';
  } else if (user.is_followed) {
    label = '已关注';
  } else {
    label = '关注';
  }
  console.log(user.is_follower);
  console.log(user.is_followed);
  console.log(`Creating label for user ${user.id}: ${label}`); // 输出标签创建情况
  return label;
};

const handleUserClick = async (userId) => {
  const userIndex = list.value.findIndex(user => user.id === userId);
  if (userIndex !== -1) {
    const user = list.value[userIndex];
    if (user.is_followed) {
      try {
        // Confirm unfollow action
        await ElMessageBox.confirm('您确定要取消关注吗？', '确认信息', {
          confirmButtonText: '确认',
          cancelButtonText: '取消',
          type: 'warning'
        });
        // API call to unfollow the user
        await unfollowUser(userId);
      } catch (error) {
        // Handling the case where the user cancels the operation
        ElMessage.info('已取消操作');
      }
    } else {
      await followUser(userId);
      }
  }
};


</script>

<style lang="less" scoped>
.user-list {
  list-style: none;
  padding: 0;
}

.user-item {
  display: flex;
  align-items: center;
  justify-content: space-between; /* Keeps elements justified but can be adjusted */
  gap: 10px; /* Reduces the gap between elements in the flex container */
  margin-bottom: 16px;
}


.user-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  margin-right: 16px;
  cursor: pointer;
}

.user-details {
  flex-grow: 1;
  margin-right: 0px; /* Adjust or remove if unnecessary */
}
.user-name {
  font-weight: bold;
}
.user-stats {
  color: rgba(0, 0, 0, 0.6);
  font-size: 14px;
}
.static-channel {
  padding: 8px 16px;
  background-color: #f0f0f0;
  border-radius: 20px;
  font-weight: bold;
  cursor: default; /* 不显示为可点击的光标形状 */
}
.feeds-page {
  flex: 1;
  padding: 0 24px;
  padding-top: 72px;

  .channel-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    user-select: none;
    -webkit-user-select: none;

    .channel-scroll-container {
      backdrop-filter: blur(20px);
      background-color: transparent;
      width: calc(100vw - 24px);

      position: relative;
      overflow: hidden;
      display: flex;
      user-select: none;
      -webkit-user-select: none;
      align-items: center;
      font-size: 16px;
      color: rgba(51, 51, 51, 0.8);
      height: 40px;
      white-space: nowrap;
      height: 72px;

      .content-container::-webkit-scrollbar {
        display: none;
      }

      .content-container {
        display: flex;
        overflow-x: scroll;
        overflow-y: hidden;
        white-space: nowrap;
        color: rgba(51, 51, 51, 0.8);

        .active {
          font-weight: 600;
          background: rgba(0, 0, 0, 0.03);
          border-radius: 999px;
          color: #333;
        }

        .channel {
          height: 40px;
          display: flex;
          justify-content: center;
          align-items: center;
          padding: 0 16px;
          cursor: pointer;
          -webkit-user-select: none;
          user-select: none;
        }
      }
    }
  }

  .feeds-container {
    position: relative;
    transition: width 0.5s;
    margin: 0 auto;

    .footer {
      padding: 12px;
      .title {
        margin-bottom: 8px;
        word-break: break-all;
        display: -webkit-box;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 2;
        overflow: hidden;
        font-weight: 500;
        font-size: 14px;
        line-height: 140%;
        color: #333;
      }

      .author-wrapper {
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 20px;
        color: rgba(51, 51, 51, 0.8);
        font-size: 12px;
        transition: color 1s;

        .author {
          display: flex;
          align-items: center;
          color: inherit;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
          margin-right: 12px;

          .author-avatar {
            margin-right: 6px;
            width: 20px;
            height: 20px;
            border-radius: 20px;
            border: 1px solid rgba(0, 0, 0, 0.08);
            flex-shrink: 0;
          }

          .name {
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
          }
        }

        .like-wrapper {
          position: relative;
          cursor: pointer;
          display: flex;
          align-items: center;

          .count {
            margin-left: 2px;
          }
        }
      }
    }
  }
}
</style>
