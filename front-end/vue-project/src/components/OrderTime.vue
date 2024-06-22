<script>
import "vue3-circle-progress/dist/circle-progress.css";
import CircleProgress from "vue3-circle-progress";
import TheButton from "@/components/TheButton.vue";
export default {
  components: {
    CircleProgress,
    TheButton,
  },
  props: {
    time: {
      type: String,
      default: "15:00",
    },
  },
  setup() {
    const link = "/booking";

    return {
      link,
    };
  },
};
</script>

<template>
  <div class="ordertime">
    <div class="ordertime_circle_progress">
      <circle-progress
        :percent="40"
        :size="117"
        fill-color="#A6BAAA"
        empty-color="#D0DDD3"
        :border-bg-width="10"
        :border-width="10"
      />
      <span class="ordertime_title">{{ time }}</span>
    </div>

    <div class="ordertime_text">
      <p>總人數: 15人</p>
      <p>已預約: 5人</p>
      <p>可預約: 10人</p>
    </div>
    <router-link to="/booking"
      ><TheButton :title="'預約'"
    /></router-link>
  </div>
</template>

<style scoped lang="scss">
@import "@/assets/_variables.scss";

.ordertime {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: white;
  width: 225px;
  height: 446px;
  padding: 30px 0;
  color: rgba(0, 0, 0, 0.7);
  font-weight: 700;
  // gap: 20px;
  justify-content: center;

  @media screen and (max-width: $medium) {
    margin-top: 50px;
    gap: 20px;
    width: 45%;
  }

  @media screen and (max-width: $small) {
    margin-top: 30px;
    width: 100%;
  }

  .ordertime_circle_progress {
    position: relative;
    text-align: center;
    width: 117px;
    height: 117px;
    // background-color: aqua;
  }

  .ordertime_title {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    font-size: 24px;
  }

  .ordertime_text {
    text-align: center;
    margin-top: 40px;
    margin-bottom: 32px;
    font-size: 16px;
  }

  .ordertime_btn {
    text-align: center;
    button {
      width: 140px;
      height: 47px;
      border-style: none;
      background-color: $accentDark;
      color: white;
      border-radius: 5px;
      font-size: 20px;
      @media screen and (max-width: $medium) {
        width: 200px;
      }
      @media screen and (max-width: $small) {
        width: 250px;
      }
    }
  }
}
</style>
