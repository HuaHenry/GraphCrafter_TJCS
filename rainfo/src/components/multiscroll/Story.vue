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
        <div class="slipt-content-inner ms-tableCell rn-plr rn-ptb-100">
          <div class="story-content">
            <div class="text-left content">
              <h2 class="section-title">Our Story</h2>
              <p>
                There are many variations of passages of Lorem Ipsum available,
                but the majority have suffered alteration in some form.
              </p>
              <p>
                Vassages of Lorem Ipsum available the majority have suffered
                alteration.
              </p>
              <div class="story-btn">
                <router-link to="/designer-portfolio"
                  >SEE OUR PORTFOLIO</router-link
                >
              </div>
            </div>
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
        src: require("../../assets/img/portfolio/my-skill.jpg"),
      };
    },
  };
</script>

<style lang="scss" scoped></style>
