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
      <Waterfall :list="list" :width="242" :hasAroundGutter="false" style="max-width: 1260px">
        <template #item="{ item }">
          <div class="card">
            <div class="image-container" >
              <LazyImg :url="item.pictures" style="border-radius: 8px; width: 100%; height: auto;" />
              <div class="hover-button" @click="() => useNow(item.descriptions, item.types)">立即使用</div>
            </div>
            <div class="footer">
              <a class="title" ><span>{{ truncatedText(item.descriptions) }}</span></a>
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

    <!-- 处理结果 -->
    <el-dialog title="处理结果" v-model="isProcessedImgOpen" width="30%" :custom-class="'rounded-dialog'">
      <div class="avatar-editor">
        <img :src="processedImg " class="avatar-preview" alt="修改图片" />
        <div class="avatar-actions">
          <el-button class="primary-button" type="primary" @click="saveProcessedImage">保存</el-button>
          <el-button class="secondary-button" @click="cancelSaveImage">取消</el-button>
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
import store from "@/store/index";
import axios from "axios";

let current_category =''
let current_description = ref('')

const router = useRouter();

const list = ref([]);
const uploadedAvatar = ref('');
const processedImg = ref('');
const fileInput = ref(null);

const isAvatarEditorOpen = ref(false);
const isProcessedImgOpen = ref(false);
const channels = [
  { name: '图像色彩', backendName: 'color' },
  { name: '图像变换', backendName: 'transform'  },
  { name: '图像过滤',  backendName: 'filter' },
  { name: '提取轮廓', backendName: 'contour' },
  { name: '图像增强', backendName: 'enhance' },
];

const activeChannel = ref(0); // 默认激活第一个频道

const fetchData = async () => {
  list.value.splice(0, list.value.length);//清空列表
  current_category = channels[activeChannel.value].name;
  let current_category_backend = channels[activeChannel.value].backendName;
  try {
    const response = await axios.get('/api/opencvimages');
    const result = response.data;
    const { ids, pictures, descriptions, codes, types } = result;

    for (let i = 0; i < ids.length; i++) {
      if(types[i] === current_category_backend){
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
  fetchData();
};

const useNow = (description, type) => {
  triggerFileInput();
  console.log("Description:", description);
  console.log("Type:", type);
  current_description =description;
  current_category = type;
  
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


  //上传要修改的图片，并获得结果
  const uploadImg = async () => {
    const file = fileInput.value.files[0];
    console.log(file,current_category,current_description);
    const userId = store.state.user_id;

    console.log("[data] ", userId, current_category, current_description, file)

    const formData = new FormData();
      formData.append('user_id', userId);
    console.log("user_id", formData);
      formData.append('process_category', current_category);
    console.log("process_category", formData);
      formData.append('process_type', current_description);
    console.log("process_type", formData);
      formData.append('file', file);
    console.log("file", formData);

    try {
        console.log(formData)
      const response = await axios.post('/api/simple-image-process', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      const data = response.data;
      if (data.error) {
        alert('Error: ' + data.error);
        return;
      }
        const newImageUrl = data.imgUrl;
      processedImg.value = newImageUrl;
      isAvatarEditorOpen.value = false;
      isProcessedImgOpen.value = true;
    } catch (error) {
      console.error('There was an error processing the image:', error);
      alert('Network response was not ok');
    }
};

function cancelSaveImage()
{
  isProcessedImgOpen.value = false;
}

async function saveProcessedImage()
{
  isProcessedImgOpen.value = false;
  const userId = store.state.user_id;
  const picInfo = {
    img: processedImg.value,
    user_id: userId,
      // label: channels[activeChannel.value].name,
    label: "2"
  };
    await axios.post('/api/post_draft/', picInfo);
    //传到picture表
    axios.post('/api/upload_Picture',{
                img:processedImg.value,
                prompt:null,
                Ptype:1
            })
}

// 处理方法的名称最多只显示20个字
function truncatedText(text) {
  if (text.length > 24) {
    return text.substring(0, 21) + '...';
  }
  return text;
}
</script>



<style lang="less" scoped>
.avatar-editor {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  
  border-radius: 20px; /* 添加圆角 */
  background-color: #fff; /* 确保弹窗背景为白色 */
  padding: 20px; /* 添加一些内边距以提供空间 */
  box-shadow: 0 8px 64px 0 rgba(0, 0, 0, 0.04), 0 1px 4px 0 rgba(0, 0, 0, 0.02);
}

.avatar-actions {
  display: flex; /* 使用 Flexbox 布局 */
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  gap: 10px; /* 按钮之间的间距 */
  margin-top: 20px; /* 可根据需要调整顶部间距 */
}

.primary-button {
  background-color: #000C42 !important; /* 自定义主按钮颜色 */
  border-color: #000C42!important;
  color: white;
  height:30px;
  width:75px;
  border-radius:10px;
  
}

.primary-button:hover {
  background-color: rgba(0, 32, 128, 0.769); /* 鼠标悬停时的背景颜色变暗 */
  border-color: #000C42; /* 鼠标悬停时的边框颜色也变暗 */
}

.secondary-button {
  background-color: #DE124A !important; /* 自定义次按钮颜色 */
  border-color: #DE124A !important;
  color: white;
  height: 30px;
  width: 75px;
  border-radius: 10px;
 
}

.secondary-button:hover {
  background-color: #DE124AB3; /* 鼠标悬停时的背景颜色变暗并半透明 */
  border-color: #DE124AB3; /* 鼠标悬停时的边框颜色也变暗并半透明 */
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
