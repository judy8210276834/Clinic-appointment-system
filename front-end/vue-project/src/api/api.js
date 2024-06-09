import http from "../utils/http";

/**
 *  @parms resquest 請求地址 例如：http://197.82.15.15:8088/request/...
 *  @param '/testIp'代表vue-cil中config，index.js中設定的代理
 */
let resquest = "http://localhost:8000";

/**
 * 使用者預約紀錄
 */

export function getListAPI(params) {
  const queryString = urlparamToString(params);
  return http.get(`${resquest}/product?${queryString}`);
}

// export function putSomeAPI(params){
//     return http.put(`${resquest}/putSome.json`,params)
// }

// export function deleteListAPI(params){
//     return http.delete(`${resquest}/deleteList.json`,params)
// }

/**
 * 醫生註冊、登入帳號
 */

export function postRegisterAPI(params) {
  return http.post(`${resquest}/register`, params);
}

export function getLoginAPI(params) {
  return http.post(`${resquest}/login`, params);
}

const urlparamToString = (params) => new URLSearchParams(params).toString();
