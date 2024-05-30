<template>
  <div
    class="row portfolio-wrapper row--55 rn-custom-portfolio-wrapper rn-hil-portfolio"
  >
    <!-- Start Single Portfoli -->
    <v-col
      v-for="(content, i) in portfolioContent"
      :key="i"
      lg="4"
      md="4"
      sm="6"
      cols="12"
    >
      <router-link to="/portfolio-details" class="portfolio-wrap">
        <div class="portfolio" :class="content.imgClass">
          <div class="content">
            <h4 class="title">{{ content.title }}</h4>
            <span class="desc">{{ content.desc }}</span>
          </div>
          <div class="bgDescription"></div>
        </div>
      </router-link>
    </v-col>
    <!-- End Single Portfoli -->
  </div>
</template>

<script>
  export default {
    data() {
      return {
        portfolioContent: [
          {
            imgClass: "project-bg--1",
            title: "3D Design",
            desc: "Photography",
          },
          {
            imgClass: "project-bg--2",
            title: "Asymmetrical layoutsy",
            desc: "Art",
          },
          {
            imgClass: "project-bg--3",
            title: "Art Deco",
            desc: "Fashion",
          },
          {
            imgClass: "project-bg--4",
            title: "Modern Mid-Century",
            desc: "Photography",
          },
          {
            imgClass: "project-bg--5",
            title: "The continuing",
            desc: "Photography",
          },
          {
            imgClass: "project-bg--6",
            title: "palettes for photos",
            desc: "Photography",
          },
        ],
      };
    },
  };
</script>

<style lang="scss" scoped>
  @media only screen and (max-width: 575px){
    .rn-hil-portfolio > div {
        margin-top: 0 !important;
    }
  }

</style>
