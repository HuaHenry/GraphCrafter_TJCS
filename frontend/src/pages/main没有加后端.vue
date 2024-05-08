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
        <div class="field-content" v-if="!editingGender">
          <span>{{ gender }}</span>
          <Edit style="margin-left: 8px; cursor: pointer; color: #13386c; width: 1em; height: 1em;" @click="startEdit('gender')" />
        </div>
        <div class="field-content" v-else>
          <el-radio-group v-model="gender">
            <el-radio label="男">男</el-radio>
            <el-radio label="女">女</el-radio>
          </el-radio-group>
          <div class="profile-actions">
            <el-button type="primary" @click="saveProfile('gender')">保存</el-button>
            <el-button @click="cancelEdit('gender')">取消</el-button>
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
import { ref } from 'vue';
import { ElMessage } from 'element-plus';
import { Close, Camera, Edit } from "@element-plus/icons-vue";
import { useRouter } from 'vue-router';

const router = useRouter();

// 初始化数据
const initialAvatar = '/path/to/default/avatar.png'; // 初始头像路径
const initialUsername = '用户昵称';
const initialGender = '女';
const initialEmail = 'user@example.com';
const initialBio = 'Be water, my friend.';

const avatar = ref(initialAvatar);
const uploadedAvatar = ref(''); // 上传后的头像路径
const username = ref(initialUsername);
const gender = ref(initialGender);
const email = ref(initialEmail);
const bio = ref(initialBio);

const isAvatarEditorOpen = ref(false);
const editingUsername = ref(false);
const editingGender = ref(false);
const editingEmail = ref(false);
const editingBio = ref(false);
const zoom = ref(1);
const offsetX = ref(0);
const offsetY = ref(0);

const dragging = ref(false);
const startX = ref(0);
const startY = ref(0);

const fileInput = ref(null);

// 触发文件选择
const triggerFileInput = () => {
  fileInput.value.click();
};

// 上传头像
const uploadAvatar = (event: Event) => {
  const target = event.target as HTMLInputElement;
  const file = target.files ? target.files[0] : null;
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      uploadedAvatar.value = e.target?.result as string;
      isAvatarEditorOpen.value = true; // 打开编辑器
    };
    reader.readAsDataURL(file);
  }
};

// 开始拖动
const startDrag = (event: MouseEvent) => {
  dragging.value = true;
  startX.value = event.clientX;
  startY.value = event.clientY;
};

// 停止拖动
const stopDrag = () => {
  dragging.value = false;
};

// 处理拖动
const onDrag = (event: MouseEvent) => {
  if (dragging.value) {
    offsetX.value += event.clientX - startX.value;
    offsetY.value += event.clientY - startY.value;
    startX.value = event.clientX;
    startY.value = event.clientY;
  }
};

// 关闭头像编辑器并取消修改
const cancelAvatarEdit = () => {
  isAvatarEditorOpen.value = false;
  zoom.value = 1; // 重置缩放比例
  offsetX.value = 0;
  offsetY.value = 0;
};

// 保存头像
const saveAvatar = () => {
  avatar.value = uploadedAvatar.value;
  ElMessage({
    message: '头像已保存',
    type: 'success',
  });
  isAvatarEditorOpen.value = false;
};

// 开始编辑字段
const startEdit = (field: string) => {
  if (field === 'username') {
    editingUsername.value = true;
  } else if (field === 'gender') {
    editingGender.value = true;
  } else if (field === 'email') {
    editingEmail.value = true;
  } else if (field === 'bio') {
    editingBio.value = true;
  }
};

// 保存字段
const saveProfile = (field: string) => {
  ElMessage({
    message: `资料(${field})已保存`,
    type: 'success',
  });
  if (field === 'username') {
    editingUsername.value = false;
  } else if (field === 'gender') {
    editingGender.value = false;
  } else if (field === 'email') {
    editingEmail.value = false;
  } else if (field === 'bio') {
    editingBio.value = false;
  }
};

// 取消编辑并恢复初始值
const cancelEdit = (field: string) => {
  if (field === 'username') {
    username.value = initialUsername;
    editingUsername.value = false;
  } else if (field === 'gender') {
    gender.value = initialGender;
    editingGender.value = false;
  } else if (field === 'email') {
    email.value = initialEmail;
    editingEmail.value = false;
  } else if (field === 'bio') {
    bio.value = initialBio;
    editingBio.value = false;
  }
};

// 退出当前页面
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
