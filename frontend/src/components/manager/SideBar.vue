<template>
<div class="sidebar">
  <el-menu class="sidebar-el-menu" background-color="#324157" unique-opened>
    <el-menu-item
        v-for="item in items"
        :key="item.index"
        :index="item.index"
        :style="{ color: item.index === activatedIndex ? 'white' : '#aaaaaa' }"
        @click="handleClick(item.index)"
    >
      <el-icon size="25px" >
        <component :is="getIconComponent(item.icon)" />
      </el-icon>
      <span style="margin-left: 8px">{{ item.title }}</span>
    </el-menu-item>
  </el-menu>
</div>
</template>

<style>
.sidebar {
    display: block;
    position: fixed;
    left: 0;
    top: 62px;
    bottom: 0;
    overflow-y: scroll;
    text-align: center;
}

.sidebar::-webkit-scrollbar {
    width: 0;
}

.sidebar-el-menu:not(.el-menu--collapse) {
    width: 250px;
}

.sidebar>ul {
    height: 100%;
}
</style>

<script>
import { House,User,ChatDotSquare,Tickets,Menu} from '@element-plus/icons-vue';

export default {
    name: 'sidebar',
    data() {
        return {
            activatedIndex: '/manage',
            items: [{
                    icon: 'House',
                    index: '/manage',
                    title: '系统首页'
                },
                {
                    icon: 'User',
                    index: '/manageUser',
                    title: '用户管理'
                },
                {
                    icon: 'Post',
                    index: '/managePost',
                    title: '发帖管理'
                },
                {
                    icon: 'Feedback',
                    index: '/manageFeedback',
                    title: '问题反馈'
                }
            ]
        };
    },
    methods: {
        handleClick(index) {
            this.activatedIndex = index
            this.$emit('func', this.activatedIndex)
        },
      getIconComponent(iconName) {
        // 根据 iconName 返回相应的图标组件
        switch (iconName) {
          case 'House':
            return House;
          case 'User':
            return User;
          case 'Menu':
            return Menu;
          case 'Post':
            return Tickets;
          case 'Feedback':
            return ChatDotSquare;
          default:
            return null;
      }
}
    }
};
</script>
