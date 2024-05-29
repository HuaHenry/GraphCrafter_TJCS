<template>
  <div
    class="note-detail-mask"
    style="transition: background-color 0.4s ease 0s"
  >
    <div class="note-container">
      <div class="media-container">
        <el-carousel height="90vh">
          <el-carousel-item v-for="item in ImageList" :key="item">
            <el-image
              :src="item"
              style="width: 100%; height: 100%"
              fit="cover"
            />
            <!-- <img :src="item" alt=""  style="width: 100%"/> -->
          </el-carousel-item>
        </el-carousel>
      </div>
      <!-- <template #items="{items}"> -->
        <div class="interaction-container">
          <div class="author-container">
            <div class="author-me">
              <div class="info">
                <!-- <img
                  class="avatar-item"
                  style="width: 40px; height: 40px"
                  :src="items.avatar"
                  src="https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg"
                /> -->
                <img
                  class="avatar-item"
                  style="width: 40px; height: 40px"
                  :src="items.avatar"
                />
                <span class="name">{{ items.author }}</span>
              </div>
              <!-- <div class="follow-btn">
                <el-button type="danger" size="large" round>关注</el-button>
              </div> -->

              <el-button type="danger" size="large" round @click="handleClick">
                  {{ buttonText }}
              </el-button>


            </div>

            <div class="note-scroller">
              <div class="note-content">
                <div class="title">{{ items.title }}</div>
                <div class="desc">
                  <span>{{ items.body }} <br /></span>
                  <!-- <a class="tag tag-search">#海贼王</a>
                  <a class="tag tag-search">#海贼王</a>
                  <a class="tag tag-search">#海贼王</a> -->
                </div>
                <div class="bottom-container">
                  <span class="date">{{ items.date }}</span>
                </div>
                <div class="buttons" style="display: flex; justify-content: center; margin-top: 2ch">
                  <el-button @click="openDialog" type="danger" size="medium" style="width: 100%; height:40px; border-radius: 10px;">一键使用模板</el-button>
                </div>
                <el-dialog :visible.sync="dialogVisible" title="Upload Image" width="30%" style="z-index:10">
                  <!-- <el-upload
                    action="/api/upload_image"
                    :on-success="handleUploadSuccess"
                    :on-error="handleUploadError"
                    :before-upload="beforeUpload"
                    :auto-upload="false"
                    :show-file-list="false"
                  >
                    <el-button slot="trigger" size="small" type="primary">Select Image</el-button>
                    <div slot="tip" class="el-upload__tip">Only JPG/PNG files are allowed</div>
                  </el-upload>
                  <span slot="footer" class="dialog-footer">
                    <el-button @click="dialogVisible = false">Cancel</el-button>
                    <el-button type="primary" @click="uploadImage">Upload</el-button>
                  </span> -->
                </el-dialog>
              </div>
              <div class="divider interaction-divider"></div>

              <!-- 评论 -->

              <div class="comments-el">
                <div class="comments-container">
                  <div class="total">共{{ items.comments_num }}条评论</div>
                  <div class="list-container">
                    <div v-for="comment in comments" :key="comments.id" class="parent-comment">
                      <div class="comment-item">
                        <div class="comment-inner-container">
                          <div class="avatar">
                            <img class="avatar-item" :src="comment.avatar" />
                          </div>
                          <div class="right">
                            <div class="author-wrapper">
                              <div class="author"><a class="name">{{ comment.author }}</a></div>
                            </div>
                            <div class="content">{{ comment.content }}</div>
                            <div class="info">
                              <div class="date"><span>{{ comment.date }}</span></div>                              
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

              <!--  -->
              </div>
            </div>
            <div class="interactions-footer">
              <div class="buttons">
                <div class="left">
                  <span class="like-wrapper"  @click="toggleLike">
                    <span class="like-lottie">                      
                      <svg v-if="isLiked" xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16" style="width: 0.8em; height: 0.8em; color: #333">
                        <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
                      </svg>
                      <svg v-else xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16" style="width: 0.8em; height: 0.8em; color: #333">
                        <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
                      </svg>
                      </span
                    ><span class="count">{{ items.likes_num }}</span></span
                  >
                  <span class="collect-wrapper"  @click="toggleCollect">
                    <span class="like-lottie"> 
                      <StarFilled v-if="isCollected" style="width: 1em; height: 1em; color: #333" /> 
                      <Star v-else style="width: 0.8em; height: 0.8em; color: #333" /> 
                      <!-- <PictureRounded style="width: 0.8em; height: 0.8em; color: #333" />  -->
                    </span>
                    <span class="count">{{ items.collects_num }}</span></span
                  >
                  <span class="chat-wrapper">
                    <span class="like-lottie"> <ChatRound style="width: 0.8em; height: 0.8em; color: #333" /> </span
                    ><span class="count">{{ items.comments_num }}</span></span
                  >
                </div>
                <div class="share-wrapper"></div>
              </div>
              <div class="comment-wrapper active comment-comp">
                <div class="input-wrapper">
                  <input class="comment-input" v-model="com_content" type="text" placeholder="回复内容" />
                  <div class="input-buttons">
                    <Close style="width: 1.2em; height: 1.2em" />
                  </div>
                </div>
                <button class="submit" @click="submitComment">发送</button>
              </div>
            </div>
          </div>
        </div>
      <!-- </template> -->
    </div>

    <div class="close-cricle">
      <div class="close close-mask-white"  @click="goBack">
        <Close style="width: 1.2em; height: 1.2em; color: rgba(51, 51, 51, 0.8)" />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { Close, Star, StarFilled, PictureRounded, ChatRound } from "@element-plus/icons-vue";
import { useRouter, useRoute } from 'vue-router';
import { ref, computed,onMounted } from 'vue';
import { ElMessage,ElMessageBox } from 'element-plus';
import store from "../store/index";
import axios from 'axios';
const router = useRouter();
const route = useRoute();

// 用户id先写死，后面实现登陆后再改为变量实现
const userId = store.state.user_id;
console.log("检查一下",store.state.user_id)
// const ImageList=ref([]);
const ImageList=ref([]);
const items=ref({});
const comments=ref([]);
const com_content=ref('');
const isLiked=ref();
const isCollected=ref();
//const author_id = ref();

const fetchPost = async () => {
  try {
    // this.$route.params.id
    const post_id = route.query.id;
    console.log(post_id);
    const response = await axios.get(`/api/post_content/${post_id}`);
    // const data = await fetch('http://127.0.0.1:5000/api/post_content/${post_id}'); 
    const result = response.data;
    // 解构出各个属性数组
    const { pictures,date,title,body,author,avatar,author_id,likes_num,comments_num,collects_num } = result;
    //author_id =  response.data.author_id;
    // 遍历数组，构建每个对象并添加到数组中
    for (let i = 0; i < pictures.length; i++) {
      ImageList.value.push(pictures[i]);
    }
    // ImageList.value= pictures;
    items.value = {
      pictures: pictures, // 使用对应索引的图片 URL 作为 src 属性
      date : date,
      title: title, // 使用对应索引的标题属性
      body: body,
      author: author, // 使用对应索引的作者属性
      avatar: avatar, // 使用对应索引的头像属性
      author_id: author_id, //获取post的id，我需要互相关注

      likes_num: likes_num, // 使用对应索引的点赞数属性
      comments_num: comments_num, // 使用对应索引的评论数属性
      collects_num: collects_num
    };
    console.log("WTFFFFFF",items.value.author_id)

  }catch(error){
    console.error('Error fetching data:', error);
  }
}

const isFollowed = ref(false);
const followStatus = ref(0);  // 0: 单独关注, 1: 互相关注

const followUser = async () => {
    // 检查是否尝试自己关注自己
    if (store.state.user_id == items.value.author_id) {
        ElMessage.error('您不能关注自己。'); // 使用ElMessage显示错误信息
        return;  // 直接返回，不执行关注操作
    }

    // 如果还未关注，则尝试执行关注操作
    if (!isFollowed.value) {
        try {
            const response = await axios.post('/api/follow', {
                follower_id: store.state.user_id,
                followed_id: items.value.author_id
            });
            if (response.status === 200) {
                isFollowed.value = true;  // 更新关注状态
                ElMessage.success('关注成功！'); // 显示成功消息
            }
        } catch (error) {
            ElMessage.error('关注失败，请稍后再试。'); // 出错时使用ElMessage显示错误信息
        }
    }
};


const unfollowUser = async () => {
    try {
        const response = await axios.post('/api/unfollow', {  // 确保后端有处理取消关注的API
            follower_id: store.state.user_id,
            followed_id: items.value.author_id
        });
        if (response.status === 200) {
            isFollowed.value = false;  // 更新未关注状态
            followStatus.value = 0;    // 更新关注状态
            ElMessage.success('取消关注成功！');
        }
    } catch (error) {
        ElMessage.error('取消关注失败，请稍后再试。');
    }
};


const checkFollowStatus = async () => {
    try {
        const response = await axios.get(`/api/check-follow/${userId}/${items.value.author_id }`);
        console.log(response.data.isFollowed)
        console.log(response.data.status)
        isFollowed.value = response.data.isFollowed;
        
        followStatus.value = response.data.status;
    } catch (error) {
        console.error('Error checking follow status:', error);
    }
};

const buttonText = computed(() => {
    if (followStatus.value === 1) {
        return '互相关注';
    } else if (isFollowed.value) {
        return '已关注';
    } else {
        return '关注';
    }
});


// const handleClick = async () => {
//     await followUser();  // 等待 followUser 方法完成
//     await checkFollowStatus();  // 然后执行 checkFollowStatus 方法
// };


const handleClick = async () => {
    // 检查是否已经关注或者互相关注
    if (isFollowed.value || followStatus.value === 1) {
        // 弹出确认取消关注的对话框
        try {
            await ElMessageBox.confirm('您确定要取消关注吗？', '确认信息', {
                confirmButtonText: '确认',
                cancelButtonText: '取消',
                type: 'warning'
            });
            // 用户确认取消关注
            await unfollowUser();  // 这是你需要实现的取消关注的方法
            await checkFollowStatus();  // 再次检查关注状态
        } catch (error) {
            // 用户取消操作
            ElMessage.info('已取消操作');
        }
    } else {
        // 如果还没有关注，则尝试关注
        await followUser();
        await checkFollowStatus();
    }
};



const fetchComments = async () => {
  try {
    const post_id = route.query.id;
    console.log(post_id);
    const response = await axios.get(`/api/post_comments/${post_id}`);
    const result = response.data;
    // 解构出各个属性数组
    const { ids,dates,contents,authors,avatars } = result;
    // 遍历数组，构建每个对象并添加到数组中
    for (let i = 0; i < contents.length; i++) {
      const item = {
        id: ids[i],
        date: dates[i],
        content: contents[i],
        author: authors[i],
        avatar: avatars[i]
      };
      comments.value.push(item);
    }
  }catch(error){
    console.error('Error fetching data:', error);
  }
}

const submitComment = async () => {
  try {
    const post_id = route.query.id;
    console.log(post_id);
    const response = await axios.post('/api/submit_comment', {
      content: com_content.value,
      postId: post_id,
      userId: userId
      // date: date.toLocaleString()
    });
    const processed_data = response.data;
    const { ids,dates,contents,authors,avatars } = processed_data;
    const item = {
        id: ids,
        date: dates,
        content: contents,
        author: authors,
        avatar: avatars
      };
    comments.value.unshift(item);
    // const { ids,dates,contents,authors,avatars } = processed_data;
    com_content.value = '';
    ElMessage({ message: '评论发布成功！', type: 'success' });
    
    
  }catch(error){
    console.error('Error sending comment:', error);
  }
}

const getStatus = async () => {
  try{
    const post_id = route.query.id;
    console.log(post_id);
    const response = await axios.get(`/api/get_status/${post_id}/${userId}`);
    const result = response.data;
    const like=result.isLiked;
    const collect=result.isCollected;
    console.log(like);
    if (like=='1') isLiked.value=true;
    else isLiked.value=false;
    console.log(isLiked.value);
    // isLiked.value = like;
    if (collect=='1') isCollected.value=true;
    else isCollected.value=false;
  }catch(error){
    console.error('Error fetching data:', error);
  }
}

const toggleLike = async () => {
  try{
    isLiked.value = !isLiked.value;
    const post_id = route.query.id;
    console.log(post_id);
    if (isLiked.value) {
      // 如果现在是已经点赞的状态，那么发送一个请求到后端来添加点赞
      await axios.post('/api/add_like', {
        postId: post_id,
        userId: userId,
        add: 1
      });
      items.value.likes_num++;
      ElMessage({ message: '点赞成功！', type: 'success' });
    } else {
      // 如果现在是未点赞的状态，那么发送一个请求到后端来删除点赞
      await axios.post('/api/add_like', {
        postId: post_id,
        userId: userId,
        add: 0
      });
      items.value.likes_num--;
      ElMessage({ message: '取消点赞成功！', type: 'success' });
    }
  }catch(error){
  console.error('Error adding like:', error);
  }
}

const toggleCollect = async () => {
  try{
    isCollected.value = !isCollected.value;
    const post_id = route.query.id;
    console.log(post_id);
    if (isCollected.value) {
      // 如果现在是已经点赞的状态，那么发送一个请求到后端来添加点赞
      await axios.post('/api/add_collect', {
        postId: post_id,
        userId: userId,
        add: 1
      });
      items.value.collects_num++;
      ElMessage({ message: '收藏成功！', type: 'success' });
    } else {
      // 如果现在是未点赞的状态，那么发送一个请求到后端来删除点赞
      await axios.post('/api/add_collect', {
        postId: post_id,
        userId: userId,
        add: 0
      });
      items.value.collects_num--;
      ElMessage({ message: '取消收藏成功！', type: 'success' });
    }
  }catch(error){
  console.error('Error adding like:', error);
  }
}

onMounted(async () => {
  await fetchPost();  //做的比较慢 要确保得到了想要的数据
  console.log("WTF",items.value.author_id)
  await checkFollowStatus();
  fetchComments();
  checkFollowStatus();
});

const goBack = () => {
  router.go(-1);
}
</script>

<style lang="less" scoped>
.note-detail-mask {
  position: fixed;
  left: 0;
  top: 0;
  display: flex;
  width: 100vw;
  height: 100vh;
  z-index: 20;
  overflow: auto;

  .close-cricle {
    left: 1.3vw;
    top: 1.3vw;
    position: fixed;
    display: flex;
    z-index: 100;
    cursor: pointer;

    .close-mask-white {
      box-shadow:
        0 2px 8px 0 rgba(0, 0, 0, 0.04),
        0 1px 2px 0 rgba(0, 0, 0, 0.02);
      border: 1px solid rgba(0, 0, 0, 0.08);
    }

    .close {
      display: flex;
      justify-content: center;
      align-items: center;
      border-radius: 100%;
      width: 40px;
      height: 40px;
      border-radius: 40px;
      cursor: pointer;
      transition: all 0.3s;
    }
  }

  .note-container {
    width: 86%;

    height: 90%;
    transition:
      transform 0.4s ease 0s,
      width 0.4s ease 0s;
    transform: translate(104px, 32px) scale(1);
    overflow: visible;

    display: flex;
    box-shadow:
      0 8px 64px 0 rgba(0, 0, 0, 0.04),
      0 1px 4px 0 rgba(0, 0, 0, 0.02);
    border-radius: 20px;
    background: #895454;
    transform-origin: left top;

    .media-container {
      width: 68%;
      height: auto;

      position: relative;
      background: rgba(0, 0, 0, 0.03);
      flex-shrink: 0;
      flex-grow: 0;
      -webkit-user-select: none;
      user-select: none;
      overflow: hidden;
      border-radius: 20px 0 0 20px;
      transform: translateZ(0);
      height: 100%;
      object-fit: contain;
      min-width: 440px;
    }

    .interaction-container {
      width: 32%;
      flex-shrink: 0;
      border-radius: 0 20px 20px 0;
      position: relative;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
      height: 100%;
      background-color: #fff;
      overflow: hidden;
      border-left: 1px solid rgba(0, 0, 0, 0.08);

      .author-me {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        padding: 24px;
        border-bottom: 1px solid transparent;

        .info {
          display: flex;
          align-items: center;

          .avatar-item {
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            border-radius: 100%;
            border: 1px solid rgba(0, 0, 0, 0.08);
            object-fit: cover;
          }

          .name {
            padding-left: 12px;
            height: 40px;
            display: flex;
            align-items: center;
            font-size: 16px;
            color: rgba(51, 51, 51, 0.8);
          }
        }
      }

      .note-scroller::-webkit-scrollbar {
        display: none;
      }

      .note-scroller {
        transition: scroll 0.4s;
        overflow-y: scroll;
        flex-grow: 1;
        height: 80vh;

        .note-content {
          padding: 0 24px 24px;
          color: var(--color-primary-label);

          .title {
            margin-bottom: 8px;
            font-weight: 600;
            font-size: 18px;
            line-height: 140%;
          }

          .desc {
            margin: 0;
            font-weight: 400;
            font-size: 16px;
            line-height: 150%;
            color: #333;
            white-space: pre-wrap;
            overflow-wrap: break-word;

            .tag-search {
              cursor: pointer;
            }

            .tag {
              margin-right: 2px;
              color: #13386c;
            }
          }

          .bottom-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 12px;

            .date {
              font-size: 14px;
              line-height: 120%;
              color: rgba(51, 51, 51, 0.6);
            }
          }
        }

        .interaction-divider {
          margin: 0 24px;
        }
        .divider {
          margin: 4px 8px;
          list-style: none;
          height: 0;
          border: solid rgba(0, 0, 0, 0.08);
          border-width: 1px 0 0;
        }

        .comments-el {
          position: relative;

          .comments-container {
            padding: 16px;

            .total {
              font-size: 14px;
              color: rgba(51, 51, 51, 0.6);
              margin-left: 8px;
              margin-bottom: 12px;
            }

            .list-container {
              position: relative;

              .parent-comment {
                margin-bottom: 16px;

                .comment-item {
                  position: relative;
                  display: flex;
                  padding: 8px;

                  .comment-inner-container {
                    position: relative;
                    display: flex;
                    z-index: 1;
                    width: 100%;
                    flex-shrink: 0;

                    .avatar {
                      flex: 0 0 auto;

                      .avatar-item {
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        cursor: pointer;
                        border-radius: 100%;
                        border: 1px solid rgba(0, 0, 0, 0.08);
                        object-fit: cover;
                        width: 40px;
                        height: 40px;
                      }
                    }

                    .right {
                      margin-left: 12px;
                      display: flex;
                      flex-direction: column;
                      font-size: 14px;
                      flex-grow: 1;

                      .author-wrapper {
                        display: flex;
                        justify-content: space-between;
                        align-items: center;

                        .author {
                          display: flex;
                          align-items: center;
                          .name {
                            color: rgba(51, 51, 51, 0.6);
                            line-height: 18px;
                          }
                        }
                      }

                      .content {
                        margin-top: 4px;
                        line-height: 140%;
                        color: #333;
                      }

                      .info {
                        display: flex;
                        flex-direction: column;
                        justify-content: space-between;
                        font-size: 12px;
                        line-height: 16px;
                        color: rgba(51, 51, 51, 0.6);

                        .date {
                          margin: 8px 0;
                        }
                        .interactions {
                          display: flex;
                          margin-left: -2px;

                          .like-wrapper {
                            padding: 0 4px;
                            color: rgba(51, 51, 51, 0.8);
                            font-weight: 500;

                            position: relative;
                            cursor: pointer;
                            display: flex;
                            align-items: center;

                            .like-lottie {
                              width: 16px;
                              height: 16px;
                              left: 4px;
                            }

                            .count {
                              margin-left: 2px;
                              font-weight: 500;
                            }
                          }
                        }
                      }
                    }
                  }
                }

                .reply-container {
                  margin-left: 52px;

                  .show-more {
                    margin-left: 44px;
                    height: 32px;
                    line-height: 32px;
                    color: #13386c;
                    cursor: pointer;
                    font-weight: 500;
                    font-size: 14px;
                  }
                }
              }
            }
          }
        }
      }

      .interactions-footer {
        position: absolute;
        bottom: 0px;
        background: #fff;
        flex-shrink: 0;
        padding: 12px 24px 24px;
        height: 130px;
        border-top: 1px solid rgba(0, 0, 0, 0.08);
        flex-basis: 130px;
        z-index: 1;

        .buttons {
          display: flex;
          justify-content: space-between;

          .count {
            margin-left: 6px;
            margin-right: 12px;
            font-weight: 500;
            font-size: 12px;
          }

          .left {
            display: flex;
            .like-wrapper {
              position: relative;
              cursor: pointer;
              display: flex;
              justify-content: left;
              color: rgba(51, 51, 51, 0.6);
              margin-right: 5px;
              align-items: center;
              .like-lottie {
                transform: scale(1.7);
              }
            }

            .collect-wrapper {
              position: relative;
              cursor: pointer;
              display: flex;
              color: rgba(51, 51, 51, 0.6);
              margin-right: 5px;
              align-items: center;
              .like-lottie {
                transform: scale(1.7);
              }
            }

            .chat-wrapper {
              cursor: pointer;
              color: rgba(51, 51, 51, 0.6);
              display: flex;
              align-items: center;
              .like-lottie {
                transform: scale(1.7);
              }
            }
          }
        }

        .comment-wrapper {
          &.active {
            .input-wrapper {
              flex-shrink: 1;
            }
          }
        }

        .comment-wrapper {
          display: flex;
          font-size: 16px;
          overflow: hidden;

          .input-wrapper {
            display: flex;
            position: relative;
            width: 100%;
            flex-shrink: 0;
            transition: flex 0.3s;

            .comment-input:placeholder-shown {
              background-image: none;
              padding: 12px 92px 12px 36px;
              background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAMAAABg3Am1AAAANlBMVEUAAAA0NDQyMjIzMzM2NjY2NjYyMjI0NDQ1NTU1NTUzMzM1NTU1NTUzMzM1NTUzMzM1NTU1NTVl84gVAAAAEnRSTlMAmUyGEzlgc2AmfRx9aToKQzCSoXt+AAAAhElEQVRIx+3Uuw6DMAyF4XOcBOdCafv+L9vQkQFyJBak/JOHT7K8GLM7epuHusRhHwP/mejJ77i32CpZh33aD+lDFDzgZFE8+tgUv5BB9NxEb9NPL3i46JvoUUhXPBKZFQ/rTPHI3ZXt8xr12KX055LoAVtXz9kKHprxNMMxXqRvmAn9ACQ7A/tTXYAxAAAAAElFTkSuQmCC);
              background-repeat: no-repeat;
              background-size: 16px 16px;
              background-position: 16px 12px;
              color: rgba(51, 51, 51, 0.3);
            }

            .comment-input {
              padding: 12px 92px 12px 16px;
              width: 100%;
              height: 40px;
              line-height: 16px;
              background: rgba(0, 0, 0, 0.03);
              caret-color: rgba(51, 51, 51, 0.3);
              border-radius: 22px;
              border: none;
              outline: none;
              resize: none;
              color: #333;
            }

            .input-buttons {
              position: absolute;
              right: 0;
              top: 0;
              height: 40px;
              display: flex;
              align-items: center;
              justify-content: center;
              width: 92px;
              color: rgba(51, 51, 51, 0.3);
            }
          }

          .submit {
            margin-left: 8px;
            width: 60px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
            font-weight: 600;
            cursor: pointer;
            flex-shrink: 0;
            background: #3d8af5;
            border-radius: 44px;
            font-size: 16px;
          }
        }

        .comment-comp {
          margin-top: 20px;
        }
      }
    }
  }
}
</style>
