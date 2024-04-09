<template>
  <BreadCrumbs :items="breadcrumbs" />
  <!-- <TheCircleProgress /> -->
  <div class="board">
    <fa icon="caret-left"/> 2023 07 <fa icon="caret-right"/>
    <Calendar />
  </div>
  

</template>

<script>
import TheCircleProgress from "../components/TheCircleProgress.vue";
import BreadCrumbs from "../components/BreadCrumbs.vue";
import Calendar from "../components/Calendar.vue";
import { reactive } from "vue";
export default {
  components: {
    TheCircleProgress,
    BreadCrumbs,
    Calendar
  },
  setup() {
    const breadcrumbs = reactive([
      {
        label: "預約日期",
        url: { name: "choose_date" },
      },
      {
        label: "預約時間",
        url: { name: "choose_time" },
      },
      {
        label: "報表",
      },
    ]);

    return {
      breadcrumbs,
    };
  },
};
</script>

<style lang="scss" scoped>
.board{
  background-color: white;
  height: 690px;
  margin-top: 20px;
  padding: 84px 120px;
  font-size: 24px;
  font-weight: bold;
  color: #81766fa0;
  text-align: center;
  @media (max-width: 991px) { padding: 60px 90px; height: 530px; }
  @media (max-width: 575px) { padding: 84px 20px; height: 400px; }
}
</style>
