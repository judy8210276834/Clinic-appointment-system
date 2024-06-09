<template>
  <nav class="navbar">
    <router-link to="/" class="navbar_logo"><fa icon="house" /></router-link>
    <span>麥醫生針灸診所</span>
    <span>
      <router-link to="/booking_record" class="navbar_link"
        >預約紀錄</router-link
      >
      <router-link to="/login" class="login_link">醫生專區</router-link>
    </span>
  </nav>
</template>

<script>
export default {};
</script>

<style scoped lang="scss">
@import "@/assets/_variables.scss";

.navbar {
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: #d1cfc3;
  height: 80px;
  //   padding: 0 182px;
  color: $primaryDark;
  font-weight: bold;

  .navbar_logo,
  .navbar_link,
  .login_link {
    color: $primaryDark;
    text-decoration: none;
    margin-left: 20px;
  }
}
</style>
