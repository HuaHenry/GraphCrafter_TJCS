<template>
  <div class="parallax-home-page">
    <HeaderMultiPageRoute class="parallax-header">
      <img slot="logo" src="../../assets/img/logo/logo-circle-white.png" />
    </HeaderMultiPageRoute>

    <!-- Start Hero Area -->
    <div
      class="slider-area paralx-slider parallax fullscreen d-flex align-center rn-bg-position-fixed"
      :style="{ backgroundImage: 'url(' + src1 + ')' }"
    >
      <v-container>
        <v-row class="row">
          <v-col lg="12">
            <div class="text-center content">
              <h2>Development</h2>
              <p>
                There are many variations of passages of Lorem Ipsum available,
                <br />but the majority have suffered alteration.
              </p>
              <router-link class="mt--30 rf_btn" to="/contact"
                >Contact Us</router-link
              >
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <!-- End Hero Area -->

    <!-- Start Hero Area -->
    <div
      class="slider-area paralx-slider parallax fullscreen d-flex align-center rn-bg-position-fixed"
      :style="{ backgroundImage: 'url(' + src2 + ')' }"
    >
      <v-container>
        <v-row class="row">
          <v-col lg="12">
            <div class="text-center content">
              <h2>UX Research</h2>
              <p>
                There are many variations of passages of Lorem Ipsum available,
                <br />but the majority have suffered alteration.
              </p>
              <router-link class="mt--30 rf_btn" to="/contact"
                >Contact Us</router-link
              >
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <!-- End Hero Area -->

    <!-- Start Hero Area -->
    <div
      class="slider-area paralx-slider parallax fullscreen d-flex align-center rn-bg-position-fixed"
      :style="{ backgroundImage: 'url(' + src3 + ')' }"
    >
      <v-container>
        <v-row class="row">
          <v-col lg="12">
            <div class="text-center content">
              <h2>Visual Design</h2>
              <p>
                There are many variations of passages of Lorem Ipsum available,
                <br />but the majority have suffered alteration.
              </p>
              <router-link class="mt--30 rf_btn" to="/contact"
                >Contact Us</router-link
              >
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <!-- End Hero Area -->

    <!-- Start Hero Area -->
    <div
      class="slider-area paralx-slider parallax fullscreen d-flex align-center rn-bg-position-fixed"
      :style="{ backgroundImage: 'url(' + src4 + ')' }"
    >
      <v-container>
        <v-row class="row">
          <v-col lg="12">
            <div class="text-center content">
              <h2>Marketing</h2>
              <p>
                There are many variations of passages of Lorem Ipsum available,
                <br />but the majority have suffered alteration.
              </p>
              <router-link class="mt--30 rf_btn" to="/contact"
                >Contact Us</router-link
              >
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <!-- End Hero Area -->

    <Footer />
  </div>
</template>

<script>
  import HeaderMultiPageRoute from "../../components/header/HeaderMultiPageRoute";
  import Footer from "../../components/footer/Footer";
  export default {
    components: {
      HeaderMultiPageRoute,
      Footer,
    },
    data() {
      return {
        src1: require("../../assets/img/bg/bg-image-6.jpg"),
        src2: require("../../assets/img/bg/bg-image-4.jpg"),
        src3: require("../../assets/img/bg/bg-image-5.jpg"),
        src4: require("../../assets/img/bg/bg-image-7.jpg"),
      };
    },
  };
</script>

<style lang="scss" scoped>
  .parallax-home-page .logo {
    img {
      @media only screen and (max-width: 575px) {
        max-width: 80%;
      }
    }
  }
</style>
