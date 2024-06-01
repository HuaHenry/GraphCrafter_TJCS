import { commonLight } from "../../_styles/common/index.mjs";
import { createTheme } from "../../_mixins/use-theme.mjs";
import { inputLight } from "../../input/styles/index.mjs";
import { buttonLight } from "../../button/styles/index.mjs";
export const self = vars => {
  const {
    fontSize,
    boxShadow2,
    popoverColor,
    textColor2,
    borderRadius,
    borderColor,
    heightSmall,
    heightMedium,
    heightLarge,
    fontSizeSmall,
    fontSizeMedium,
    fontSizeLarge,
    dividerColor
  } = vars;
  return {
    panelFontSize: fontSize,
    boxShadow: boxShadow2,
    color: popoverColor,
    textColor: textColor2,
    borderRadius,
    border: `1px solid ${borderColor}`,
    heightSmall,
    heightMedium,
    heightLarge,
    fontSizeSmall,
    fontSizeMedium,
    fontSizeLarge,
    dividerColor
  };
};
const colorPickerLight = createTheme({
  name: 'ColorPicker',
  common: commonLight,
  peers: {
    Input: inputLight,
    Button: buttonLight
  },
  self
});
export default colorPickerLight;