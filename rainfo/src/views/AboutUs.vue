<template>
  <div>
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
                  About Us
                </h2>
                <p>Fresh From The Press Discription</p>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>
    <!-- End Bradcaump area -->
    <div class="about_page-main">
      <About />
      <!-- End About -->
    </div>

    <Footer />
    <!-- End Footer -->
  </div>
</template>

<script>
  import HeaderFive from "../components/header/HeaderFive";
  import About from "../components/about/About";
  import Footer from "../components/footer/Footer";
  export default {
    components: {
      HeaderFive,
      About,
      Footer
    },
    data() {
      return {};
    },
  };
</script>

<style lang="scss">
  .about_page-main {
    .content h2 {
      font-size: 36px;
      line-height: 1.5;
      margin-bottom: 28px;

      @media only screen and (max-width: 767px) {
        font-size: 26px;
      }
    }
  }
</style>
