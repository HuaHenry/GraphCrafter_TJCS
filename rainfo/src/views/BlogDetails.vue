<template>
  <div class="blog-details-page">
    <HeaderFive>
      <img slot="logo" src="../assets/img/logo/portfolio.png" />
    </HeaderFive>

    <!-- Start Bradcaump area -->
    <div class="bradcaump_area">
      <div class="parallaxContainer" data-black-overlay="6">
        <v-container>
          <v-row>
            <v-col cols="12">
              <div class="text-center bradcaump_inner">
                <h2 class="bradcaump-title">
                  WEBSITE DEVELOPMENT
                </h2>
                <ul class="blog-meta">
                  <li>{{ blogMeta.date }}</li>
                  <li :class="blogMeta.className">-</li>
                  <li>
                    By :
                    <a :href="blogMeta.authorUrl" target="_blank">
                      {{ blogMeta.author }}</a
                    >
                  </li>
                  <li :class="blogMeta.className">-</li>
                  <li>{{ blogMeta.comments }}</li>
                </ul>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>
    <!-- End Bradcaump area -->

    <!-- Start Blog Details Area -->
    <div class="rf-blog-details section-ptb-xl">
      <v-container>
        <v-row>
          <v-col lg="12">
            <div class="text-left blog-details-wrapper">
              <div class="dropcaps-inner">
                <p>
                  There are many variations of passages of Lorem Ipsum
                  available, but the majority have suffered alteration in some
                  form, by injected humour, looked up one of the more obscure Latin words, consectetur,
                  from a Lorem Ipsum passage, and going through the cites of the
                  word in classical literature, or randomised words which don't look
                  even slightly believable. If you are going to use a passage of
                  Lorem Ipsum.
                </p>
              </div>
              <div class="content">
                <p>
                  Contrary to popular belief, Lorem Ipsum is not simply random
                  text. It has roots in a piece of classical Latin literature
                  from 45 BC, making it over 2000 years old. Richard McClintock,
                  a Latin professor at Hampden-Sydney College in Virginia,
                  looked up one of the more obscure Latin words, consectetur,
                  from a Lorem Ipsum passage, and going through the cites of the
                  word in classical literature,
                </p>
                <blockquote>
                  <p>
                    Neque porro quisquam est qui dolorem ipsum quia dolor sit
                    amet,looked up one of the more obscure Latin words, consectetur,
                  from a Lorem Ipsum passage looked up one of the more obscure Latin words
                  </p>
                </blockquote>
                  <p>
                  There are many variations of passages of Lorem Ipsum
                  available, but the majority have suffered alteration in some
                  form, by injected humour, looked up one of the more obscure Latin words, consectetur,
                  from a Lorem Ipsum passage, and going through the cites of the
                  word in classical literature, or randomised words which don't look
                  even slightly believable. If you are going to use a passage of
                  Lorem Ipsum.
                </p>
                <p>
                  Discovered the undoubtable source. Lorem Ipsum comes from
                  sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et
                  Malorum" (The Extremes of Good and Evil) by Cicero, written in
                  45 BC. This book is a treatise on the theory of ethics, very
                  popular during the Renaissance. The first line of Lorem Ipsum,
                  "Lorem ipsum dolor sit amet..", comes from a line in section
                  1.10.32.
                </p>

                <div class="bl-feature">
                  <ul class="feature-blog-list d-flex">
                    <li>
                      <img :src="blogListImage.img1" alt="personal portfolio" />
                    </li>
                    <li>
                      <img :src="blogListImage.img2" alt="personal portfolio" />
                    </li>
                      <li>
                      <img :src="blogListImage.img1" alt="personal portfolio" />
                    </li>
                      <li>
                      <img :src="blogListImage.img2" alt="personal portfolio" />
                    </li>
                  </ul>
                </div>

                  <p>
                  Contrary to popular belief, Lorem Ipsum is not simply random
                  text. It has roots in a piece of classical Latin literature
                  from 45 BC, making it over 2000 years old. Richard McClintock,
                  a Latin professor at Hampden-Sydney College in Virginia,
                  looked up one of the more obscure Latin words, consectetur,
                  from a Lorem Ipsum passage, and going through the cites of the
                  word in classical literature,
                </p>
                <p>
                  Contrary to popular belief, Lorem Ipsum is not simply random
                  text. It has roots in a piece of classical Latin literature
                  from 45 BC, making it over 2000 years old. Richard McClintock,
                  a Latin professor at Hampden-Sydney College in Virginia,
                  looked up one of the more obscure Latin words, consectetur,
                  from a Lorem Ipsum passage, and going through the cites of the
                  word in classical literature,The point of using Lorem Ipsum is that it has a more-or-less
                  normal distribution of letters, as opposed to using 'Content
                  here content.
                </p>
                  <p>
                  It is a long established fact that a reader will be distracted
                  by the readable content of a page when looking at its layout.
                  The point of using Lorem Ipsum is that it has a more-or-less
                  normal distribution of letters, as opposed to using 'Content
                  here, content here alo.
                </p>
              </div>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <!-- End Blog Details Area -->

    <Footer />
  </div>
</template>

<script>
  import HeaderFive from "../components/header/HeaderFive";
  import Footer from "../components/footer/Footer";
  export default {
    components: {
      HeaderFive,
      Footer,
    },
    data() {
      return {
        blogMeta: {
          date: "April 1, 2021",
          className: "separator",
          author: "RainbowIt",
          authorUrl: "https://themeforest.net/user/rainbow-themes/portfolio",
          comments: "07 Comments",
        },
        blogListImage: {
          img1: require("../assets/img/news/md-img-1.jpg"),
          img2: require("../assets/img/news/md-img-2.jpg"),
        },
      };
    },
  };
</script>

<style lang="scss" scoped>
  .blog-details-page .-rn-footer {
    background: #f9f9f9;
  }
</style>
