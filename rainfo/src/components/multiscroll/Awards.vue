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
        <div
          class="slipt-content-inner ms-tableCell award-content rn-plr rn-ptb-100"
        >
          <div class="content">
            <h2 class="section-title">Awards.</h2>

            <ul class="rn-award-list">
              <li v-for="(award, i) in awardContent" :key="i">
                <a :href="award.url" target="_blank"
                  >{{ award.name }} <span>- {{ award.position }}</span></a
                >
                {{ award.year }}
              </li>
            </ul>
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
        src: require("../../assets/img/award/awards-1.jpg"),
        awardContent: [
          {
            url: "https://www.awwwards.com/",
            name: "Awwwards.com",
            position: "Winner",
            year: " 2010 - 2011",
          },
          {
            url: "https://www.csswinner.com/",
            name: "CSS winner",
            position: "star",
            year: "2011 - 2012",
          },
          {
            url: "https://www.designnominees.com/",
            name: "Design nominees",
            position: "site of the day",
            year: "2013- 2014",
          },
          {
            url: "https://www.cssdesignawards.com/",
            name: "CSS Design Awards",
            position: "Winner",
            year: "2015 - 2016",
          },
          {
            url: "https://www.ux-design-awards.com/en",
            name: "UI/UX Design Awards",
            position: "Winner",
            year: "2016 - 2017",
          },
        ],
      };
    },
  };
</script>

<style lang="scss" scoped></style>
