<script>
import { useStore } from "vuex";
import { computed } from "vue";
import { clearMsgAfterDelay } from "@/utils/clearMsgAfterDelay";
import { useRouter } from "vue-router";

export default {
  setup() {
    const store = useStore();
    const router = useRouter();

    const status = computed(() => store.getters.getStatus);
    const getLoginText = computed(() => store.getters.getLoginText);

    const isLoggedIn = computed(() => store.getters.getStatus);

    const logout = async () => {
      try {
        const response = await store.dispatch("getLogout");

        if (getLoginText.value == "") {
          await router.push("/login");
        }
  
      } catch (err) {
        console.error("login failed:", err);
      }
    };

    return {
      logout,
      getLoginText,
      status,
      isLoggedIn
    };
  },
};
</script>

<template>
  <nav class="navbar">
    <router-link v-if="!isLoggedIn" to="/" class="navbar_logo"><fa icon="house" /></router-link>
    <router-link v-else to="/back_choose_date" class="navbar_logo"><fa icon="house" /></router-link>
    <span>麥醫生針灸診所</span>
    <span>
      <router-link v-if="!isLoggedIn" to="/booking_record" class="navbar_link"
        >預約紀錄</router-link
      >
      <span v-if="isLoggedIn" @click="logout" class="navbar_link">{{ getLoginText }}</span>
    </span>
  </nav>
</template>

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
    cursor: pointer;
  }
}
</style>
