<template>
  <div class="breadCrumbs">
    <div v-for="(item, idx) in items" :key="idx">
    <router-link class="breadLink" v-if="item.url" :to="item.url">{{ item.label }}</router-link>
    <span class="breadNonLink" v-else>{{ item.label }}</span>
    <span class="arrow" v-if="idx < items.length - 1"><fa icon="chevron-right" /></span>
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

<style lang="scss" scoped>
.breadCrumbs{
    display: flex;
    font-size: 16px;
    color: #81766F;
    .arrow{
        margin: 0 5px;
    }
    .breadLink{
        text-decoration: none;
        color: #81766F;
        font-weight: bold;
    }
    .breadNonLink{
        color: #81766fa0;
        font-weight: bold;
    }
}
</style>
