<template>
  <div class="freelancer-page">
    <HeaderTwo>
      <img slot="logo" src="../../assets/img/logo/rainfo-circle-color.png" />
    </HeaderTwo>
    <SliderOne />
    <!-- Start Portfolio Area -->
    <div class="rn-portfolio-area section-ptb-xl" id="portfolio">
      <v-container>
        <v-row>
          <v-col lg="12">
            <div class="section-title-2 text-center">
              <h2>Our Portfolio</h2>
              <p>My work will prove my quality</p>
            </div>
          </v-col>
        </v-row>
        <Portfolio />
      </v-container>
    </div>
    <!-- End Portfolio Area -->

    <Awards />
    <News />
    <Footer />
  </div>
</template>

<script>
  import HeaderTwo from "../../components/header/HeaderTwo";
  import SliderOne from "../../components/slider/SliderOne";
  import Portfolio from "../../components/portfolio/Portfolio";
  import Awards from "../../components/awards/Awards";
  import News from "../../components/news/News";
  import Footer from "../../components/footer/Footer";
  export default {
    components: {
      HeaderTwo,
      SliderOne,
      Portfolio,
      Awards,
      News,
      Footer,
    },
    data() {
      return {};
    },
  };
</script>

<style lang="scss" scoped>
  .freelancer-page .logo {
    img {
      @media only screen and (max-width: 575px) {
        max-width: 80%;
      }
    }
  }
</style>
