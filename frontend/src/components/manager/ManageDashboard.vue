<template>
<div>
    <el-row :gutter="20">
        <el-col :span="23">
            <el-row :gutter="20" class="mgb20">
                <el-col :span="8">
                    <el-card shadow="hover" :body-style="{padding: '0px'}">
                        <div class="grid-content grid-con-1">
                            <el-avatar class="icon" src="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png"></el-avatar>
                            <div class="grid-cont-right">
                                <div class="grid-num">{{ name }}</div>
                                <div>管理员账号</div>
                            </div>
                        </div>
                    </el-card>
                </el-col>
                <el-col :span="8">
                    <el-card shadow="hover" :body-style="{padding: '0px'}">
                        <div class="grid-content grid-con-1">
                            <i class="el-icon-lx-notice grid-con-icon"></i>
                            <div class="grid-cont-right">
                                <div class="grid-num">{{ userCount }}</div>
                                <div>注册用户</div>
                            </div>
                        </div>
                    </el-card>
                </el-col>
                <el-col :span="8">
                    <el-card shadow="hover" :body-style="{padding: '0px'}">
                        <div class="grid-content grid-con-2">
                            <i class="el-icon-lx-goods grid-con-icon"></i>
                            <div class="grid-cont-right">
                                <div class="grid-num" style="color:#72d476;">{{ postCount }}</div>
                                <div >发布帖子</div>
                            </div>
                        </div>
                    </el-card>
                </el-col>
            </el-row>
            <el-card shadow="hover" style="height:403px;">
                <div slot="header" class="clearfix">
                    <span >待办事项</span>
<!--                    <el-button style="float: right; padding: 3px 0" type="text">添加</el-button>-->
                </div>
                <el-table :show-header="false" :data="todoList" style="width:100%;">
                    <el-table-column width="40">
                      <template v-slot="scope">
                        <el-checkbox v-model="scope.row.status"></el-checkbox>
                      </template>
                    </el-table-column>
                    <el-table-column>
                      <template v-slot="scope">
                        <div
                            class="todo-item"
                            :class="{'todo-item-del': scope.row.status}"
                        >
                          {{ scope.row.title }}
                        </div>
                      </template>
                    </el-table-column>
                    <el-table-column width="60">
                        <template>
                            <i class="el-icon-edit"></i>
                            <i class="el-icon-delete"></i>
                        </template>
                    </el-table-column>
                </el-table>
            </el-card>
        </el-col>
    </el-row>
</div>
</template>

<script>
import axios from 'axios';
import qs from "qs";

export default {
    name: 'dashboard',
    data() {
        return {
            name: localStorage.getItem('userName'),
            userCount: 0,
            postCount: 0,
            todoList: [
                {
                    title: '浏览新发布的帖子',
                    status: false
                },
              {
                title: '浏览新收到的反馈',
                status: false
              },
                {
                    title: '处理3天内收到的反馈',
                    status: false
                },
                {
                    title: '解禁符合条件的内容',
                    status: false
                },
                {
                    title: '禁用违反网络安全法的帖子',
                    status: false
                },
                {
                    title: '解禁符合条件的用户',
                    status: true
                },
                {
                    title: '禁用违反网络安全法的用户',
                    status: true
                }
            ],
        };
    },
    computed: {
        role() {
            return this.name = 'admin';
        }
    },
    created() {
        if (window.localStorage.getItem('userType') === 'admin') {//待改
            console.error("你没有管理员权限访问后台，即将跳转到登录页面");
            // this.$router.push('/login');
        }
        else {
            axios({
            method: 'get',
            url: '/api/get-user-post-num',
            }).then((response) => {
                this.userCount = response.data.userNum;
                this.postCount = response.data.postNum;
            }).catch(function (error) {
                console.log(error);
            })
        }
    },
    methods: {
        changeDate() {
            const now = new Date().getTime();
            this.data.forEach((item, index) => {
                const date = new Date(now - (6 - index) * 86400000);
                item.name = `${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()}`;
            });
        }
    }
};
</script>

<style scoped>
    .icon {
        width: 60px;
        height: 60px;
        margin: 10px;
        margin-left: 30px;
    }

    .el-row {
        margin-bottom: 20px;
    }

    .grid-content {
        display: flex;
        align-items: center;
        height: 100px;
    }

    .grid-cont-right {
        flex: 1;
        text-align: center;
        font-size: 14px;
        color: #999;
    }

    .grid-num {
        font-size: 30px;
        font-weight: bold;
    }

    .grid-con-icon {
        font-size: 50px;
        width: 100px;
        height: 100px;
        text-align: center;
        line-height: 100px;
        color: #fff;
    }

    .grid-con-1 .grid-con-icon {
        background: rgb(45, 140, 240);
    }

    .grid-con-1 .grid-num {
        color: rgb(45, 140, 240);
    }

    .grid-con-2 .grid-con-icon {
        background: rgb(100, 213, 114);
    }

    .grid-con-2 .grid-num {
        color: rgb(45, 140, 240);
    }

    .grid-con-3 .grid-con-icon {
        background: rgb(242, 94, 67);
    }

    .grid-con-3 .grid-num {
        color: rgb(242, 94, 67);
    }

    .user-info {
        display: flex;
        align-items: center;
        padding-bottom: 20px;
        margin-bottom: 20px;
    }

    .user-avator {
        width: 120px;
        height: 120px;
        border-radius: 50%;
    }

    .user-info-cont {
        padding-left: 50px;
        flex: 1;
        font-size: 14px;
        color: #999;
    }

    .user-info-cont div:first-child {
        font-size: 30px;
        color: #222;
    }

    .user-info-list {
        font-size: 14px;
        color: #999;
        line-height: 25px;
    }

    .user-info-list span {
        margin-left: 70px;
    }

    .mgb20 {
        margin-bottom: 20px;
    }

    .todo-item {
        font-size: 14px;
    }

    .todo-item-del {
        text-decoration: line-through;
        color: #999;
    }

</style>
