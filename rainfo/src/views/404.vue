<template>
  <div>
    <!-- Start Header Area -->
    <HeaderFive>
      <img slot="logo" src="../assets/img/logo/portfolio.png" />
    </HeaderFive>
    <!-- End Header Area -->

    <!-- Start 404 Page  -->
    <div class="error-page-inner bg_color--3">
      <v-container>
        <v-row>
          <v-col cols="12">
            <div class="inner">
              <h1 class="heading-title theme-gradient">404!</h1>
              <h3 class="sub-title">Page not found</h3>
              <span>The page you were looking for could not be found.</span>
              <div class="error-button">
                <router-link to="/" class="rf-btn"
                  >Back To Homepage</router-link
                >
              </div>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <!-- End 404 Page  -->

    <FooterTwo />
  </div>
</template>

<script>
  import HeaderFive from "../components/header/HeaderFive";
  import FooterTwo from "../components/footer/FooterTwo";
  export default {
    components: {
      HeaderFive,
      FooterTwo,
    },
    data() {
      return {};
    },
  };
</script>

<style lang="scss" scoped></style>
