<script>
import "vue3-circle-progress/dist/circle-progress.css";
import CircleProgress from "vue3-circle-progress";
import { useWindowSize } from "@vueuse/core";
import { watchEffect, ref, computed } from "vue";
import { useStore } from "vuex";

export default {
  components: { CircleProgress },
  props: {
    day: {
      type: Number,
    },
  },
  setup() {
    const { width, height } = useWindowSize();
    const store = useStore();

    const circleSize = computed(() => {
      return width.value <= 575 ? 33 : width.value <= 991 ? 50 : 66;
    });

    const isLoggedIn = computed(() => store.getters.getStatus);

    const targetLink = computed(() => {
    return isLoggedIn.value ? '/back_booking_record' : '/choose_time';
  });
    

    return {
      circleSize,
      isLoggedIn,
      targetLink
    };
  },
};
</script>
<template>
  <div class="thecircleprogress_container">
    <div class="thecircleprogress">
      <router-link :to="targetLink" class="thecircleprogress_link"
        ><circle-progress
          :percent="40"
          :size="circleSize"
          fill-color="#A6BAAA"
          empty-color="#D0DDD3"
          :border-bg-width="5"
          :border-width="5"
        />
        <span class="thecircleprogress_text">{{ day }}</span></router-link
      >
      <div v-has class="thecircleprogress_msg_alert">3</div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@import "@/assets/_variables.scss";

.thecircleprogress {
  cursor: pointer;
  position: relative;
  width: 66px;
  .thecircleprogress_link {
    color: $primaryMiddle;
  }
  @media (max-width: 991px) {
    width: 50px;
  }
  @media (max-width: 575px) {
    width: 33px;
  }
  .thecircleprogress_text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 24px;
    @media (max-width: 991px) {
      font-size: 16px;
    }
    @media (max-width: 575px) {
      font-size: 16px;
    }
  }
}

.thecircleprogress_msg_alert {
  position: absolute;
  width: 25px;
  height: 25px;
  background-color: #ca1b1b;
  font-size: 16px;
  color: white;
  border-radius: 50%;
  right: -6px;
  top: -6px;
  @media (max-width: 991px) {
    width: 20px;
    height: 20px;
    font-size: 14px;
  }
}
</style>
