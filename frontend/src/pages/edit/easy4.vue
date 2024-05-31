<template>
  <div class="feeds-page">
    <div class="channel-container">
      <div class="scroll-container channel-scroll-container">
        <div class="content-container">
          <div
            v-for="(channel, index) in channels"
            :key="index"
            :class="['channel', { active: activeChannel === index }]"
            @click="handleChannelClick(index)"
          >
            {{ channel.name }}
          </div>
        </div>
      </div>
    </div>
    <div class="loading-container"></div>
    <div class="feeds-container">
      <Waterfall :list="list" :width="220" :hasAroundGutter="false" style="max-width: 1260px">
        <template #item="{ item }">
          <div class="card">
            <LazyImg :url="item.pictures" style="border-radius: 8px" @click="toMain(item.ids)" />
            <div class="footer">
              <a class="title"><span>{{ item.titles }}</span></a>
            </div>
          </div>
        </template>
      </Waterfall>
    </div>
    <div class="feeds-loading"></div>
  </div>
</template>



<script lang="ts" setup>
import { LazyImg, Waterfall } from "vue-waterfall-plugin-next";
import "vue-waterfall-plugin-next/dist/style.css";
import { useRouter } from "vue-router";
import { ref, onMounted } from "vue";

const router = useRouter();

const list = ref([]);

const channels = ref([
  { name: '图像色彩', path: '/easy1' },
  { name: '图像变换', path: '/easy2' },
  { name: '图像过滤', path: '/easy3' },
  { name: '提取直线、轮廓、区域', path: '/easy4' },
  { name: '图像增强', path: '/easy5' },
]);

const activeChannel = ref(3); // 默认激活第四个频道

const fetchData = async () => {
  try {
    const data = await fetch('http://127.0.0.1:8080/api/posts'); // Replace URL with your endpoint
    const result = await data.json();
    const { ids, authors, avatars, pictures, titles } = result;
    for (let i = 0; i < titles.length; i++) {
      const item = {
        ids: ids[i],
        pictures: pictures[i],
        titles: titles[i],
        authors: authors[i],
        avatars: avatars[i],
      };
      list.value.push(item);
    }
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

onMounted(() => {
  fetchData();
});

const handleChannelClick = (index: number) => {
  activeChannel.value = index;
  const path = channels.value[index].path;
  router.push({ path });
};

const toMain = (id: number) => {
  router.push({ path: "/main", query: { id: id } });
};
</script>


<style lang="less" scoped>
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
    }
  }
}
</style>
