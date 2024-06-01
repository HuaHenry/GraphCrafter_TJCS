import { commonLight } from "../../_styles/common/index.mjs";
const self = vars => {
  return {
    borderRadius: vars.borderRadius
  };
};
const themeLight = {
  name: 'QrCode',
  common: commonLight,
  self
};
export default themeLight;