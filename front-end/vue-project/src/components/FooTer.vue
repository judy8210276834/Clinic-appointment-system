<template>
  <footer>
    <div class="footer_container">
      <div class="qrcode">
        <img src="../assets/qrcode.png" alt="" />
      </div>
      <div class="footer_text">
        <h6>
          <router-link to="/back_choose_date" class="footer_login_link"
            >醫生專區</router-link
          >
        </h6>
        <h6>營業時間 星期一 ~ 星期六</h6>
        <h6>電話 098765431</h6>
        <h6>地址 台北市內湖區</h6>
      </div>
    </div>
  </footer>
</template>

<script>
export default {};
</script>
<style scoped lang="scss">
@import "@/assets/_variables.scss";

footer {
  background-color: #a79d8e;
  width: 100%;
  height: 194px;
  display: flex;
  justify-content: center;
  .footer_container {
    margin: 20px;
    display: flex;
    gap: 40px;
    align-items: center;
    .footer_text {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      color: white;

      h6 {
        font-size: 16px;
        .footer_login_link {
          color: $primaryDark;
        }
      }
    }
  }
}
</style>
