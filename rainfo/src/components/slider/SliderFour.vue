<template>
  <!-- Start Single Slider -->
  <div>
    <div
      class="slider slider--3 ptb--200 pl--150 rfanimation-style--2"
      v-for="(slider, i) in sliderContent"
      :key="i"
      :class="slider.imgClass"
    >
      <v-container>
        <v-row>
          <v-col cols="12">
            <div class="content">
              <h3 class="heading-title">{{ slider.subTitle }}</h3>
              <h1>{{ slider.title }}</h1>
              <p class="description">
                {{ slider.desc }}
              </p>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <!-- End Single Slide  -->
  </div>
</template>

<script>
  export default {
    data() {
      return {
        sliderContent: [
          {
            imgClass: "bg_image--8",
            title: "Rainfo Creative Agency",
            subTitle: "Welcome",
            desc: `There are many variations of passages of Lorem Ipsum available 
                  but the majority have suffered alteration.`,
          },
        ],
      };
    },
  };
</script>

<style lang="scss">
  .slick-slide {
    img {
      display: block;
      width: 100%;
    }
  }
  @media only screen and (max-width: 575px) {
    .slider.slider--3 {
      padding: 100px 0;
    }
  }
</style>
