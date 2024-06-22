<script>
import BreadDoctor from "../components/BreadDoctor.vue";
import BlankPage from "@/components/BlankPage.vue";
export default {
  components: {
    BreadDoctor,
    BlankPage,
  },
};
</script>
<template>
    <BreadDoctor />
    <BlankPage :title="'預約時間'" />
</template>

<style scoped lang="scss">
@import "@/assets/_variables.scss";
</style>
