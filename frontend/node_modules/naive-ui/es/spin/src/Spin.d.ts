import { type PropType, type CSSProperties } from 'vue';
import { type ExtractPublicPropTypes } from '../../_utils';
export declare const spinProps: {
    contentClass: StringConstructor;
    contentStyle: PropType<string | CSSProperties>;
    description: StringConstructor;
    stroke: StringConstructor;
    size: {
        type: PropType<number | "small" | "medium" | "large">;
        default: string;
    };
    show: {
        type: BooleanConstructor;
        default: boolean;
    };
    strokeWidth: NumberConstructor;
    rotate: {
        type: BooleanConstructor;
        default: boolean;
    };
    spinning: {
        type: BooleanConstructor;
        validator: () => boolean;
        default: undefined;
    };
    delay: NumberConstructor;
    theme: PropType<import("../../_mixins").Theme<"Spin", {
        fontSize: string;
        textColor: string;
        sizeTiny: string;
        sizeSmall: string;
        sizeMedium: string;
        sizeLarge: string;
        sizeHuge: string;
        color: string;
        opacitySpinning: string;
    }, any>>;
    themeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"Spin", {
        fontSize: string;
        textColor: string;
        sizeTiny: string;
        sizeSmall: string;
        sizeMedium: string;
        sizeLarge: string;
        sizeHuge: string;
        color: string;
        opacitySpinning: string;
    }, any>>>;
    builtinThemeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"Spin", {
        fontSize: string;
        textColor: string;
        sizeTiny: string;
        sizeSmall: string;
        sizeMedium: string;
        sizeLarge: string;
        sizeHuge: string;
        color: string;
        opacitySpinning: string;
    }, any>>>;
};
export type SpinProps = ExtractPublicPropTypes<typeof spinProps>;
declare const _default: import("vue").DefineComponent<{
    contentClass: StringConstructor;
    contentStyle: PropType<string | CSSProperties>;
    description: StringConstructor;
    stroke: StringConstructor;
    size: {
        type: PropType<number | "small" | "medium" | "large">;
        default: string;
    };
    show: {
        type: BooleanConstructor;
        default: boolean;
    };
    strokeWidth: NumberConstructor;
    rotate: {
        type: BooleanConstructor;
        default: boolean;
    };
    spinning: {
        type: BooleanConstructor;
        validator: () => boolean;
        default: undefined;
    };
    delay: NumberConstructor;
    theme: PropType<import("../../_mixins").Theme<"Spin", {
        fontSize: string;
        textColor: string;
        sizeTiny: string;
        sizeSmall: string;
        sizeMedium: string;
        sizeLarge: string;
        sizeHuge: string;
        color: string;
        opacitySpinning: string;
    }, any>>;
    themeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"Spin", {
        fontSize: string;
        textColor: string;
        sizeTiny: string;
        sizeSmall: string;
        sizeMedium: string;
        sizeLarge: string;
        sizeHuge: string;
        color: string;
        opacitySpinning: string;
    }, any>>>;
    builtinThemeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"Spin", {
        fontSize: string;
        textColor: string;
        sizeTiny: string;
        sizeSmall: string;
        sizeMedium: string;
        sizeLarge: string;
        sizeHuge: string;
        color: string;
        opacitySpinning: string;
    }, any>>>;
}, {
    mergedClsPrefix: import("vue").Ref<string>;
    active: import("vue").Ref<boolean>;
    mergedStrokeWidth: import("vue").ComputedRef<number>;
    cssVars: import("vue").ComputedRef<{
        '--n-bezier': string;
        '--n-opacity-spinning': string;
        '--n-size': string;
        '--n-color': string;
        '--n-text-color': string;
    }> | undefined;
    themeClass: import("vue").Ref<string> | undefined;
    onRender: (() => void) | undefined;
}, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, {}, string, import("vue").PublicProps, Readonly<import("vue").ExtractPropTypes<{
    contentClass: StringConstructor;
    contentStyle: PropType<string | CSSProperties>;
    description: StringConstructor;
    stroke: StringConstructor;
    size: {
        type: PropType<number | "small" | "medium" | "large">;
        default: string;
    };
    show: {
        type: BooleanConstructor;
        default: boolean;
    };
    strokeWidth: NumberConstructor;
    rotate: {
        type: BooleanConstructor;
        default: boolean;
    };
    spinning: {
        type: BooleanConstructor;
        validator: () => boolean;
        default: undefined;
    };
    delay: NumberConstructor;
    theme: PropType<import("../../_mixins").Theme<"Spin", {
        fontSize: string;
        textColor: string;
        sizeTiny: string;
        sizeSmall: string;
        sizeMedium: string;
        sizeLarge: string;
        sizeHuge: string;
        color: string;
        opacitySpinning: string;
    }, any>>;
    themeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"Spin", {
        fontSize: string;
        textColor: string;
        sizeTiny: string;
        sizeSmall: string;
        sizeMedium: string;
        sizeLarge: string;
        sizeHuge: string;
        color: string;
        opacitySpinning: string;
    }, any>>>;
    builtinThemeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"Spin", {
        fontSize: string;
        textColor: string;
        sizeTiny: string;
        sizeSmall: string;
        sizeMedium: string;
        sizeLarge: string;
        sizeHuge: string;
        color: string;
        opacitySpinning: string;
    }, any>>>;
}>>, {
    size: number | "small" | "medium" | "large";
    show: boolean;
    rotate: boolean;
    spinning: boolean;
}, {}>;
export default _default;
