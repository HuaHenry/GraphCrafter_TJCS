import { commonLight } from "../../_styles/common/index.mjs";
import { createTheme } from "../../_mixins/index.mjs";
import { avatarLight } from "../../avatar/styles/index.mjs";
export const self = () => {
  return {
    gap: '-12px'
  };
};
const avatarGroupLight = createTheme({
  name: 'AvatarGroup',
  common: commonLight,
  peers: {
    Avatar: avatarLight
  },
  self
});
export default avatarGroupLight;