<script setup>
import "./assets/base.scss";
import NavBar from "./components/NavBar.vue";
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
</template>

<style lang="scss" scoped>
.router-content {
  padding: 20px; 
  display: flex;
  justify-content: center; 
  align-items: center; 
}
</style>
