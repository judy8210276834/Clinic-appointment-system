import { createApp } from "vue";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import permissionDirective from '@/directive/permissionDirective';

library.add(fas);

const app = createApp(App);

app.directive('has', permissionDirective);

store.dispatch('checkLoginStatus').then(() => {
  app
    .component("fa", FontAwesomeIcon) 
    .use(store) 
    .use(router) 
    .mount("#app"); 
});