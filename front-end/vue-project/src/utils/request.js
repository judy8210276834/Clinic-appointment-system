import axios from "axios";
import Cookies from 'js-cookie';

const service = axios.create({
  baseURL: process.env.BASE_API,
  timeout: 3 * 1000,
});

// request攔截器
service.interceptors.request.use(
  function (config) {
    //發請求前做的一些處理，資料轉化，設定請求頭，設定token,設定loading等...
    config.data = config.data;
    config.headers = {
      "Content-Type": "application/x-www-form-urlencoded",
    };

    const token = Cookies.get('userToken'); 
    if (token) {
      config.params = { token: token }; 
      config.headers.token = token; 
    }

    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);

// response攔截器
service.interceptors.response.use(
  function (response) {

    const token = response.headers['token'];
    if (token) {
    Cookies.set('userToken', token);
    }
    // 接收到響應資料併成功後的一些共有的處理，關閉loading等

    return response;
  },
  function (error) {
    if (error && error.response) {
      
      switch (error.response.status) {
        case 400:
          error.message = "錯誤請求";
          break;
        case 401:
          error.message = "未授權，請重新登入";
          break;
        case 403:
          error.message = "拒絕存取";
          break;
        case 404:
          error.message = "請求錯誤,未找到該資源";
          // window.location.href = "/NotFound";
          break;
        case 405:
          error.message = "請求方法未允許";
          break;
        case 408:
          error.message = "請求超時";
          break;
        case 500:
          error.message = "伺服器端出錯";
          break;
        case 501:
          error.message = "網路未實現";
          break;
        case 502:
          error.message = "網路錯誤";
          break;
        case 503:
          error.message = "服務不可用";
          break;
        case 504:
          error.message = "網路超時";
          break;
        case 505:
          error.message = "http版本不支援該請求";
          break;
        default:
          error.message = `連線錯誤${error.response.status}`;
      }
    } else {
      // 超時處理
      if (JSON.stringify(error).includes("timeout")) {
        // Message.error("伺服器響應超時，請重新整理當前頁");
      }
      error.message("連線伺服器失敗");
    }

    Message.error(error.message);
    /***** 處理結束 *****/
    //如果不需要錯誤處理，以上的處理過程都可省略
    return Promise.resolve(error.response);
    // return Promise.reject(error);
  }
);

export default service