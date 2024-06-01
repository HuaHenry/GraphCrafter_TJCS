import rtlStyle from "../src/styles/rtl.cssr.mjs";
import { scrollbarRtl } from "../../_internal/scrollbar/styles/rtl.mjs";
export const drawerRtl = {
  name: 'Drawer',
  style: rtlStyle,
  peers: [scrollbarRtl]
};
export default drawerRtl;