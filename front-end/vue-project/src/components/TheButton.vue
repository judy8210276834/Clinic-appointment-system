<script>
export default {};
</script>

<template>
    <div class="button">
        <button>預約</button>
    </div>
  
</template>

<style scoped lang="scss">
@import "@/assets/_variables.scss";

.button {
    text-align: center;
    button {
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
