<template>
  <!-- Footer -->
  <footer class="-rn-footer" id="footer">
    <div class="rn-footer-wrapper footer">
      <v-container fluid>
        <v-row>
          <v-col lg="12">
            <div class="footer-top">
              <div class="content">
                <span>Starting a project!</span>
                <h4>Contact Me</h4>
              </div>
            </div>
          </v-col>
        </v-row>
      </v-container>
      <div class="footer-wrapper ptb--100">
        <v-container fluid>
          <v-row>
            <!-- Start Single Wedget -->
            <v-col lg="3" md="3" sm="6" cols="12">
              <div class="footer-widget">
                <h3 class="ft-title">Present Address</h3>
                <div class="content">
                  <p>
                    500 South Main Street <br />
                    Bishop, CA 93514
                  </p>
                </div>
              </div>
            </v-col>
            <v-col lg="3" md="3" sm="6" cols="12">
              <div class="footer-widget">
                <h3 class="ft-title">Home Address</h3>
                <div class="content">
                  <p>400 South Main Street <br />Bishop, CA 93514</p>
                </div>
              </div>
            </v-col>
            <v-col lg="3" md="3" sm="6" cols="12">
              <div class="footer-widget">
                <h3 class="ft-title">Contact</h3>
                <div class="content">
                  <div class="address">
                    <p>
                      <a href="mailto:example@domain.com">example@domain.com</a>
                    </p>
                    <p><a href="tel:0123344556677">+012 3344 556677</a></p>
                  </div>
                </div>
              </div>
            </v-col>
            <v-col lg="3" md="3" sm="6" cols="12">
              <div class="footer-widget">
                <h3 class="ft-title">Quick Link</h3>
                <div class="content">
                  <ul class="quick-link">
                    <li v-for="(link, i) in quickLink" :key="i">
                      <router-link :to="link.RouteName">{{
                        link.name
                      }}</router-link>
                    </li>
                  </ul>
                </div>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>

    <FooterTwo />
  </footer>
  <!--// Footer -->
</template>

<script>
  import FooterTwo from "./FooterTwo";
  export default {
    components: {
      FooterTwo,
    },
    data() {
      return {
        quickLink: [
          {
            name: "Blog",
            RouteName: "/blog",
          },
          {
            name: "Service",
            RouteName: "service",
          },
          {
            name: "Portfolio",
            RouteName: "portfolio",
          },
        ],
      };
    },
  };
</script>

<style lang="scss" scoped></style>
