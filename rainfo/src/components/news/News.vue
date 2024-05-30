<template>
  <!-- Start Blog Area -->
  <div class="rn-blog-area home-one-blog d-flex bg_color--3" id="blog">
    <div class="rn-blog-left w-50">
      <div class="blog-content d-flex align-items-center h-100">
        <div class="text-left content news-content rn-plr section-ptb-xl">
          <h2 class="section-title">Latest News</h2>
          <div class="blog-wrapper">
            <!-- Start Single Blog -->
            <div class="rn-blog">
              <h2
                @mouseover="activetab = 1"
                :class="[activetab === 1 ? 'active' : '']"
              >
                <router-link to="/blog-details"
                  >There are many variations -
                  <span class="date">March 16, 2021</span></router-link
                >
              </h2>
              <p>
                There are many variations of passages of Lorem Ipsum available,
                but the majority have suffered alteration in majority some form.
              </p>
            </div>
            <!-- End Single Blog -->

            <!-- Start Single Blog -->
            <div class="rn-blog">
              <h2
                @mouseover="activetab = 2"
                :class="[activetab === 2 ? 'active' : '']"
              >
                <router-link to="/blog-details"
                  >The Lorem Ipsum generators -
                  <span class="date">March 16, 2021</span></router-link
                >
              </h2>
              <p>
                There are many variations of passages of Lorem Ipsum available,
                but the majority.
              </p>
            </div>
            <!-- End Single Blog -->

            <!-- Start Single Blog -->
            <div class="rn-blog">
              <h2
                @mouseover="activetab = 3"
                :class="[activetab === 3 ? 'active' : '']"
              >
                <router-link to="/blog-details"
                  >The Lorem Ipsum generators -
                  <span class="date">March 16, 2021</span></router-link
                >
              </h2>
              <p>
                There are many variations of passages of Lorem Ipsum available,
                but the majority have suffered alteration in some passages of
                form.
              </p>
            </div>
            <!-- End Single Blog -->
          </div>
        </div>
      </div>
    </div>

    <div class="rn-blog-right w-50 ">
      <v-fade-transition leave-absolute>
        <div
          v-if="activetab === 1"
          class="h-full rn-images-bg-wrapper"
          :style="{ backgroundImage: 'url(' + src1 + ')' }"
        ></div
      ></v-fade-transition>
      <v-fade-transition leave-absolute>
        <div
          v-if="activetab === 2"
          class="h-full rn-images-bg-wrapper"
          :style="{ backgroundImage: 'url(' + src2 + ')' }"
        ></div
      ></v-fade-transition>
      <v-fade-transition leave-absolute>
        <div
          v-if="activetab === 3"
          class="h-full rn-images-bg-wrapper"
          :style="{ backgroundImage: 'url(' + src3 + ')' }"
        ></div
      ></v-fade-transition>
    </div>
  </div>
  <!-- End Blog Area -->
</template>

<script>
  export default {
    data() {
      return {
        el: "#blog",
        activetab: 1,
        src1: require("../../assets/img/news/news-1.jpg"),
        src2: require("../../assets/img/news/news-2.jpg"),
        src3: require("../../assets/img/news/news-3.jpg"),
      };
    },
  };
</script>

<style lang="scss" scoped>
  .rn-blog-area {
    overflow: hidden;
  }
</style>
