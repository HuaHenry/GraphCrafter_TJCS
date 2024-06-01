import type { ThemeCommonVars } from '../../_styles/common';
import { type Theme } from '../../_mixins';
declare const self: (vars: ThemeCommonVars) => {
    borderRadius: string;
};
export type QrCodeThemeVars = ReturnType<typeof self>;
declare const themeLight: Theme<'QrCode', QrCodeThemeVars>;
export default themeLight;
export type QrCodeTheme = typeof themeLight;
