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
                  Services
                </h2>
                <p>Fresh From The Press Discription</p>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>
    <!-- End Bradcaump area -->

    <div class="serive-page">
      <Service />
    </div>
    <!-- End About -->

    <Footer />
    <!-- End Footer -->
  </div>
</template>

<script>
  import HeaderFive from "../components/header/HeaderFive";
  import Service from "../components/service/Service";
  import Footer from "../components/footer/Footer";
  export default {
    components: {
      HeaderFive,
      Service,
      Footer,
    },
    data() {
      return {};
    },
  };
</script>

<style lang="scss" scoped></style>
