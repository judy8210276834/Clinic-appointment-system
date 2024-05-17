<template>
  <div class="layout_content">
    <slot></slot>
  </div>
</template>

<script>
export default {};
</script>

<style scoped lang="scss">
@import '@/assets/_variables.scss'; 

.layout_content {
  padding: 80px 128px 150px 128px;
  background-color: #c2bfaf;

  @media screen and (max-width: $medium) {
      padding: 60px 90px 100px 90px;
  }
  
  @media screen and (max-width: $small) {
      padding: 40px 20px 80px 20px;
  }

  
}
</style>
