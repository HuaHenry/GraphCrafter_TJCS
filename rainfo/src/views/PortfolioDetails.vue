<template>
  <div class="portfolio-details-page">
    <HeaderFive>
      <img slot="logo" src="../assets/img/logo/portfolio.png" />
    </HeaderFive>

    <!-- Start Bradcaump area -->
    <div class="bradcaump_area">
      <div
        class="parallaxContainer paralaxbg--2 rn-bg-position-fixed"
        data-black-overlay="5"
      >
        <v-container>
          <v-row>
            <v-col cols="12">
              <div class="text-center bradcaump_inner">
                <h2 class="bradcaump-title">Mr. Jharuin joly</h2>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>
    <!-- End Bradcaump area -->

    <!-- Start Portfolio Details Area -->
    <div class="rf-portfolio-details section-ptb-xl">
      <v-container class="container">
        <v-row>
          <v-col sm="6" cols="12" class="pr--60 pr-md-15 pr-sm-15">
            <div class="rp-port-thumb">
              <div class="port-single-thumb">
                <img
                  src="../assets/img/portfolio/portfolio-single-1.jpg"
                  alt="portfolio"
                />
              </div>

              <div class="port-single-thumb mt--30">
                <img
                  src="../assets/img/portfolio/portfolio-single-2.jpg"
                  alt="portfolio"
                />
              </div>

              <div class="port-single-thumb mt--30">
                <img
                  src="../assets/img/portfolio/portfolio-single-3.jpg"
                  alt="portfolio"
                />
              </div>
            </div>
          </v-col>
          <v-col sm="6" cols="12">
            <div class="rp-port-details-inner sticky-top">
              <div class="content">
                <h3>Branding Portfolio Details.</h3>
                <p>
                  Etia reprimi no pri, vix no reque dolore di sentiet, vel at
                  wisi mazim feugiat. Ne ali quam apeirian mel, an ese choro
                  regione virtute per. iusto oporter and. Ius vitae parte repudi
                  andae, sed an harum simul dolor, pro reque graec.
                </p>
                <p>
                  Ne ali quam apeirian mel, an ese choro regione virtute per.
                  Etia reprimi no pri, vix no reque dolore di sentiet, vel at
                  wisi mazim feugiat.iusto oporter and. Ius vitae parte repudi
                  andae, sed an harum simul dolor, pro reque graec.
                </p>
                <div class="port-info">
                  <div class="port-meta">
                    <span>Date:</span>
                    <p>07.05.2020</p>
                  </div>

                  <div class="port-meta">
                    <span>Clients:</span>
                    <p>Rianbow Theme</p>
                  </div>

                  <div class="port-meta">
                    <span>Category:</span>
                    <p>Branding</p>
                  </div>
                </div>
              </div>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <!-- End Portfolio Details Area -->

    <Footer />
  </div>
</template>

<script>
  import HeaderFive from "../components/header/HeaderFive";
  import Footer from "../components/footer/Footer";
  export default {
    components: {
      HeaderFive,
      Footer,
    },
    data() {
      return {};
    },
  };
</script>

<style lang="scss" scoped>
  .portfolio-details-page .-rn-footer {
    background: #f9f9f9;
  }
</style>
