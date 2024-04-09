<template>
  <div class="circle-container">
    <circle-progress
      :percent="40"
      :size="circleSize"
      fill-color="#A6BAAA"
      empty-color="#D0DDD3"
      :border-bg-width="10"
      :border-width="10"
    />
    <span class="center-text">{{ day }}</span>
  </div>

</template>

<script>
import "vue3-circle-progress/dist/circle-progress.css";
import CircleProgress from "vue3-circle-progress";
import { useWindowSize } from "@vueuse/core";
import { watchEffect, ref } from "vue";

export default {
  components: { CircleProgress },
  props: {
    day: {
      type: Number,
    },
  },
  setup() {
    const { width, height } = useWindowSize();
    const circleSize = ref(width.value <= 575 ? 33 : width.value <= 991 ? 50 : 66);

    return {
      circleSize
    }
  },
};
</script>

<style scoped>
.circle-container {
  position: relative;
  width: 66px;
  @media (max-width: 991px) {
    width: 50px;
  }
  @media (max-width: 575px) {
    width: 33px;
  }
}

.center-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 24px;
}
</style>
