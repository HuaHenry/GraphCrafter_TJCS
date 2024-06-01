import { changeColor } from 'seemly';
import { checkboxLight } from "../../checkbox/styles/index.mjs";
import { emptyLight } from "../../empty/styles/index.mjs";
import { scrollbarLight } from "../../_internal/scrollbar/styles/index.mjs";
import { commonLight } from "../../_styles/common/index.mjs";
import { createTheme } from "../../_mixins/use-theme.mjs";
export const self = vars => {
  const {
    borderRadiusSmall,
    dividerColor,
    hoverColor,
    pressedColor,
    primaryColor,
    textColor3,
    textColor2,
    textColorDisabled,
    fontSize
  } = vars;
  return {
    fontSize,
    lineHeight: '1.5',
    nodeHeight: '30px',
    nodeWrapperPadding: '3px 0',
    nodeBorderRadius: borderRadiusSmall,
    nodeColorHover: hoverColor,
    nodeColorPressed: pressedColor,
    nodeColorActive: changeColor(primaryColor, {
      alpha: 0.1
    }),
    arrowColor: textColor3,
    nodeTextColor: textColor2,
    nodeTextColorDisabled: textColorDisabled,
    loadingColor: primaryColor,
    dropMarkColor: primaryColor,
    lineColor: dividerColor
  };
};
const treeLight = createTheme({
  name: 'Tree',
  common: commonLight,
  peers: {
    Checkbox: checkboxLight,
    Scrollbar: scrollbarLight,
    Empty: emptyLight
  },
  self
});
export default treeLight;