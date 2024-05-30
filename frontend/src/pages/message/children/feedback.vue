<template>
  <div class="chat-module-container">
    <div class="chat-body-container">
      <div class="chat-sidebar-header">反馈消息</div>
      <!--消息侧边栏-->
      <div class="chat-sidebar-container">
        <div
            v-for="(chat, index) in chatList"
            :key="index"
            :class="['chat-sidebar-bubble', { 'active-chat': currentChat.id === chat.id }]"
            @click="changeChat(index)"
        >
          <div v-if="chat.sender.id !== user.id" class="user-container">
            <img :src="chat.sender.avatar" alt="Message Icon" class="user-avatar" />
            <div  class="user-info">
              <div class="user-name">{{ chat.sender.name }}</div>
              <div class="user-last-msg">{{ chat.messages[chat.messages.length - 1].content }}</div>
            </div>
          </div>
          <div v-else class="user-container">
            <img :src="chat.receiver.avatar" alt="Message Icon" class="user-avatar" />
            <div class="user-info">
              <div class="user-name">{{ chat.receiver.name }}</div>
              <div class="user-last-msg">{{ chat.messages[chat.messages.length - 1].content }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--聊天窗口-->
    <div class="chat-window-container">
      <ChatWindow v-if="ready & login" :url="server_url" :chat="currentChat" :user="user" :otherside="otherside"/>
    </div>
  </div>

</template>

<script lang="ts">
import axios from 'axios';
import ChatWindow from "./chatwindow.vue";
import store from "@/store/index";

export default{
  name:"feedback",
  components:{ChatWindow},

  data() {
    return {
      server_url: 'localhost:8080',
      ready: false,
      login: false,
      user: {id: 1, name: '加完班打麻药', avatar: ''},
      otherside: {id: 0, name: '', avatar: ''},
      chatList: [],
      currentChat: null,
    };
  },
  mounted(): void {
    this.checkLogin();
  },
  methods: {
    async checkLogin(): Promise<void> {
      if (!store.state.isLoggedIn){
        this.$message.error("请先登录");
        this.$router.push("/login");
      }
      this.login = true;
      this.user.id = store.state.user_id;
      const response = await axios.get(`/api/get-user-info/${this.user.id}`);
      this.user.name = response.data.name;
      this.user.avatar = response.data.avatar;
      console.log(response.data);
      await this.fetchFeedbackList();
    },

    async fetchFeedbackList(): Promise<void> {
      try {
        const response = await axios.get(`/api/chat-feedback/${this.user.id}`);
        this.chatList = response.data;
        if (this.user.name === this.chatList[0].sender.name) {
          this.user = this.chatList[0].sender;
          this.otherside = this.chatList[0].receiver;
        } else {
          this.user = this.chatList[0].receiver;
          this.otherside = this.chatList[0].sender;
        }
        this.currentChat = this.chatList[0];
        this.ready = true;
      } catch (error) {
        console.error('Error fetching messages:', error);
      }
    },

    // Change Chat
    changeChat(chatIndex: number): void {
      if (this.chatList[chatIndex]) {
        if (this.user.name === this.chatList[chatIndex].sender.name) {
          this.user = this.chatList[chatIndex].sender;
          this.otherside = this.chatList[chatIndex].receiver;
        } else {
          this.user = this.chatList[chatIndex].receiver;
          this.otherside = this.chatList[chatIndex].sender;
        }
        this.currentChat = this.chatList[chatIndex];
        console.log('curChat:', this.currentChat);
      }
    },
  }
}
</script>

<style scoped>
.chat-module-container{
  background-color:#ffffff ;
  width: 900px;
  height: 80%;
  display: flex;
  flex-direction:row;
  align-items: flex-start;
  justify-content: center;
  border-radius: 10px;
  border: 1px solid #e9eaec;
}
.chat-header-container {
  display: flex;
  justify-content: space-around;
  align-items: center;
  height: 10%;
}
.room-info {
  width: 80%;
  font-size: 1.25rem;
  margin: 10px;
}
.chat-sidebar-header{
  padding: 12px 10px 10px 15px;
  height: 48px;
  font-size: 16px;
  text-align: left;
  margin: 0 0 0 0;
  vertical-align: center;
  color:#666666;
  background: #fbfcff;
  border-bottom: 1px solid #e9eaec;
}
.chat-window-container{
  width: 700px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.chat-sidebar-container {
  width: 270px;
  background-color: #f5f5f5;
}
.chat-sidebar-bubble {
  /* 设置侧边消息气泡的样式 */
  display: flex;
  align-content: flex-start;
  padding: 10px;
  background: #fff;
}
.active-chat{
  background: #e4e5e6;
}
.chat-sidebar-bubble:hover{
  background: #e4e5e6;
}
.chat-sidebar-bubble .user-avatar{
  width: 50px;
  height: 50px;
  border-radius: 50px;
  margin:2px;
}
.user-name{
  margin: 0 0 0 5px;
  font-size: 16px;
  text-align: left;
}
.user-last-msg{
  margin: 2px 0 0 5px;
  font-size: 14px;
  text-align: left;
  align-items: center;
  justify-content: center;
  color: #a7a7a7;
}
</style>