<template>
  <nav class="navbar">
    <router-link to="/" class="logo"><fa icon="house" /></router-link>
    <span>麥醫生針灸診所</span>
    <router-link to="/booking_record" class="booking_record_link">預約紀錄</router-link>
  </nav>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.navbar {
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: #d1cfc3;
  height: 80px;
//   padding: 0 182px;
  color: #81766f;
  font-weight: bold;

  .logo,.booking_record_link{
    color: #81766f;
    text-decoration: none; 
  }
}
</style>
