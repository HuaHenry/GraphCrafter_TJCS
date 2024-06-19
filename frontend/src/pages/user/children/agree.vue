<template>
  <div class="feeds-container">
    <div><el-select v-model="selected_label" placeholder="请选择标签" style="margin-left: 60px;margin-bottom: 20px; width: 200px;margin-top: 20px;">
    <el-option
      v-for="item in labels"
      :key="item"
      :label="item"
      :value="item">
    </el-option>
  </el-select>
  <el-button type="primary"  @click="labelSearch" style="margin-left: 20px;background-color: #000C42; color: white; border-color: #000C42;">搜索</el-button></div>
    
  <Waterfall :list="list" :width="220" :hasAroundGutter="false" style="max-width: 1260px" >
      <template #item="{item}">
        <div class="card" :key="componentKey" @mouseover="item.showPostButton = true"
            @mouseout="item.showPostButton = false" @click="toggleShowPostDialog(item)">          
          <LazyImg :url="item.pictures" style="border-radius: 8px"      />
          <!-- <el-button v-if="item.showPostButton" class="post-button" @click="toggleShowPostDialog">发帖</el-button> -->
          <div class="footer">
            <a class="title"><span>{{ item.labels }}</span></a>
            
            <div class="author-wrapper">
              <a class="author">
                <!-- <img class="author-avatar" :src="item.avatars" /> @click="toDel_draft(item.ids)" -->
                <span class="name">{{ item.dates }}</span>
              </a>
            </div>
          </div>
        </div>
        
      </template>
    </Waterfall>

    <el-dialog title="发布帖子"  v-model="showPostDialog" width="500" >
            <el-image :src="currentItem.pictures"></el-image>
            <el-input v-model="ruleForm.name" type="text" id="title" name="title" placeholder="请输入标题"></el-input>
            <el-input v-model="ruleForm.summary" type="textarea" id="description" name="description" placeholder="请输入内容..."></el-input>
            <span slot="footer" class="dialog-footer">
              <el-button @click="showPostDialog = false">取 消</el-button>
              <el-button type="primary" @click="submitForm('ruleForm')">发 布 动 态</el-button>
            </span>
        </el-dialog>
  </div>
</template>
<script lang="ts" setup>
// import { Star } from "@element-plus/icons-vue";
import { Search } from "@element-plus/icons-vue";
import { LazyImg, Waterfall } from "vue-waterfall-plugin-next";
import { ElMessage } from "element-plus";
import "vue-waterfall-plugin-next/dist/style.css";
// import { ref } from "vue";

import { ref, onMounted } from "vue";
import axios from 'axios';
import store from "../../../store/index";

import { useRouter } from "vue-router";
const router = useRouter();
const toDel_draft = (id: number) => {
  router.push({ path: "/del_draft", query: { post_id: id } });
};

let  componentKey=0;

const list = ref([]);

const labels=ref();
const selected_label=ref();
// const showPostButton = ref(false);
const showPostDialog = ref(false);
const ruleForm = ref({
    name:'',
    image:'',
    summary:'',
    issue:'',
});
const currentItem = ref();

const get_labels = async() => {
  try{
    const data = await axios.get(`/api/get_labels/${store.state.user_id}`);
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
        ids:ids[i],
        showPostButton:false
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
    const data = await axios.get(`/api/drafts/${store.state.user_id}`);
    const result = data.data;
    // 解构出各个属性数组
    const { pictures, dates, labels, ids } = result;
    // 遍历数组，构建每个对象并添加到数组中
    for (let i = 0; i < pictures.length; i++) {
      const item = {
        pictures: pictures[i], // 使用对应索引的图片 URL 作为 src 属性
        dates: dates[i], // 使用对应索引的标题属性
        labels: labels[i], // 使用对应索引的作者属性
        ids:ids[i],
        showPostButton:false
      };
      list.value.push(item);
    }
    // console.log(result);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};
function toggleShowPostDialog(item)
{
  currentItem.value = item;
  showPostDialog.value =true;
  console.log(showPostDialog.value);
}

const submitForm =()=>
{
  // console.log(ruleForm.value);
  console.log(currentItem.value.pictures);
  try{
    axios.post('/api/postnotes',{
      pics:[currentItem.value.pictures],
      title:ruleForm.value.name,
      description:ruleForm.value.summary,
      userId:store.state.user_id,
  });
  }catch (error) {
    console.error('Error fetching data:', error);
  }
  ElMessage.success({
    message: "发布成功",
    duration: 1000,
  });
    // 清空表单
    ruleForm.value.name = "";
    ruleForm.value.summary = "";

  // 使用setTimeout延迟1秒后执行页面跳转
  setTimeout(() => {
    location.href = "/dashboard";
  }, 800);  // 延时800毫秒

}
onMounted(() => {
  fetchData(); // Call fetchData function when the component is mounted
  get_labels();
});
</script>
<style lang="less" scoped>
.post-button {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  z-index: 1000;
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
