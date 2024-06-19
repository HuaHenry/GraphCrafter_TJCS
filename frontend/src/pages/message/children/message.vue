<template>
  <div class="chat-module-container">
    <div class="chat-body-container">
      <div class="chat-sidebar-header">近期消息</div>
      <!--消息侧边栏-->
      <div class="chat-sidebar-container">
        <div
            v-for="(chat, index) in chatList"
            :key="index"
            :class="['chat-sidebar-bubble', { 'active-chat': currentChat.id === chat.id }]"
            @click="changeChat(index)"
        >
          <div v-if="chat.sender.id !== user.id" class="user-container" @contextmenu.prevent="showContextMenu($event, index)">
            <img :src="chat.sender.avatar" alt="Message Icon" class="user-avatar" />
            <div  class="user-info">
              <div class="user-name">{{ chat.sender.name }}</div>
              <div class="user-last-msg">{{ chat.messages[chat.messages.length - 1]?chat.messages[chat.messages.length - 1].content :" " }}</div>
            </div>
          </div>
          <div v-else class="user-container" @contextmenu.prevent="showContextMenu($event, index)">
            <img :src="chat.receiver.avatar" alt="Message Icon" class="user-avatar" />
            <div class="user-info">
              <div class="user-name">{{ chat.receiver.name }}</div>
              <div class="user-last-msg">{{ chat.messages[chat.messages.length - 1]?chat.messages[chat.messages.length - 1].content :" " }}</div>
            </div>
          </div>
          <!--删除-->
          <div v-if="showMenu" class="chat-context-menu" :style="{ top: menuY + 'px', left: menuX + 'px' }" @click="deleteChat">
            删除会话
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
import store from "../../../store/index";
import {onBeforeUnmount} from "vue";

export default{
  name:"ChatRoom",
  components:{ChatWindow},

  data() {
    return {
      // server_url: 'localhost:8080',
      server_url: 'http://123.60.90.34:3306',
      ready: false,
      login: false,
      user: {id: 1, name: '加完班打麻药', avatar: ''},
      otherside: {id: 0, name: '', avatar: ''},
      chatList: [],
      currentChat: null, //当前显示的会话

      showMenu: true,
      menuX: 0,
      menuY: 0,
      selectChatIndex:0,//要进行操作的会话
    };
  },
  setup(){
    const beforeLeave = (to, from, next) => {
      console.log('即将离开消息界面，执行检查对话操作');
      axios.post(`/api/check_empty_chat`);
      next();
    };
    onBeforeUnmount(() => {
      axios.post(`/api/check_empty_chat`);
    });
  },
  mounted(): void {
    this.checkLogin();
  },
  methods: {
    async checkLogin(): Promise<void> {
      if (store.state.isLoggedIn){
        this.user.id = store.state.user_id;
        const response = await axios.get(`/api/get-user-info/${this.user.id}`);
        this.user.name = response.data.name;
        this.user.avatar = response.data.avatar;
        this.login = true;
        await this.fetchChatList();
      }
      else{
        this.$message.error("请先登录");
        this.$router.push("/login");
      }
    },

    async fetchChatList(): Promise<void> {
      try {
        const response = await axios.get(`/api/chat/${this.user.id}`);
        // const response = await axios.get(`/api/chat/1`);
        this.chatList = response.data;
        console.log(this.chatList);
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

    showContextMenu(event,index) {
      event.preventDefault();
      this.menuX = event.pageX;
      this.menuY = event.pageY;
      this.showMenu = true;
      this.selectChatIndex = index;

      // 点击其他地方时隐藏菜单
      document.addEventListener('click', this.hideContextMenuOnce);
    },
    hideContextMenuOnce(event) {
      // 检查点击的位置是否在右键菜单之外
      const contextMenu = document.querySelector('.chat-context-menu');
      if (contextMenu && !contextMenu.contains(event.target)) {
        this.showMenu = false;
        document.removeEventListener('click', this.hideContextMenuOnce);
      }
    },
    deleteChat() {
      let index = this.selectChatIndex;
      //从数据库中删掉消息
      axios.delete(`/api/delete_chat/${ this.chatList[index].id }`)
          .then(response => {
            console.log('Chat deleted successfully');
          })
          .catch(error => {
            console.error('Error:', error);
          });
      this.chatList.splice(index, 1);//从页面中删掉会话
      this.showMenu = false; // 隐藏右键菜单
    },
  }
}
</script>

<style scoped>
.chat-module-container{
  background-color:#ffffff ;
  width: 820px;
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
  width: 250px;
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
  /*background: #efefef;*/
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

.chat-context-menu {
  position: absolute;
  background-color: #fff;
  border: 1px solid #ccc;
  color: #666666;
  padding: 5px 25px;
  font-size: 14px;
  box-shadow: 0 0 5px 2px rgba(0, 0, 0, 0.02);
  z-index: 3;
}
.chat-context-menu:hover{
  background-color: #f5f4f4;
}
</style>