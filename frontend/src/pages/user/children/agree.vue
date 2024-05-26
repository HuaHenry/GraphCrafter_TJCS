<template>
  <div class="feeds-container">
    <div><el-select v-model="selected_label" placeholder="请选择标签" style="margin-left: 60px;margin-bottom: 20px; width: 200px;margin-top: 20px;">
    <el-option
      v-for="item in labels"
      :key="item"
      :label="item"
      :value="item">
    </el-option>
  </el-select><el-button type="primary"  @click="labelSearch" style="margin-left: 20px;">搜索</el-button></div>
    <Waterfall :list="list" :width="220" :hasAroundGutter="false" style="max-width: 1260px">
      <template #item="{item}">
        <div class="card" :key="componentKey">
          <LazyImg :url="item.pictures" style="border-radius: 8px"  @click="toDel_draft(item.ids)"    />
          <div class="footer">
            <a class="title"><span>{{ item.labels }}</span></a>
            
            <div class="author-wrapper">
              <a class="author">
                <!-- <img class="author-avatar" :src="item.avatars" /> -->
                <span class="name">{{ item.dates }}</span>
              </a>
              <!-- <span class="like-wrapper like-active">
                <Search style="width: 1em; height: 1em" />
                <span class="count">{{ item.likes }}</span>
              </span> -->
            </div>
          </div>
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

import { ref, onMounted } from "vue";
import axios from 'axios';


import { useRouter } from "vue-router";
const router = useRouter();
const toDel_draft = (id: number) => {
  router.push({ path: "/del_draft", query: { post_id: id } });
};

let  componentKey=0;

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

const labels=ref();
const selected_label=ref();

const get_labels = async() => {
  try{
    const data = await axios.get("/api/get_labels");
    labels.value= data.data;
    console.log(labels.value);
  } catch (error) {
    console.error('Error fetching labels:', error);
  }
};

const labelSearch = async () => {
  try {
    // Simulated asynchronous database query
    console.log(selected_label);
    const data = await axios.get(`/api/search_drafts/${selected_label.value}`);
    const result = data.data;
    // 解构出各个属性数组
    list.value=[];
    const { pictures, dates, labels, ids } = result;
    // 遍历数组，构建每个对象并添加到数组中
    for (let i = 0; i < pictures.length; i++) {
      const item = {
        pictures: pictures[i], // 使用对应索引的图片 URL 作为 src 属性
        dates: dates[i], // 使用对应索引的标题属性
        labels: labels[i], // 使用对应索引的作者属性
        ids:ids[i]
      };
      list.value.push(item);
    }
    componentKey=componentKey+1;
    // console.log(result);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};


const fetchData = async () => {
  try {
    // Simulated asynchronous database query
    const data = await axios.get("/api/drafts");
    const result = data.data;
    // 解构出各个属性数组
    const { pictures, dates, labels, ids } = result;
    // 遍历数组，构建每个对象并添加到数组中
    for (let i = 0; i < pictures.length; i++) {
      const item = {
        pictures: pictures[i], // 使用对应索引的图片 URL 作为 src 属性
        dates: dates[i], // 使用对应索引的标题属性
        labels: labels[i], // 使用对应索引的作者属性
        ids:ids[i]
      };
      list.value.push(item);
    }
    // console.log(result);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};
onMounted(() => {
  fetchData(); // Call fetchData function when the component is mounted
  get_labels();
});
</script>
<style lang="less" scoped>
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
