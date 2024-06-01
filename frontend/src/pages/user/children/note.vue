<template>
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
           <!-- 添加删除按钮 -->
          <button class="delete-button" @click="deleteItem(item.ids)">
              删除
          </button>
        </div>
      </template>
    </Waterfall>
  </div>
</template>
<script lang="ts" setup>
// import { Star } from "@element-plus/icons-vue";
import { Search } from "@element-plus/icons-vue";
import { LazyImg, Waterfall } from "vue-waterfall-plugin-next";
import "vue-waterfall-plugin-next/dist/style.css";
// import { ref } from "vue";
import store from "../../../store/index";
import { ref, onMounted } from "vue";
import axios from 'axios';

import { useRouter } from "vue-router";
import {ElMessage} from "element-plus";
const router = useRouter();
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
    const data = await axios.get(`/api/note/${store.state.user_id}`);
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

const deleteItem = async (id: number) => {
  // 弹出确认对话框
  if (confirm("是否确认删除?")) {
    try {
      await axios.delete(`/api/delete-post/${id}`);
      list.value = list.value.filter(item => item.id !== id);
      // 显示删除成功的消息
      ElMessage.success({
        message: "删除成功",
        duration: 1500
      });
      //console.log('删除成功');
      setTimeout(() => {
        location.href = "/note";
      }, 800);  // 延时800毫秒
      //window.location.reload(); // 刷新页面
    } catch (error) {
      // 处理删除失败的情况
      console.error('Error deleting post:', error);
      alert('删除失败');  // 可以选择在这里显示更多错误信息
    }
  } else {
    // 用户取消了删除操作
    console.log('Delete operation canceled');
  }
};



onMounted(() => {
  fetchData(); // Call fetchData function when the component is mounted
});
</script>
<style lang="less" scoped>

.delete-button {
  position: absolute;
  top: 10px; // 调整位置以适应你的设计
  right: 10px;
  background: #ff4d4f;
  border: none;
  border-radius: 50%;
  color: white;
  cursor: pointer;
  padding: 5px 10px;
  font-size: 14px;

  &:hover {
    background: #ff7875;
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
</style>
