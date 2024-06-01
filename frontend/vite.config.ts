import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
import { resolve } from "path";
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": resolve(__dirname, "./src"),
    },
    //extensions: [".ts", ".js", ".vue", ".json", ".mjs"],
    extensions: [".mjs", ".js", ".ts", ".jsx", ".tsx", ".json", ".vue"],
    },
    // server: {
    //     port: '',//端口号
    //     strictPort: true,//是否是严格的端口号，如果true，端口号被占用的情况下，vite会退出
    //     host: 'localhost',
    //     cors: true,//为开发服务器配置 CORS , 默认启用并允许任何源
    //     https: false,//是否支持http2 如果配置成true 会打开https://localhost:3001/xxx;
    //     open: true,//是否自动打开浏览器
    //     // 反向代理 跨域配置
    //     proxy: {
    //         '/api': {
    //             target: "https://xxxx.com/",
    //             changeOrigin: true,
    //             rewrite: (path) => path.replace(/^\/api/, '')
    //         }
    //     }
    // },
});
