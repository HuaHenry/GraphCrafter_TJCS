<template>
  <div class="ms-container-wrapper">
    <div class="ms-left">
      <div
        class="ms-section bg_image "
        :style="{ backgroundImage: 'url(' + src + ')' }"
      ></div>
    </div>
    <div class="ms-right">
      <div class="ms-section ms-table">
        <div class="slipt-content-inner ms-tableCell slider rn-plr rn-ptb-100">
          <div class="content">
            <span>{{ heroContent.name }}!</span>
            <h2>{{ heroContent.title }}</h2>
            <p>
              {{ heroContent.desc }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        src: require("../../assets/img/slider/slider-6.jpg"),
        heroContent: {
          name: "Hello",
          title: "I’m Rainfo",
          desc: `There are many variations of passages of Lorem Ipsum available,
              but the majority have suffered alteration in some form.`,
        },
      };
    },
  };
</script>

<style lang="scss" scoped></style>
