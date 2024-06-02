<template>
  <div class="container">
    <div class="top">
      <header class="mask-paper">
        <img src="https://graphcrafter.oss-cn-beijing.aliyuncs.com/LOGO.gif" class="logo" style="width:20%;position: relative; top:10px; left:-50px; z-index: -1;" @click="toDemo"/>
          
        <div class="tool-box"></div>
        <div class="input-box">
          <input type="text" class="search-input" placeholder="搜索" v-model="searchQuery"  />
          <div class="input-button">
            <div class="close-icon" @click="clearSearch">
              <Close class="icon-hover" style="width: 1em; height: 1em; margin-right: 8px" /></div>
            <div class="search-icon" @click="searchPosts">
              <Search class="icon-hover" style="width: 1em; height: 1em; margin-right: 8px" /></div>
          </div>
        </div>
        <div class="right"></div>
      </header>
    </div>
    <div class="main">
      <div class="side-bar" style="z-index:10">
        <ul class="channel-list">
          <li :class="{ 'active-channel': activeChannel === 'dashboard' }">
            <a class="link-wrapper" @click="toDashboard">
              <House style="width: 1em; height: 1em; margin-right: 8px" /><span class="channel">发现</span>
            </a>
          </li>
          <li :class="{ 'active-channel': activeChannel === 'photoshop' || activeChannel === 'easy' || activeChannel === 'conversation' }">
            <a class="link-wrapper" @click="togglePhotoshop">
              <Brush style="width: 1em; height: 1em; margin-right: 8px" /><span class="channel">修图</span>
            </a>
          </li>

          <ul v-if="activeChannel === 'photoshop' || activeChannel === 'easy' || activeChannel === 'conversation'|| activeChannel === 'p2p'" class="sub-menu">
              <li :class="{ 'active-channel': activeChannel === 'conversation' }" @click="toConversation">
                <a class="link-wrapper">
                  <DataAnalysis style="width: 1em; height: 1em; margin-right: 8px" /><span class="channel">图像评估</span>
                </a>
              </li>
              <li :class="{ 'active-channel': activeChannel === 'easy' }" @click="toEasy">
                <a class="link-wrapper">
                  <MagicStick style="width: 1em; height: 1em; margin-right: 8px" /><span class="channel">简单修图</span>
                </a>
              </li>
              <li :class="{ 'active-channel': activeChannel === 'p2p' }" @click="top2p">
                <a class="link-wrapper">
                  <ChatDotRound style="width: 1em; height: 1em; margin-right: 8px" /><span class="channel">对话修图</span>
                </a>
              </li>
            </ul>
          
            <!-- <li v-if="activeChannel === 'photoshop'" :class="{ 'active-channel': activeChannel === 'photoshop' }">
              <a class="link-wrapper" @click="toConversation">
                <House style="width: 1em; height: 1em; margin-right: 8px" />
                <span class="channel">对话</span>
              </a>
            </li>

            <li v-if="activeChannel === 'photoshop'" :class="{ 'active-channel': activeChannel === 'photoshop' }">
              <a class="link-wrapper" @click="toEasy">
                <House style="width: 1em; height: 1em; margin-right: 8px" />
                <span class="channel">简单</span>
              </a>
            </li> -->


          <li :class="{ 'active-channel': activeChannel === 'message' }">
            <a class="link-wrapper" @click="toMessage">
              <Bell style="width: 1em; height: 1em; margin-right: 8px" /><span class="channel">消息</span>
            </a>
          </li>
          <li :class="{ 'active-channel': activeChannel === 'push' }">
            <a class="link-wrapper" @click="toPush">
              <CirclePlus style="width: 1em; height: 1em; margin-right: 8px" /><span class="channel">发布</span>
            </a>
          </li>
          <li :class="{ 'active-channel': activeChannel === 'user' }">
            <a class="link-wrapper" @click="toUser">
              <User style="width: 1em; height: 1em; margin-right: 8px" /><span class="channel">个人</span>
            </a>
          </li>
        </ul>
        <div class="information-container">
          <div class="information-pad">
            <div class="container" id="more-info" style="visibility: hidden">
              <div>
                <div>
                  <div class="group-wrapper">
                    <div class="menu-item hover-effect">
                      <span>关于图匠</span>
                      <div class="icon">
                        <ArrowRight style="width: 1em; height: 1em; margin-right: 8px" />
                      </div>
                    </div>
                  </div>
                  <div class="divider"></div>
                </div>
                <div>
                  <div class="group-wrapper">
                    <div class="menu-item hover-effect">
                      <span @click="Logout">退出登录</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="information-wrapper">
            <More style="width: 1em; height: 1em; margin-right: 8px" @click="toggleMoreInfoState" />
            <span class="channel" @click="toggleMoreInfoState"> 更多</span>
          </div>
        </div>
      </div>
      <div class="main-content with-side-bar">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import {
  Search,
  Close,
  House,
  Bell,
  User,
  ArrowRight,
  More,
  CirclePlus,
  Brush,
  MagicStick,
  ChatDotRound,
  ChatSquare,
  DataAnalysis
} from "@element-plus/icons-vue";
import { useRouter } from "vue-router";
import { ref } from "vue";
import store from "../store/index";
import axios from "axios";

/* 搜索 */
const searchQuery = ref("");

const searchPosts = async () => {
  try {
    await axios.get('/api/posts/search', {
      params: {
        query: searchQuery.value
      }
    });
    router.push({ name: 'SearchBoard', query: { query: searchQuery.value } });
  } catch (error) {
    console.error("Error fetching posts:", error);
  }
};

const clearSearch = () => {
  searchQuery.value = "";
  router.push('/dashboard'); // 跳转到 dashboard 页面
};

const toDemo = () => {
  router.push({ name: 'Demo' });  // 确保这里的路由名称与你的routes配置中的主页名称相匹配
  activeChannel.value = 'Demo';
};

const router = useRouter();

const activeChannel = ref(null);

const toDashboard = () => {
  router.push({ name: 'dashboard' });
  activeChannel.value = 'dashboard';
};
const toMessage = () => {
  router.push({ name: 'message' });
  activeChannel.value = 'message';
};
const toPush = () => {
  router.push({ name: 'push' });
  activeChannel.value = 'push';
};
const toUser = () => {
  router.push({ name: 'user' });
  activeChannel.value = 'user';
};

const toConversation = () => {
  router.push({ name: 'conversation' });
  activeChannel.value = 'conversation';
};
const toEasy = () => {
  router.push({ name: 'easy1' });
  activeChannel.value = 'easy';
};

const top2p = () => {
  router.push({ name: 'p2p' });
  activeChannel.value = 'p2p';
};

const togglePhotoshop = () => {
  activeChannel.value = activeChannel.value === 'photoshop' ? null : 'photoshop';
};


const toggleMoreInfoState = () => {
  let div = document.getElementById('more-info');
  if (div.style.visibility === 'hidden') {
    div.style.visibility = 'visible';
  } else {
    div.style.visibility = 'hidden';
  }
}
function Logout(){
  store.commit("setLoginState",false);
  store.commit("setCurUserID",null);
  localStorage.removeItem("user");
  router.push("/");
}
// 保存到本地，这样不需要每次刷新都得登录
store.commit("setLoginState",localStorage.getItem("user")?true:false);
store.commit("setCurUserID",localStorage.getItem("user")?localStorage.getItem("user"):null);
</script>

<style lang="less" scoped>

// /deep/ div#app{
//   height: 100px;
// }

.icon-hover {
  cursor: pointer; /* 使鼠标悬浮时变为手型 */
  transition: transform 0.3s ease; /* 过渡效果，可以添加其他视觉效果，如轻微放大 */
}

.icon-hover:hover {
  transform: scale(1.1); /* 轻微放大图标 */
}


.sub-menu {
  padding-left: 20px;  /* 保持适当的缩进 */
  background-color: rgba(255, 255, 255, 0);
  border-radius:  999px;;
  margin-top: 0px;
  min-height: 48px; 
  
}

.channel-list > li {
  position: relative;  /* 确保设置了定位上下文 */
}

.sub-menu li {
  padding: 8px 16px;  /* 子菜单项的内边距 */
  white-space: nowrap;  /* 防止文本换行 */
  cursor: pointer;
  height: 40px;  /* Explicit height for each submenu item */
}

.sub-menu li:hover {
  background-color:  rgba(0, 0, 0, 0.03);
  border-radius: 999px;
  
}

.container {
  max-width: 1728px;
  background-color: #fff;
  margin: 0 auto;

  .top {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100vw;
    height: 72px;
    position: fixed;
    left: 0;
    top: 0;
    z-index: 10;
    align-items: center;
    background: #fff;

    header {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      max-width: 1728px;
      height: 72px;
      padding: 0 16px 0 24px;
      z-index: 10;
      .logo {
          cursor: pointer;  /* 设置鼠标为手形指针 */
      }
      .tool-box {
        width: 24px;
        height: 70px;
        position: absolute;
        left: 0;
        top: 0;
      }

      .input-box {
        height: 40px;
        position: fixed;
        left: 50%;
        transform: translate(-50%);

        @media screen and (max-width: 695px) {
          display: none;
        }

        @media screen and (min-width: 960px) and (max-width: 1191px) {
          width: calc(-36px + 50vw);
        }

        @media screen and (min-width: 1192px) and (max-width: 1423px) {
          width: calc(-33.6px + 40vw);
        }

        @media screen and (min-width: 1424px) and (max-width: 1727px) {
          width: calc(-42.66667px + 33.33333vw);
        }

        @media screen and (min-width: 1728px) {
          width: 533.33333px;
        }
        .search-input {
          padding: 0 84px 0 16px;
          width: 100%;
          height: 100%;
          font-size: 16px;
          line-height: 120%;
          color: #333;
          caret-color: #ff2442;
          background: rgba(0, 0, 0, 0.03);
          border-radius: 999px;
        }

        .input-button {
          position: absolute;
          right: 0;
          top: 0;
          display: flex;
          align-items: center;
          justify-content: center;
          height: 100%;
          color: rgba(51, 51, 51, 0.8);

          .close-icon .search-icon {
            width: 40px;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            color: rgba(51, 51, 51, 0.8);
          }
        }
      }
    }
  }

  .main {
    display: flex;

    .side-bar {
      @media screen and (max-width: 695px) {
        display: none;
      }
      @media screen and (min-width: 696px) and (max-width: 959px) {
        display: none;
      }

      @media screen and (min-width: 960px) and (max-width: 1191px) {
        width: calc(-18px + 25vw);
        margin-left: 12px;
      }

      @media screen and (min-width: 1192px) and (max-width: 1423px) {
        width: calc(-16.8px + 20vw);
        margin-left: 12px;
      }

      @media screen and (min-width: 1424px) and (max-width: 1727px) {
        width: calc(-21.33333px + 16.66667vw);
        margin-left: 16px;
      }

      @media screen and (min-width: 1728px) {
        width: 266.66667px;
        margin-left: 16px;
      }

      height: calc(100vh - 72px);
      overflow-y: scroll;
      background-color: #fff;
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      padding-top: 16px;
      margin-top: 72px;
      position: fixed;
      overflow: visible;

      .channel-list > li {
        position: relative;  /* Ensuring that the positioning context is set */
      }

      .channel-list {
        min-height: auto;
        -webkit-user-select: none;
        user-select: none;
        

        .active-channel {
          background-color: rgba(0, 0, 0, 0.03);
          border-radius: 999px;
          color: #333;
        }

        li {
          padding-left: 16px;
          min-height: 48px;
          display: flex;
          align-items: center;
          cursor: pointer;
          margin-bottom: 8px;
          color: rgba(51, 51, 51, 0.6);

          .link-wrapper {
            display: flex;
            width: 100%;
            height: 48px;
            align-items: center;
          }
        }

        .channel {
          font-size: 16px;
          font-weight: 600;
          margin-left: 12px;
          color: #333;
          white-space: nowrap;  /* 防止文本换行 */
        }
      }

      .information-container {
        display: inline-block;
        width: 100%;
        color: #333;
        font-size: 16px;
        position: absolute;
        bottom: 0;

        .information-pad {
          z-index: 16;
          margin-bottom: 4px;
          width: 100%;

          .container {
            width: 100%;
            background: #fff;
            box-shadow:
              0 4px 32px 0 rgba(0, 0, 0, 0.08),
              0 1px 4px 0 rgba(0, 0, 0, 0.04);
            border-radius: 12px;

            .divider {
              margin: 0px 12px;
              list-style: none;
              height: 0;
              border: 1px solid rgba(0, 0, 0, 0.08);
              border-width: 1px 0 0;
            }

            .group-wrapper {
              padding: 4px;

              .group-header {
                display: flex;
                align-items: center;
                padding: 0 12px;
                font-weight: 400;
                height: 32px;
                color: rgba(51, 51, 51, 0.6);
                font-size: 12px;
              }

              .menu-item {
                height: 40px;
                color: rgba(51, 51, 51, 0.8);
                font-size: 16px;
                border-radius: 8px;
                display: flex;
                align-items: center;
                padding: 0 12px;
                font-weight: 400;

                .icon {
                  color: rgba(51, 51, 51, 0.3);
                  margin-left: auto;
                }

                .component {
                  margin-left: auto;
                }

                .multistage-toggle {
                  position: relative;
                  background: rgba(0, 0, 0, 0.03);
                  display: flex;
                  padding: 2px;
                  border-radius: 999px;
                  cursor: pointer;

                  .active {
                    background: #fff;
                    box-shadow:
                      0 2px 8px 0 rgba(0, 0, 0, 0.04),
                      0 1px 2px 0 rgba(0, 0, 0, 0.02);
                    color: #333;
                  }

                  .toggle-item {
                    border-radius: 999px;
                    background: transparent;
                    color: rgba(51, 51, 51, 0.6);

                    .icon-wrapper {
                      width: 24px;
                      height: 24px;
                      display: flex;
                      align-items: center;
                      justify-content: center;
                      cursor: pointer;
                    }
                  }
                }
              }
            }
          }
        }

        .information-wrapper {
          -webkit-user-select: none;
          user-select: none;
          cursor: pointer;
          position: relative;
          margin-bottom: 20px;
          height: 48px;
          width: 100%;
          display: flex;
          font-weight: 600;
          align-items: center;
          border-radius: 999px;
          padding: 0 16px;
        }
      }
    }

    .main-content {
      width: 100%;
    }

    .main-content {
      @media screen and (min-width: 960px) and (max-width: 1191px) {
        padding-left: calc(-6px + 25vw);
      }

      @media screen and (min-width: 1192px) and (max-width: 1423px) {
        padding-left: calc(-4.8px + 20vw);
      }

      @media screen and (min-width: 1424px) and (max-width: 1727px) {
        padding-left: calc(-5.33333px + 16.66667vw);
      }

      @media screen and (min-width: 1728px) {
        padding-left: 282.66667px;
      }
    }
  }
}
</style>
