import { reactive, onMounted, onUnmounted } from "vue";
import { io } from "socket.io-client";

export type Message = {
  type: string;
  id: number;
  user: User;
  content: string;
  time:string;
  show_time:boolean
}

export type User = {
  id: number;
  name: string;
  avatar: string;
}

export type Chat = {
  id: number;
  sender: User;
  receiver: User;
  unread_sender: boolean;
  unread_receiver: boolean;
  last_time: Date;
  messages: Message[];
}

type Information = {
  id: string;
  message: Message;
  roomUsers: string[];
}

export type SocketState = {
  connected: boolean,
  id: string,
  chat_id: string,
  messages: Message[],
  users:string[],
}

export function formatDateTime(date: Date): string {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1);
  const day = String(date.getDate());
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');
  const seconds = String(date.getSeconds()).padStart(2, '0');

  return `${year}年${month}月${day}日 ${hours}:${minutes}:${seconds}`;
}

export function useSocket(url: string, chat_id: string, prevMessages:Message[]) {
  const socketState: SocketState = reactive({
    connected: false,
    id: "",
    chat_id: chat_id ? chat_id : "",
    messages: prevMessages,
    users: [],
  })
  const socket = io(url);

  socket.on("connect", () => {
    console.log("connected!");
    socketState.connected = true;
    socketState.id = socket.id;
  });

  socket.on("disconnect", () => {
    socketState.connected = false;
    socketState.id = "";
    socketState.chat_id = "";
  });

  socket.on("message", (data: Information) => {
    console.log("receiving from server:",data);
    const message: Message = data.message;
    if(message.type !== 'system'){
      message.type = data.id === socketState.id ? 'source' : 'destination';
    }
    socketState.messages.push(message);
  });

  socket.on("connect_error", (err:Error) =>{
    const message: Message = {type:'system',id:0,User: {id:0,name:"",avatar:""},content:err.message,time:formatDateTime(new Date())};
    socketState.messages.push(message);
  })

  onMounted(() => socket.connect());
  onUnmounted(() => socket.disconnect());

  return { socketState, socket };

}

