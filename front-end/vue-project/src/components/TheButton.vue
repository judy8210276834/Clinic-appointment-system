<script>
export default {
  props: {
    title: {
      type: String,
      default: "",
    },
    url: {
      type: String,
      default: "",
    },
  },
};
</script>

<template>
  <div class="button">
    <!-- <a v-if="url" :href="url">
      <button class="the-button">{{ title }}</button>
    </a>
    <button v-else>{{ title }}</button> -->
    <button>{{ title }}</button>
  </div>
</template>

<style scoped lang="scss">
@import "@/assets/_variables.scss";

.button {
  text-align: center;

  button {
    cursor: pointer;
    width: 140px;
    height: 47px;
    border-style: none;
    background-color: $accentDark;
    color: white;
    border-radius: 5px;
    font-size: 20px;
    @media screen and (max-width: $medium) {
      width: 200px;
    }
    @media screen and (max-width: $small) {
      width: 250px;
    }
  }
}
</style>
