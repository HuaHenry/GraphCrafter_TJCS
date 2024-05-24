<template>
<div class='manageUser-main'>
    <el-col :span="23" class="data-table">
      <el-table :data="paginatedData" border style="width: 100%" @sort-change="handleSort">
        <el-table-column label="用户ID" width="100px" prop="id" sortable fixed>
          <template #default="scope">
            <span>{{ scope.row.id }}</span>
          </template>
        </el-table-column>
        <el-table-column label="用户名" width="150px">
          <template #default="scope">
            <el-popover trigger="hover" placement="top">
              <template #default>
                <div class="user-info">
                  <img :src="scope.row.userProfile" class="user-avator" alt style="height: 100px;" />
                  <div class="user-info-cont">
                    <p>名称: {{ scope.row.name }}</p>
                    <p>密码: {{ scope.row.password }}</p>
                    <p>介绍: {{ scope.row.description }}</p>
                  </div>
                </div>
              </template>
              <template #reference>
                <div class="name-wrapper">
                  <span style="color:rgb(64,158,255);">{{ scope.row.name }}</span>
                </div>
              </template>
            </el-popover>
          </template>
        </el-table-column>
        <el-table-column label="密码" width="180px">
          <template #default="scope">
            <span>{{ scope.row.password }}</span>
          </template>
        </el-table-column>
        <el-table-column label="性别" width="100px">
          <template #default="scope">
            <span v-if="!scope.row.sex">女</span>
            <span v-else>男</span>
          </template>
        </el-table-column>
        <el-table-column label="年龄" width="100px">
          <template #default="scope">
            <span>{{ scope.row.age }}</span>
          </template>
        </el-table-column>
        <el-table-column label="头像" width="80px">
          <template #default="scope">
            <img :src="scope.row.avatar" style="height: 50px; width:50px; border-radius: 50px" />
          </template>
        </el-table-column>
        <el-table-column label="邮箱" width="200px">
          <template #default="scope">
            <span>{{ scope.row.email }}</span>
          </template>
        </el-table-column>
        <el-table-column label="等级" width="100px">
          <template #default="scope">
            <span v-if="scope.row.senior" >高级</span>
            <span v-else style="color:#b6b4b3;">普通</span>
          </template>
        </el-table-column>
        <el-table-column label="状态" width="100px;">
          <template #default="scope">
            <el-tag v-if="!scope.row.status" type="success"  plain>Normal</el-tag>
            <el-tag v-else type="danger" plain>Disable</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" :span="1">
          <template v-slot:default="scope">
            <el-button size="mini" type="primary" @click="handleAble(scope.$index, scope.row)" :disabled="!scope.row.status">解禁</el-button>
            <el-button slot="reference" size="mini" type="danger"  @click="handleDisable(scope.$index, scope.row)" :disabled="scope.row.status" style="margin-left: 5px;">禁用</el-button>
          </template>
        </el-table-column>
      </el-table>
        <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage" :page-sizes="[5, 10]" :page-size="pagesize" background layout="total, sizes, prev, pager, next, jumper" :total="tableData.length" style="padding-top:20px">
        </el-pagination>
    </el-col>
</div>
</template>

<style scoped>
.data-table {
    margin-top: 20px;
}
</style>

<script>
import axios from "axios";

export default {
    name: 'manageUser',
    mounted() {
        if (window.localStorage.getItem('userType') === 'admin') {//待改
            this.$message.error("你没有管理员权限访问后台，即将跳转到登录页面")
            // this.$router.push('/login')
        } else {
            axios({
                method: 'get',
                url: '/api/get-all-user'
            }).then((response) => {
                this.$message.success('加载用户数据成功');
                this.tableData = response.data.userList;
                console.log(this.tableData);
            }).catch(function (error) {
                console.log(error);
            })
        }
    },
    data() {
        return {
            currentUserID: '',
            prevUserName: '',
            currentPage: 1,
            pagesize: 5,
            dialogVisible: false,
            tableData: [],
        }
    },
    computed:{
      paginatedData(){
        return this.tableData.slice((this.currentPage - 1) * this.pagesize, this.currentPage * this.pagesize);
      }
    },
    methods: {
      updatePostStatus(user_id){
        axios({
          method: 'post',
          url: `/api/update-user-status/${user_id}`
        }).then((response) =>  {
          this.$message.success('更新数据成功');
        }).catch(function (error) {
          console.log(error);
        })
      },
      handleAble(index, row) {
        row.status = false;
        this.updatePostStatus(row.id);
      },

      handleDisable(index, row) {
        row.status = true;
        this.updatePostStatus(row.id);
      },
        handleSizeChange: function (size) {
            this.pagesize = size;
            console.log(this.pagesize) //每页下拉显示数据
        },
        handleCurrentChange: function (currentPage) {
            this.currentPage = currentPage;
            console.log(this.currentPage) //点击第几页
        },
      handleSort({ column, prop, order }) {
        this.tableData.sort((a, b) => {
          const valueA = a[prop];
          const valueB = b[prop];
          console.log(valueA,valueB);
          if (order === 'ascending') {
            return valueA > valueB ? 1 : -1;
          } else if (order === 'descending') {
            return valueA < valueB ? 1 : -1;
          }
        });
        return 0;
      }
    }
}
</script>
