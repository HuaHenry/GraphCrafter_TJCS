<template>
  <div>
    <ul class="message-container">
      <div v-for="comment in comments" :key="comments.id" class="parent-comment">
        <li class="message-item">
          <a class="user-avatar">
            <!-- https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png -->
            <img class="avatar-item" :src="comment.avatar" />
          </a>
          <div class="main">
            <div class="info">
              <div class="user-info">
                <a class>{{ comment.author }}</a>
              </div>
              <div class="interaction-hint"><span>评论了您的笔记&nbsp;</span><span>{{ comment.date }}</span></div>
              <div class="interaction-content">
                <span>{{ comment.content }}</span>
              </div>
            
            </div>
            <div class="extra">
              <img class="extra-image" :src="comment.picture" />
            </div>
          </div>
        </li>
      </div>
      
    </ul>
  </div>
</template>
<script lang="ts" setup>
import { ChatRound, Star } from "@element-plus/icons-vue";
import { ref, computed,onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';
import store from "../../../store/index";
const router = useRouter();
const route = useRoute();
const userId = store.state.user_id;
const comments=ref([]);
const fetchComments = async () => {
  try {
    const post_id = route.query.id;
    console.log(post_id);
    const response = await axios.get(`/api/all_comments/${userId}`);
    const result = response.data;
    // 解构出各个属性数组
    const { ids,dates,contents,authors,avatars,pictures } = result;
    // 遍历数组，构建每个对象并添加到数组中
    for (let i = 0; i < contents.length; i++) {
      const item = {
        id: ids[i],
        date: dates[i],
        content: contents[i],
        author: authors[i],
        avatar: avatars[i],
        picture: pictures[i]
      };
      comments.value.push(item);
    }
  }catch(error){
    console.error('Error fetching data:', error);
  }
}
onMounted(async () => {
  fetchComments();
});
</script>




<style lang="less" scoped>
textarea {
  overflow: auto;
}
.message-container {
  width: 40rem;
  height: 80vh;
  background-color: #fff;
  // border-radius: 15px;
  border: #fff;
  .message-item {
    display: flex;
    flex-direction: row;
    padding-top: 24px;

    .user-avatar {
      margin-right: 24px;
      flex-shrink: 0;

      .avatar-item {
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        border-radius: 100%;
        border: 1px solid rgba(0, 0, 0, 0.08);
        object-fit: cover;
      }
    }

    .main {
      flex-grow: 1;
      flex-shrink: 1;
      display: flex;
      flex-direction: row;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(0, 0, 0, 0.08);

      .info {
        flex-grow: 1;
        flex-shrink: 1;

        .user-info {
          display: flex;
          flex-direction: row;
          align-items: center;
          justify-content: space-between;
          margin-bottom: 4px;
          a {
            color: #333;
            font-size: 16px;
            font-weight: 600;
          }
        }
        .interaction-hint {
          font-size: 14px;
          color: rgba(51, 51, 51, 0.6);
          margin-bottom: 8px;
        }

        .interaction-content {
          display: flex;
          font-size: 14px;
          color: #333;
          line-height: 140%;
          cursor: pointer;
          margin-bottom: 12px;
          .msg-count {
            width: 20px;
            height: 20px;
            line-height: 20px;
            font-size: 13px;
            color: #fff;
            background-color: red;
            text-align: center;
            border-radius: 100%;
          }
        }

        .quote-info {
          font-size: 12px;
          display: flex;
          align-items: center;
          color: rgba(51, 51, 51, 0.6);
          margin-bottom: 12px;
          cursor: pointer;
        }

        .quote-info::before {
          content: "";
          display: inline-block;
          border-radius: 8px;
          margin-right: 6px;
          width: 4px;
          height: 17px;
          background: rgba(0, 0, 0, 0.08);
        }

        .action {
          display: flex;
          color: rgba(51, 51, 51, 0.8);

          .action-reply {
            cursor: pointer;
            width: 88px;
            height: 40px;
            border: 1px solid rgba(0, 0, 0, 0.08);
            border-radius: 999px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: rgba(51, 51, 51, 0.8);

            .action-text {
              margin-left: 4px;
              font-size: 16px;
            }
          }

          .action-like {
            cursor: pointer;
            width: 40px;
            height: 40px;
            margin-left: 12px;
            border: 1px solid rgba(0, 0, 0, 0.08);
            border-radius: 999px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: rgba(51, 51, 51, 0.8);
          }

          .action-comment {
            flex-grow: 1;
            width: 100%;

            .input-wrapper {
              height: auto;
              display: flex;
              position: relative;
              width: calc(100% - 70px);
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

          .action-cancel {
            flex-shrink: 0;
            margin-left: 8px;
            cursor: pointer;
            height: 40px;
            border: 1px solid rgba(0, 0, 0, 0.08);
            padding: 10px 16px;
            border-radius: 999px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            color: rgba(51, 51, 51, 0.8);
          }
          .comment-wrapper {
            display: flex;
            font-size: 16px;
            overflow: hidden;
          }
        }
      }

      .extra {
        min-width: 48px;
        flex-shrink: 0;
        margin-left: 24px;

        .extra-image {
          cursor: pointer;
          width: 48px;
          height: 48px;
          border: 1px solid rgba(0, 0, 0, 0.02);
          border-radius: 6px;
          object-fit: cover;
        }
      }
    }
  }
}
</style>
