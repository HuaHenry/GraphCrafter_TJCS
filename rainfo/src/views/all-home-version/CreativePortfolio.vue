<template>
  <div>
    <HeaderThree>
      <img slot="logo" src="../../assets/img/logo/portfolio.png" />
    </HeaderThree>
    <!-- Start Hero Area -->
    <div class="slider-area slide--5 bg_color--3" id="home">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="content text-center">
              <h1>Quality is our beauty.</h1>
              <p>
                There are many variations of passages of Lorem Ipsum available,
                but the majority have suffered alteration in some form, by
                injected humour, or randomised words which don't look even
                slightly believable. If you are going to use a passage of Lorem
                Ipsum, you need to be sure there.
              </p>
              <router-link to="#portfolio">Explore More</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- End Hero Area -->

    <div
      class="rn-portfolio-area section-ptb-md rp-product-container5"
      id="portfolio"
    >
      <v-container>
        <v-row class="row">
          <v-col lg="12">
            <div class="section-title-2 text-center mb--30">
              <h2>Our Portfolio</h2>
            </div>
          </v-col>
        </v-row>
        <PortfolioThree />
      </v-container>
    </div>

    <Awards />
    <News />

    <Footer />
  </div>
</template>

<script>
  import HeaderThree from "../../components/header/HeaderThree";
  import PortfolioThree from "../../components/portfolio/PortfolioThree";
  import Awards from "../../components/awards/Awards";
  import News from "../../components/news/News";
  import Footer from "../../components/footer/Footer";

  export default {
    components: {
      HeaderThree,
      PortfolioThree,
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
