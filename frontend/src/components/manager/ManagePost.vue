<template>
<div>
<!--    <div class="top-bar">-->
<!--        <el-button :span="1" >搜索</el-button>-->
<!--    </div>-->
    <el-col :span="23" class="data-table">
        <el-table :data="tableData.slice((currentPage - 1)* pagesize, currentPage * pagesize)" @sort-change="handleSort" border style="width: 100%">
            <el-table-column label="帖子ID" width="100px" prop="id" sortable fixed>
              <template v-slot:default="scope">
                <span>{{ scope.row.id }}</span>
              </template>
            </el-table-column>
          <el-table-column label="用户ID" width="100px" prop="author_id" sortable fixed>
            <template v-slot:default="scope">
              <span>{{ scope.row.author_id }}</span>
            </template>
          </el-table-column>

          <el-table-column label="标题" width="200px" fixed>
            <template v-slot:default="scope">
              <span>{{ scope.row.title }}</span>
            </template>
          </el-table-column>
          <el-table-column label="内容" width="250px" fixed>
            <template v-slot:default="scope">
              <span>{{ scope.row.content }}</span>
            </template>
          </el-table-column>
            <el-table-column label="图片" width="150px" fixed>
              <template v-slot="scope">
                <div>
                  <el-popover
                      trigger="hover"
                      placement="top"
                      width="auto"
                  >
                    <template #reference>
                      <div v-for="(pic, index) in scope.row.pics" :key="index">
                        <img v-if="pic" :src="pic" style="height: 50px" :alt="'Image thumbnail ' + index" />
                      </div>
                    </template>
                    <div v-for="(pic, index) in scope.row.pics" :key="index">
                      <img v-if="pic" :src="pic" style="width: 250px" :alt="'Image ' + index" />
                    </div>
                  </el-popover>
                </div>
              </template>
            </el-table-column>

            <el-table-column label="发帖时间" width="210px" prop="date" sortable>
                <template v-slot:default="scope">
                    <span style="margin-left: 10px">{{ scope.row.date }}</span>
                </template>
            </el-table-column>
          <el-table-column label="状态" width="100px" fixed>
            <template v-slot:default="scope">
              <el-tag v-if="!scope.row.status" type="success"  plain>Normal</el-tag>
              <el-tag v-else type="danger" plain>Disable</el-tag>
            </template>
          </el-table-column>
            <el-table-column label="操作" width="177px;" fixed="right">
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

<script>
import axios from "axios";

export default {
    name: 'managePost',
    data() {
        return {
            currentPage: 1,
            pagesize: 5,
            tableData: [],
            userName: '',
            dialogVisible: false,
            imgDialogVisible: false,
        }
    },
    mounted() {
        if (window.localStorage.getItem('userType') === 'admin') {//待改
            this.$message.error("你没有管理员权限访问后台，即将跳转到登录页面")
            //this.$router.push('/login')
        } else {
            this.userName = window.localStorage.getItem('userName');
            axios({
                method: 'get',
                url: '/api/get-all-post',
            }).then((response) => {
              this.$message.success('加载帖子数据成功');
              this.tableData = response.data.dataList;
              console.log(this.tableData);
            }).catch((error) => {
              console.log(error);
            })
        }
    },
    methods: {
      handleSort({ column, prop, order }) {
        this.tableData.sort((a, b) => {
          // 对日期单独处理
          if(typeof a[prop] === 'string'){
            const isoDateString = this.convertToIsoDateString(a[prop]);
            const valueA = new Date(isoDateString);
            const isoDateString2 = this.convertToIsoDateString(b[prop]);
            const valueB = new Date(isoDateString2);
            if (order === 'ascending') {
              return valueA - valueB;
            } else if (order === 'descending') {
              return valueB - valueA;
            }
          }
          else{
            const valueA = a[prop];
            const valueB = b[prop];
            console.log(valueA,valueB);
            if (order === 'ascending') {
              return valueA > valueB ? 1 : -1;
            } else if (order === 'descending') {
              return valueA < valueB ? 1 : -1;
            }
          }

          return 0;
        });
      },

      convertToIsoDateString(dateString) {
        const [datePart, timePart] = dateString.split(' ');
        const [year, month, day] = datePart.match(/\d+/g);
        const [hour, minute, second] = timePart.match(/\d+/g);
        return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}T${hour.padStart(2, '0')}:${minute.padStart(2, '0')}:${second.padStart(2, '0')}`;
      },

        // 初始页currentPage、初始每页数据数pagesize和数据data
        handleSizeChange: function (size) {
            this.pagesize = size;
            console.log(this.pagesize); //每页下拉显示数据
        },
        handleCurrentChange: function (currentPage) {
            this.currentPage = currentPage;
            console.log(this.currentPage); //点击第几页
        },
        updatePostStatus(post_id){
          axios({
            method: 'post',
            url: `/api/update-post-status/${post_id}`
          }).then(function (response) {
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
        }
    }
}
</script>

<style scoped>
.data-table {
    margin-top: 20px;
}
</style>