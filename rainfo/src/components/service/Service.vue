<template>
  <!-- Start Service Area -->
  <div class="rn-service-area d-flex bg_color--3" id="service">
    <div class="rn-service-left w-50 rn-service-bg-wrapper">
      <v-fade-transition leave-absolute>
        <div
          v-if="activetab === 1"
          class="h-full rn-service-bg-wrapper"
          :style="{ backgroundImage: 'url(' + src1 + ')' }"
        ></div>
      </v-fade-transition>
      <v-fade-transition leave-absolute>
        <div
          v-if="activetab === 2"
          class="h-full rn-service-bg-wrapper"
          :style="{ backgroundImage: 'url(' + src2 + ')' }"
        ></div
      ></v-fade-transition>
      <v-fade-transition leave-absolute>
        <div
          v-if="activetab === 3"
          class="h-full rn-service-bg-wrapper"
          :style="{ backgroundImage: 'url(' + src3 + ')' }"
        ></div
      ></v-fade-transition>
      <v-fade-transition leave-absolute>
        <div
          v-if="activetab === 4"
          class="h-full rn-service-bg-wrapper"
          :style="{ backgroundImage: 'url(' + src4 + ')' }"
        ></div
      ></v-fade-transition>
    </div>

    <div class="rn-service-right w-50 d-flex align-items-center">
      <div class="text-left story-content rn-plr section-ptb-xl">
        <div class="content">
          <h2 class="section-title">Services</h2>
          <div class="service-wrapper">
            <!-- Start Single Service -->
            <div class="service">
              <h4
                @mouseover="activetab = 1"
                :class="[activetab === 1 ? 'active' : '']"
              >
                <router-link to="/service-details"
                  >User Experience Design</router-link
                >
              </h4>
              <p>There are many variations of passages of Lorem Ipsum</p>
            </div>
            <!-- End Single Service -->

            <!-- Start Single Service -->
            <div class="service">
              <h4
                @mouseover="activetab = 2"
                :class="[activetab === 2 ? 'active' : '']"
              >
                <router-link to="/service-details"
                  >Software Development</router-link
                >
              </h4>
              <p>The majority have suffered alteration in some form.</p>
            </div>
            <!-- End Single Service -->

            <!-- Start Single Service -->
            <div class="service">
              <h4
                @mouseover="activetab = 3"
                :class="[activetab === 3 ? 'active' : '']"
              >
                <router-link to="/service-details"
                  >Interfaces & Branding</router-link
                >
              </h4>
              <p>
                All the Lorem Ipsum generators on the Internet tend to repeat
                predefined.
              </p>
            </div>
            <!-- End Single Service -->

            <!-- Start Single Service -->
            <div class="service">
              <h4
                @mouseover="activetab = 4"
                :class="[activetab === 4 ? 'active' : '']"
              >
                <router-link to="/service-details"
                  >If you need Custom Service?</router-link
                >
              </h4>

              <p>
                Please <router-link to="/contact">Contact with us</router-link>
              </p>
            </div>
            <!-- End Single Service -->
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- End Service Area -->
</template>

<script>
  export default {
    data() {
      return {
        el: "#service",
        activetab: 1,
        src1: require("../../assets/img/service/services-1.jpg"),
        src2: require("../../assets/img/service/services-2.jpg"),
        src3: require("../../assets/img/service/services-3.jpg"),
        src4: require("../../assets/img/service/services-4.jpg"),
      };
    },
  };
</script>

<style lang="scss" scoped>
  .rn-service-area {
    overflow: hidden;
  }
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }
</style>
