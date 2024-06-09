<script>
import TheButton from "@/components/TheButton.vue";
import { ref } from "vue";
import { useStore } from "vuex";
import { clearMsgAfterDelay } from "@/utils/clearMsgAfterDelay";
export default {
  components: {
    TheButton,
  },
  setup() {
    const store = useStore();
    const type = ref(true);
    const typeTitle = ref("登入");
    const typeButton = ref("註冊");
    const loginMsg = ref("");

    const typeChangeFunc = () => {
      type.value = !type.value; //true登入；false註冊
      typeTitle.value = type.value ? "登入" : "註冊";
      typeButton.value = type.value ? "註冊" : "登入";
    };

    const registerFunc = async () => {
      try {
        const response = await store.dispatch("postRegister", {
          name: "張洛慈",
          email: "aaa060903281@gmail.com",
          password: "aaa",
        });

        console.log("register ok:", response);
      } catch (err) {
        console.error("Registration failed:", err);
      }
    };

    const loginFunc = async () => {
      try {
        const response = await store.dispatch("getLogin", {
          email: "aaa060903281@gmail.com",
          password: "aaa",
        });

        if (response.data.result.status == "登入成功。") {
          loginMsg.value = response.data.result.loginMember;
        } else {
          loginMsg.value = response.data.result.err;
        }

        clearMsgAfterDelay(loginMsg, 3000);

      } catch (err) {
        console.error("login failed:", err);
      }
    };


    // registerFunc();

    return {
      type,
      typeChangeFunc,
      typeButton,
      typeTitle,
      loginMsg,
    };
  },
};
</script>

<template>
  <div class="loginsend">
    <div class="loginsend_container">
      <div class="loginsend_container_title_wrap">
        <p>醫生專區 - {{ typeTitle }}</p>
        <br />
        <span>{{ loginMsg }}</span>
      </div>

      <div class="loginsend_container_input_wrap">
        <div v-if="!type">
          <label for="people_count">姓名: </label>
          <input
            type="number"
            name="people_count"
            id="people_count"
            placeholder=" 請輸入人數..."
          />
        </div>
        <div>
          <label for="name">Email: </label>
          <input
            type="text"
            name="name"
            id="name"
            placeholder=" 請輸入姓名..."
          />
        </div>
        <div>
          <label for="phone">密碼: </label>
          <input
            type="number"
            name="phone"
            id="phone"
            placeholder=" 請輸入電話..."
          />
        </div>
        <div>
          <button class="loginsend_type_utton" @click="typeChangeFunc">
            {{ typeButton }}
          </button>
        </div>
      </div>
      <div class="loginsend_container_button_wrap">
        <TheButton :title="typeTitle" />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "@/assets/_variables.scss";
.loginsend {
  width: 100%;
  display: flex;
  justify-content: center;

  .loginsend_container {
    width: 350px;
    background-color: rgba(255, 255, 255, 0.2);
    padding: 80px;
    box-shadow: 5px 5px 5px rgba(128, 128, 128, 0.237);

    @media screen and (max-width: $small) {
      width: 100%;
      padding: 30px 40px;
    }

    .loginsend_container_title_wrap {
      text-align: center;
      font-size: 20px;
      color: $primaryDark;
    }
    .loginsend_container_input_wrap {
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
        .loginsend_type_utton {
          border: none;
          background: transparent;
          cursor: pointer;
          color: $primaryDark;
          border-bottom: 1px solid $primaryDark;
        }
      }
    }
    .loginsend_container_button_wrap {
      margin-top: 35px;
    }
  }
}
</style>
