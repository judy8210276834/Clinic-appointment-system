<template>
  <div class="breadCrumbs">
    <div v-for="(item, idx) in items" :key="idx">
      <router-link class="breadCrumbs_link" v-if="item.url" :to="item.url">{{
        item.label
      }}</router-link>
      <span class="breadCrumbs_nolink" v-else>{{ item.label }}</span>
      <span class="breadCrumbs_arrow" v-if="idx < items.length - 1">
        <fa icon="chevron-right" />
      </span>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    items: {
      type: Array,
    },
  },
};
</script>

<style scoped lang="scss">
@import "@/assets/_variables.scss";

.breadCrumbs {
  display: flex;
  font-size: 16px;
  color: $primaryDark;
  margin-bottom: 20px;

  .breadCrumbs_arrow {
    margin: 0 5px;
  }

  .breadCrumbs_link {
    text-decoration: none;
    color: $primaryDark;
    font-weight: bold;
  }

  .breadCrumbs_nolink {
    color: #81766fa0;
    font-weight: bold;
  }
}
</style>
