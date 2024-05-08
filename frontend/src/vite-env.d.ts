/// <reference types="vite/client" />
declare module "*.vue" {
  import type { DefineComponent } from "vue";
  const vueComponent: DefineComponent<{}, {}, any>;
  export default vueComponent;
}
declare module 'vue-waterfall-plugin-next';

declare module "element-plus";
declare module "element-plus/icons-vue";
declare module "axios";