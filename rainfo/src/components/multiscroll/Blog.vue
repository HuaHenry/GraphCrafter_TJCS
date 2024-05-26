<template>
  <div class="ms-container-wrapper">
    <div class="ms-left">
      <div
        class="ms-section bg_image "
        :style="{ backgroundImage: 'url(' + src + ')' }"
      ></div>
    </div>

    <div class="ms-right">
      <div class="ms-section ms-table">
        <div
          class="slipt-content-inner ms-tableCell blog-content rn-plr rn-ptb-100"
        >
          <h2 class="section-title">Latest News</h2>
          <div class="blog-wrapper">
            <!-- Start Single Blog -->
            <div class="rn-blog" v-for="(blog, i) in blogContent" :key="i">
              <h2>
                <a :href="blog.targetRoute"
                  >{{ blog.blogTitle }} -
                  <span class="date">{{ blog.dateMeta }}</span></a
                >
              </h2>
              <p>
                {{ blog.desc }}
              </p>
            </div>
            <!-- End Single Blog -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        src: require("../../assets/img/news/news-1.jpg"),
        blogContent: [
          {
            blogTitle: "The Lorem Ipsum generators",
            dateMeta: "March 26, 2021",
            targetRoute: "/blog-details",
            desc: `There are many variations of passages of Lorem Ipsum available,
                but the majority have suffered alteration in some form.`,
          },
          {
            blogTitle: "The Lorem Ipsum generators",
            dateMeta: "April 2, 2021",
            targetRoute: "/blog-details",
            desc: `There are many variations of passages of Lorem Ipsum available,
                but the majority have suffered alteration in some form.`,
          },
          {
            blogTitle: "The Lorem Ipsum generators",
            dateMeta: "April 12, 2020",
            targetRoute: "/blog-details",
            desc: `There are many variations of passages of Lorem Ipsum available,
                but the majority have suffered alteration in some form.`,
          },
        ],
      };
    },
  };
</script>

<style lang="scss" scoped></style>
