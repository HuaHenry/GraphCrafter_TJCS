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
            <div class="image-container" >
              <LazyImg :url="item.pictures" style="border-radius: 8px; width: 100%; height: auto;" />
              <div class="hover-button" @click="() => useNow(item.descriptions, item.types)">立即使用</div>
            </div>
            <div class="footer">
              <a class="title"><span>{{ item.descriptions }}</span></a>
            </div>
          </div>
        </template>

      </Waterfall>
    </div>
    <div class="feeds-loading"></div>
    <input type="file" accept="image/*" @change="PreviewImg" class="hidden-input" ref="fileInput" />

    <!-- 预览弹窗 -->
    <el-dialog title="修改图片" v-model="isAvatarEditorOpen" width="30%" :custom-class="'rounded-dialog'">
        <div class="avatar-editor">
          <img :src="uploadedAvatar " class="avatar-preview" alt="修改图片" />
          <div class="avatar-actions">
            <el-button class="primary-button" type="primary" @click="uploadImg">上传</el-button>
            <el-button class="secondary-button" @click="cancelAvatarEdit">取消</el-button>
          </div>
        </div>
    </el-dialog>

  </div>

  
</template>




<script lang="ts" setup>
import { LazyImg, Waterfall } from "vue-waterfall-plugin-next";
import "vue-waterfall-plugin-next/dist/style.css";
import { useRouter } from "vue-router";
import { ref, onMounted } from "vue";

let current_type = ref('')
let current_description = ref('')

const router = useRouter();

const list = ref([]);
const uploadedAvatar = ref('');
const fileInput = ref(null);

const isAvatarEditorOpen = ref(false);
const channels = ref([
  { name: '图像色彩', path: '/easy1' },
  { name: '图像变换', path: '/easy2' },
  { name: '图像过滤', path: '/easy3' },
  { name: '提取轮廓', path: '/easy4' },
  { name: '图像增强', path: '/easy5' },
]);

const activeChannel = ref(3); // 默认激活第一个频道

const fetchData = async () => {
  try {
    const data = await fetch('http://127.0.0.1:8080/api/opencvimages'); // Replace URL with your endpoint
    const result = await data.json();
    const { ids, pictures, descriptions, codes, types } = result;
    for (let i = 0; i < ids.length; i++) {
      if(types[i] === 'contour'){
        const item = {
          ids: ids[i],
          pictures: pictures[i],
          descriptions: descriptions[i],
          codes: codes[i],
          types: types[i],
        };
        list.value.push(item);
      }
      
    }
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};


onMounted(() => {
  fetchData(); // 也可以根据实际情况改变默认参数
});

const handleChannelClick = (index: number) => {
  activeChannel.value = index;
  const path = channels.value[index].path;
  router.push({ path });
};

const useNow = (description, type) => {
  
  triggerFileInput();
  console.log("Description:", description);
  console.log("Type:", type);
  current_description =description;
  current_type = type;
  
};

const triggerFileInput = () => {
  console.log(fileInput.value)
    if (fileInput.value) {
        fileInput.value.value = '';  // 清空选择的文件
        fileInput.value.click();  // 触发点击事件
    }
};

const PreviewImg = (event) => {
    isAvatarEditorOpen.value = true;
    const target = event.target as HTMLInputElement;
    console.log(target)
    const file = target.files ? target.files[0] : null;
    
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        // 只将图片预览结果存储到 uploadedAvatar 中
        uploadedAvatar.value = e.target?.result as string;
       
        isAvatarEditorOpen.value = true; // 打开预览编辑器
        //console.log(isAvatarEditorOpen.value)
      };
      reader.readAsDataURL(file);
      
    }
  };


    // 关闭头像编辑器并取消修改
    const cancelAvatarEdit = () => {
    isAvatarEditorOpen.value = false;
    
  
  };


  //上传要修改的图片
  const uploadImg = async () => {
    const file = fileInput.value.files[0];
    console.log(file,current_type,current_description)
    
};


</script>



<style lang="less" scoped>

.avatar-actions {
  display: flex; /* 使用 Flexbox 布局 */
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  gap: 10px; /* 按钮之间的间距 */
  margin-top: 20px; /* 可根据需要调整顶部间距 */
}

.primary-button {
  background-color: #409EFF; /* 自定义主按钮颜色 */
  border-color: #409EFF;
  color: white;
}

.secondary-button {
  background-color: #F56C6C; /* 自定义次按钮颜色 */
  border-color: #F56C6C;
  color: white;
}

.hover-button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: none; /* 默认隐藏，鼠标悬浮时显示 */
  padding: 5px 10px;
  background-color: rgba(86, 83, 83, 0.6); /* 半透明黑色背景 */
  color: white;
  border-radius: 5px;
  cursor: pointer;
  z-index: 10;
  font-size: 12px; /* 调整字体大小为12px */
}

.hidden-input {
  display: none;
}

.image-container:hover .hover-button {
  display: block; /* 鼠标悬浮时显示 */
}
.card {
  background-color: #f3f3f3; /* 浅灰色背景 */
  border-radius: 8px; /* 保持你已有的圆角 */
  box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* 可选：添加轻微的阴影效果提升立体感 */
  overflow: hidden; /* 防止内部内容溢出 */
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
    justify-content: center; /* 水平居中 */
    align-items: center; /* 垂直居中 */
    text-align: center; /* 文本居中，对内联内容或单行文本有用 */

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
