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
                  <button @click="toEdit" class="edit-button">编辑</button>
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
                <div><span class="count">{{ followingCount }}</span><span class="shows">关注</span></div>
                <div><span class="count">{{ followersCount }}</span><span class="shows">粉丝</span></div>

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
          <div class="reds-tab-item" :class="{ active: activeTab === 'collection' }" style="padding: 0px 16px; margin-right: 0px; font-size: 16px">
            <!----><!----><span @click="toCollection">收藏</span>
          </div>
          <div class="reds-tab-item" :class="{ active: activeTab === 'note' }" style="padding: 0px 16px; margin-right: 0px; font-size: 16px">
            <!----><!----><span @click="toNote">笔记</span>
          </div>
          <div class="reds-tab-item" :class="{ active: activeTab === 'drafts' }" style="padding: 0px 16px; margin-right: 0px; font-size: 16px">
            <span @click="toDrafts">草稿箱</span>
          </div>
          <!---->
          <div class="active-tag" style="width: 64px; left: 627px"></div>
        </div>
      </div>
    </div>
    <div class="feeds-tab-container">
      <router-view />
    </div>
  </div>
</template>


<script lang="ts" setup>
// import { Star } from "@element-plus/icons-vue";
import { useRouter } from "vue-router";
import { ref, onMounted } from 'vue';
import axios from 'axios';
const router = useRouter();
import store from "../../store/index";

//const userId = 1;

const avatar = ref('');
const username = ref('');
const description = ref('');
const activeTab = ref('collection'); 
const is_premium = ref('');
const uid = ref('');
const sex = ref('');

const userStats = ref({
    likes: 0,
    favorites: 0
});



const toNote = () => {
  router.push({ path: "/note" });
  activeTab.value = 'note';
};

const toCollection = () => {
  router.push({ path: "/collection" });
  activeTab.value = 'collection';
};

const toEdit = () => {
  router.push({ path: "/editprofile" });
};

const toDrafts = () => {
  router.push({ path: "/drafts" });
  activeTab.value = 'drafts';
};

const followingCount = ref(0);
const followersCount = ref(0);

// Load user profile and follow counts
const loadUserProfile = async () => {
  try {
    // Fetch the main user data
    const userProfileResponse = await axios.get(`/api/user/${store.state.user_id}`);
    const userData = userProfileResponse.data;
    avatar.value = userData.photo || 'http://graphcrafter.oss-cn-beijing.aliyuncs.com/avatars/1-default.webp';
    username.value = userData.name || '未知用户';
    description.value = userData.bio || '未填写简介';
    is_premium.value = userData.is_premium == 1 ? "高级" : "普通";
    uid.value = userData.id;
    sex.value = userData.sex == 1 ? "男" : "女";

    // Fetch the follow counts
    const followCountsResponse = await axios.get(`/api/user/${store.state.user_id}/counts`);
    followingCount.value = followCountsResponse.data.following_count;
    followersCount.value = followCountsResponse.data.followers_count;
  } catch (error) {
    console.error('Error loading user profile and follow counts:', error);
  }
};

const fetchUserStats = async () => {
    try {
        const response = await axios.get(`/api/user-stats/${store.state.user_id}`);
        userStats.value = response.data;
    } catch (error) {
        console.error('Error fetching user stats:', error);
    }
};

// 组件加载时调用
onMounted(()=>{
  fetchUserStats();
  toCollection();
  loadUserProfile();
});

</script>
<style lang="less" scoped>
.user-page {
  background: #fff;
  overflow-y: scroll;
  overflow-x: hidden;

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
  }
}
</style>
