<template>
  <BreadCrumbs :items="breadcrumbs" />
  <FormSend />
</template>

<script>
import BreadCrumbs from "@/components/BreadCrumbs.vue";
import FormSend from "@/components/FormSend.vue";
import { reactive } from "vue";
export default {
  components: {
    FormSend,
    BreadCrumbs
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
        label: "預約",
      },
    ]);

    return {
      breadcrumbs,
    };
  },
};
</script>

<style></style>
