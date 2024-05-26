<template>
  <div>
    <v-tabs v-model="tab" centered flat hide-slider color="primary">
      <v-tab :ripple="false" v-for="item in tabItems" :key="item.id">{{
        item.name
      }}</v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item v-for="item in tabContent" :key="item.id">
        <v-row
          class="portfolio-wrapper row--55 rn-custom-portfolio-wrapper rn-hil-portfolio"
          id="animated-thumbnials"
        >
          <v-col
            lg="4"
            md="4"
            sm="6"
            cols="12"
            v-for="(item, i) in item.content"
            :key="i"
            @click="index = i"
          >
            <a href="portfolio-details.html">
              <div class="portfolio" :class="item.imgClass">
                <div class="content">
                  <h4 class="title">{{ item.title }}</h4>
                  <span class="desc">{{ item.desc }}</span>
                </div>
                <div class="bgDescription"></div>
              </div>
            </a>
          </v-col>
        </v-row>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        tab: null,
        index: null,
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
                imgClass: "project-bg--1",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
              {
                imgClass: "project-bg--2",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
              {
                imgClass: "project-bg--3",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
              {
                imgClass: "project-bg--4",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
              {
                imgClass: "project-bg--5",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
              {
                imgClass: "project-bg--6",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
            ],
          },
          {
            id: 2,
            content: [
              {
                imgClass: "project-bg--4",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
              {
                imgClass: "project-bg--5",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
              {
                imgClass: "project-bg--6",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
            ],
          },
          {
            id: 3,
            content: [
              {
                imgClass: "project-bg--2",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
              {
                imgClass: "project-bg--4",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
            ],
          },
          {
            id: 4,
            content: [
              {
                imgClass: "project-bg--1",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
              {
                imgClass: "project-bg--3",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
              {
                imgClass: "project-bg--5",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
            ],
          },
          {
            id: 5,
            content: [
              {
                imgClass: "project-bg--4",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
              {
                imgClass: "project-bg--5",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
              {
                imgClass: "project-bg--6",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
            ],
          },
          {
            id: 6,
            content: [
              {
                imgClass: "project-bg--2",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
              {
                imgClass: "project-bg--4",
                title: `Mr. Joharuin Joly`,
                desc: "Photography",
              },
            ],
          },
        ],
      };
    },
  };
</script>
