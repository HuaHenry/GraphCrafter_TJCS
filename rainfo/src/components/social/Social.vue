<template>
  <div class="social-icon">
    <a
      v-for="(icon, i) in socialIconList"
      :key="i"
      :data-hover="icon.dataHover"
      :href="icon.url"
      target="_blank"
      >{{ icon.name }} <span class="circle"></span
    ></a>
  </div>
</template>

<script>
  export default {
    data() {
      return {
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
  };
</script>

<style lang="scss" scoped></style>
