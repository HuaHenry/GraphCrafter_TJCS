<template>
  <div>
    <HeaderMultiPageRoute>
      <img slot="logo" src="../../assets/img/logo/portfolio.png" />
    </HeaderMultiPageRoute>
    <!-- End Header -->

    <hooper :settings="settings" class="multiscroll-slider-wrapper">
      <slide>
        <Banner />
      </slide>
      <slide>
        <Story />
      </slide>
      <slide>
        <Awards />
      </slide>
      <slide>
        <Services />
      </slide>
      <slide>
        <Blog />
      </slide>
      <slide>
        <Contact />
      </slide>
      <hooper-pagination slot="hooper-addons"></hooper-pagination>
    </hooper>
    <!-- End hooper slider content -->
  </div>
</template>

<script>
  import HeaderMultiPageRoute from "../../components/header/HeaderMultiPageRoute";
  import Banner from "../../components/multiscroll/Banner";
  import Story from "../../components/multiscroll/Story";
  import Awards from "../../components/multiscroll/Awards";
  import Services from "../../components/multiscroll/Services";
  import Blog from "../../components/multiscroll/Blog";
  import Contact from "../../components/multiscroll/Contact";
  import { Hooper, Slide, Pagination as HooperPagination } from "hooper";

  export default {
    components: {
      HeaderMultiPageRoute,
      Hooper,
      Slide,
      HooperPagination,
      Banner,
      Story,
      Awards,
      Services,
      Blog,
      Contact,
    },
    data() {
      return {
        settings: {
          vertical: true,
          mouseDrag: false,
          infiniteScroll: true,
          transition: 800,
        },
      };
    },
  };
</script>

<style lang="scss">
  .ms-right,
  .ms-section.ms-table,
  .ms-tableCell {
    height: 100%;
  }
  .ms-section.ms-table {
    display: table;
    width: 100%;
  }
  .ms-tableCell {
    display: table-cell;
    vertical-align: middle;
    width: 100%;
  }
  .ms-container-wrapper {
    display: flex;
    height: 100vh;

    .ms-left {
      flex: 0 0 50%;
      max-width: 50%;
      @media only screen and (max-width: 1199px) {
        flex: 0 0 100%;
        max-width: 100%;
      }
    }
    .ms-right {
      flex: 0 0 50%;
      max-width: 50%;
      @media only screen and (max-width: 1199px) {
        flex: 0 0 100%;
        max-width: 100%;
        position: absolute;
        width: 100%;
        height: 100vh;
        background: rgba(255, 255, 255, 0.6);
      }
    }
    .ms-section {
      height: 100%;
    }
  }
  .multiscroll-slider-wrapper.hooper {
    @media only screen and (max-width: 767px) {
      .hooper-indicators {
        display: none;
      }
    }
    .hooper-pagination.is-vertical {
      @media only screen and (max-width: 1199px) {
        right: 15px;
        padding: 0;
      }
    }
  }
  .multiscroll-slider-wrapper
    .hooper-pagination.is-vertical
    .hooper-indicator::after,
  .multiscroll-slider-wrapper .hooper-pagination.is-vertical .hooper-indicator {
    transition: all 0.5s ease-in-out;
  }
</style>
