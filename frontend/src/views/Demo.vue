<template>
    <div>
        <!-- Header -->
        <header class="bg-white header root-demo">
            <!-- <div> -->
                <router-link to="/"><img src="https://graphcrafter.oss-cn-beijing.aliyuncs.com/LOGO.gif" alt="图匠" 
                        style="width:300px;position: relative; top:20px; left:-50px; z-index: -1;" /></router-link>
            <!-- </div> -->

            <div class="text-right purchase-button" style="position: relative;top:20px;">
                <router-link :to="isLoggedIn ? '/' : '/login'" @click.native="handleAuth">
                    {{ buttonText }}
                </router-link>
            </div>
        </header>
        <!--// Header -->

    <!-- Banner -->
    <div class="banner-wrapper">
      <div class="container">
        <div class="banner-inner">
          <div class="banner-content">
            <h1>
              图匠 —— 对话式图像创意室<br/>
              edit your pictures
            </h1>
          </div>
          <div class="row">
            <div class="col-lg-4 col-md-4 col-sm-6 col-12" v-for="(item, i) in menuContent" :key="i">
              <div class="demo-item" @click="handleLinkClick(item, $event)">
                  <img :src="item.src" alt="Main Demo" class="image-shadow"/>
                  <span class="title-style">{{ item.title }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- End Banner -->

    <!-- Demos -->
    <div class="demo-wrapper bg_color--1">
      <div class="container-fluid">
        <div class="row-title" style="" >
          <div class="col-md-12 text-center" >
            <div class="title-wrapper" >
              <h1 class="text-center">Picture Edit Demos</h1>
              <p>
                Choose one of demo or cutomize easily your picture following your
                ideas
              </p>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-4 col-md-6 col-sm-12" v-for="(item, i) in demoContent" :key="i">
            <div class="demo-item">
<!--              <a :href="item.href" target="_blank">-->
                <img :src="item.src" alt="Main Demo" class="image-shadow"/>
                <span class="title-style">{{ item.title }}</span>
<!--              </a>-->
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- End Demos -->

    <!-- User Agreement and Feature Introduction Buttons -->
    <div class="button-container text-center mt-4">
      <button @click="showUserAgreement" class="btn btn-primary mx-2">用户协议</button>
       <a href="../../public/Introduction.html">
        <button class="btn btn-primary mx-2">功能介绍</button>
      </a>
    </div>

    <!-- User Agreement Modal -->
    <el-dialog v-model="isUserAgreementVisible" >
      <div>
        <h2>用户协议</h2>
        <p>欢迎使用我们的服务。在使用前，请仔细阅读以下用户协议：</p>

        <h4>1. 接受条款</h4>
        <p>通过访问和使用本服务，您表示同意遵守这些条款和条件。</p>

        <h4>2. 服务内容</h4>
        <p>我们提供图片编辑和创意设计功能。</p>

        <h4>3. 用户账户</h4>
        <p>您需要注册一个账户才能使用某些功能。请确保提供真实、准确的信息。</p>

        <h4>4. 用户责任</h4>
        <p>您对使用本服务的行为负全部责任。请勿进行任何违法或侵权行为。</p>

        <h4>5. 知识产权</h4>
        <p>所有内容（包括图片、文本、软件、代码）归我们所有，受法律保护。</p>

        <h4>6. 隐私政策</h4>
        <p>我们重视您的隐私。请参阅我们的隐私政策了解详情。</p>

        <h4>7. 免责声明</h4>
        <p>本服务按“现状”提供，我们不保证其准确性、完整性或可靠性。</p>

        <h4>8. 终止</h4>
        <p>我们有权随时终止或暂停您的服务访问。</p>

        <h4>9. 修改条款</h4>
        <p>我们保留随时修改这些条款的权利，修改后的条款将在本页面公布。</p>

        <h4>10. 联系我们</h4>
        <p>如有疑问，暂时联系不到我们。</p>
      </div>
      <template #footer>
        <el-button @click="isUserAgreementVisible = false">关闭</el-button>
      </template>
    </el-dialog>

    <!-- Feature Introduction Modal -->
<!--    <el-dialog v-model="isFeatureIntroductionVisible" title="功能介绍">-->
<!--      <p>这里是功能介绍的内容...</p>-->
<!--      <template #footer>-->
<!--        <el-button @click="isFeatureIntroductionVisible = false">关闭</el-button>-->
<!--      </template>-->
<!--    </el-dialog>-->

  </div>
</template>

<script>
  import feather from "feather-icons";
  import { mapGetters, mapActions } from 'vuex';
  import "vue-slick-carousel/dist/vue-slick-carousel.css";
  import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
  import "hooper/dist/hooper.css";
  import '../assets/scss/style.scss'
  import "../assets/css/home-style.css";
  import {ElMessage} from "element-plus";
  export default {
    data() {
      return {
        menuContent: [
          {
            src: new URL("@/assets/img/menu/edit.jpg", import.meta.url).href,
            title: "图像处理",
            href: "/easy1",
          },
          {
            src:  new URL("@/assets/img/menu/share.jpg", import.meta.url).href,
            title: "分享广场",
            href: "/index",
          },
          {
            src:  new URL("../assets/img/menu/me.jpg", import.meta.url).href,
            title: "个人中心",
            href: "/collection",
          },
        ],
        demoContent: [
          {
            src:  new URL("../assets/img/demos/demo1.jpg", import.meta.url).href,
            title: "假日海边风景拍照配方",
            href: "/minimal-agency",
          },
          {
            src:  new URL("../assets/img/demos/demo2.jpg", import.meta.url).href,
            title: "旋转的春日",
            href: "/freelancer",
          },
          {
            src: new URL("../assets/img/demos/demo3.jpg", import.meta.url).href,
            title: "绿野仙踪调色",
            href: "/creative-portfolio",
          },
          {
            src:  new URL("../assets/img/demos/demo4.jpg", import.meta.url).href,
            title: "假期去旅行",
            href: "/agency",
          },
          {
            src:  new URL("../assets/img/demos/demo5.jpg", import.meta.url).href,
            title: "治愈通透配方",
            href: "/multiscroll-portfolio",
          },
          {
            src:  new URL("../assets/img/demos/demo6.jpg", import.meta.url).href,
            title: "草原山脉配方",
            href: "/designer-portfolio",
          },
        ],
        innerPageContent: [
          {
            src:  "../assets/img/demos/inner-pages/about.jpg",
            title: "About Us",
            href: "/about-us",
          },
          {
            src:  ("../assets/img/demos/inner-pages/portfolio.jpg"),
            title: "Portfolio",
            href: "/portfolio",
          },
          {
            src:  ("../assets/img/demos/inner-pages/portfolio-details.jpg"),
            title: "Portfolio Details",
            href: "/portfolio-details",
          },
          {
            src:  ("../assets/img/demos/inner-pages/awards.jpg"),
            title: "Awards",
            href: "/awards",
          },
          {
            src:  ("../assets/img/demos/inner-pages/blog.jpg"),
            title: "Blog",
            href: "/blog",
          },
          {
            src:  ("../assets/img/demos/inner-pages/blog-details.jpg"),
            title: "Blog Details",
            href: "/blog-details",
          },
          {
            src:  ("../assets/img/demos/inner-pages/service.jpg"),
            title: "Service",
            href: "/service",
          },
          {
            src:  ("../assets/img/demos/inner-pages/service-details.jpg"),
            title: "Service Details",
            href: "/service-details",
          },
          {
            src:  ("../assets/img/demos/inner-pages/contact.jpg"),
            title: "Contact",
            href: "/contact",
          },
          {
            src:  ("../assets/img/demos/inner-pages/404.jpg"),
            title: "404 Page",
            href: "/404",
          },
          {
            src:  ("../assets/img/demos/inner-pages/coming-soon.jpg"),
            title: "Coming Soon",
            href: "",
          },
          {
            src:  ("../assets/img/demos/inner-pages/coming-soon.jpg"),
            title: "Coming Soon",
            href: "",
          },
        ],
        featuresContent: [
          {
            icon: "check-square",
            title: "VueJS",
            desc: ` No.1 Github Start & Developer Friendly Top Progressive JavaScript Framework `,
            calssName: "vue",
          },
          {
            icon: "cast",
            title: "Vuetify Js",
            desc: `It's a complete UI framework built with Vue.js which you get rich user experiences`,
            calssName: "vuetify",
          },
          {
            icon: "smartphone",
            title: "Perfect Responsive",
            desc: `Vuetify takes a mobile first approach to design like phone, tablet, or desktop computer.`,
            calssName: "responsive",
          },
          {
            icon: "archive",
            title: "Sass Available",
            desc: ` The tamplate has Sass available for css. You can Change
                        css by sass`,
            calssName: "sass",
          },
          {
            icon: "arrow-down-circle",
            title: "Fast Loading Speed",
            desc: `Trydo is faster loading speed.Trydo create your theme so
                        much faster way`,
            calssName: "speed",
          },

          {
            icon: "command",
            title: "Modern Design",
            desc: `Trydo is a modern creatuve design for Creative Agency ,
                        Personal Portfolio etc....`,
            calssName: "modern",
          },
          {
            icon: "code",
            title: "Well Documented Codes",
            desc: `The Trydo code is awesome well documented code. And Its
                        customization is very easily`,
            calssName: "code",
          },
          {
            icon: "headphones",
            title: "24 Support System",
            desc: `We are provide 24 hours support for all clients.You can
                        purchase without hesitation.`,
            calssName: "support",
          },
        ],
        panel: 0,
        isUserAgreementVisible: false,
        isFeatureIntroductionVisible: false,
      };
    },
    computed: {
    ...mapGetters(['isLoggedIn']),
    buttonText() {
      return this.isLoggedIn ? 'Log Out' : 'Log In';
    }
  },
    methods: {
      ...mapActions(['login', 'logout']),
      handleAuth(event) {
        if (this.isLoggedIn) {
          event.preventDefault(); // 阻止默认行为，防止页面跳转
          this.logout();
        }
      },
      iconSvg(icon) {
        return feather.icons[icon].toSvg();
      },
      handleLinkClick(item, event) {
        if (!this.isLoggedIn) {
          event.preventDefault(); // 阻止链接跳转
          ElMessage.error({
            message: "请先登录！",
            duration: 1500
          });
        } else {
          this.$router.push(item.href); // 手动执行路由跳转
        }
      },
      showUserAgreement() {
        this.isUserAgreementVisible = true;
      },

    },
    mounted() {
      feather.replace();
    },
  };
</script>

<style lang="scss" scoped>
.button-container {
  margin-top: 20px;
}

.btn {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

.mx-2 {
  margin-left: 10px;
  margin-right: 10px;
}

.mt-4 {
  margin-top: 20px;
}

.container {
  max-width: 100%;
  margin-right: auto;
  margin-left: auto;
  padding-right: 15px;
  padding-left: 15px;
}

.banner-inner {
  text-align: center;
  padding: 20px;
}

.banner-content {
  margin-bottom: 20px;
}

.row {
  display: flex;
  flex-wrap: wrap;
  margin-right: -15px;
  margin-left: -15px;
}

.col-lg-4,
.col-md-4,
.col-sm-6,
.col-12 {
  position: relative;
  width: calc(100% / 3);
  padding-right: 15px;
  padding-left: 15px;
}

.demo-item {
  margin-bottom: 20px;
}

img.image-shadow {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.title-style {
  display: block;
  margin-top: 10px;
  font-size: 16px;
  font-weight: bold;
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-right: 15px;
  padding-left: 15px;
  .row-title{
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  .row {
    display: flex;
    flex-wrap: wrap;
    margin-right: -15px;
    margin-left: -15px;

    .col-lg-4 {
      flex: 0 0 33.33333%; // 设置每列占据 1/3 的宽度
      max-width: 33.33333%;
    }

    .text-center {
      text-align: center;
    }

    .title-wrapper {
      text-align: center;
      margin-bottom: 20px;
    }

    .demo-item {
      margin-bottom: 20px;
    }

    .title-style {
      display: block;
      margin-top: 10px;
      font-weight: bold;
    }

    .image-shadow {
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
    }
  }
}
  .image-shadow {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); /* X偏移量, Y偏移量, 模糊半径, 扩展半径, 颜色 */
    border-radius: 15px; /* 添加圆角 */
  }
  .title-style {
    font-family: 'STZhongsong', '华文中宋', serif; /* 设置字体族 */
    font-weight: bold; /* 设置字体粗细 */
  }
  .theme--light.about-expension-panels .v-expansion-panel-content p {
    color: #333;
    font-size: 15px;
    margin-bottom: 0;
  }
  .slide--5 .content h1 {
    color: #000;
  }
  b,
  strong {
    font-weight: 400;
  }
  .theme--light.about-expension-panels .v-expansion-panel-header {
    margin-top: 20px;
    margin-bottom: 15px;
    padding: 0 0 10px 0;
    font-size: 18px;
    color: #000;
    border: none;
    @media only screen and (max-width: 767px) {
      margin-bottom: 5px;
    }
  }
  .theme--light.about-expension-panels .v-expansion-panel {
    background-color: transparent;
    color: #1f1f25;
  }

  .demo-wrapper {
    margin-top: 130px;

    &.inner-pages {
      margin-top: 0;
    }
  }
  .bg_color--1 {
    background: #f9f9f9;
  }
  .bg_color--2 {
    background: #fff;
  }
  .section-title {
    h2 {
      font-size: 50px;
      font-weight: 600;
      line-height: 62px;
      margin-bottom: 20px;
      color: #000 !important;
      @media only screen and (max-width: 767px) {
        font-size: 34px;
        line-height: 45px;
      }
    }
    p {
      color: #333;
    }
  }

  @media only screen and (max-width: 767px) {
    .pv-feaq-area {
      &.ptb--120 {
        padding: 60px 0;
      }
    }
    .section-title h2 {
      font-size: 30px;
      line-height: 40px;
    }
    .section-title.text-left.pb--30 {
      padding-bottom: 0;
    }
    .slide--5 .content h1 {
      font-size: 25px;
      line-height: 40px;
    }
  }

  .single-feature {
    background: #fff;
    padding: 50px;
    transition: transform 0.65s cubic-bezier(0.05, 0.2, 0.1, 1),
      box-shadow 0.65s cubic-bezier(0.05, 0.2, 0.1, 1);
    z-index: 2;
    border-radius: 10px;
    height: 100%;
    @media only screen and (max-width: 767px) {
      padding: 25px 15px;
    }

    .icon {
      font-weight: 400;
      margin-bottom: 23px;
      display: inline-flex;
    }

    h3 {
      margin-bottom: 19px;
      font-weight: 600;
      font-size: 20px;
      color: #333;
    }
    p {
      color: #333;
    }
  }
  .plr--120 {
    padding: 0 120px;
  }
  .features-area {
    [class*="col-"] {
      margin-top: 30px;
    }
  }
  .features-area {
    .col-lg-12 {
      margin-top: 0;
    }
  }
  strong,
  .theme-gradient,
  .v-application .pv-feaq-area a {
    color: #f42a59 !important;
  }
  .demo-wrapper {
    @media screen and (min-width: 768px) {
      [class*="col-"] {
        padding: 0 35px;
      }
    }
    .demo-item {
      background: #fff;
      box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.05);
    }
  }
  .demo-wrapper {
    &.inner-pages {
      .demo-item {
        box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.05);
      }
    }
  }
  @media (max-width: 767px) {
    .banner-content h1 {
      font-size: 28px;
      line-height: 42px;
    }
  }
  .section-title {
    @media (max-width: 767px) {
      &.pb_md--0 {
        padding-bottom: 0;
      }
      p {
        margin-bottom: 10px;
      }
    }
  }
</style>

<style lang="scss">
  .theme--light.about-expension-panels {
    .v-expansion-panel-header {
      min-height: 30px;
      padding: 0 0 5px 0;
      margin-top: 7px;
      margin-bottom: 8px;
      font-size: 16px;
      line-height: 24px;
      font-weight: 500;
      display: inline-flex;
      width: auto;
      font-family: "Poppins", sans-serif;

      &::after {
        position: absolute;
        content: "";
        left: 0;
        bottom: 0;
        width: 100%;
        height: 1px;
        background: #555;
        -webkit-transition: 0.3s;
        -o-transition: 0.3s;
        transition: 0.3s;
      }
      &:not(.v-expansion-panel-header--mousedown):focus::before {
        opacity: 0;
      }
    }
    .v-expansion-panel {
      background-color: transparent;
      color: #1f1f25;
    }
    .v-expansion-panel-content__wrap {
      font-size: 18px;
      line-height: 30px;
      background: none;
      border: none;
      padding: 0 0 15px;
    }
  }
  .single-feature {
    svg {
      width: 54px;
      height: 54px;
      stroke-width: 1 !important;
    }
    &:hover {
      box-shadow: 0 2px 70px 0 rgb(253 71 102 / 5%);
      transform: translateY(-5px);
    }
    .vue {
      color: #42b883;
    }
    .vuetify {
      color: #1867c0;
    }
    .code {
      color: #12d8df;
    }
    .sass {
      color: #59c98d;
    }
    .support {
      color: #f767b4;
    }
    .speed {
      color: #6f41f6;
    }
    .responsive {
      color: #337dff;
    }
    .modern {
      color: #fd4766;
    }
  }
  .features-area {
    padding: 120px 120px;
    @media only screen and (max-width: 767px) {
      padding: 60px 15px;
    }
  }
  .pv-feaq-area.ptb--120 {
    @media only screen and (max-width: 991px) {
      padding: 100px 0;
    }
  }

//   /deep/ logo {
//   width: 700px; /* 调整宽度 */
// //   height: 300px; /* 保持宽高比 */
//     }

</style>
