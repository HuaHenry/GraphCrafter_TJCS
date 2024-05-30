<template>
  <div
    class="row portfolio-wrapper row--55 rn-custom-portfolio-wrapper rn-hil-portfolio"
  >
    <v-col
      lg="4"
      md="4"
      sm="6"
      cols="12"
      v-for="(content, i) in portfolioContent"
      :key="i"
    >
      <router-link to="/portfolio-details" class="portfolio-wrap">
        <div class="item-shadow">
          <img :src="content.src" />
        </div>
        <div class="portfolio" :class="content.bgClassName">
          <div class="content">
            <h4 class="title">{{ content.title }}</h4>
            <span class="desc">{{ content.desc }}</span>
          </div>
          <div class="bgDescription"></div>
        </div>
      </router-link>
    </v-col>
    <!-- Start Single Portfoli -->
  </div>
</template>

<script>
  export default {
    data() {
      return {
        portfolioContent: [
          {
            bgClassName: "colorful-project-bg--8",
            src: require("../../assets/img/project/colorful/work-8.jpg"),
            title: "3D Design",
            desc: "Photography",
          },
          {
            bgClassName: "colorful-project-bg--2",
            src: require("../../assets/img/project/colorful/work-2.jpg"),
            title: "Asymmetrical layoutsy",
            desc: "Art",
          },
          {
            bgClassName: "colorful-project-bg--3",
            src: require("../../assets/img/project/colorful/work-3.jpg"),
            title: "Art Deco",
            desc: "Fashion",
          },
          {
            bgClassName: "colorful-project-bg--4",
            src: require("../../assets/img/project/colorful/work-4.jpg"),
            title: "Modern Mid-Century",
            desc: "Photography",
          },
          {
            bgClassName: "colorful-project-bg--5",
            src: require("../../assets/img/project/colorful/work-5.jpg"),
            title: "The continuing",
            desc: "Photography",
          },
          {
            bgClassName: "colorful-project-bg--6",
            src: require("../../assets/img/project/colorful/work-6.jpg"),
            title: "palettes for photos",
            desc: "Fashion",
          },
          {
            bgClassName: "colorful-project-bg--7",
            src: require("../../assets/img/project/colorful/work-7.jpg"),
            title: "Custom illustrations",
            desc: "Photography",
          },
          {
            bgClassName: "colorful-project-bg--1",
            src: require("../../assets/img/project/colorful/work-1.jpg"),
            title: "Buxom serifs",
            desc: "Photography",
          },
          {
            bgClassName: "colorful-project-bg--9",
            src: require("../../assets/img/project/colorful/work-9.jpg"),
            title: "Open compositions",
            desc: "Photography",
          },
        ],
      };
    },
  };
</script>
