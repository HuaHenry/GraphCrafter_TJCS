<template>
  <div>
    <HeaderTwo>
      <img slot="logo" src="../../assets/img/logo/rainfo-white.png" />
    </HeaderTwo>
    <SliderTwo />
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
  import HeaderTwo from "../../components/header/HeaderTwo";
  import SliderTwo from "../../components/slider/SliderTwo";
  import PortfolioTwo from "../../components/portfolio/PortfolioTwo";
  import Awards from "../../components/awards/Awards";
  import News from "../../components/news/News";
  import Footer from "../../components/footer/Footer";
  export default {
    components: {
      HeaderTwo,
      SliderTwo,
      PortfolioTwo,
      Awards,
      News,
      Footer,
    },
    data() {
      return {};
    },
  };
</script>

<style lang="scss" scoped></style>
