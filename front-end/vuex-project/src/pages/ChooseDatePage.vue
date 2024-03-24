<template>
  
  <BreadCrumbs :items="breadcrumbs" />
  <!-- <TheCircleProgress /> -->
</template>

<script>
import TheCircleProgress from "../components/TheCircleProgress.vue";
import BreadCrumbs from "../components/BreadCrumbs.vue";
import { reactive } from "vue";
export default {
  components: {
    TheCircleProgress,
    BreadCrumbs,
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
        label: "報表"
      },
    ]);

    return {
        breadcrumbs
    }
  },
};
</script>

<style></style>
