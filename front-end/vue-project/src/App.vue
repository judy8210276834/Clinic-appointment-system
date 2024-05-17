<script>
import "./assets/base.scss";
import NavBar from "./components/NavBar.vue";
import BottomFooter from "./components/FooTer.vue";
import LayOut from "./components/LayOut.vue";
import HelloWorld from "./components/HelloWorld.vue";
// import axios from "axios";
import { onMounted } from "vue";

export default {
  components: {
    NavBar,
    BottomFooter,
    LayOut,
    HelloWorld
  },
  setup() {
    onMounted(async () => {
      // ngrok免費版基礎設定
      // const headers = {
      //   "ngrok-skip-browser-warning": "true",
      //   "User-Agent": "MyCustomUserAgent",
      // };
      // const res = await axios.get(
      //   "https://ef00-2001-b400-e35f-fa42-6df2-b7a9-85a8-4112.ngrok-free.app/",
      //   { headers }
      // );
    });
  },
};
</script>

<template>
  <!-- <HelloWorld /> -->
  <header class="header">
    <NavBar />
  </header>
  <LayOut>
    <router-view />
  </LayOut>
  <footer>
    <BottomFooter />
  </footer>
</template>
<style lang="scss" scoped>
</style>

