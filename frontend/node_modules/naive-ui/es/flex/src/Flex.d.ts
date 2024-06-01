import { type PropType } from 'vue';
import type { ExtractPublicPropTypes } from '../../_utils';
export declare const flexProps: {
    readonly align: PropType<import("csstype").Property.AlignItems>;
    readonly justify: {
        readonly type: PropType<import("csstype").Property.JustifyContent>;
        readonly default: "start";
    };
    readonly inline: BooleanConstructor;
    readonly vertical: BooleanConstructor;
    readonly reverse: BooleanConstructor;
    readonly size: {
        readonly type: PropType<number | [number, number] | "small" | "medium" | "large">;
        readonly default: "medium";
    };
    readonly wrap: {
        readonly type: BooleanConstructor;
        readonly default: true;
    };
    readonly theme: PropType<import("../../_mixins").Theme<"Flex", {
        gapSmall: string;
        gapMedium: string;
        gapLarge: string;
    }, any>>;
    readonly themeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"Flex", {
        gapSmall: string;
        gapMedium: string;
        gapLarge: string;
    }, any>>>;
    readonly builtinThemeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"Flex", {
        gapSmall: string;
        gapMedium: string;
        gapLarge: string;
    }, any>>>;
};
export type FlexProps = ExtractPublicPropTypes<typeof flexProps>;
declare const _default: import("vue").DefineComponent<{
    readonly align: PropType<import("csstype").Property.AlignItems>;
    readonly justify: {
        readonly type: PropType<import("csstype").Property.JustifyContent>;
        readonly default: "start";
    };
    readonly inline: BooleanConstructor;
    readonly vertical: BooleanConstructor;
    readonly reverse: BooleanConstructor;
    readonly size: {
        readonly type: PropType<number | [number, number] | "small" | "medium" | "large">;
        readonly default: "medium";
    };
    readonly wrap: {
        readonly type: BooleanConstructor;
        readonly default: true;
    };
    readonly theme: PropType<import("../../_mixins").Theme<"Flex", {
        gapSmall: string;
        gapMedium: string;
        gapLarge: string;
    }, any>>;
    readonly themeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"Flex", {
        gapSmall: string;
        gapMedium: string;
        gapLarge: string;
    }, any>>>;
    readonly builtinThemeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"Flex", {
        gapSmall: string;
        gapMedium: string;
        gapLarge: string;
    }, any>>>;
}, {
    rtlEnabled: import("vue").Ref<import("../../config-provider/src/internal-interface").RtlItem | undefined> | undefined;
    mergedClsPrefix: import("vue").Ref<string>;
    margin: import("vue").ComputedRef<{
        horizontal: number;
        vertical: number;
    }>;
}, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, {}, string, import("vue").PublicProps, Readonly<import("vue").ExtractPropTypes<{
    readonly align: PropType<import("csstype").Property.AlignItems>;
    readonly justify: {
        readonly type: PropType<import("csstype").Property.JustifyContent>;
        readonly default: "start";
    };
    readonly inline: BooleanConstructor;
    readonly vertical: BooleanConstructor;
    readonly reverse: BooleanConstructor;
    readonly size: {
        readonly type: PropType<number | [number, number] | "small" | "medium" | "large">;
        readonly default: "medium";
    };
    readonly wrap: {
        readonly type: BooleanConstructor;
        readonly default: true;
    };
    readonly theme: PropType<import("../../_mixins").Theme<"Flex", {
        gapSmall: string;
        gapMedium: string;
        gapLarge: string;
    }, any>>;
    readonly themeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"Flex", {
        gapSmall: string;
        gapMedium: string;
        gapLarge: string;
    }, any>>>;
    readonly builtinThemeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"Flex", {
        gapSmall: string;
        gapMedium: string;
        gapLarge: string;
    }, any>>>;
}>>, {
    readonly inline: boolean;
    readonly size: number | [number, number] | "small" | "medium" | "large";
    readonly reverse: boolean;
    readonly wrap: boolean;
    readonly vertical: boolean;
    readonly justify: import("csstype").Property.JustifyContent;
}, {}>;
export default _default;
