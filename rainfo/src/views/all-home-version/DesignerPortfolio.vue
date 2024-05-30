<template>
  <div class="designer-portfolio">
    <!-- Static Sidebar -->
    <div class="rf-sidebar sidebar--content">
      <div class="sidebar-wrapper">
        <div class="logo">
          <router-link to="/"> 
            <img
                src="../../assets/img/logo/logo-circle.png"
                alt="personal portfolio"
              />
            </router-link>
        </div>
        <div class="sidebar-social-icon">
          <ul class="social-icon hover-icon" :class="{ show: active }">
            <li v-for="(icon, i) in socialIconList" :key="i">
              <a :data-hover="icon.dataHover" :href="icon.url"
                >{{ icon.name }} <span class="circle"></span
              ></a>
            </li>
          </ul>

          <div class="icon-on-hover" :class="{ focus: active }">
            <span
              class="icon"
              @click="active = !active"
              :aria-pressed="active ? 'true' : 'false'"
              v-html="iconSvg(icon)"
            ></span>
          </div>
        </div>
      </div>
    </div>
    <!-- End Static Sidebar -->
    <div class="page-content sidebar--page--content rp-product-new">
      <PortfolioFive />
    </div>

    <Footer />
  </div>
</template>

<script>
  import PortfolioFive from "../../components/portfolio/PortfolioFive";
  import Footer from "../../components/footer/Footer";
  import feather from "feather-icons";
  export default {
    components: {
      PortfolioFive,
      Footer,
    },
    data() {
      return {
        active: false,
        icon: "more-horizontal",
        socialIconList: [
          {
            name: "FB",
            dataHover: "FB",
            url: "https://www.facebook.com/",
          },
          {
            name: "DB",
            dataHover: "DB",
            url: "https://dribbble.com/",
          },
          {
            name: "Be",
            dataHover: "Be",
            url: "https://www.behance.net/",
          },
          {
            name: "Tw",
            dataHover: "Tw",
            url: "https://twitter.com/",
          },
          {
            name: "Co",
            dataHover: "Co",
            url: "https://codepen.io/",
          },
        ],
      };
    },
    methods: {
      iconSvg(icon) {
        return feather.icons[icon].toSvg();
      },
    },
  };
</script>

<style lang="scss" scoped></style>
