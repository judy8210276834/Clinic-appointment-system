<template>
  <div class="circle-container">
    <circle-progress
      :percent="40"
      :size="66"
      fill-color="#A6BAAA"
      empty-color="#D0DDD3"
      :border-bg-width="10"
      :border-width="10"
    />
    <span class="center-text">1月</span>
  </div>
</template>

<script>
import "vue3-circle-progress/dist/circle-progress.css";
import CircleProgress from "vue3-circle-progress";
export default {
  components: { CircleProgress },
};
</script>

<style>
.circle-container {
  position: relative;
}

.center-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
