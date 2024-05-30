<template>
<div class="main">
    <SideBar @func="getIndex"></SideBar>
    <div class="manage-container">
        <ManageUser v-if="index === '/manageUser'" />
        <ManagePost v-else-if="index === '/managePost'" />
        <feedback v-else-if="index === '/manageFeedback'" style="margin: 60px"/>
        <ManageDashboard v-else />
    </div>
</div>
</template>

<script lang="ts">
import SideBar from '@/components/manager/SideBar.vue';
import ManageDashboard from '@/components/manager/ManageDashboard.vue';
import ManageUser from '@/components/manager/ManageUser.vue';
import ManagePost from '@/components/manager/ManagePost.vue';
import ManageFeedback from '@/components/manager/ManageFeedback.vue';
import feedback from "@/pages/message/children/feedback.vue";

export default {
  components: {
    SideBar,
    ManageDashboard,
    ManageUser,
    ManagePost,
    ManageFeedback,
    feedback
  },
  data(){
    return{
      name: "Manager",
      index: '',
    }
  },

  methods:{
    getIndex(data: string) {
      this.index = data;
    }
  }

}
</script>

<style scoped>
.manage-container {
    padding-left: 280px;
    padding-top: 30px;
    padding-bottom: 30px;
}
</style>
