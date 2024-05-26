<template>
  <div class="about-page">
    <div class="rn-story-area d-flex bg_color--3" id="about">
      <div
        class="rn-story-left w-50 rn-story-bg-wrapper"
        :style="{ backgroundImage: 'url(' + aboutSrc + ')' }"
      ></div>
      <div class="rn-story-right w-50 d-flex align-items-center">
        <div
          class="story-style--3 story-content text-left rn-plr--160 section-ptb-xl"
        >
          <div class="content text-left">
            <h2>
              Refreshingly Unique <br />
              Company About.
            </h2>
            <p>
              There are many variations of passages of Lorem Ipsum available,
              but the majority have suffered alteration of passages all are in
              some form.
            </p>
            <p>
              There are many variations of passages of Lorem Ipsum available,
              but the majority have suffered alteration of passages all are in
              some form.
            </p>
            <div
              class="story-btn  wow newFadeInUp"
              data-wow-duration="1s"
              data-wow-delay="1000ms"
            >
              <router-link to="/contact">Get Connected</router-link>
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
  </div>
</template>

<script>
  import Skills from "../../components/skill/Skills";
  export default {
    components: {
      Skills,
    },
    data() {
      return {
        aboutSrc: require("../../assets/img/portfolio/about-image.jpg"),
        skillSrc: require("../../assets/img/portfolio/my-skill.jpg"),
      };
    },
  };
</script>

<style lang="scss" scoped>
  .about-page {
    .rn-skill-right {
      @media only screen and (max-width: 767px) {
        order: 2;
      }
    }
  }
</style>
