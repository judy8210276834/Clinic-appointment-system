<script>
export default {
  props: {
    title: {
      type: String,
      default: "網頁",
    },
  },
};
</script>

<template>
  <div class="blank">
    <h4>{{ title }}系統開發中。。。</h4>
  </div>
</template>

<style scoped lang="scss">
@import "@/assets/_variables.scss";
.blank {
  width: 100%;
  height: 300px;
  h4{
    color: $primaryDark;
  }
}
</style>
