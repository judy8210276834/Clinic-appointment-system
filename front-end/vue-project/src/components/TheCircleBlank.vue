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

<template>
  <div class="thecircleblank">
    <span class="thecircleblank_text">{{ day }}</span>
  </div>
</template>

<style scoped lang="scss">
@import "@/assets/_variables.scss";

.thecircleblank {
  position: relative;
  width: 66px;
  height: 66px;
  background-color: #d9d9d9;
  border-radius: 50%;
  @media screen and (max-width: $medium) {
    width: 50px;
    height: 50px;
  }

  @media screen and (max-width: $small) {
    width: 33px;
    height: 33px;
  }
}

.thecircleblank_text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 24px;
  @media screen and (max-width: $medium) {
    font-size: 16px;
  }

  @media screen and (max-width: $small) {
    font-size: 16px;
  }
}
</style>
