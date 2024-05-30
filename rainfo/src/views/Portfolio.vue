<template>
  <div class="portfolio-page">
    <HeaderFive>
      <img slot="logo" src="../assets/img/logo/portfolio.png" />
    </HeaderFive>
    <!-- End Header -->

    <!-- Start Bradcaump area -->
    <div class="bradcaump_area">
      <div class="parallaxContainer paralaxbg--3" data-black-overlay="6">
        <v-container>
          <v-row>
            <v-col cols="12">
              <div class="text-center bradcaump_inner">
                <h2 class="bradcaump-title">
                  Portfolio
                </h2>
                <p>Fresh From The Press Discription</p>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>
    <!-- End Bradcaump area -->

    <!-- Start Portfolio Area -->
    <div class="rn-portfolio-area section-ptb-100" id="portfolio">
      <v-container>
        <v-row>
          <v-col lg="12">
            <div class="section-title-2 text-center">
              <h2>Our Portfolio</h2>
              <p>My work will prove my quality</p>
            </div>
          </v-col>
        </v-row>
        <PortfolioFive />
      </v-container>
    </div>
    <!-- End Portfolio Area -->

    <Footer />
    <!-- End Footer -->
  </div>
</template>

<script>
  import HeaderFive from "../components/header/HeaderFive";
  import PortfolioFive from "../components/portfolio/PortfolioFive";
  import Footer from "../components/footer/Footer";
  export default {
    components: {
      HeaderFive,
      PortfolioFive,
      Footer,
    },
    data() {
      return {};
    },
  };
</script>

<style lang="scss">
  .rn-portfolio-area.section-ptb-100
    .masonry-tabs
    .v-slide-group__wrapper
    .v-slide-group__content {
    justify-content: center !important;
  }
  .portfolio-page .-rn-footer {
    background: #f9f9f9;
  }
</style>
