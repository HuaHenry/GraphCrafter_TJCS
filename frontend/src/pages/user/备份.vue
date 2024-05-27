<template>
    <div class="profile-editor-container">
      <!-- 退出按钮 -->
      <div class="close-cricle">
        <div class="close close-mask-white" @click="exitPage">
          <Close style="width: 1.2em; height: 1.2em; color: rgba(51, 51, 51, 0.8)" />
        </div>
      </div>
  
      <div class="profile-editor">
        <!-- 头像区域 -->
        <div class="avatar-container" @click="triggerFileInput">
          <img :src="avatar" alt="头像" class="avatar" />
          <div class="avatar-overlay">
            <Camera style="width: 1.5em; height: 1.5em" />
            <span>修改我的头像</span>
          </div>
          <!-- 隐藏的文件上传 -->
          <input type="file" accept="image/*" @change="uploadAvatar" class="hidden-input" ref="fileInput" />
        </div>
  
        <!-- 用户名 -->
        <div class="profile-field">
          <label>用户名</label>
          <div class="field-content" v-if="!editingUsername">
            <span>{{ username }}</span>
            <Edit style="margin-left: 8px; cursor: pointer; color: #13386c; width: 1em; height: 1em;" @click="startEdit('username')" />
          </div>
          <div class="field-content" v-else>
            <el-input
              type="text"
              v-model="username"
              placeholder="输入您的用户名"
              maxlength="20"
            ></el-input>
            <div class="profile-actions">
              <el-button type="primary" @click="saveProfile('username')">保存</el-button>
              <el-button @click="cancelEdit('username')">取消</el-button>
            </div>
          </div>
        </div>
  
        <!-- 性别 -->
        <div class="profile-field">
          <label>性别</label>
          <div class="field-content" v-if="!editingsex">
            <span>{{ sex }}</span>
            <Edit style="margin-left: 8px; cursor: pointer; color: #13386c; width: 1em; height: 1em;" @click="startEdit('sex')" />
          </div>
          <div class="field-content" v-else>
            <el-radio-group v-model="sex">
              <el-radio label="男">男</el-radio>
              <el-radio label="女">女</el-radio>
            </el-radio-group>
            <div class="profile-actions">
              <el-button type="primary" @click="saveProfile('sex')">保存</el-button>
              <el-button @click="cancelEdit('sex')">取消</el-button>
            </div>
          </div>
        </div>
  
         <!-- 年龄 -->
         <div class="profile-field">
          <label>年龄</label>
          <div class="field-content" v-if="!editingAge">
            <span>{{ age }}</span>
            <Edit style="margin-left: 8px; cursor: pointer; color: #13386c; width: 1em; height: 1em;" @click="startEdit('age')" />
          </div>
          <div class="field-content" v-else>
            <el-input
              type="text"
              v-model="age"
              placeholder="输入您的年龄"
            ></el-input>
            <div class="profile-actions">
              <el-button type="primary" @click="saveProfile('age')">保存</el-button>
              <el-button @click="cancelEdit('age')">取消</el-button>
            </div>
          </div>
        </div>
  
  
  
        <!-- 邮箱 -->
        <div class="profile-field">
          <label>邮箱</label>
          <div class="field-content" v-if="!editingEmail">
            <span>{{ email }}</span>
            <Edit style="margin-left: 8px; cursor: pointer; color: #13386c; width: 1em; height: 1em;" @click="startEdit('email')" />
          </div>
          <div class="field-content" v-else>
            <el-input
              type="text"
              v-model="email"
              placeholder="输入您的邮箱地址"
              maxlength="50"
            ></el-input>
            <div class="profile-actions">
              <el-button type="primary" @click="saveProfile('email')">保存</el-button>
              <el-button @click="cancelEdit('email')">取消</el-button>
            </div>
          </div>
        </div>
  
        <!-- 简介 -->
        <div class="profile-field">
          <label>简介</label>
          <div class="field-content" v-if="!editingBio">
            <span>{{ bio }}</span>
            <Edit style="margin-left: 8px; cursor: pointer; color: #13386c; width: 1em; height: 1em;" @click="startEdit('bio')" />
          </div>
          <div class="field-content" v-else>
            <el-input
              type="text"
              v-model="bio"
              placeholder="填写兴趣爱好、生活方式等个人简介"
              maxlength="50"
              show-word-limit
            ></el-input>
            <div class="profile-actions">
              <el-button type="primary" @click="saveProfile('bio')">保存</el-button>
              <el-button @click="cancelEdit('bio')">取消</el-button>
            </div>
          </div>
        </div>
      </div>
  
   <!-- 头像编辑弹窗 -->
   <el-dialog title="预览头像" v-model="isAvatarEditorOpen" width="30%" :custom-class="'rounded-dialog'">
        <div class="avatar-editor">
          <img :src="uploadedAvatar || avatar" class="avatar-preview" alt="预览头像" />
          <div class="avatar-actions">
            <el-button type="primary" @click="saveAvatar">保存</el-button>
            <el-button @click="cancelAvatarEdit">取消</el-button>
          </div>
        </div>
      </el-dialog>
    </div>
  </template>
  
  <script lang="ts" setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { ElMessage } from 'element-plus';
  import { Close, Camera, Edit } from '@element-plus/icons-vue';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  
  const userId = 1;
  
  // 初始化数据
  const initialAvatar = '/static/avatars/default.png'; // 初始头像路径
  const initialUsername = '';
  const initialsex = '';
  const initialEmail = '';
  const initialBio = '';
  const initialAge = '';
  
  const avatar = ref(initialAvatar);
  const uploadedAvatar = ref('');
  const username = ref(initialUsername);
  const sex = ref(initialsex);
  const age = ref(initialAge);
  const email = ref(initialEmail);
  const bio = ref(initialBio);
  
  const isAvatarEditorOpen = ref(false);
  const editingUsername = ref(false);
  const editingsex = ref(false);
  const editingEmail = ref(false);
  const editingBio = ref(false);
  const editingAge = ref(false);
  const fileInput = ref(null);
  
  // 预先存储的变量，用于保存编辑前的值
  const originalUsername = ref('');
  const originalsex = ref('');
  const originalEmail = ref('');
  const originalBio = ref('');
  const originalAge = ref('');
  
  
  
  const loadUserProfile = async () => {
    try {
      const response = await axios.get(`/api/user/${userId}`);
      const data = response.data;
      username.value = data.name;
      email.value = data.email;
      avatar.value = data.photo;
      sex.value = data.sex ? '男' : '女';
      bio.value = data.bio;
      age.value = data.age;
    } catch (error) {
      console.error('Error loading user profile:', error);
    }
  };
  
  // 加载用户数据
  onMounted(loadUserProfile);
  
  const triggerFileInput = () => {
    fileInput.value.click();
  };
  
  const uploadAvatar = (event) => {
    const target = event.target as HTMLInputElement;
    const file = target.files ? target.files[0] : null;
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        // 只将图片预览结果存储到 uploadedAvatar 中
        uploadedAvatar.value = e.target?.result as string;
        isAvatarEditorOpen.value = true; // 打开预览编辑器
      };
      reader.readAsDataURL(file);
    }
  };
  
  const saveAvatar = async () => {
    const formData = new FormData();
    formData.append('file', fileInput.value.files[0]);
  
    try {
      const response = await axios.post('/api/upload-avatar', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      avatar.value = response.data.photo; // 从服务器获取更新后的头像路径
      ElMessage({ message: '头像已保存', type: 'success' });
    } catch (error) {
      console.error('Error saving avatar:', error);
    }
  
    isAvatarEditorOpen.value = false; // 关闭编辑器
  };
  
  
  // 关闭头像编辑器并取消修改
  const cancelAvatarEdit = () => {
    isAvatarEditorOpen.value = false;
  
  };
  
  // 开始编辑字段
  const startEdit = (field: string) => {
    if (field === 'username') {
      originalUsername.value = username.value;
      editingUsername.value = true;
    } else if (field === 'sex') {
      originalsex.value = sex.value;
      editingsex.value = true;
    } else if (field === 'email') {
      originalBio.value = bio.value;
      editingEmail.value = true;
    } else if (field === 'bio') {
      originalBio.value = bio.value;
      editingBio.value = true;
    } else if (field === 'age') {
      originalAge.value = age.value;
      editingAge.value = true;
    }
  };
  
  
  // 更新用户数据
  const saveProfile = async (field: string) => {
    try {
      const updatedData: Record<string, any> = {
        id: userId, // 包含用户 ID
        name: username.value,
        email: email.value,
        photo: avatar.value,
        bio: bio.value,
        sex: sex.value === '男', // 转换性别
        age: age.value, // 转换性别
      };
      if (field === 'username') updatedData.name = username.value;
      if (field === 'sex') updatedData.sex = sex.value === '男';
      if (field === 'email') updatedData.email = email.value;
      if (field === 'bio') updatedData.bio = bio.value;
      if (field === 'age') updatedData.age = age.value;
      console.log(updatedData)
  
      await axios.post('/api/update-profile', updatedData); // 使用 POST 方法
      ElMessage({ message: `资料(${field})已保存`, type: 'success' });
    } catch (error) {
      console.error('Error updating profile:', error);
    }
  
    // 关闭编辑状态
    if (field === 'username') editingUsername.value = false;
    if (field === 'sex') editingsex.value = false;
    if (field === 'email') editingEmail.value = false;
    if (field === 'bio') editingBio.value = false;
    if (field === 'age') editingAge.value = false;
  };
  
  
  // 取消编辑并恢复到原始值
  const cancelEdit = (field: string) => {
    if (field === 'username') {
      username.value = originalUsername.value;
      editingUsername.value = false;
    } else if (field === 'sex') {
      sex.value = originalsex.value;
      editingsex.value = false;
    } else if (field === 'email') {
      email.value = originalEmail.value;
      editingEmail.value = false;
    } else if (field === 'bio') {
      bio.value = originalBio.value;
      editingBio.value = false;
    } else if (field === 'age') {
      age.value = originalAge.value;
      editingAge.value = false;
    }
  };
  
  const exitPage = () => {
    router.go(-1);
  };
  </script>
  
  
  
  <style scoped>
  .profile-editor-container {
    background-color: white;
    border-radius: 20px;
    box-shadow: 0 8px 64px 0 rgba(0, 0, 0, 0.04), 0 1px 4px 0 rgba(0, 0, 0, 0.02);
    padding: 32px;
    max-width: 600px;
    margin: auto;
    margin-top: 50px;
    position: relative;
  }
  
  .profile-editor {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }
  
  .profile-field {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  
  .field-content {
    min-height: 50px; /* 为每个字段预留固定的高度 */
  }
  
  .profile-actions {
    display: flex;
    gap: 10px;
  }
  
  .avatar-container {
    position: relative;
    width: 120px;
    height: 120px;
    cursor: pointer;
    margin-bottom: 24px; /* 为头像与用户名预留空间 */
  }
  
  .avatar {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
  }
  
  .avatar-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: rgba(0, 0, 0, 0.4);
    color: white;
    opacity: 0;
    transition: opacity 0.3s;
  }
  
  .avatar-container:hover .avatar-overlay {
    opacity: 1;
  }
  
  .hidden-input {
    display: none;
  }
  
  .avatar-editor {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    border-radius: 20px; /* 添加圆角 */
    background-color: #fff; /* 确保弹窗背景为白色 */
    padding: 20px; /* 添加一些内边距以提供空间 */
    box-shadow: 0 8px 64px 0 rgba(0, 0, 0, 0.04), 0 1px 4px 0 rgba(0, 0, 0, 0.02);
  }
  
  
  .avatar-preview {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    object-fit: cover;
  }
  
  .avatar-actions {
    display: flex;
    gap: 10px;
  }
  
  .close-cricle {
    position: absolute;
    top: -15px;
    left: -15px;
    z-index: 100;
    cursor: pointer;
  }
  
  .close-mask-white {
    box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.04), 0 1px 2px 0 rgba(0, 0, 0, 0.02);
    border: 1px solid rgba(0, 0, 0, 0.08);
  }
  
  .close {
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 100%;
    width: 40px;
    height: 40px;
    cursor: pointer;
    transition: all 0.3s;
  }
  
  .rounded-dialog {
    border-radius:40px; /* 设置弹窗的整体圆角 */
  }
  
  </style>
  