// const { defineConfig } = require('@vue/cli-service');

// module.exports = defineConfig({
//   transpileDependencies: true,
//   devServer: {
//     client: {
//       overlay: { // 将 overlay 放在 client 选项中
//         warnings: true,
//         errors: true
//       },
//     },
//     host: "localhost",
//     port: 8080, // 端口号
//     https: false, // https:{type:Boolean}
//     open: false, // 设置后自动启动浏览器
//     hot: true, // 启用热模块替换
//     proxy: 'http://localhost:8000',
//     // proxy: { // 设置多个代理
//     //   "/testIp": {
//     //     target: "http://197.0.0.1:8088",
//     //     changeOrigin: true,
//     //     ws: true, // websocket 支持
//     //     secure: false,
//     //     pathRewrite: {
//     //       "^/testIp": "/"
//     //     }
//     //   },
//     //   "/elseIp": {
//     //     target: "http://197.0.0.2:8088",
//     //     changeOrigin: true,
//     //     // ws: true, // websocket 支持
//     //     secure: false,
//     //     pathRewrite: {
//     //       "^/elseIp": "/"
//     //     }
//     //   },
//     // }
//   }
// });
