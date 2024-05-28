<template>
  <div class="profile-editor-container">
    <!-- 退出按钮 -->
    <div class="close-cricle">
      <div class="close close-mask-white" @click="exitPage">
        <Close style="width: 1.2em; height: 1.2em; color: rgba(51, 51, 51, 0.8)" />
      </div>
    </div>

    <!-- 使用 flex 布局，将头像和信息部分分为左右两列 -->
    <div class="profile-editor">
      <!-- 左侧：头像区域 -->
      <div class="left-column">
        <div class="avatar-container" @click="triggerFileInput">
          <img :src="avatar" alt="头像" class="avatar" />
          <div class="avatar-overlay">
            <Camera style="width: 1.5em; height: 1.5em" />
            <span>修改我的头像</span>
          </div>
          <!-- 隐藏的文件上传 -->
          <input type="file" accept="image/*" @change="uploadAvatar" class="hidden-input" ref="fileInput" />
        </div>
      </div>

      <!-- 右侧：用户信息部分 -->
      <div class="right-column">
        <!-- 用户名 -->
        <div class="profile-field">
          <div class="field-label">用户名</div>
          <div class="field-content" v-if="!editingUsername">
            <span style="font-size: 16px;">{{ username }}</span>
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
          <!-- 横线 -->
          <hr class="field-separator" />
        </div>

        <!-- 性别 -->
        <div class="profile-field">
          <div class="field-label">性别</div>
          <div class="field-content" v-if="!editingsex">
            <span style="font-size: 16px;">{{ sex }}</span>
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
          <!-- 横线 -->
          <hr class="field-separator" />
        </div>

        <!-- 年龄 -->
        <div class="profile-field">
          <div class="field-label">年龄</div>
          <div class="field-content" v-if="!editingAge">
            <span style="font-size: 16px;">{{ age }}</span>
            <Edit style="margin-left: 8px; cursor: pointer; color: #13386c; width: 1em; height: 1em;" @click="startEdit('age')" />
          </div>
          <div class="field-content" v-else>
            <!-- 使用 el-input-number 来允许数字输入和调整 -->
            <el-input-number
              v-model="age"
              :min="0"  
              :max="120" 
              placeholder="请输入年龄"
              controls-position="right">
            </el-input-number>
            <div class="profile-actions">
              <el-button type="primary" @click="saveProfile('age')">保存</el-button>
              <el-button @click="cancelEdit('age')">取消</el-button>
            </div>
          </div>
          <!-- 横线 -->
          <hr class="field-separator" />
        </div>


        <!-- 邮箱 -->
        <div class="profile-field">
          <div class="field-label">邮箱</div>
          <div class="field-content" v-if="!editingEmail">
            <span style="font-size: 16px;">{{ email }}</span>
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
          <!-- 横线 -->
          <hr class="field-separator" />
        </div>

        <!-- 简介 -->
        <div class="profile-field">
          <div class="field-label">简介</div>
          <div class="field-content" v-if="!editingBio">
            <span style="font-size: 16px;">{{ bio }}</span>
            <Edit style="margin-left: 8px; cursor: pointer; color: #13386c; width: 1em; height: 1em;" @click="startEdit('bio')" />
          </div>
          <div class="field-content" v-else>
            <el-input
              type="textarea"
              v-model="bio"
              placeholder="填写兴趣爱好、生活方式等个人简介"
              maxlength="50"
              
              show-word-limit
              :rows="2" 
            ></el-input>
            <div class="profile-actions">
              <el-button type="primary" @click="saveProfile('bio')">保存</el-button>
              <el-button @click="cancelEdit('bio')">取消</el-button>
            </div>
          </div>
          <!-- 横线 -->
          <hr class="field-separator" />
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
  import store from "../../store/index";

  import OSS from 'ali-oss';
  const router = useRouter();
  

  const client = new OSS({
  region: "oss-cn-beijing",
  accessKeyId: "LTAI5tR1c1uhFRfWxjq8BWT4",
  accessKeySecret: "BdN5OIEdet7IO6KWOq7TJiivHOsC5B",
  bucket: "graphcrafter",
  });

 const userId = store.state.user_id;
  
 
  // 初始化数据
  const initialAvatar = 'http://graphcrafter.oss-cn-beijing.aliyuncs.com/avatars/1-default.webp'; // 初始头像路径
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
      avatar.value = data.photo ? data.photo : 'http://graphcrafter.oss-cn-beijing.aliyuncs.com/avatars/1-default.webp';
      sex.value = data.sex == null ? "未知" : data.sex == 1 ? '男' : '女';
      bio.value = data.bio;
      age.value = data.age == null ? "未知" :  data.age;
    } catch (error) { 
      console.error('Error loading user profile:', error);
    }
  };
  
  // 加载用户数据
  onMounted(loadUserProfile);
  
  const triggerFileInput = (event) => {
    // 清空input的值
    event.target.value = '';
    fileInput.value.click();
  };
  
  const uploadAvatar = (event) => {
    isAvatarEditorOpen.value = true;
    const target = event.target as HTMLInputElement;
    console.log(target)
    const file = target.files ? target.files[0] : null;
    
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        // 只将图片预览结果存储到 uploadedAvatar 中
        uploadedAvatar.value = e.target?.result as string;
       
        isAvatarEditorOpen.value = true; // 打开预览编辑器
        //console.log(isAvatarEditorOpen.value)
      };
      reader.readAsDataURL(file);
      
    }
  };
  
  const saveAvatar = async () => {
    const file = fileInput.value.files[0];
    if (!file) {
      console.error('No file selected for upload');
      return;
    }

    try {
      const filePath = `avatars/${userId}-${file.name}`; // Unique path for the avatar
      const options = { headers: { 'Content-Type': file.type } };

      // Perform upload to OSS
      const result = await client.put(filePath, file, options);
      console.log('Upload result:', result);

      // Retrieve URL
      const avatarUrl = `http://graphcrafter.oss-cn-beijing.aliyuncs.com/${filePath}`;
      avatar.value = avatarUrl;

      // Update the avatar URL in the backend
      await axios.post('/api/update-avatar', {
        user_id: userId,
        photo: avatarUrl
      });

      ElMessage({ message: '头像已保存', type: 'success' });
    } catch (e) {
      console.error('Error saving avatar:', e);
      ElMessage({ message: '上传头像时出现问题，请稍后重试', type: 'error' });
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
      originalEmail.value = email.value;
      editingEmail.value = true;
    } else if (field === 'bio') {
      originalBio.value = bio.value;
      editingBio.value = true;
    } else if (field === 'age') {
      originalAge.value = age.value;
      editingAge.value = true;
    }
  };
  
  
// 检查用户名是否唯一
const checkUsernameUnique = async (newUsername) => {
  try {
    const response = await axios.get(`/check-username?username=${encodeURIComponent(newUsername)}&user_id=${userId}`);
    return response.data.is_unique; // 假设端点返回 { is_unique: boolean }
  } catch (error) {
    console.error('Error checking username uniqueness:', error);
    return false; // 出错时假设用户名不唯一
  }
};


  // 更新用户数据
  //此处需要向数据库中查询所有的用户名
  //还需要向后端传输自己的用户名，允许他假装改一下

  const saveProfile = async (field) => {
  if (field === 'username' && username.value !== originalUsername.value) {
    const isUnique = await checkUsernameUnique(username.value);
    if (!isUnique) {
      ElMessage({ message: '用户名已被占用，请选择其他用户名', type: 'error' });
      return; // 停止保存操作
    }
  }

  // 如果用户名是唯一的或者字段不是用户名，继续保存操作
  try {
    const updatedData = {
      id: userId,
      name: username.value,
      email: email.value,
      photo: avatar.value,
      bio: bio.value,
      sex: sex.value === '男',
      age: age.value,
    };

    // 使用新数据更新数据库
    await axios.post('/api/update-profile', updatedData);
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


.left-column {
  width: 180px;
}

.right-column {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-left:  40px
}




.profile-editor-container {
  background-color: white;
  border-radius: 20px;
  box-shadow: 0 8px 64px 0 rgba(0, 0, 0, 0.04), 0 1px 4px 0 rgba(0, 0, 0, 0.02);
  padding: 32px;
  max-width: 800px;
  margin: auto;
  margin-top: 100px;
  position: relative;
}

.profile-editor {
  display: flex;
  gap: 24px;
}

.profile-field {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.field-content {
  min-height: 20px; /* 为每个字段预留固定的高度 */
  
}

.profile-actions {
  display: flex;
  gap: 10px;
  margin-top: 10px; /* 在元素上方添加20px的外边距 */
}

.avatar-container {
  position: relative;
  width: 180px;
  height: 180px;
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
  top: -0px;
  left: -25px;
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


.username-placeholder {
  height: 30px; /* 在用户名之前预留出 20px 的空白 */
}


.field-label {
  font-weight: bold;
}

.field-separator {
  border: none;
  border-top: 1px solid #e0e0e0;
  margin: 0;
  margin-bottom: 10px; /* 添加底部间距 */
}


</style>
