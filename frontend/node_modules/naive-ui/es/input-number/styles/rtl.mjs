import rtlStyle from "../src/styles/rtl.cssr.mjs";
import { inputRtl } from "../../input/styles/rtl.mjs";
import { buttonRtl } from "../../button/styles/rtl.mjs";
export const inputNumberRtl = {
  name: 'InputNumber',
  style: rtlStyle,
  peers: [inputRtl, buttonRtl]
};