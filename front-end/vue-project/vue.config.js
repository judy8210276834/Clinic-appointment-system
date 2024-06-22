const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    host: "localhost", //手機測試，之後改回localsite
    client: {
      overlay: {
        warnings: true,
        errors: true,
      },
    },
    port: 8080, 
    https: false, 
    open: false, 
    hot: true, 
    proxy: "http://localhost:8000",
  },
});
