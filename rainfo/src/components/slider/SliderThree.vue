<template>
  <div class="slider-wrapper default-home-slider">
    <VueSlickCarousel v-bind="settings" class="slider-activation-with-slick">
      <div
        class="slide slider-container"
        v-for="(slider, i) in sliderContent"
        :key="i"
      >
        <div class="slider-inner">
          <div class="slide-content txt">
            <div class="txt-wrapper">
              <span class="copy">{{ slider.info }}</span>
              <h2 class="copy2">{{ slider.title }}</h2>
              <p class="excerpt copy3">{{ slider.desc }}</p>
              <ul class="social-icon hover-icon icon-position">
                <li>
                  <a
                    v-for="(icon, i) in slider.socialIconList"
                    :key="i"
                    :data-hover="icon.dataHover"
                    :href="icon.url"
                    target="_blank"
                    >{{ icon.name }} <span class="circle"></span
                  ></a>
                </li>
              </ul>
            </div>
          </div>

          <div class="slide-content img">
            <img :src="slider.src" alt="personal portfolio" />
          </div>
        </div>
      </div>
    </VueSlickCarousel>
  </div>
</template>

<script>
  import VueSlickCarousel from "vue-slick-carousel";
  // import Social from "../social/Social";
  export default {
    components: { VueSlickCarousel },
    data() {
      return {
        sliderContent: [
          {
            src: require("../../assets/img/slider/slider-1.jpg"),
            info: "Hello!",
            title: "I’m Ms. Rainfo",
            desc: `There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.`,
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
          },
          {
            src: require("../../assets/img/slider/slider-2.jpg"),
            info: "What I Do!",
            title: "Development",
            desc: `There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.`,
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
          },
          {
            src: require("../../assets/img/slider/slider-3.jpg"),
            info: "What I Do!",
            title: "UX Research",
            desc: `There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.`,
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
          },
          {
            src: require("../../assets/img/slider/slider-4.jpg"),
            info: "What I Do!",
            title: "Visual Design",
            desc: `There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.`,
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
          },
          {
            src: require("../../assets/img/slider/slider-5.jpg"),
            info: "What I Do!",
            title: "Development",
            desc: `There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form.`,
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
          },
        ],
        settings: {
          fade: true,
          dots: true,
          arrows: false,
          infinite: true,
          speed: 1000,
          slidesToShow: 1,
          slidesToScroll: 1,
          margin: 20,
        },
      };
    },
  };
</script>

<style lang="scss" scoped></style>
