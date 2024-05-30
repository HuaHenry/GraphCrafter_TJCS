<template>
  <v-app id="inspire">
    <v-main>
      <router-view></router-view>
    </v-main>
    <v-fab-transition>
      <div
        class="scrolltop-wrapper"
        v-show="fab"
        v-scroll="onScroll"
        @click="toTop"
      >
        <div class="scrolltotop">
          <div class="arrow-top"></div>
          <div class="arrow-top-line"></div>
        </div>
      </div>
    </v-fab-transition>
  </v-app>
</template>

<script>
  export default {
    data() {
      return {
        fab: false,
      };
    },

    methods: {
      onScroll(e) {
        if (typeof window === "undefined") return;
        const top = window.pageYOffset || e.target.scrollTop || 0;
        this.fab = top > 60;
      },
      toTop() {
        this.$vuetify.goTo(0);
      },
    },
  };
</script>

<style scoped>
  .scrolltop-wrapper {
    position: fixed;
    right: 30px;
    top: auto;
    bottom: 50px;
  }
  .hidden {
    opacity: 0;
  }

  .hidden-right {
    transform: translate(50px, 0);
  }

  .hidden-left {
    transform: translate(-50px, 0);
  }

  .showElement {
    opacity: 1;
    transform: translate(0, 0);
    -webkit-transition: all 0.5s ease-out;
    -moz-transition: all 0.5s ease-out;
    transition: all 0.5s ease-out;
  }
</style>
