<template>
  <div class="user-page">
    <div class="user">
      <div class="user-info">
        <div class="avatar">
          <div class="avatar-wrapper">
            <img
              :src="avatar"
              class="user-image"
              style="border: 1px solid rgba(0, 0, 0, 0.08)"
            />
          </div>
        </div>
        <div class="info-part">
          <div class="info">
            <div class="basic-info">
              <div class="user-basic">
                <div class="user-nickname">
                  <!-- 使用动态数据的用户名 -->
                  <div class="user-name">{{ username }}</div>
                  <el-button type="danger" size="medium" round @click="handleClick">
                  {{ buttonText }}
                  </el-button>
                  <button @click="chatWithOther" class="chat-with-other-button">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-chat-dots" viewBox="0 0 16 16">
                      <path d="M5 8a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm3 1a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"/>
                      <path d="m2.165 15.803.02-.004c1.83-.363 2.948-.842 3.468-1.105A9.06 9.06 0 0 0 8 15c4.418 0 8-3.134 8-7s-3.582-7-8-7-8 3.134-8 7c0 1.76.743 3.37 1.97 4.6a10.437 10.437 0 0 1-.524 2.318l-.003.011a10.722 10.722 0 0 1-.244.637c-.079.186.074.394.273.362a21.673 21.673 0 0 0 .693-.125zm.8-3.108a1 1 0 0 0-.287-.801C1.618 10.83 1 9.468 1 8c0-3.192 3.004-6 7-6s7 2.808 7 6c0 3.193-3.004 6-7 6a8.06 8.06 0 0 1-2.088-.272 1 1 0 0 0-.711.074c-.387.196-1.24.57-2.634.893a10.97 10.97 0 0 0 .398-2z"/>
                    </svg>
                  </button>
                </div>
                <div class="user-content">
                  <span class="user-redId">图匠id号：{{ uid }}</span>
                  <span class="user-redId">权限：{{ is_premium}}</span>
                </div>
              </div>
            </div>
            <!-- 使用动态数据的简介 -->
            <div class="user-desc">{{ description }}</div>
            <div class="user-tags">
                <div v-if="sex === '男'" class="tag-item" style="color: blue; font-weight: 900; font-size: 13px;">♂</div>
                <div v-else class="tag-item" style="color: red; font-weight: 900; font-size: 13px;">♀</div>
            </div>


            <div class="data-info">
              <div class="user-interactions">
                <div @click="" class="navigation-item">
                  <span class="count">{{ followingCount }}</span>
                  <span class="shows">关注</span>
                </div>
                <div @click="" class="navigation-item">
                  <span class="count">{{ followersCount }}</span>
                  <span class="shows">粉丝</span>
                </div>
                <div><span class="count">{{ userStats.likes }}</span><span class="shows">获赞</span></div>
                <div><span class="count">{{ userStats.favorites }}</span><span class="shows">收藏</span></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="reds-sticky-box user-page-sticky">
      <div class="reds-sticky">
        <div class="reds-tabs-list">
          <div class="reds-tab-item" :class="{ active: activeTab === 'note' }" style="padding: 0px 16px; margin-right: 0px; font-size: 16px">
            <!----><!----><span @click="">笔记</span>
          </div>
          <!---->
          <div class="active-tag" style="width: 64px; left: 627px"></div>
        </div>
      </div>
    </div>
    <div class="feeds-tab-container">
      <!-- <router-view />
       -->
       <div class="feeds-container">
    <Waterfall :list="list" :width="220" :hasAroundGutter="false" style="max-width: 1260px">
      <template #item="{item}">
        <div class="card">
          <LazyImg :url="item.pictures" style="border-radius: 8px"   @click="toMain(item.ids)"    />
          <div class="footer">
            <a class="title"><span>{{ item.titles }}</span></a>
            <div class="author-wrapper">
              <a class="author">
                <img class="author-avatar" :src="item.avatars" />
                <span class="name">{{ item.authors }}</span>
              </a>
              <span class="like-wrapper like-active">
                <Search style="width: 1em; height: 1em" />
                <span class="count">{{ item.likes }}</span>
              </span>
            </div>
          </div>
        </div>
      </template>
    </Waterfall>
  </div>
    </div>
    <div class="close-cricle">
      <div class="close close-mask-white"  @click="goBack">
        <Close style="width: 1.2em; height: 1.2em; color: rgba(51, 51, 51, 0.8)" />
      </div>
    </div>
  </div>
</template>


<script lang="ts" setup>
// import { Star } from "@element-plus/icons-vue";
import { useRouter,useRoute } from "vue-router";
import { ref, onMounted,computed } from 'vue';
import axios from 'axios';
const router = useRouter();
const route = useRoute();
import store from "../store/index";
import { ElMessage,ElMessageBox } from 'element-plus';
import { Close } from "@element-plus/icons-vue";
import { LazyImg, Waterfall } from "vue-waterfall-plugin-next";
//const userId = 1;

const avatar = ref('');
const username = ref('');
const description = ref('');
const activeTab = ref('note'); 
const is_premium = ref('');
const uid = ref('');
const sex = ref('');
const other_user_id = route.query.id;

const userStats = ref({
    likes: 0,
    favorites: 0
});

const toFans = () => {
  router.push({ path: "/fanspage" });
};

const toFollow = () => {
  router.push({ path: "/Follow" });
};

const goBack = () => {
  router.go(-1);
}

const followingCount = ref(0);
const followersCount = ref(0);

// Load user profile and follow counts
const loadUserProfile = async () => {
  try {
    // Fetch the main user data
    const userProfileResponse = await axios.get(`/api/user/${other_user_id}`);
    const userData = userProfileResponse.data;
    avatar.value = userData.photo || 'http://graphcrafter.oss-cn-beijing.aliyuncs.com/avatars/1-default.webp';
    username.value = userData.name || '未知用户';
    description.value = userData.bio || '未填写简介';
    is_premium.value = userData.is_premium == 1 ? "高级" : "普通";
    uid.value = userData.id;
    sex.value = userData.sex == 1 ? "男" : "女";

    // Fetch the follow counts
    const followCountsResponse = await axios.get(`/api/user/${other_user_id}/counts`);
    followingCount.value = followCountsResponse.data.following_count;
    followersCount.value = followCountsResponse.data.followers_count;
  } catch (error) {
    console.error('Error loading user profile and follow counts:', error);
  }
};

const fetchUserStats = async () => {
    try {
        const response = await axios.get(`/api/user-stats/${other_user_id}`);
        userStats.value = response.data;
    } catch (error) {
        console.error('Error fetching user stats:', error);
    }
};


const isFollowed = ref(false);
const followStatus = ref(0);  // 0: 单独关注, 1: 互相关注

const followUser = async () => {
    // 检查是否尝试自己关注自己
    if (store.state.user_id == other_user_id) {
        ElMessage.error('您不能关注自己。'); // 使用ElMessage显示错误信息
        return;  // 直接返回，不执行关注操作
    }

    // 如果还未关注，则尝试执行关注操作
    if (!isFollowed.value) {
        try {
            const response = await axios.post('/api/follow', {
                follower_id: store.state.user_id,
                followed_id: other_user_id
            });
            if (response.status === 200) {
                isFollowed.value = true;  // 更新关注状态
                ElMessage.success('关注成功！'); // 显示成功消息
            }
        } catch (error) {
            ElMessage.error('关注失败，请稍后再试。'); // 出错时使用ElMessage显示错误信息
        }
    }
};


const unfollowUser = async () => {
    try {
        const response = await axios.post('/api/unfollow', {  // 确保后端有处理取消关注的API
            follower_id: store.state.user_id,
            followed_id: other_user_id
        });
        if (response.status === 200) {
            isFollowed.value = false;  // 更新未关注状态
            followStatus.value = 0;    // 更新关注状态
            ElMessage.success('取消关注成功！');
        }
    } catch (error) {
        ElMessage.error('取消关注失败，请稍后再试。');
    }
};


const checkFollowStatus = async () => {
    try {
        const response = await axios.get(`/api/check-follow/${store.state.user_id}/${other_user_id }`);
        console.log(response.data.isFollowed)
        console.log(response.data.status)
        isFollowed.value = response.data.isFollowed;
        
        followStatus.value = response.data.status;
    } catch (error) {
        console.error('Error checking follow status:', error);
    }
};

const buttonText = computed(() => {
    if (followStatus.value === 1) {
        return '互相关注';
    } else if (isFollowed.value) {
        return '已关注';
    } else {
        return '关注';
    }
});

const handleClick = async () => {
    // 检查是否已经关注或者互相关注
    if (isFollowed.value || followStatus.value === 1) {
        // 弹出确认取消关注的对话框
        try {
            await ElMessageBox.confirm('您确定要取消关注吗？', '确认信息', {
                confirmButtonText: '确认',
                cancelButtonText: '取消',
                type: 'warning'
            });
            // 用户确认取消关注
            await unfollowUser();  // 这是你需要实现的取消关注的方法
            await checkFollowStatus();  // 再次检查关注状态
        } catch (error) {
            // 用户取消操作
            ElMessage.info('已取消操作');
        }
    } else {
        // 如果还没有关注，则尝试关注
        await followUser();
        await checkFollowStatus();
    }
};

const toMain = (id: number) => {
  router.push({ path: "/main", query: { id: id } });
};

const list = ref([
  // { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.Zte3ljd4g6kqrWWyg-8fhAHaEo?w=264&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
  // { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.cGc4c8dVlqnfV3uwcS1IogHaE8?w=260&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
  // { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.Zte3ljd4g6kqrWWyg-8fhAHaEo?w=264&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
  // { src: "https://tse4-mm.cn.bing.net/th/id/OIP-C.N0USLldg_iKDGVKT12vB4AHaEK?w=292&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
  // { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.jzcWzXf_uts2sgE2WChuCQHaEo?w=263&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
  // { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.Zte3ljd4g6kqrWWyg-8fhAHaEo?w=264&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
  // { src: "https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg" },
  // { src: "https://fuss10.elemecdn.com/1/34/19aa98b1fcb2781c4fba33d850549jpeg.jpeg" },
  // { src: "https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg" },
  // { src: "https://fuss10.elemecdn.com/0/6f/e35ff375812e6b0020b6b4e8f9583jpeg.jpeg" },
  // { src: "https://fuss10.elemecdn.com/9/bb/e27858e973f5d7d3904835f46abbdjpeg.jpeg" },
  // { src: "https://fuss10.elemecdn.com/3/28/bbf893f792f03a54408b3b7a7ebf0jpeg.jpeg" },
  // { src: "https://fuss10.elemecdn.com/2/11/6535bcfb26e4c79b48ddde44f4b6fjpeg.jpeg" },
  // { src: "https://tse4-mm.cn.bing.net/th/id/OIP-C.N0USLldg_iKDGVKT12vB4AHaEK?w=292&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
  // { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.jzcWzXf_uts2sgE2WChuCQHaEo?w=263&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
  // { src: "https://tse3-mm.cn.bing.net/th/id/OIP-C.YzEeJqgWky6RQMatrMd6-gHaHa?w=170&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
  // { src: "https://tse3-mm.cn.bing.net/th/id/OIP-C.YzEeJqgWky6RQMatrMd6-gHaHa?w=170&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
  // { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.Zte3ljd4g6kqrWWyg-8fhAHaEo?w=264&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
  // { src: "https://tse4-mm.cn.bing.net/th/id/OIP-C.N0USLldg_iKDGVKT12vB4AHaEK?w=292&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
  // { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.jzcWzXf_uts2sgE2WChuCQHaEo?w=263&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
  // { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.Zte3ljd4g6kqrWWyg-8fhAHaEo?w=264&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
  // { src: "https://tse1-mm.cn.bing.net/th/id/OIP-C.cGc4c8dVlqnfV3uwcS1IogHaE8?w=260&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7" },
]);

const fetchData = async () => {
  try {
    // Simulated asynchronous database query
    const data = await axios.get(`/api/note/${other_user_id}`);
    const result = data.data;
    // 解构出各个属性数组
    const { authors, avatars, likes, pictures, titles, ids } = result;
    // 遍历数组，构建每个对象并添加到数组中
    for (let i = 0; i < titles.length; i++) {
      const item = {
        pictures: pictures[i], // 使用对应索引的图片 URL 作为 src 属性
        titles: titles[i], // 使用对应索引的标题属性
        authors: authors[i], // 使用对应索引的作者属性
        avatars: avatars[i], // 使用对应索引的头像属性
        likes: likes[i], // 使用对应索引的点赞数属性
        ids: ids[i]
      };
      list.value.push(item);
    }
    // console.log(result);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

async function chatWithOther()
{
  try {
    const response = await axios.post('/create_chat', {
      sender_id: store.state.user_id,
      receiver_id: other_user_id
    });
    router.push({ path: "/message" });
  } catch (error) {
    console.error('There was an error creating the chat!', error);
  }
}
// 组件加载时调用
onMounted(()=>{
  fetchUserStats();
  fetchData();
  loadUserProfile();
  checkFollowStatus();
});

</script>
<style lang="less" scoped>

.count, .shows {
  cursor: pointer;
}

.navigation-item {
  cursor: pointer; /* Indicates the item is clickable */
  color: black; /* Text color */
}

.navigation-item:hover {
  color: #51a8d7; /* Change color on hover */
}
.user-page {
  background: #fff;
  overflow-y: scroll;
  overflow-x: hidden;

  .close-cricle {
    left: 21.3vw;
    top: 7.3vw;
    position: fixed;
    display: flex;
    z-index: 100;
    cursor: pointer;

    .close-mask-white {
      box-shadow:
        0 2px 8px 0 rgba(0, 0, 0, 0.04),
        0 1px 2px 0 rgba(0, 0, 0, 0.02);
      border: 1px solid rgba(0, 0, 0, 0.08);
    }

    .close {
      display: flex;
      justify-content: center;
      align-items: center;
      border-radius: 100%;
      width: 40px;
      height: 40px;
      border-radius: 40px;
      cursor: pointer;
      transition: all 0.3s;
    }
  }

  .user {
    padding-top: 72px;
    display: flex;
    align-items: center;
    justify-content: center;
    .user-info {
      display: flex;
      justify-content: center;
      padding: 48px 0;

      .avatar {
        .avatar-wrapper {
          text-align: center;
          width: 250.66667px;
          height: 175.46667px;
          .user-image {
            border-radius: 50%;
            margin: 0 auto;
            width: 70%;
            height: 100%;
            object-fit: cover;
          }
        }
      }
  
      .info-part {
        position: relative;
        width: 100%;

        .info {
          @media screen and (min-width: 1728px) {
            width: 533.33333px;
          }
          margin-left: 32px;
          .basic-info {
            display: flex;
            align-items: center;
            .user-basic {
              width: 100%;
              .user-nickname {
                width: 100%;
                display: flex;
                align-items: center;
                max-width: calc(100% - 96px);
                .user-name {
                  font-weight: 600;
                  font-size: 24px;
                  line-height: 120%;
                  color: #333;
                  margin-right: 20px;
                }
              }
              .edit-button {
                  margin-left: 16px;
                  padding: 8px 12px;
                  font-size: 14px;
                  background-color: #b3acc6;
                  border: none;
                  color: #fff;
                  border-radius: 6px;
                  cursor: pointer;
                  transition: all 0.2s;
                }
              .chat-with-other-button {
                margin-left: 16px;
                padding: 6px 8px;
                font-size: 14px;
                background-color: rgba(132, 131, 134, 0.3);
                border: none;
                color: #fff;
                border-radius: 10px;
                cursor: pointer;
                transition: all 0.2s;
              }
              .chat-with-other-button:hover{
                background-color: rgba(132, 131, 134, 0.4);
              }
              .user-content {
                width: 100%;
                font-size: 12px;
                line-height: 120%;
                color: rgba(51, 51, 51, 0.6);
                display: flex;
                margin-top: 8px;
                .user-redId {
                  padding-right: 12px;
                }
              }
            }
          }
          // .user-desc {
          //   width: 100%;
          //   font-size: 14px;
          //   line-height: 140%;
          //   color: #333;
          //   margin-top: 16px;
          //   white-space: pre-line;
          // }
          .user-desc {
            width: 450px; /* 根据25个字符实际需要的宽度进行调整 */
            font-size: 14px;
            line-height: 140%;
            color: #333;
            margin-top: 16px;
            white-space: pre-wrap; /* 改为pre-wrap以实现自然换行 */
            overflow-wrap: break-word; /* 确保长单词可以换行到下一行 */
            word-wrap: break-word; /* 适用于旧浏览器 */
          }

          .user-tags {
            height: 24px;
            margin-top: 16px;
            display: flex;
            align-items: center;
            font-size: 12px;
            color: #333;
            text-align: center;
            font-weight: 400;
            line-height: 120%;
            .tag-item :first-child {
              padding: 3px 6px;
            }
            .tag-item {
              display: flex;
              align-items: center;
              justify-content: center;
              padding: 4px 8px;
              grid-gap: 4px;
              gap: 4px;
              height: 18px;
              border-radius: 41px;
              background: rgba(0, 0, 0, 0.03);
              height: 24px;
              line-height: 24px;
              margin-right: 6px;
              color: rgba(51, 51, 51, 0.6);
            }
          }
          .data-info {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 20px;
            .user-interactions {
              width: 100%;
              display: flex;
              align-items: center;
              .count {
                font-weight: 500;
                font-size: 14px;
                margin-right: 4px;
              }
              .shows {
                color: rgba(51, 51, 51, 0.6);
                font-size: 14px;
                line-height: 120%;
              }
            }
            .user-interactions > div {
              height: 100%;
              display: flex;
              align-items: center;
              justify-content: center;
              text-align: center;
              margin-right: 16px;
            }
          }
        }

        .follow {
          position: absolute;
          margin-left: auto;
          display: block;
          right: 0;
          top: 0;
        }
      }
    }
  }

  .reds-sticky {
    padding: 16px 0;
    z-index: 5 !important;
    background: hsla(0, 0%, 100%, 0.98);

    .reds-tabs-list {
      screen and (min-width: 1728px) {
        width: 1445.33333px;
      }
      display: flex;
      flex-wrap: nowrap;
      position: relative;
      font-size: 16px;
      justify-content: center;

      .reds-tab-item {
        padding: 0px 16px;
        margin-right: 0px;
        font-size: 16px;
        display: flex;
        align-items: center;
        box-sizing: border-box;
        height: 40px;
        cursor: pointer;
        color: rgba(51, 51, 51, 0.8);
        white-space: nowrap;
        transition: transform 0.3s cubic-bezier(0.2, 0, 0.25, 1);
        z-index: 1;
      }
      .reds-tab-item.active {
        background-color: rgba(0, 0, 0, 0.03);
        border-radius: 20px;
        font-weight: 600;
        color: rgba(51, 51, 51, 0.8);
      }
    }
  }

  .feeds-tab-container {
    padding-left: 2rem;
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
}
</style>
