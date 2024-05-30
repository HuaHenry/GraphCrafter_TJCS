<template>
  <div class="box-layout">
    <HeaderFour>
      <img slot="logo" src="../../assets/img/logo/portfolio.png" />
    </HeaderFour>

    <!-- Start Hero Area -->
    <SliderFour />
    <!-- Start Story Area -->

    <div class="mt--100 mt-sm-10">
      <About />
    </div>
    <!-- End Story Area -->

    <div
      class="rn-portfolio-area section-ptb-md rp-product-container5"
      id="portfolio"
    >
      <v-row class="row">
        <v-col lg="12">
          <div class="section-title-2 text-center mb--60 mb-sm-30">
            <h2>New Project</h2>
            <p>My work will prove my quality</p>
          </div>
        </v-col>
      </v-row>
      <PortfolioSix />
    </div>

    <Footer />
  </div>
</template>

<script>
  import HeaderFour from "../../components/header/HeaderFour";
  import SliderFour from "../../components/slider/SliderFour";
  import About from "../../components/about/About";
  import PortfolioSix from "../../components/portfolio/PortfolioSix";
  import Footer from "../../components/footer/Footer";
  export default {
    components: {
      HeaderFour,
      SliderFour,
      About,
      PortfolioSix,
      Footer,
    },
    data() {
      return {
        aboutSrc: require("../../assets/img/portfolio/about-image.jpg"),
      };
    },
  };
</script>

<style lang="scss" scoped>
  .box-layout {
    .-rn-footer {
      background: #f9f9f9;
    }
    header.header.header-flat {
      padding: 0;
    }
  }
</style>
<style lang="scss">
  .box-layout {
    header.header.header-flat,
    .v-toolbar__content {
      padding: 0;
    }
    .mt--100.mt-sm-10 {
      margin-top: 50px;
    }
  }
</style>
