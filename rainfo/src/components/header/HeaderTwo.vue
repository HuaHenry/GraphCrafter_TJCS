<template>
  <div id="home">
    <v-navigation-drawer
      class="hidden-md-and-up custom-navigation-drawer"
      v-model="drawer"
      fixed
      dark
      right
      temporary
      width="320"
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
      dark
      color="transparent"
      fixed
      elevate-on-scroll
      class="text-white header rn-header rn-header--withmenu header-transparent header-one-page-nav"
    >
      <router-link to="/" class="logo">
        <slot name="logo"></slot>
      </router-link>
      <!-- End brand logo -->
      <v-spacer></v-spacer>
      <v-app-bar-nav-icon
        class="hidden-md-and-up"
        @click="drawer = !drawer"
      ></v-app-bar-nav-icon>
      <!-- End mobile menu icon -->
      <v-toolbar-items
        class="hidden-xs-only hidden-sm-only height-auto mainmenu-wrap"
      >
        <scrollactive
          active-class="v-btn--active"
          bezier-easing-value=".5,0,.35,1"
          :offset="70"
          :duration="1000"
        >
          <v-btn
            v-for="item in items"
            :key="item.title"
            :to="item.to"
            link
            :ripple="false"
            text
            class="scrollactive-item"
            >{{ item.title }}</v-btn
          >
        </scrollactive>
        <div class="purchase-btn">
          <a target="_blank" href="https://themeforest.net/checkout/from_item/31671489?license=regular">
            Purchase Now
          </a>
        </div>
      </v-toolbar-items>
      <!-- End header menu item -->
    </v-app-bar>
    <!-- End top header navbar -->
  </div>
</template>

<script>
  export default {
    data: () => ({
      drawer: false,
      items: [
        { title: "Home", to: "#home" },
        { title: "Portfolio", to: "#portfolio" },
        { title: "Awards", to: "#awards" },
        { title: "News", to: "#blog" },
        { title: "Contact", to: "#footer" },
      ],
      icon: "menu",
    }),
    methods: {},
  };
</script>
