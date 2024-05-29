<template>
  <div class="container">
    <h2>请选择图片</h2>
    <div class="upload_con">
        <el-form
            :rules="rules"
            ref="ruleF"
            :model="ruleForm"
        >
        <el-form-item>
        <el-upload
            :class="{uoloadSty:showBtnDealImg,disUoloadSty:noneBtnImg}"
            ref="upload"
            action=""
            list-type="picture-card"
            accept="image/*"

            :on-preview="handlePictureCardPreview"
            :on-remove="handleRemove"
            :on-change="upclick_click"
            :limit="5"
            :file-list="fileList"
            :auto-upload="false"
        >
          <i class="el-icon-plus"></i>
          <template #tip>
            <!-- <div style="font-size: 12px;color: #919191;">
              单次限制上传一张图片
            </div> -->
          </template>
        </el-upload>
        <el-dialog v-model="dialogVisible" style="line-height: 0;">
          <img style="width: 100%;height: 100%"  :src="dialogImageUrl" alt="" />
        </el-dialog>
      </el-form-item>
      </el-form>
    </div>
    <!-- <el-button id="upload">上传图片</el-button>
    <img id="uploadedImage" style="visibility:hidden" alt="Uploaded Image" /> -->
    <input v-model="ruleForm.name" type="text" id="title" name="title" placeholder="请输入标题"/>
    <textarea v-model="ruleForm.summary" id="description" name="description" placeholder="请输入内容..."></textarea>
    <el-button type="primary" @click="submitForm('ruleF')" id="submit_button">发布动态</el-button>
  </div>

  <div class="input_txt">
    <el-form-item>
        <!-- 标题和一段文字的摘要 -->
        
    </el-form-item>
  </div>
  
</template>

<style lang="less" scoped>
    .container {
    position: relative;
    top: 80px;
    flex: 1;
    padding: 30px;
    // left:20%;
    width:80%;
    height: 650px;
    border-radius: 40px;
    margin: 0 auto;
    // background-color:rgb(157,13,67);
    box-shadow: rgba(9, 30, 66, 0.25) 0px 4px 8px -2px, rgba(9, 30, 66, 0.08) 0px 0px 0px 1px;
    color:rgb(36, 36, 36);
    
    .upload_con{
        text-align: center;
        position:relative 

        .uoloadSty .el-upload--picture-card{
            width:110px;
            height:110px;
            line-height:110px;
        }

        .disUoloadSty .el-upload--picture-card{
            display:none;   /* 上传按钮隐藏 */
        }

        .files{
            width:100px;
            height:100px;
            display:none;
        }
    }

    #title{
        position: relative;
        top: 20px;
        width: 100%;
        font-size: 20px;
        font-weight: 500;
        border-radius: 13px;
        border: 1.5px solid rgb(255, 255, 255);
        padding-left: 15px;
        padding-top: 10px;  
        padding-bottom: 10px;
        padding-right: 20px;
        background-color: rgb(240, 240, 240);
    }

    #title:focus{
        border: 1.5px solid rgb(255, 131, 117);
    }

    #description{
        position: relative;
        top: 30px;
        width: 100%;
        height: 200px;
        font-size: 15px;
        // font-weight: 600;
        border-radius: 13px;
        border: 1.5px solid rgb(255, 255, 255);
        padding-left: 15px;
        padding-top: 10px;
        padding-bottom: 10px;
        padding-right: 20px;
        background-color: rgb(240, 240, 240);
        outline: none;
    }

    #description:focus{
        border-bottom: 1.5px solid rgb(255, 131, 117);
    }

    #submit_button{
        position: relative;
        height:50px;
        width: 40%;
        top: 40px;
        border-radius: 13px;
        background-color: rgb(174, 17, 0);
        border-color: rgb(174, 17, 0);
    }

    }


    .input_txt{
        position: relative;
        top: 100px;
        flex: 1;
        padding: 30px;
        // left:20%;
        width:80%;
        height: 300px;
        margin: 0 auto;
        // background-color:rgb(157,13,67);

    }
</style>

<script>
import { useRouter } from "vue-router";
const router = useRouter();
import "https://gosspublic.alicdn.com/aliyun-oss-sdk-6.18.0.min.js";
import axios from "axios";
import {ElMessage} from "element-plus";
import {Buffer} from 'buffer';
import store from "../../store/index";

export default {
    name:"upclick_click",
    data(){
        return {
            showBtnDealImg:true,
            oneBtnImg:false,
            limitCountImg:5,   //上传图片的最大数量
            auto:'',
            fileList: [],
            dialogImageUrl: '',
            dialogVisible: false,
            hideUploadEdit: true, //是否隐藏上传按钮
            ruleForm: {
                name:'',
                image:'',
                summary:'',
                issue:'',
            },
            push_fileList: [],
            ruleForm: {
                name:'',
                image:[],
                summary:'',
                issue:'',
            },

            rules: {
                name: [
                {
                    required: true,
                    message: '请输入标题',
                    trigger: 'blur',
                },
                ],
                summary: [
                {
                    required: true,
                    message: '请输入简介',
                    trigger: 'blur',
                },
                ]
            },
        }
    },
    mounted() {
    },
    methods: {
        //  upload_click() {
        //      console.log("func");
        //     //  const file = document.getElementById("file");
        //     //  const data = file.files[0];
        //     const data = file.raw
        //     //调用mounted中的putObject函数
        //     var that = this;
        //     // this.auto = putObject(data);
        //  },
        // fileToBlob(file) {
        //     return new Blob([file], { type: file.type });
        // },

        upclick_click(file, fileList) {
            
            const client = new OSS({
                region: "oss-cn-beijing",
                accessKeyId: "LTAI5tR1c1uhFRfWxjq8BWT4",
                accessKeySecret: "BdN5OIEdet7IO6KWOq7TJiivHOsC5B",
                bucket: "graphcrafter",
            });

            // const upload = document.getElementById("upload");
            
            async function putObject(data,that) {
                // var that = this;
                try {
                    const options = {
                        meta: { temp: "demo" },
                        mime: "json",
                        headers: { "Content-Type": "Buffer" },
                    };
                    //获取年月日时间
                    const ops = { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false };
                    const formattedTime = new Intl.DateTimeFormat('en-US', ops).format(new Date()).replace(/[^0-9]/g, '');
                    //设置图片名称

                    // TODO:替换为session中的用户名
                    const Uname = "加完班打麻药";
                    // 
                
                    const imgName = Uname +'/'+ formattedTime + ".jpg";
                    const result = await client.put(imgName, data, options);

                    //存储图片的url至本地消息中
                    const imgURL = "https://graphcrafter.oss-cn-beijing.aliyuncs.com/" + imgName;
                    console.log(imgURL);
                    that.push_fileList.push(imgURL);
                    console.log(that.push_fileList);

                } catch (e) {
                    console.log(e);
                }
            }

            function fileToBlob(file) {
                return new Blob([file], { type: file.type });
            }

            function imageToBase64(imageObj) {
                var canvas = document.createElement('canvas');
                var context = canvas.getContext('2d');
                canvas.width = imageObj.width;
                canvas.height = imageObj.height;
                context.drawImage(imageObj, 0, 0);
                var base64 = canvas.toDataURL('image/jpeg');
                return base64;
            }

            console.log("upload image ...");

            const arr = Array.from(Object.entries(file));
            const arrayBuffer = new Uint8Array(arr).buffer;
            const data = (arrayBuffer);
            console.log(data.type);
            putObject(fileToBlob(file.raw),this);
            console.log(fileList);
            this.noneBtnImg = fileList.length >= this.limitCountImg;
            
        },
        //移除图片功能
        handleRemove(file, fileList) {
            console.log(file, fileList);
            this.noneBtnImg = fileList.length >= this.limitCountImg;
        },

        //预览图片功能
        handlePictureCardPreview(file) {
            console.log(file.url);
            this.dialogVisible = true;
            this.dialogImageUrl = file.url;
        },

        submitForm(formName) {
            //获取内容
            try {
                const title = document.getElementById("title").value;
                const description = document.getElementById("description").value;
                const ruleForm =this.ruleForm
                console.log(title, description)
                console.log(this.reluForm)
                const userId = store.state.user_id
                axios.post('/api/postnotes', {
                    pics: this.push_fileList,
                    title: title,
                    description: description,
                    userId: userId
                });
                alert("发布成功！")
                location.href = "/dashboard";
                // var that = this
                // axios.post('/api/postnotes', {
                //     pics: that.ruleForm,
                //     title: title,
                //     description: description,
                //     userId: userId
                // })
                //     .then(function(res){
                //         console.log(res);
                // })
            } catch(error) {
                console.error('Error adding like:', error);
            }  
        },
    },
};
</script>

