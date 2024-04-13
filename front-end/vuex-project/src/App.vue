<script>
import "./assets/base.scss";
import NavBar from "./components/NavBar.vue";
import Footer from "./components/Footer.vue";
import axios from "axios";
import { onMounted } from "vue";

export default {
  components: {
    NavBar,
    Footer,
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
  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
  <header class="header">
    <NavBar />
  </header>
  <div class="router-content">
    <router-view />
  </div>
  <footer>
    <Footer />
  </footer>
</template>

<style lang="scss" scoped>
.router-content {
  padding: 80px 128px 150px 128px;
  background-color: #c2bfaf;
  @media (max-width: 991px) {
    padding: 60px 90px 100px 90px;
  }
  @media (max-width: 575px) {
    padding: 40px 20px 80px 20px;
  }
}
</style>
