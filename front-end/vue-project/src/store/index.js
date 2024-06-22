import { createStore } from "vuex";
import { postRegisterAPI, postLoginAPI, postLogoutAPI } from "@/api/api";
import Cookies from "js-cookie";

export default createStore({
  state: {
    msg: "",
    status: false,
    login_text: "",
  },
  getters: {
    getMsg: (state) => state.msg,
    getStatus: (state) => state.status,
    getLoginText: (state) => state.login_text,
  },
  mutations: {
    setMsg(state, msg) {
      state.msg = msg;
    },

    setStatus(state, status) {
      state.status = status;
    },

    setClearMessage(state) {
      state.msg = "";
    },

    setLoginText(state, status) {
      state.login_text = status;
    },
  },
  actions: {
    async postRegister({ commit }, payload) {
      try {
        const response = await postRegisterAPI(payload);
        commit("setMsg", response.data.result.status);
        commit("setStatus", true);
        return response;
      } catch (err) {
        console.log("postRegister API Error:", err);
        throw err;
      }
    },

    async getLogin({ commit }, payload) {
      try {
        const response = await postLoginAPI(payload);
        console.log(response);
        if (response.data.result.status == "登入成功。") {
          commit("setMsg", response.data.result.status);
          commit("setStatus", true);
          commit("setLoginText", "登出");
          console.log("登入成功");
        } else {
          commit("setMsg", response.data.result.err);
          commit("setStatus", false);
        }

        return response;
      } catch (err) {
        console.log("getLogin API Error:", err);
        throw err;
      }
    },

    async getLogout({ commit }, payload) {
      try {
        const response = await postLogoutAPI(payload);
        Cookies.remove("userToken");
        commit("setClearMessage");

        if (response.data.result.status == "登出成功。") {
          commit("setMsg", "");
          commit("setStatus", false);
          commit("setLoginText", "");
        }

        return response;
      } catch (err) {
        console.log("getLogout API Error:", err);
        throw err;
      }
    },

    async clearMessage({ commit }) {
      commit("setClearMessage");
    },

    async checkLoginStatus({ commit }) {
      return new Promise((resolve) => {
        const token = Cookies.get("userToken");
        if (token) {
          commit("setStatus", true);
          commit("setLoginText", "登出");
        } else {
          commit("setStatus", false);
          commit("setLoginText", "登入");
        }
        resolve(); 
      });
    },
  
  },
  modules: {},
});
