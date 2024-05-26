<template>
  <div class="masonry-wrapper">
    <div class="pt--45 pb--45 masonry-tabs">
      <v-tabs v-model="tab" centered flat hide-slider color="primary">
        <v-tab :ripple="false" v-for="item in tabItems" :key="item.id">{{
          item.name
        }}</v-tab>
      </v-tabs>
    </div>

    <v-tabs-items v-model="tab" no-animation>
      <v-tab-item
        v-for="item in tabContent"
        :key="item.id"
        transition="0"
        reverse-transition="0"
      >
        <vue-masonry-wall :items="item.content" :options="options">
          <template v-slot:default="{ item }">
            <div class="portfolio_style--3 Item">
              <div class="thumb">
                <router-link to="/portfolio-details">
                  <img :src="item.src" alt="personal portfolio"
                /></router-link>
                <div class="port-hover-action">
                  <div class="content">
                    <h3>
                      <router-link to="/portfolio-details">{{
                        item.title
                      }}</router-link>
                    </h3>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </vue-masonry-wall>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
  import VueMasonryWall from "vue-masonry-wall";
  export default {
    components: { VueMasonryWall },
    data() {
      return {
        tab: null,
        index: null,
        options: {
          width: 535,
          padding: {
            default: 7.5,
          },
        },
        tabItems: [
          {
            id: 1,
            name: "All",
          },
          {
            id: 2,
            name: "Fashion",
          },
          {
            id: 3,
            name: "Minimal",
          },
          {
            id: 4,
            name: "Photography",
          },
          {
            id: 5,
            name: "Black",
          },
          {
            id: 6,
            name: "Model",
          },
        ],
        tabContent: [
          {
            id: 1,
            content: [
              {
                src: require("../../assets/img/project/port-4/portfolio-1.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-2.jpg"),
                title: `Creative`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-3.jpg"),
                title: `Development`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-4.jpg"),
                title: `Motion Graphy`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-5.jpg"),
                title: `Minimal`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-6.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-7.jpg"),
                title: `Motion Graphy`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-8.jpg"),
                  title: `Development`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-9.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-10.jpg"),
                title: `Motion Graphy`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-11.jpg"),
                  title: `Development`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-12.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-13.jpg"),
                title: `Development`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-14.jpg"),
                title: `Motion Graphy`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-15.jpg"),
                title: `Creative`,
              },
            ],
          },
          {
            id: 2,
            content: [
              {
                src: require("../../assets/img/project/port-4/portfolio-4.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-5.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-6.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-7.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-8.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-9.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-10.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-11.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-12.jpg"),
                title: `Mr. Joharuin Joly`,
              },
            ],
          },
          {
            id: 3,
            content: [
              {
                src: require("../../assets/img/project/port-4/portfolio-8.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-9.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-10.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-11.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-12.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-13.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-14.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-15.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-16.jpg"),
                title: `Mr. Joharuin Joly`,
              },
            ],
          },
          {
            id: 4,
            content: [
              {
                src: require("../../assets/img/project/port-4/portfolio-4.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-5.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-6.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-7.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-8.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-9.jpg"),
                title: `Mr. Joharuin Joly`,
              },
            ],
          },
          {
            id: 5,
            content: [
              {
                src: require("../../assets/img/project/port-4/portfolio-8.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-9.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-10.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-11.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-12.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-13.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-14.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-15.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-16.jpg"),
                title: `Mr. Joharuin Joly`,
              },
            ],
          },
          {
            id: 6,
            content: [
              {
                src: require("../../assets/img/project/port-4/portfolio-4.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-5.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-6.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-7.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-8.jpg"),
                title: `Mr. Joharuin Joly`,
              },
              {
                src: require("../../assets/img/project/port-4/portfolio-9.jpg"),
                title: `Mr. Joharuin Joly`,
              },
            ],
          },
        ],
      };
    },
  };
</script>

<style scoped lang="scss">
  .Item {
    overflow: hidden;
    width: 100%;
    background: #f5f5f5;
  }

  img {
    object-fit: cover;
    width: 100%;
    height: 100%;
    line-height: 0;
    display: block;
  }
  .portfolio_style--3 {
    margin-bottom: 0;
  }
  .masonry-wall {
    flex-wrap: wrap;
  }
</style>
