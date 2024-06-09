<script>
import TheButton from "@/components/TheButton.vue";
export default {
  components: {
    TheButton,
  },
};
</script>

<template>
  <div class="formsend">
    <div class="formsend_container">
      <div class="formsend_container_title_wrap">
        <p>2023.12.07 (四)</p>
        <p>15:00</p>
      </div>

      <div class="formsend_container_input_wrap">
        <div>
          <label for="people_count">人數: </label>
          <input
            type="number"
            name="people_count"
            id="people_count"
            placeholder=" 請輸入人數..."
          />
        </div>
        <div>
          <label for="name">姓名: </label>
          <input
            type="text"
            name="name"
            id="name"
            placeholder=" 請輸入姓名..."
          />
        </div>
        <div>
          <label for="phone">電話: </label>
          <input
            type="number"
            name="phone"
            id="phone"
            placeholder=" 請輸入電話..."
          />
        </div>
      </div>
      <div class="formsend_container_button_wrap">
        <TheButton :title="'預約'" />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "@/assets/_variables.scss";
.formsend {
  width: 100%;
  // height: 500px;
  display: flex;
  justify-content: center;

  .formsend_container {
    width: 350px;
    background-color: rgba(255, 255, 255, 0.2);
    padding: 80px;
    box-shadow: 5px 5px 5px rgba(128, 128, 128, 0.237);

    @media screen and (max-width: $small) {
      width: 100%;
      padding: 30px 40px;
    }

    .formsend_container_title_wrap {
      text-align: center;
      font-size: 20px;
      color: $primaryDark;
    }
    .formsend_container_input_wrap {
      font-size: 20px;
      color: $primaryDark;
      margin-top: 30px;
      div {
        margin-top: 10px;
        input {
          width: 100%;
          height: 40px;
          font-size: 16px;
          border: none;
          color: $primaryDark;
          margin-top: 8px;
        }
      }
    }
    .formsend_container_button_wrap {
      margin-top: 35px;
    }
  }
}
</style>
