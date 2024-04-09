<template>
  <div class="footer">
    <div class="contain">
      <div class="qrcode">
        <img src="../assets/qrcode.png" alt="" />
      </div>
      <div class="text">
        <h6>營業時間 星期一 ~ 星期六</h6>
        <h6>電話 098765431</h6>
        <h6>地址 台北市內湖區</h6>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.footer {
  background-color: #a79d8e;
  width: 100%;
  height: 194px;
  display: flex;
  justify-content: center;
  .contain {
    margin: 20px;
    display: flex;
    gap: 40px;
    align-items: center;
    .text {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 77px;
      color: white;

      h6 {
        font-size: 16px;
      }
    }
  }
}
</style>
