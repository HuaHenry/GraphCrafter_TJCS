<template>

  <div class="custom-box">
    <!--顶栏-->
    <div class="header">
      <div class="room-info">{{ otherside.name }}</div>
    </div>
    <!--对话框-->
    <div ref="content" class="message-container">
      <template v-for="(message, index) in socketState.messages" :key="index">
        <!--时间-->
        <div v-if="message.show_time">
          <div class="system-message">{{message.time}}</div>
        </div>
        <!--自己-->
        <div v-if="message.user.id===$props.user.id" class="chat-bubble left">
          <!-- 消息 -->
          <span class="chat-bubble-right">
     		  <div class="chat-text" @contextmenu.prevent="showContextMenu($event, index)">{{message.content}}</div>
          <!--删除-->
          <div v-if="showMenu" class="context-menu" :style="{ top: menuY + 'px', left: menuX + 'px' }" @click="deleteMessage">
            删除
          </div>
          </span>
          <span class="triangle-top-right"></span>
          <!-- 头像 -->
          <img :src="$props.user.avatar" class="user-avatar">
        </div>
        <!--对方-->
        <div v-else class="chat-bubble right">
          <!-- 头像 -->
          <img :src="$props.otherside.avatar" class="user-avatar">
          <!-- 消息 -->
          <span class="triangle-top-left" :class="{ 'change-border': isLeftBubbleHover }"></span>
          <span class="chat-bubble-left" @mouseover="changeLeftArrowColor(true)" @mouseout="changeLeftArrowColor(false)">
          <div class="chat-text" @contextmenu.prevent="showContextMenu($event, index)">{{message.content}}</div>
            <!--删除-->
          <div v-if="showMenu" class="context-menu" :style="{ top: menuY + 'px', left: menuX + 'px' }" @click="deleteMessage">
            删除
          </div>
     	    </span>
        </div>

      </template>
    </div>
    <!--发送框-->
    <div class="chat-footer">
      <input class="message-input" v-model.trim="text" autocomplete="off" />
      <button class="message-send-button" @click="sendMessage">发送</button>
    </div>
  </div>
</template>

<script lang="ts">
import Vue, { Ref, WatchOptions } from 'vue';
import { computed, watch, ref } from 'vue';
import { useSocket,formatDateTime } from '@/utils/socket';
import type {User,Chat,Message} from "@/utils/socket";
import axios from 'axios';

export default {
  name:"ChatWindow",
  props: {
    url: {type:String},
    user: {type:Object as () => User},
    otherside: {type:Object as () => User},
    chat: {type:Object as () => Chat},
  },
  data(){
    return{
      showMenu: true,
      menuX: -100,
      menuY: -100,
      selectMessageIndex:0,
      isLeftBubbleHover: false,

    }
  },
  emits: ['close'],
  methods: {
    showContextMenu(event,index) {
      event.preventDefault();
      this.menuX = event.pageX;
      this.menuY = event.pageY;
      this.showMenu = true;
      this.selectMessageIndex = index;

      // 点击其他地方时隐藏菜单
      document.addEventListener('click', this.hideContextMenuOnce);
    },
    hideContextMenuOnce(event) {
      // 检查点击的位置是否在右键菜单之外
      const contextMenu = document.querySelector('.context-menu');
      if (contextMenu && !contextMenu.contains(event.target)) {
        this.showMenu = false;
        document.removeEventListener('click', this.hideContextMenuOnce);
      }
    },
    deleteMessage() {
      let index = this.selectMessageIndex;
      //从数据库中删掉消息
      axios.post('/api/delete_message', { message_id:this.socketState.messages[index].id })
          .then(response => {
            console.log('Message deleted successfully');
          })
          .catch(error => {
            console.error('Error:', error);
          });
      this.socketState.messages.splice(index, 1);//从页面中删掉消息
      this.showMenu = false; // 隐藏右键菜单
    },
    changeLeftArrowColor(value) {
      this.isLeftBubbleHover = value;
    }
  },
  setup(props, { emit }) {
    const { socketState, socket } = useSocket(props.url, props.chat.id, props.chat.messages);
    const prevMessageLength = socketState.messages.length;
    const text: Ref<string> = ref("");
    const content: Ref<HTMLElement | null> = ref(null);
    const isConnected = computed<boolean>(() => socketState.connected);
    var curTimeFirstMsg=true;
    // 监测变量
    watch(isConnected, (current: boolean) => {
      if (current) {
        socket.emit("join", { chat_id: socketState.chat_id });
      }
    });

    watch(() => props.chat.messages, (newValue: any) => {
      socketState.messages = newValue;
    });

    watch(() => props.chat.id, (newValue: any) => {
      socketState.chat_id = props.chat.id;
      socketState.messages = props.chat.messages;
      socket.emit("join", { chat_id: socketState.chat_id });
    });

    function checkTimeDiff(){
      const lastMessageTimeString = props.chat?.messages.length > 0 ? props.chat.messages[props.chat.messages.length - 1].time : null;
      const now = new Date();
      if (lastMessageTimeString) {
        // 将类似 '2024年5月29日 21:42:15' 的字符串转换为 '2024-05-29T21:42:15'
        const dateTimeParts = lastMessageTimeString.split(' ');
        const datePart = dateTimeParts[0].replace(/[年月]/g, '-').replace('日', '');
        const dateSegments = datePart.split('-');
        const year = dateSegments[0];
        const month = dateSegments[1].padStart(2, '0'); // 补齐月份
        const day = dateSegments[2].padStart(2, '0'); // 补齐日期
        const formattedDatePart = `${year}-${month}-${day}`;
        const timePart = dateTimeParts[1];
        const isoDateTimeString = `${formattedDatePart}T${timePart}`;

        const lastMessageTime = new Date(isoDateTimeString);
        console.log(lastMessageTimeString);
        if (!isNaN(lastMessageTime.getTime())) {
          const diff = now - lastMessageTime;
          const diffInHours = diff / (1000 * 60 * 60);
          console.log(lastMessageTime.getTime());
          console.log(diffInHours);
          if (diffInHours > 0.5) { // 半小时
            return true;
          } else {
            return false;
          }
        }
      }
      return false;
    }
    async function sendMessage(e: Event): void {
      if (props.chat?.messages.length === 0){
        curTimeFirstMsg = true;
      }
      else if(checkTimeDiff()===false){
        curTimeFirstMsg = false;
      }
      e.preventDefault();
      if (text.value === "") return;
      let msg: Message = {
        type: "text",
        id: 0,
        user: props.user,
        content: text.value,
        time: formatDateTime(new Date()),
        show_time:curTimeFirstMsg,
      };

      let new_data ={ chat_id: props.chat.id, message: msg };

      // 后端存储
      let msg_id=0;
      await axios.post('/api/save_message', new_data)
          .then(function(response) {
            msg_id = response.data['message_id'];
          })
          .catch(function(error) {
            console.error('Error:', error);
          });
      // 实时通信
      new_data.message.id = msg_id;
      socket.emit("message", new_data);
      if (content.value) {
        (content.value as HTMLElement).scrollTop = (content.value as HTMLElement).scrollHeight;
      }
      text.value = "";
    }

    function close(): void {
      socket.disconnect();
      // socket.emits('close', props.room);
    }

    return {
      socketState,
      text,
      content,
      prevMessageLength,
      sendMessage
    };
  }
};

</script>

<style>
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
  border-radius: 0 10px 10px 0;
  background-color:#fbfcff;
  color: #fff;
  border-left: 1px solid #e9eaec;
  width: 100%;

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
  height: 360px;
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
  height: 100px;
}

.message-input {
  width: 85%;
  align-self: flex-start;
  height: 40%;
  background-color: #fbfcff;
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