import type { Theme } from '../../_mixins';
declare const self: () => {
    gapSmall: string;
    gapMedium: string;
    gapLarge: string;
};
export type FlexThemeVars = ReturnType<typeof self>;
declare const flexLight: Theme<'Flex', FlexThemeVars>;
export default flexLight;
export type FlexTheme = typeof flexLight;
