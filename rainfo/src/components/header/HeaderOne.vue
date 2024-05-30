<template>
  <div id="home">
    <v-navigation-drawer
      class="custom-navigation-drawer"
      v-model="drawer"
      fixed
      right
      dark
      temporary
      width="50vw"
    >
      <scrollactive
        active-class="v-btn--active"
        bezier-easing-value=".5,0,.35,1"
        :offset="70"
        :duration="1000"
      >
        <v-list flat>
          <v-list-item
            :ripple="false"
            v-for="item in items"
            :key="item.title"
            :to="item.to"
            link
            class="scrollactive-item"
          >
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <!-- End mobile menu sidebar item list -->
        </v-list>
      </scrollactive>
      <div class="menu menu-toggle open" id="menu-toggle">
        <div class="menu-toggle-inner" @click="drawer = !drawer">
          <div class="menu-text-wrap">
            <span class="menu-text close-text">Close</span>
          </div>
          <div class="hamburger-wrap">
            <div id="hamburger">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        </div>
      </div>
    </v-navigation-drawer>
    <!-- End sidebar mobile menu -->

    <v-app-bar
      flat
      fixed
      color="transparent"
      class="header rn-header rn-header--withmenu header-transparent text-white main-default-header"
      height="70px"
    >
      <router-link to="/" class="logo">
        <slot name="logo"></slot>
      </router-link>
      <!-- End brand logo -->
      <v-spacer></v-spacer>
      <div class="menu menu-toggle" id="menu-toggle">
        <div class="menu-toggle-inner" @click="drawer = !drawer">
          <div class="menu-text-wrap">
            <span class="menu-text open-text">Menu</span>
          </div>
          <div class="hamburger-wrap">
            <div id="hamburger">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        </div>
      </div>
      <!-- End mobile menu icon -->
    </v-app-bar>
    <!-- End top header navbar -->
  </div>
</template>

<script>
  export default {
    data: () => ({
      drawer: false,
      items: [
        { title: "home", to: "#home" },
        { title: "about us", to: "#about" },
        { title: "best services", to: "#service" },
        { title: "awesome works", to: "#portfolio" },
        { title: "our awards", to: "#awards" },
        { title: "latest post", to: "#blog" },
        { title: "contact us", to: "#footer" },
      ],
      active: false,
    }),
    methods: {},
  };
</script>

<style lang="scss" scoped>
  .main-default-header {
    @media only screen and (max-width: 991px) {
      height: 70px !important;
    }
    &.v-app-bar--is-scrolled {
      background-color: #fff !important;
      box-shadow: 0 10px 40px 0 rgb(62 68 125 / 8%) !important;
    }
  }
  @media only screen and (max-width: 767px) {
    .rn-header.rn-header--withmenu.header-transparent.main-default-header {
      top: 0;
    }
  }
</style>
