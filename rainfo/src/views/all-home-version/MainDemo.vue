<template>
  <div class="main-demo-page">
    <HeaderOne>
      <img slot="logo" src="../../assets/img/logo/portfolio.png" />
    </HeaderOne>
    <!-- End Header One Area -->

    <!-- Start Slider Area -->
    <div class="rv-slider-wrapper black-pagination pagination-bottom" id="home">
      <SliderThree />
    </div>
    <!-- End Slider Area -->

    <!-- Start Story Area -->
    <div class="rn-story-area d-flex bg_color--3 section-padding-lg" id="about">
      <div
        class="rn-story-left w-50 rn-story-bg-wrapper"
        :style="{ backgroundImage: 'url(' + aboutSrc + ')' }"
      ></div>
      <div class="rn-story-right w-50 d-flex align-items-center">
        <div class="text-left story-content rn-plr section-ptb-xl">
          <div class="text-left content">
            <h2 class="section-title">Our Story</h2>
            <p>
              There are many variations of passages of Lorem Ipsum available,
              but the majority have suffered alteration in some form.
            </p>
            <p>
              Vassages of Lorem Ipsum available the majority have suffered
              alteration.
            </p>
            <div class="story-btn">
              <router-link to="#portfolio">SEE OUR PORTFOLIO</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- End Story Area -->

    <!-- Start Skill Area -->
    <div class="rn-skill-area home-one-skill d-flex bg_color--3" id="skill">
      <div class="rn-skill-right w-50 d-flex align-items-center">
        <div class="text-left rn-skill rn-plr section-ptb-xl">
          <Skills />
        </div>
      </div>
      <div
        class="rn-skill-left w-50 rn-skill-bg-wrapper"
        :style="{ backgroundImage: 'url(' + skillSrc + ')' }"
      ></div>
    </div>
    <!-- End Skill Area -->

    <Service />
    <!-- Start Portfolio Area -->
    <div class="rn-portfolio-area section-ptb-xl" id="portfolio">
      <v-container>
        <v-row>
          <v-col lg="12">
            <div class="text-center section-title-2">
              <h2>Our Portfolio</h2>
              <p>My work will prove my quality</p>
            </div>
          </v-col>
        </v-row>
        <PortfolioTwo />
      </v-container>
    </div>
    <!-- End Portfolio Area -->

    <Awards />
    <News />
    <Footer />
  </div>
</template>

<script>
  import HeaderOne from "../../components/header/HeaderOne";
  import SliderThree from "../../components/slider/SliderThree";
  import Service from "../../components/service/Service";
  import PortfolioTwo from "../../components/portfolio/PortfolioTwo";
  import Awards from "../../components/awards/Awards";
  import News from "../../components/news/News";
  import Skills from "../../components/skill/Skills";
  import Footer from "../../components/footer/Footer";

  export default {
    components: {
      HeaderOne,
      SliderThree,
      Service,
      PortfolioTwo,
      Awards,
      News,
      Skills,
      Footer,
    },
    data() {
      return {
        aboutSrc: require("../../assets/img/portfolio/our-story.jpg"),
        skillSrc: require("../../assets/img/portfolio/my-skill.jpg"),
      };
    },
  };
</script>

<style lang="scss" scoped>
  .main-demo-page {
    @media only screen and (max-width: 767px) {
      .rn-skill-right {
        order: 2;
      }
      .rn-story-area {
        margin-top: -8px;
      }
    }
  }
</style>
