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
          class="slipt-content-inner ms-tableCell story-content rn-plr rn-ptb-100"
        >
          <div class="content">
            <h2 class="section-title">Services</h2>
            <div class="service-wrapper">
              <!-- Start Single Service -->
              <div
                class="service"
                v-for="(service, i) in serviceContent"
                :key="i"
              >
                <h4>
                  <router-link :to="service.targetRoute">{{
                    service.title
                  }}</router-link>
                </h4>
                <p>
                  {{ service.desc }}
                </p>
                <h4 v-if="service.customService">
                  {{ service.customService }}
                </h4>
                <p v-if="service.lastItem">
                  Please
                  <router-link :to="service.contact">Contact us</router-link>
                </p>
              </div>
              <!-- End Single Service -->
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
        src: require("../../assets/img/service/services-1.jpg"),
        serviceContent: [
          {
            targetRoute: "/service-details",
            title: "User Experience Design",
            desc: `There are many variations of passages of Lorem Ipsum`,
          },
          {
            targetRoute: "/service-details",
            title: "Software Development",
            desc: `The majority have suffered alteration in some form.`,
          },
          {
            targetRoute: "/service-details",
            title: "Interfaces & Branding",
            desc: `All the Lorem Ipsum generators on the Internet tend to repeat
                  predefined.`,
          },
          {
            targetRoute: "/service-details",
            customService: "If you need Custom Service?",
            contact: "/contact",
            lastItem: true,
          },
        ],
      };
    },
  };
</script>

<style lang="scss" scoped></style>
