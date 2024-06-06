<template>
  <div class="custom-box">
    <!--顶栏-->
    <div class="header">
      <div class="room-info">图像评估建议专家</div>
    </div>
    <!--对话框-->
    <div ref="content" class="message-container">
      <template v-for="(message, index) in messages" :key="index">
        <!--时间-->
          <div class="system-message">{{message.time}}</div>
        <!--自己-->
        <div v-if="message.role=='user'" class="chat-bubble left">
          <!-- 消息 -->
          <span class="chat-bubble-right">
     		  <div class="chat-text">{{message.content}}</div>
            <img v-if="message.picture!=null" :src="message.picture" style="height: 200px;">
          </span>
          <span class="triangle-top-right"></span>
          <!-- 头像 -->
           <img :src="info" class="user-avatar">
        </div>
        <!--对方-->
        <div v-else class="chat-bubble right">
          <!-- 头像 -->
           <img src="https://graphcrafter.oss-cn-beijing.aliyuncs.com/1/06012024191642.jpg" class="user-avatar">
          <!-- 消息 -->
          <span class="triangle-top-left" :class="{ 'change-border': isLeftBubbleHover }"></span>
           <span class="chat-bubble-left">
<!--       <span class="chat-bubble-left" @mouseover="changeLeftArrowColor(true)" @mouseout="changeLeftArrowColor(false)"> -->
             <div class="chat-text">{{message.content}}</div>
     	     </span>
        </div>

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

export default {
  data(){
    return{
      isLeftBubbleHover: false,
      selectMessageIndex:0,
      showMenu: true,
      menuX: -100,
      menuY: -100,
      fileList:[],
    }
  },
  emits: ['close'],
  methods: {
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
    }
  },
  setup() {
    const text=ref("");
    let messages=ref([]);
    let img_url=ref("");
    let info=ref();
    axios.post("/api/get_info",{
      user_id:store.state.user_id
    }).then(function (response) {
      info.value=response.data["info"];
    }).catch(function (error) {
      console.log(error);
    });
    axios.get(`/api/getmsg/${store.state.user_id}`).then(function (response) {
      messages.value=response.data["data"];
      console.log(messages);
    }).catch(function (error) {
      console.log(error);
    });

    const file = ref(null);
    // 清空消息，删库
    async function clearMsg(){
      axios.get(`/clear_history/${store.state.user_id}`).then(function (response) {
        messages.value=[];
        console.log(response);
      }).catch(function (error) {
        console.log(error);
      });
    }
    // 发送消息
    async function sendMsg(){
      const newMsg={
        content:text.value,
        picture:img_url.value,
        time: formatDateTime(new Date()),
        role:"user"
      };
      messages.value.push(newMsg);
      text.value='';
      axios.post("/gpt",{
        user_id:store.state.user_id,
        question:newMsg.content,
        img_url:img_url.value,
        time: formatDateTime(new Date()),
      }).then(function (response) {
        // 重新获取消息
        axios.get(`/api/getmsg/${store.state.user_id}`).then(function (response) {
          messages.value = response.data["data"];
          console.log(response);
        }).catch(function (error) {
          console.log(error);
        });
        console.log(response);
      }).catch(function (error) {
        console.log(error);
      });
    }


    onMounted(() => {

    });

    return {
      text,
      messages,
      sendMsg,
      file,
      img_url,
      clearMsg,
      info
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

.chat-bubble {
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
  padding: 10px;
  border-radius: 5px;
  background-color: #fdfdfe;
  color: black;
}

.chat-bubble .chat-bubble-left:hover{
  background-color: #ebebeb;
}
.chat-bubble-right {
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
  border-top: 1px solid #e9eaec;
  border-bottom: 1px solid #e9eaec;
  height: 540px;
  overflow-y: scroll;
  background-color: #f4f5f7;
  /*border-radius: 8px;*/
  padding: 8px;

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