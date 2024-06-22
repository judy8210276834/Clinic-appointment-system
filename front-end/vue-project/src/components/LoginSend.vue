<script>
import TheButton from "@/components/TheButton.vue";
import { reactive, ref, watch, computed } from "vue";
import { useStore } from "vuex";
import { clearMsgAfterDelay } from "@/utils/clearMsgAfterDelay";
import { validateForm, clearErrorsMsg } from "@/utils/validateCheck";
import { useRouter } from "vue-router";
export default {
  components: {
    TheButton,
  },
  setup() {
    const store = useStore();
    const router = useRouter();
    const type = ref(true);
    const typeTitle = ref("登入");
    const typeButton = ref("註冊");
    const loginMsg = ref("");
    const userData = reactive({
      name: "",
      email: "",
      password: "",
    });
    const errors = reactive({
      name: "",
      email: "",
      password: "",
    });

    const status = computed(() => store.getters.getStatus);
    const getMsg = computed(() => store.getters.getMsg);

    watch(errors, (n, o) => {
      console.log(n);
    });
    const typeChangeFunc = () => {
      clearErrorsMsg(errors);
      clearUserData();
      store.commit("setMsg", "");

      type.value = !type.value; //true登入；false註冊
      typeTitle.value = type.value ? "登入" : "註冊";
      typeButton.value = type.value ? "註冊" : "登入";
    };

    const registerFunc = async () => {
      if (!validateForm(type.value, userData, errors)) return;

      try {
        const response = await store.dispatch("postRegister", {
          name: userData.name,
          email: userData.email,
          password: userData.password,
        });

        await clearMsgAfterDelay(3000);
      } catch (err) {
        console.error("Registration failed:", err);
      }
    };

    const loginFunc = async () => {
      if (!validateForm(type.value, userData, errors)) return;

      try {
        const response = await store.dispatch("getLogin", {
          email: userData.email,
          password: userData.password,
        });

        if (status.value == true) {
          await clearMsgAfterDelay(3000);
          router.push("/back_choose_date");
        }
        
      } catch (err) {
        console.error("login failed:", err);
      }
    };

    const clearUserData = () => {
      userData.name = "";
      userData.email = "";
      userData.password = "";
    };

    // registerFunc();

    return {
      type,
      typeChangeFunc,
      typeButton,
      typeTitle,
      loginMsg,
      userData,
      registerFunc,
      loginFunc,
      errors,
      getMsg,
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
        <span>{{ getMsg }}</span>
      </div>

      <div class="loginsend_container_input_wrap">
        <form>
          <div v-if="!type">
            <label for="name">姓名: </label
            ><span class="loginsend_err_msg">{{ errors.name }}</span>
            <input
              v-model="userData.name"
              type="text"
              name="name"
              id="name"
              placeholder=" 請輸入姓名..."
              autocomplete="name"
            />
          </div>
          <div>
            <label for="email">Email: </label
            ><span class="loginsend_err_msg">{{ errors.email }}</span>
            <input
              v-model="userData.email"
              type="text"
              name="email"
              id="email"
              placeholder=" 請輸入Email..."
              autocomplete="email"
            />
          </div>
          <div>
            <label for="password">密碼: </label
            ><span class="loginsend_err_msg">{{ errors.password }}</span>
            <input
              v-model="userData.password"
              type="password"
              name="password"
              id="password"
              placeholder=" 請輸入密碼..."
              autocomplete="password"
            />
          </div>
          <div>
            <button
              @click.prevent="typeChangeFunc()"
              class="loginsend_type_btn"
            >
              {{ typeButton }}
            </button>
          </div>
        </form>
      </div>
      <div
        @click="type ? loginFunc() : registerFunc()"
        class="loginsend_container_button_wrap"
      >
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
        .loginsend_err_msg {
          color: red;
          font-size: 12px;
        }
        input {
          width: 100%;
          height: 40px;
          font-size: 16px;
          border: none;
          color: $primaryDark;
          margin-top: 8px;
        }
        .loginsend_type_btn {
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
