<template>
    <BreadCrumbs :items="breadcrumbs" />
    <LoginSend />
  </template>
  
  <script>
  import BreadCrumbs from "@/components/BreadCrumbs.vue";
  import LoginSend from "@/components/LoginSend.vue";
  import { reactive } from "vue";
  export default {
    components: {
        LoginSend,
      BreadCrumbs
    },
    setup() {
      const breadcrumbs = reactive([
        {
          label: "預約日期",
          url: { name: "choose_date" },
        },
        {
          label: "醫生專區"
        }
      ]);
  
      return {
        breadcrumbs,
      };
    },
  };
  </script>
  
  <style></style>
  