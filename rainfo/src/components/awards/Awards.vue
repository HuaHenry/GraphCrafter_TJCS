<template>
    <!-- Start Awards Area ¸ü¶àÏÂÔØ£ºHttp://www.bootstrapmb.com -->
    <div class="rn-award-area d-flex bg_color--3" id="awards">
        <div class="rn-award-left w-50 ">
            <v-fade-transition leave-absolute>
                <div v-if="activetab === 1"
                     class="h-full rn-images-bg-wrapper"
                     :style="{ backgroundImage: 'url(' + src1 + ')' }"></div>
            </v-fade-transition>
            <v-fade-transition leave-absolute>
                <div v-if="activetab === 2"
                     class="h-full rn-images-bg-wrapper"
                     :style="{ backgroundImage: 'url(' + src2 + ')' }"></div>
            </v-fade-transition>
            <v-fade-transition leave-absolute>
                <div v-if="activetab === 3"
                     class="h-full rn-images-bg-wrapper"
                     :style="{ backgroundImage: 'url(' + src3 + ')' }"></div>
            </v-fade-transition>
            <v-fade-transition leave-absolute>
                <div v-if="activetab === 4"
                     class="h-full rn-images-bg-wrapper"
                     :style="{ backgroundImage: 'url(' + src4 + ')' }"></div>
            </v-fade-transition>
            <v-fade-transition leave-absolute>
                <div v-if="activetab === 5"
                     class="h-full rn-images-bg-wrapper"
                     :style="{ backgroundImage: 'url(' + src2 + ')' }"></div>
            </v-fade-transition>
        </div>
        <div class="rn-award-right w-50 d-flex align-items-center">
            <div class="text-left award-content rn-plr section-ptb-xl">
                <div class="content">
                    <h2 class="section-title">Awards.</h2>

                    <ul class="tabs rn-award-list">
                        <li>
                            <a @mouseover="activetab = 1"
                               :class="[activetab === 1 ? 'active' : '']"
                               href="https://www.awwwards.com/"
                               target="_blank">Awwwards.com <span>- Winner</span></a>
                            2010 - 2011
                        </li>
                        <li>
                            <a @mouseover="activetab = 2"
                               :class="[activetab === 2 ? 'active' : '']"
                               href="https://www.csswinner.com/"
                               target="_blank">CSS winner <span>- star</span></a>
                            2011 - 2012
                        </li>
                        <li>
                            <a @mouseover="activetab = 3"
                               :class="[activetab === 3 ? 'active' : '']"
                               href="https://www.designnominees.com/"
                               target="_blank">Design nominees <span>- site of the day</span></a>
                            2013- 2014
                        </li>
                        <li>
                            <a @mouseover="activetab = 4"
                               :class="[activetab === 4 ? 'active' : '']"
                               href="https://www.cssdesignawards.com/"
                               target="_blank">CSS Design Awards <span>- Winner</span></a>
                            2015 - 2016
                        </li>
                        <li>
                            <a @mouseover="activetab = 5"
                               :class="[activetab === 5 ? 'active' : '']"
                               href="https://www.ux-design-awards.com/en"
                               target="_blank">UI/UX Design Awards <span>- Winner</span></a>
                            2016 - 2017
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    <!-- End Awards Area -->
</template>

<script>
  export default {
    data() {
      return {
        el: "#award",
        activetab: 1,
        src1: require("../../assets/img/award/awards-1.jpg"),
        src2: require("../../assets/img/award/awards-2.jpg"),
        src3: require("../../assets/img/award/awards-3.jpg"),
        src4: require("../../assets/img/award/awards-4.jpg"),
      };
    },
  };
</script>

<style lang="scss" scoped>
  .rn-award-area {
    overflow: hidden;
  }
  .award-content ul.rn-award-list li a:focus {
    outline: none;
  }
</style>
