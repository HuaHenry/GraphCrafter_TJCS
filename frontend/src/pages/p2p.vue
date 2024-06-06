<template>
  <div class="custom-box" >
    
    <!--顶栏-->
    <div class="header">
      <div class="room-info">对话修图模型</div>
    </div>
    <!--对话框-->
    <div ref="content" class="message-container" >
      <div class="load"  v-loading="isLoading"
      element-loading-text="Loading..."
      element-loading-svg-view-box="-10, -10, 50, 50"
      element-loading-background="rgba(122, 122, 122, 0)"
      style="width: 100%"> </div>
      <!-- <el-loading lock text="正在加载..." spinner="el-icon-loading" background="rgba(255, 0, 0, 0.7)" v-model="isLoading" style="z-index:10"></el-loading> -->
      <template v-for="(message, index) in messages" :key="index">
        <!--时间-->
          <div class="system-message">{{message.time}}</div>
        <!--自己-->
        <div v-if="message.role=='user'" class="chat-bubble left" >
          <!-- 消息 -->
          <span class="chat-bubble-right" >
     		  <div class="chat-text">{{message.content}}</div>
            <img v-if="message.picture!=null" :src="message.picture" style="height: 200px;" @click="showDialog_user[index]=true">
            
            <!-- <el-button v-if="message.picture!=null && showButton[index]" class="button-below" type="info" plain>存草稿</el-button> -->
          </span>
          <span class="triangle-top-right"></span>
          <!-- 头像 -->
           <img :src="message.photo" class="user-avatar">
          
        </div>
        
        <!--对方-->
        <div v-else class="chat-bubble right">
          <!-- 头像 -->
           <img src="https://graphcrafter.oss-cn-beijing.aliyuncs.com/1/06012024191642.jpg" class="user-avatar">
          <!-- 消息 -->
          <span class="triangle-top-left" :class="{ 'change-border': isLeftBubbleHover }" ></span>
           <span class="chat-bubble-left">
<!--       <span class="chat-bubble-left" @mouseover="changeLeftArrowColor(true)" @mouseout="changeLeftArrowColor(false)"> -->
             <div class="chat-text">{{message.content}}</div>
             <img :src="message.picture" style="height: 200px;" @click="showDialog_gpt[index]=true">
             <!-- <el-button v-if="showButton_gpt[index]" class="button-below-gpt" type="info" plain @click="saveAsDraft_user">存草稿</el-button> -->

     	     </span>
        </div>

        <el-dialog  v-model="showDialog_user[index]" width="500" >
        <el-image :src="message.picture"></el-image>        
        <span slot="footer" class="dialog-footer">
          <el-button @click="showDialog_user[index] = false">取 消</el-button>
          <el-button type="primary" @click="saveAsDraft_user(index)">存草稿</el-button>
        </span>
        </el-dialog>

        <el-dialog  v-model="showDialog_gpt[index]" width="500" >
        <el-image :src="message.picture"></el-image>        
        <span slot="footer" class="dialog-footer">
          <el-button @click="showDialog_gpt[index] = false">取 消</el-button>
          <el-button type="primary" @click="saveAsDraft_gpt(index)">存草稿</el-button>
        </span>
        </el-dialog>
      </template>
    </div>
    
    <!--发送框-->
    <div class="chat-footer">

      <input class="message-input" v-model.trim="text" autocomplete="off" />
<!--      <input class="message-send-button" style="" ref="file" @change="" type="file" />-->

    </div>
    <div>
      <el-upload
          class="upload-demo"
          ref="upload"
          action="action"
          :on-success="handleSuccess"
          :on-error="handleError"
          :on-preview="handlePreview"
          :on-remove="handleRemove"
          :before-remove="beforeRemove"
          :http-request="uploadFile"
          multiple
          :limit="1"
          :on-exceed="handleExceed"
          :file-list="fileList"
          accept=".jpg,.png"
          style="margin-right: 10px;"
      >
        <el-button size="large" type="">上传图片</el-button>
      </el-upload>
      <el-button size="large" type="" @click="clearMsg" style="margin-right: 10px;">清空历史</el-button>
      <el-button size="large" type="" @click="sendMsg" style="float: right;">发送</el-button>
    </div>



  </div>
</template>

<script lang="ts">
import axios from 'axios';
import store from "../store/index";
import { ref,onMounted } from 'vue';
import "https://gosspublic.alicdn.com/aliyun-oss-sdk-6.18.0.min.js";
import { formatDateTime } from '@/utils/socket';
import { ElMessage } from 'element-plus';
import { fa } from 'element-plus/es/locale/index.mjs';
import { ElLoading } from 'element-plus';

export default {
  data(){
    return{
      // isLoading:false,
      isLeftBubbleHover: false,
      selectMessageIndex:0,
      showMenu: true,
      menuX: -100,
      menuY: -100,
      showButton: [],
      showDialog_gpt: [],
      fileList:[],
      showDialog_user: [],
    }
  },
  emits: ['close'],
  methods: {
    // hideButton(index) {
    //   setTimeout(() => {
    //     this.showButton[index] = false;
    //   }, 1000); // delay in milliseconds
    // },
    uploadFile(params) {
      this.file = params.file;
      const client = new OSS({
        region: "oss-cn-beijing",
        accessKeyId: "LTAI5tR1c1uhFRfWxjq8BWT4",
        accessKeySecret: "BdN5OIEdet7IO6KWOq7TJiivHOsC5B",
        bucket: "graphcrafter",
      });
      function fileToBlob(file) {
        return new Blob([file], { type: file.type });
      }
      async function putObject(data) {
        try {
          const options = {
            meta: { temp: "demo" },
            mime: "json",
            headers: { "Content-Type": "Buffer" },
          };
          //获取年月日时间
          const ops = { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false };
          const formattedTime = new Intl.DateTimeFormat('en-US', ops).format(new Date()).replace(/[^0-9]/g, '');
          //设置图片名称

          // TODO:替换为session中的用户名
          const Uname = store.state.user_id ;
          //
          const imgName = Uname +'/'+ formattedTime + ".jpg";
          const result = await client.put(imgName, data, options);
          //存储图片的url至本地消息中
          const imgURL = "https://graphcrafter.oss-cn-beijing.aliyuncs.com/" + imgName;
          axios.post('/api/upload_Picture',{
            img:imgURL,
            prompt:null,
            Ptype:0
          })
          console.log(imgURL);
          return imgURL;
        } catch (e) {
          console.log(e);
        }
      }
      putObject(fileToBlob(this.file)).then(imgURL => {
        this.img_url = imgURL; // 将返回的 imgURL 赋值给 this.img_url
      })
          .catch(error => {
            console.error("Error uploading file:", error);
          });;
    },
    handleClose(done) {
      done();
      this.fileList = [];
      this.xlsx_url = "";
    },
    beforeRemove(file, fileList) {
      return this.$confirm(`确定移除 ${file.name}？`);
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handleSuccess(response, file) {
      this.xlsx_url = response.url;
    },
    handleError(err, file, fileList) {
      let myError = err.toString();
      myError = myError.replace("Error: ", "");
      myError = JSON.parse(myError);
      this.$message.error(myError.message);
    },
    handlePreview(file) {
      console.log(file, "handlePreview");
    },
    handleExceed(files, fileList) {
      this.$message.warning(`只允许上传 1 个文件`);
    },
    saveAsDraft_user(index){
      this.showDialog_user[index]=false;
      console.log('button clicked');
      axios.post('/api/post_draft/',{
        img:this.messages[index].picture,
        user_id:store.state.user_id,
        label:"0"
      }).then(function (response) {
        console.log(response.data['img']);
      }).catch(function (error) {
        console.log(error);
      });
      ElMessage.success('图片已保存至草稿箱！');
    },
    saveAsDraft_gpt(index){
      this.showDialog_gpt[index]=false;
      console.log('button clicked');
      axios.post('/api/post_draft/',{
        img:this.messages[index].picture,
        user_id:store.state.user_id,
        label:"3"
      }).then(function (response) {
        console.log(response.data['img']);
      }).catch(function (error) {
        console.log(error);
      });
      ElMessage.success('图片已保存至草稿箱！');
    }
    
  },
  setup() {
    const text=ref("");
    let messages=ref([]);
    let img_url=ref("");
    let info=ref();
    const isLoading = ref(false);
    axios.post("/api/get_info",{
      user_id:store.state.user_id
    }).then(function (response) {
      info.value=response.data["info"];
    }).catch(function (error) {
      console.log(error);
    });
    async function clearMsg(){
      messages.value=[];
      img_url.value="";
    }
    async function sendMsg(){
      const newMessage = {
        content: text.value,
        time: formatDateTime(new Date()),
        role: "user",
        picture: img_url.value, // 使用 img_url.value 而不是 img_url
        photo: info.value // 使用 info.value 而不是 info
      };
      messages.value.push(newMessage);
      isLoading.value=true;

      // const loading = ElLoading.service({ lock: false ,background: 'rgba(0, 0, 0, 0)',text: 'Loading',});
      
      text.value='';
      axios.post('/api/chat_P2P',{
        img_url:img_url.value,
        prompt:newMessage.content,
        user_id:store.state.user_id,
      }).then(function (response) {
        console.log(response.data['img']);
        const newMsg={
          time: formatDateTime(new Date()),
          role:"assistant",
          picture:response.data['img']
        };
        messages.value.push(newMsg);
        img_url.value=response.data['img'];
        isLoading.value=false;
        // loading.close();
        }).catch(function (error) {
          console.log(error);
          // loading.close();
          isLoading.value=false;

        });
        
    }


    onMounted(() => {

    });

    return {
      text,
      messages,
      sendMsg,
      img_url,
      clearMsg,
      isLoading
    };
  }
};

</script>

<style scoped>

/deep/ .upload-demo{
  display: flex;
  flex-direction: row; /* 默认值，可以省略 */
  justify-content: flex-start; /* 默认值，可以省略 */
  margin-bottom: 10px;
}

/deep/ .el-upload-list__item {
  margin-left: 10px;
  width:200px;
  height:36px;
  background-color: #ebebeb;
}

#upload {
  display: none;
}

.user-avatar{
  width: 40px;
  height: 40px;
  border-radius: 30px;
  margin:0 2px 0 2px;
}
.user-container{
  display: flex;
  justify-content: flex-start;
  align-items: center;
}
.user-container .user-info{
  display: flex;
  justify-content: left;
  flex-direction: column;
  align-items: flex-start;
  color:black;
}

.triangle-top-left {
  width: 2px;
  height: 3px;
  border-top: 10px solid #fdfdfe;
  border-left: 15px solid transparent;
  margin-top: 10px;
  margin-left: 10px;
}
.change-border {
  /* 悬停时的样式 */
  border-top: 10px solid #ebebeb;
}
.triangle-top-right {
  width: 2px;
  height: 3px;
  border-top: 10px solid #80b9f2;
  border-right: 15px solid transparent;
  margin-top: 10px;
  margin-right: 10px;
}


.chat-bubble.right div:before, .chat-bubble.left div:before {
  border-style: solid;
  margin-top: 5px;
}
.button-below {
  position: absolute;
  bottom: 0; /* Adjust this value as needed */
  right:50%;
  /* align-items: center; */
  transform: translateX(50%);
  z-index: 3;
}

.button-below-gpt {
  position: absolute;
  bottom: 0; /* Adjust this value as needed */
  left:50%;
  transform: translateX(-50%);
  z-index: 3;
}

.chat-bubble {
  /* position: relative; */
  margin: 20px 0;
  display: -webkit-flex;
  display: flex;
  -webkit-align-items: top;
  align-items: top;
}

.chat-bubble.left {
  -webkit-justify-content: right;
  justify-content: right;
}

.chat-bubble .chat-bubble-left {
  position: relative;
  padding: 10px;
  border-radius: 5px;
  background-color: #fdfdfe;
  color: black;
}

.chat-bubble .chat-bubble-left:hover{
  background-color: #ebebeb;
}
.chat-bubble-right {
  position: relative;

  padding: 10px;
  background-color: #80b9f2;
  border-radius: 5px;
  color: white;
}

.chat-bubble-right:hover{
  background-color: #7ab1e8;
}

.chat-bubble-right:hover + .triangle-top-right{
  border-top: 10px solid #7ab1e8;
}

.chat-bubble.right {
  margin-left: 10px;
  border-width:12px 12px 0 0;
}
.chat-bubble.left {
  margin-right: 5px;
  border-width: 0 0 12px 12px ;
}
.chat-image{
  width: 150px;
  height: 150px;
}
.chat-text {
  max-width: 300px;
  text-align: left;
}

.custom-box {
  position: relative;
  top:72px;
  bottom: 0px;
  flex: 1;
  padding: 0 24px;
  /* padding-top: 72px; */
  border-radius: 0 10px 10px 0;
  background-color:#fbfcff;
  color: #fff;
  border-left: 1px solid #e9eaec;
  width: 100%;
  /* height: 100%; */
}

.header {
  display: flex;
  padding: 20px;
  justify-content: space-around;
  align-items: center;
  height: 45px;
  font-size: 14px;

}

.room-info {
  color: #858383;
  width: 100%;
  font-size: 16px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  margin: 10px 10px 10px 5px;
  text-align: center;
}
.connection-status {
  width: 20%;
  text-align: center;
}
.close-button {
  width: 32px;
  height: 32px;
  border-radius: 10px;
  background-color: #cec5c5;
  display: flex;
  justify-content: center;
  align-items: center;
}

.message-container {
  position:relative;
  border-top: 1px solid #e9eaec;
  border-bottom: 1px solid #e9eaec;
  height: 540px;
  overflow-y: scroll;
  background-color: #f4f5f7;
  /*border-radius: 8px;*/
  padding: 8px;

}
.load{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.system-message {
  height: 30px;
  margin-top: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #888;
  font-size: 14px;
}

.source-message {
  height: 40px;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  color: #0f0;
}

.default-message {
  height: 40px;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  color: #a020f0;
}

.chat-footer {
  margin: 10px;
  display: flex;
  justify-content: space-around;
  align-items: flex-end;
  height: 50px;
}

.message-input {
  width: 100%;
  align-self: flex-start;
  height: 100%;
  background-color:#e1e1e1;
  padding: 5px;
  border-radius: 8px;
}

.message-send-button{
  padding: 5px;
  width: 15%;
  height: 30px;
  border: 1px solid #e1e1e1;
  border-radius: 5px;
  background: #ffffff;
  color: #666666;
  display: flex;
  justify-content: center;
  align-items: center;
}

.photo-button{
  margin-right: 10px;
  padding: 5px;
  width: 15%;
  height: 30px;
  border: 1px solid #e1e1e1;
  border-radius: 5px;
  background: #ffffff;
  color: #666666;
  display: flex;
  justify-content: center;
  align-items: center;
}

.message-send-button:hover{
  color: #acacb0;
}
.context-menu {
  position: absolute;
  background-color: #fff;
  border: 1px solid #ccc;
  color: #666666;
  padding: 5px 25px;
  font-size: 14px;
  box-shadow: 0 0 5px 2px rgba(0, 0, 0, 0.02);
}
.context-menu:hover{
  background-color: #f5f4f4;
}
</style>