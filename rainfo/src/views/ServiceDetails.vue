<template>
  <div class="service-details-page">
    <HeaderFive>
      <img slot="logo" src="../assets/img/logo/portfolio.png" />
    </HeaderFive>

    <!-- Start Bradcaump area -->
    <div class="bradcaump_area">
      <div class="parallaxContainer paralaxbg--3" data-black-overlay="6">
        <v-container>
          <v-row>
            <v-col cols="12">
              <div class="text-center bradcaump_inner">
                <h2 class="bradcaump-title">
                  WEBSITE DEVELOPMENT
                </h2>
                <p>Fresh From The Press Discription</p>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>
    <!-- End Bradcaump area -->

    <!-- Start Service Details Area -->
    <div class="rf-service-details section-ptb-xl">
      <v-container class="container">
        <v-row class="mb--80">
          <v-col md="6" cols="12" class="pr--60 pr-md-15 pr-sm-15">
            <div class="rp-port-thumb">
              <div class="port-single-thumb">
                <img
                  src="../assets/img/portfolio/portfolio-single-1.jpg"
                  alt="portfolio"
                />
              </div>
            </div>
          </v-col>
          <v-col md="6" cols="12" class="">
            <div class="rp-port-details-inner">
              <div class="content">
                <p>
                  Etia reprimi no pri, vix no reque dolore di sentiet, vel at
                  wisi mazim feugiat. Ne ali quam apeirian mel, an ese choro
                  regione virtute per. iusto oporter and. Ius vitae parte repudi
                  andae, sed an harum simul dolor, pro reque graec.
                </p>
                <p>
                  Etia reprimi no pri, vix no reque dolore di sentiet, vel at
                  wisi mazim feugiat. Ne ali quam apeirian mel, an ese choro
                  regione virtute per. iusto oporter and.
                </p>
                <div class="mt--40">
                  <h4 class="heading-title">Proceess of metel</h4>
                  <ul class="liststyle bullet">
                    <li>Yet this above sewed flirted opened ouch</li>
                    <li>Goldfinch realistic sporadic ingenuous</li>
                    <li>
                      Abominable this abidin far successfully then like piquan
                    </li>
                    <li>Risus commodo viverra</li>
                    <li>Lorem ipsum dolor sit amet, consectetur adipiscing</li>
                  </ul>
                </div>
              </div>
            </div>
          </v-col>
        </v-row>
        <v-row>
          <v-col md="6" cols="12" order="2" order-lg="1">
            <div class="rp-port-details-inner">
              <div class="content">
                <p>
                  Etia reprimi no pri, vix no reque dolore di sentiet, vel at
                  wisi mazim feugiat. Ne ali quam apeirian mel, an ese choro
                  regione virtute per. iusto oporter and. Ius vitae parte repudi
                  andae, sed an harum simul dolor.
                </p>
                <div class="mt--40">
                  <h4 class="heading-title">Our Working Progress</h4>
                  <ul class="liststyle bullet">
                    <li>Yet this above sewed flirted opened ouch</li>
                    <li>Goldfinch realistic sporadic ingenuous</li>
                    <li>
                      Abominable this abidin far successfully then like piquan
                    </li>
                  </ul>
                </div>
                <p>
                  Etia reprimi no pri, vix no reque dolore di sentiet, vel at
                  wisi mazim feugiat. Ne ali quam apeirian mel, an ese choro
                  regione virtute per. iusto oporter and.
                </p>
              </div>
            </div>
          </v-col>
          <v-col md="6" cols="12" order-lg="2" class="pr--60 pr-md-15 pr-sm-15">
            <div class="rp-port-thumb">
              <div class="port-single-thumb">
                <img
                  src="../assets/img/portfolio/portfolio-single-2.jpg"
                  alt="portfolio"
                />
              </div>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <!-- End Service Details Area -->

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
  .service-details-page {
    .-rn-footer {
      background: #f9f9f9;
    }
    .rp-port-details-inner {
      p:last-child {
        margin-bottom: 0;
      }
    }
  }
</style>
