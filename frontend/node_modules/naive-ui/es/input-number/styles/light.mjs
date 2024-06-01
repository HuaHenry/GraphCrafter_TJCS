import { buttonLight } from "../../button/styles/index.mjs";
import { inputLight } from "../../input/styles/index.mjs";
import { commonLight } from "../../_styles/common/index.mjs";
import { createTheme } from "../../_mixins/index.mjs";
const self = vars => {
  const {
    textColorDisabled
  } = vars;
  return {
    iconColorDisabled: textColorDisabled
  };
};
const inputNumberLight = createTheme({
  name: 'InputNumber',
  common: commonLight,
  peers: {
    Button: buttonLight,
    Input: inputLight
  },
  self
});
export default inputNumberLight;