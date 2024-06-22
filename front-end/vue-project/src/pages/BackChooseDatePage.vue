<script>
import TheCircleProgress from "../components/TheCircleProgress.vue";
import BreadDoctor from "../components/BreadDoctor.vue";
import Calendar from "../components/Calendar.vue";
import { reactive, ref } from "vue";
export default {
  components: {
    TheCircleProgress,
    BreadDoctor,
    Calendar,
  },
  setup() {
    const currentDate = new Date();
    const year = ref(currentDate.getFullYear());
    const month = ref(currentDate.getMonth() + 1);

    const addMonth = () => {
      month.value++;
      if (month.value > 12) {
        month.value = 1;
        year.value++;
      }
    };

    const minusMonth = () => {
      month.value--;
      if (month.value < 1) {
        month.value = 12;
        year.value--;
      }
    };

    return {
      year,
      month,
      addMonth,
      minusMonth,
    };
  },
};
</script>

<template>
  <BreadDoctor />
  <!-- <TheCircleProgress /> -->
  <div class="choosedate_page_board">
    <fa
      class="choosedate_page_minusMonth"
      icon="caret-left"
      @click="minusMonth"
    />
    <span>{{ year }}</span> ． <span>{{ month }}</span>
    <fa class="choosedate_page_addMonth" icon="caret-right" @click="addMonth" />
    <Calendar :year="year" :month="month" />
  </div>
</template>

<style scoped lang="scss">
@import "@/assets/_variables.scss";

.choosedate_page_board {
  background-color: white;
  // height: 690px;
  padding: 84px;
  font-size: 24px;
  font-weight: bold;
  color: $primaryMiddle;
  text-align: center;

  .choosedate_page_minusMonth,
  .choosedate_page_addMonth {
    cursor: pointer;
    font-size: 18px;
    margin: 0 15px;
  }

  @media screen and (max-width: $medium) {
    padding: 84px;
    height: 530px;
    font-size: 20px;
  }

  @media screen and (max-width: $small) {
    padding: 40px;
    height: 400px;
    font-size: 20px;
  }
}
</style>
