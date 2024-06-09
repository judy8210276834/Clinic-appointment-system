import { createStore } from "vuex";
import { postRegisterAPI, getLoginAPI } from "@/api/api";

export default createStore({
  state: {},
  getters: {},
  mutations: {},
  actions: {
    async postRegister({ commit }, payload) {
      try {
        const response = postRegisterAPI(payload);
        // commit("setRegisterResponse", response.data);
        return response;
      } catch (err) {
        console.log("postRegister API Error:", err);
        throw err;
      }
    },

    async getLogin({ commit }, payload) {
      try {
        const response = getLoginAPI(payload);
        return response;
      } catch (err) {
        console.log("getLogin API Error:", err);
        throw err;
      }
    },
  },
  modules: {},
});
