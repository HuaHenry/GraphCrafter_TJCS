import { createRouter, createWebHistory } from "vue-router";
// import Login from "@/pages/login.vue";
import Dashboard from "@/pages/dashboard/dashboard.vue";
import easy1 from "@/pages/edit/easy1.vue";
import Manage from "@/pages/manager/Manage.vue";
import conversation from "@/pages/gpt.vue";
import p2p from "@/pages/p2p.vue";
import Demo from "@/views/Demo.vue";
import Login from "@/components/Login.vue";
import Register from "@/components/Register.vue";
import SearchBoard from '@/pages/dashboard/searchboard.vue';
export const routes = [
 
  {
    name: "Demo",
    path: "/Demo",
    component: Demo,
  },
  {
    path: "/",
    redirect: "/Demo",
  },
  {
    name: "login",
    path: "/login",
    component: Login,
  },
  {
    name: "Register",
    path: "/Register",
    component: Register,
  },
  {
    name: "manager",
    path: "/manager",
    component: Manage,
  },
  {
    name: "index",
    path: "/index",
    component: () => import("@/pages/index.vue"),
    redirect: "/dashboard",
    children: [
      {
        name: "conversation",
        path: "/conversation",
        component: conversation,
      },
      {
        name: "p2p",
        path: "/p2p",
        component: p2p,
      },
      {
        name: "easy1",
        path: "/easy1",
        component: easy1,
      },
      {
        path: "/dashboard",
        component: Dashboard,
        name: "dashboard", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
      },
      {
        path: '/searchboard',
        name: 'SearchBoard',
        component: SearchBoard,
        props: route => ({ query: route.query.query })
      },
      {
        path: "/followTrend",
        component: () => import("@/pages/follow-trend/follow-trend.vue"),
        name: "followTrend", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
      },
      {
        path: "/notice",
        component: () => import("@/pages/message/index.vue"),
        name: "notice", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
        redirect: "/message",
        children: [
          {
            path: "/message",
            component: () => import("@/pages/message/children/message.vue"),
            name: "message", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
          },
          {
            path: "/feedback",
            component: () => import("@/pages/message/children/feedback.vue"),
            name: "feedback",
          },
          {
            path: "/agreeCollection",
            component: () => import("@/pages/message/children/agree-collection.vue"),
            name: "agreeCollection", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
          },
          {
            path: "/follower",
            component: () => import("@/pages/message/children/follower.vue"),
            name: "follower", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
          },
          {
            path: "/comment",
            component: () => import("@/pages/message/children/comment.vue"),
            name: "comment", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
          },
          {
            path: "/chat",
            component: () => import("@/pages/chat/index.vue"),
            name: "chat", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
          },
        ],
      },
      {
        path: "/user",
        component: () => import("@/pages/user/index.vue"),
        name: "user", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
        redirect: "/collection",
        children: [
          {
            path: "/note",
            component: () => import("@/pages/user/children/note.vue"),
            name: "note", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
          },
          {
            path: "/drafts",
            component: () => import("@/pages/user/children/agree.vue"),
            name: "drafts", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
          },
          {
            path: "/collection",
            component: () => import("@/pages/user/children/collection.vue"),
            name: "collection", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
          },
        ],
      },
      {
        path: "/editprofile",
        component: () => import("@/pages/user/editprofile.vue"),
        name: "editprofile", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
      },
      {
        path: "/fanspage",
        component: () => import("@/pages/user/fanspage.vue"),
        name: "fanspage", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
      },
      {
        path: "/followpage",
        component: () => import("@/pages/user/followpage.vue"),
        name: "followpage", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
      },
      {
        path: "/other",
        component: () => import("@/pages/other.vue"),
        name: "other", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
      },
      {
        path: "/push",
        component: () => import("@/pages/push/index.vue"),
        name: "push", // 用于 keep-alive, 必须与SFC自动推导或者显示声明的组件name一致
      },
    ],
  },
  {
    name: "main",
    path: "/main",
    component: () => import("@/pages/main.vue"),
  },
  {
    name: "del_draft",
    path: "/del_draft",
    component: () => import("@/pages/del_draft.vue"),
  },
];
const router = createRouter({
  scrollBehavior: () => ({ left: 0, top: 0 }),
  history: createWebHistory(),
  routes,
});
// router.beforeEach((to, from, next) => {
router.beforeEach((next) => {
  next;
});
export default router;
