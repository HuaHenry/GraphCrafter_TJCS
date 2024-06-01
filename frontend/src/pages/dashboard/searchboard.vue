<template>
  <div class="feeds-page">
    <div class="channel-container">
      <div class="scroll-container channel-scroll-container">
        <div class="content-container">
          <!-- <div class="channel active">推荐</div>
          <div class="channel">关注</div>         -->
          <div class="static-channel">全部</div>
        </div>
      </div>
    </div>
    <div class="loading-container"></div>
    <div class="feeds-container">
      <Waterfall :list="list" :width="242" :hasAroundGutter="false" style="max-width: 1260px">
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
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import { LazyImg, Waterfall } from "vue-waterfall-plugin-next";
import "vue-waterfall-plugin-next/dist/style.css";
import store from "../../store/index";

const route = useRoute();
const router = useRouter();

const list = ref([]);

// 获取搜索结果
const fetchSearchResults = async () => {
    const query = route.query.query;
    if (!query) {
        list.value = [];
        return;
    }
    try {
        const response = await axios.get(`/api/posts/search`, { params: { query } });
        list.value = response.data.posts.map(post => ({
            ids: post.id,
            pictures: post.picture1,
            titles: post.title,
            authors: post.author,
            avatars: post.avatar,
            likes: post.likes
        }));
    } catch (error) {
        console.error('Error fetching search results:', error);
    }
};

onMounted(fetchSearchResults);
// const toMain = (id: number) => {
//   router.push({ path: "/main" });
// };
const toMain = (id: number) => {
  router.push({ path: "/main", query: { id: id } });
};
</script>

<style lang="less" scoped>
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
