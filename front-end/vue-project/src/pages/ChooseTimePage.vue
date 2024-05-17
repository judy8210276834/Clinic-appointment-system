<script>
import OrderTime from "@/components/OrderTime.vue";
import BreadCrumbs from "@/components/BreadCrumbs.vue";
import { reactive } from "vue";
export default {
  components: {
    OrderTime,
    BreadCrumbs
  },
   setup(){
    const breadcrumbs = reactive([
      {
        label: "預約日期",
        url: { name: "choose_date" },
      },{
        label: "預約時間"
      },
      // {
      //   label: "預約時間",
      //   url: { name: "choose_time" },
      // },
      // {
      //   label: "報表",
      // },
    ]);
    const time_arr = reactive(['15:00','16:00','17:00','18:00']);

    return {
      breadcrumbs,
      time_arr
    }
   }
};
</script>

<template>
  <BreadCrumbs :items="breadcrumbs" />
  <div class="choosetime_page_container">
    <OrderTime v-for="time in time_arr" :time="time" />
  </div>
</template>

<style scoped lang="scss">
@import "@/assets/_variables.scss";

.choosetime_page_container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;

}
</style>
