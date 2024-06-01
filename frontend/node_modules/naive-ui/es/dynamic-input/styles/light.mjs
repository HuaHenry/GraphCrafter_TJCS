import { inputLight } from "../../input/styles/index.mjs";
import { buttonLight } from "../../button/styles/index.mjs";
import { commonLight } from "../../_styles/common/index.mjs";
import commonVariables from "./_common.mjs";
import { createTheme } from "../../_mixins/index.mjs";
const self = () => {
  return commonVariables;
};
const dynamicInputLight = createTheme({
  name: 'DynamicInput',
  common: commonLight,
  peers: {
    Input: inputLight,
    Button: buttonLight
  },
  self
});
export default dynamicInputLight;