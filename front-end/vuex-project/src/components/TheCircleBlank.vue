<template>
  <div class="circle-container">
    <div class="blank"></div>
    <span class="center-text">{{ day }}</span>
  </div>
</template>

<script>
import "vue3-circle-progress/dist/circle-progress.css";
import CircleProgress from "vue3-circle-progress";
export default {
  components: { CircleProgress },
  props: {
    day: {
      type: Number,
    },
  },
};
</script>

<style scoped>
.circle-container {
  position: relative;
  width: 66px;
  height: 66px;
  background-color: #d9d9d9;
  border-radius: 50%;
  @media (max-width: 991px) {
    width: 50px;
    height: 50px;
  }
  @media (max-width: 575px) {
    width: 33px;
    height: 33px;
  }
}

.center-text {
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
</style>
