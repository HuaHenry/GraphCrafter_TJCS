<template>
  <div>
    <HeaderMultiPageRoute>
      <img slot="logo" src="../../assets/img/logo/portfolio.png" />
    </HeaderMultiPageRoute>

    <hooper :settings="settings">
      <slide v-for="(slider, i) in sliderContent" :key="i">
        <div
          class="swiper-slide section slider-area fullscreen-slider fullscreen d-flex align-items-center bg_image award-content"
          :style="{ backgroundImage: 'url(' + slider.src + ')' }"
        >
          <v-container>
            <v-row class="d-flex fullscreen" align="center">
              <v-col cols="12">
                <div class="content text-center">
                  <h2>{{ slider.title }}</h2>
                  <p class="subtitle">
                    {{ slider.desc }}
                  </p>
                  <ul class="rn-award-list">
                    <li v-for="(item, i) in slider.awardList" :key="i">
                      <a :href="item.url"
                        >{{ item.name }} <span>- {{ item.result }}</span></a
                      >
                      {{ item.year }}
                    </li>
                  </ul>

                  <ul class="rn-award-list">
                    <li v-for="(item, i) in slider.contactInfo" :key="i">
                      {{ item.name }}
                      <a :href="item.to">{{ item.desc }}</a>
                    </li>
                  </ul>
                </div>
              </v-col>
            </v-row>
          </v-container>
        </div>
        <!-- End Hero Area -->
      </slide>
      <hooper-pagination slot="hooper-addons"></hooper-pagination>
    </hooper>
  </div>
</template>

<script>
  import HeaderMultiPageRoute from "../../components/header/HeaderMultiPageRoute";
  import { Hooper, Slide, Pagination as HooperPagination } from "hooper";

  export default {
    components: {
      HeaderMultiPageRoute,
      Hooper,
      Slide,
      HooperPagination,
    },
    data() {
      return {
        sliderContent: [
          {
            src: require("../../assets/img/slider-6/slider-1.jpg"),
            title: "Creative Agency",
            desc: ` There are many variations of passages of Lorem Ipsum available
                  but the majority have suffered alteration.`,
          },
          {
            src: require("../../assets/img/slider-6/slider-2.jpg"),
            title: "Our Story",
            desc: ` There are many variations of passages of Lorem Ipsum available
                  but the majority have suffered alteration.`,
          },
          {
            src: require("../../assets/img/slider-6/slider-3.jpg"),
            title: "Awards",
            desc: ` There are many variations of passages of Lorem Ipsum available
                  but the majority have suffered alteration.`,
            awardList: [
              {
                name: "Awwwards.com",
                result: "Winner",
                year: "2010 - 2011",
                url: "https://www.awwwards.com/",
              },
              {
                name: "CSS winner",
                result: "star",
                year: "2011 - 2012",
                url: "https://www.csswinner.com/",
              },
              {
                name: "Design nominees",
                result: "site of the day",
                year: "2013- 2014",
                url: "https://www.designnominees.com/",
              },
              {
                name: "CSS Design Awards",
                result: "Winner",
                year: "2015 - 2016",
                url: "https://www.cssdesignawards.com/",
              },
            ],
          },
          {
            src: require("../../assets/img/slider-6/slider-4.jpg"),
            title: "Contact US",
            desc: ` There are many variations of passages of Lorem Ipsum available
                  but the majority have suffered alteration.`,
            contactInfo: [
              {
                name: "Address",
                desc: "500 South Main Street Bishop, CA 93514",
                to: "",
              },
              {
                name: "Email Address",
                desc: "example@domain.com",
                to: "mailto:example@domain.com",
              },
              {
                name: "Hot Line",
                desc: "+012 3344 556677",
                to: "tel:+496170961709",
              },
            ],
          },
        ],
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

<style lang="scss" scoped>
  .subtitle {
    padding: 0 17%;
    @media only screen and (max-width: 767px) {
      padding: 0;
    }
  }
</style>
