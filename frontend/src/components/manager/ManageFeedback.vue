<template>
<div>
    <el-button type="danger" icon="el-icon-s-promotion" @click="quit()">退出账号</el-button>
</div>
</template>

<script>

export default {
    name: 'manageFeedback',
    methods: {
        quit() {
            window.localStorage.setItem('userName', '')
            window.localStorage.setItem('userType', 'null')
            this.$router.push('/login')
            this.$message.success("退出当前账号")
        }
    },
    created() {
        if (window.localStorage.getItem('userType') !== 'admin') {
            this.$message.error("你没有管理员权限访问后台，即将跳转到登录页面")
            //this.$router.push('/login')
        }
    }
}
</script>
