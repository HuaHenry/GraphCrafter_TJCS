<template>
  <div>
    <HeaderFive>
      <img slot="logo" src="../assets/img/logo/portfolio.png" />
    </HeaderFive>

    <!-- Start Bradcaump area -->
    <div class="bradcaump_area">
      <div
        class="bg-fixed bradcaump_area bg_image--12 static-breadcaump"
        data-black-overlay="5"
      >
        <v-container>
          <v-row>
            <v-col cols="12">
              <div class="text-center bradcaump_inner">
                <h2 class="bradcaump-title">Contact Us</h2>
                <p>
                  Communication can make hard work to easy. We are ready 24
                  hours to help you. If you want, you can send me message
                  without any hesitation.
                </p>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>
    <!-- End Bradcaump area -->

    <!-- Start Contact Area -->
    <div class="rf-contact-area ">
      <div class="contact-wrapper">
        <v-row align="center">
          <v-col lg="5" md="6" sm="12" cols="12">
            <ValidationObserver v-slot="{ handleSubmit }">
              <form @submit.prevent="handleSubmit(onSubmit)">
                <div class="form-wrapper">
                  <ValidationProvider
                    name="name"
                    rules="required"
                    v-slot="{ errors }"
                  >
                    <label>
                      <input
                        type="text"
                        v-model="formData.name"
                        placeholder="Your Name *"
                      />
                      <span class="inpur-error">{{ errors[0] }}</span>
                    </label>
                  </ValidationProvider>
                  <ValidationProvider
                    name="email"
                    rules="required|email"
                    v-slot="{ errors }"
                  >
                    <label>
                      <input
                        type="text"
                        rules="required|email"
                        v-model="formData.email"
                        placeholder="Your email *"
                      />
                      <span class="inpur-error">{{ errors[0] }}</span>
                    </label>
                  </ValidationProvider>
                  <ValidationProvider
                    name="subject"
                    rules="required"
                    v-slot="{ errors }"
                  >
                    <label>
                      <input
                        type="text"
                        v-model="formData.subject"
                        placeholder="Subject *"
                      />
                      <span class="inpur-error">{{ errors[0] }}</span>
                    </label>
                  </ValidationProvider>
                  <ValidationProvider
                    name="message"
                    rules="required"
                    v-slot="{ errors }"
                  >
                    <label>
                      <textarea
                        v-model="formData.message"
                        placeholder="Message *"
                      ></textarea>
                      <span class="inpur-error">{{ errors[0] }}</span>
                    </label>
                  </ValidationProvider>
                  <button type="submit">
                    <span>Submit</span>
                    <svg
                      fill="#000"
                      width="25"
                      height="8"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        d="M44.102 4l-2.444-2.445.009-1.405 4.325 4.325-4.38 4.38.01-1.423L44.101 5H.002V4z"
                        fill-rule="evenodd"
                      ></path>
                    </svg>
                  </button>
                </div>
              </form>
            </ValidationObserver>
            <div class="form-output">
              <p class="form-messege-active"></p>
            </div>
          </v-col>
          <v-col lg="7" md="6" sm="12" cols="12">
            <div class="contact-address">
              <h2 class="heading-title">Address</h2>
              <div
                class="address"
                v-for="(address, i) in addressContent"
                :key="i"
              >
                <i class="icon" v-html="iconSvg(address.icon)"></i>
                <div class="content">
                  <p v-if="address.isAddress">
                    {{ address.desc1 }} <br />
                    {{ address.desc2 }}
                  </p>
                  <p v-if="address.isNumber">
                    <a :href="address.to">{{ address.num1 }}</a>
                  </p>
                  <p v-if="address.isNumber">
                    <a :href="address.to">{{ address.num2 }}</a>
                  </p>
                  <p v-if="address.isMail">
                    <a :href="`mailto:${address.to}`">{{ address.mail }}</a>
                  </p>
                </div>
              </div>
            </div>
          </v-col>
        </v-row>
      </div>
    </div>
    <!-- End Contact Area -->

    <!-- Start Google MAp -->
    <div class="google-map">
      <div class="mapouter">
        <div class="gmap_canvas">
          <iframe
            id="gmap_canvas"
            src="https://maps.google.com/maps?q=Dhaka%20bangladesh&t=&z=13&ie=UTF8&iwloc=&output=embed"
            frameborder="0"
            scrolling="no"
            marginheight="0"
            marginwidth="0"
          ></iframe
          ><a href="https://embedgooglemap.net/maps/70"></a><br />
          <a href="https://www.embedgooglemap.net">google map code embed</a>
        </div>
      </div>
    </div>
    <!-- End Google MAp -->
    <Footer />
  </div>
</template>

<script>
  import HeaderFive from "../components/header/HeaderFive";
  import Footer from "../components/footer/Footer";
  import feather from "feather-icons";
  import { ValidationObserver } from "vee-validate";
  import { ValidationProvider } from "vee-validate/dist/vee-validate.full.esm";
  export default {
    components: {
      HeaderFive,
      Footer,
      ValidationObserver,
      ValidationProvider,
    },
    data() {
      return {
        formData: {
          name: "",
          email: "",
          subject: "",
          message: "",
        },
        addressContent: [
          {
            icon: "map-pin",
            desc1: "500 South Main Street",
            desc2: " Bishop, CA 93514 93514",
            isAddress: true,
          },
          {
            icon: "smartphone",
            num1: "+012 3344 556677",
            num2: "+012 3344 556677",
            to: "tel:0123344556677",
            isNumber: true,
          },
          {
            icon: "mail",
            mail: "example@gmail.com",
            to: "mailto:example@domain.com",
            isMail: true,
          },
        ],
      };
    },

    methods: {
      iconSvg(icon) {
        return feather.icons[icon].toSvg();
      },
      onSubmit() {
        console.log(this.formData);
      },
    },
  };
</script>

<style lang="scss" scoped>
  .inpur-error,
  .inpur-success {
    display: block;
    margin-top: 5px;
    font-size: 14px;
  }
  .inpur-error {
    color: #f10;
  }
  .gmap_canvas {
    overflow: hidden;
    background: none !important;
    height: 800px;
    width: 100%;

    iframe {
      width: 100%;
      height: 100%;
    }
  }
  .mapouter {
    position: relative;
    width: 100%;
    height: 100%;
  }
</style>
