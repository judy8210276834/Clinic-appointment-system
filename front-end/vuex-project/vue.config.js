module.exports = {
  // 其他配置项...

  // 定义特性标志
  chainWebpack: (config) => {
    config.plugin("define").tap((args) => {
      const defineArgs = args[0] || {};
      defineArgs["__VUE_PROD_HYDRATION_MISMATCH_DETAILS__"] = true;
      return [defineArgs];
    });
  },
};

// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })
module.exports = {
  devServer: {
     historyApiFallback: true,
     allowedHosts:"all",
   },
};