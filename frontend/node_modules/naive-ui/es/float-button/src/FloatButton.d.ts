import { type PropType, type CSSProperties } from 'vue';
import { type ExtractPublicPropTypes, type MaybeArray } from '../../_utils';
export declare const floatButtonProps: {
    readonly width: {
        readonly type: PropType<string | number>;
        readonly default: 40;
    };
    readonly height: {
        readonly type: PropType<string | number>;
        readonly default: 40;
    };
    readonly left: PropType<string | number>;
    readonly right: PropType<string | number>;
    readonly top: PropType<string | number>;
    readonly bottom: PropType<string | number>;
    readonly shape: {
        readonly type: PropType<"circle" | "square">;
        readonly default: "circle";
    };
    readonly position: {
        readonly type: PropType<"fixed" | "absolute" | "relative">;
        readonly default: "fixed";
    };
    readonly type: {
        readonly type: PropType<"default" | "primary">;
        readonly default: "default";
    };
    readonly menuTrigger: PropType<"click" | "hover">;
    readonly showMenu: {
        readonly type: BooleanConstructor;
        readonly default: undefined;
    };
    readonly onUpdateShowMenu: {
        readonly type: PropType<MaybeArray<(value: boolean) => void>>;
        readonly default: undefined;
    };
    readonly 'onUpdate:showMenu': {
        readonly type: PropType<MaybeArray<(value: boolean) => void>>;
        readonly default: undefined;
    };
    readonly theme: PropType<import("../../_mixins").Theme<"FloatButton", {
        color: string;
        colorHover: string;
        colorPressed: string;
        colorPrimary: string;
        colorPrimaryHover: string;
        colorPrimaryPressed: string;
        textColor: string;
        boxShadow: string;
        boxShadowHover: string;
        boxShadowPressed: string;
        textColorPrimary: string;
        borderRadiusSquare: string;
    }, any>>;
    readonly themeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"FloatButton", {
        color: string;
        colorHover: string;
        colorPressed: string;
        colorPrimary: string;
        colorPrimaryHover: string;
        colorPrimaryPressed: string;
        textColor: string;
        boxShadow: string;
        boxShadowHover: string;
        boxShadowPressed: string;
        textColorPrimary: string;
        borderRadiusSquare: string;
    }, any>>>;
    readonly builtinThemeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"FloatButton", {
        color: string;
        colorHover: string;
        colorPressed: string;
        colorPrimary: string;
        colorPrimaryHover: string;
        colorPrimaryPressed: string;
        textColor: string;
        boxShadow: string;
        boxShadowHover: string;
        boxShadowPressed: string;
        textColorPrimary: string;
        borderRadiusSquare: string;
    }, any>>>;
};
export type FloatButtonProps = ExtractPublicPropTypes<typeof floatButtonProps>;
declare const _default: import("vue").DefineComponent<{
    readonly width: {
        readonly type: PropType<string | number>;
        readonly default: 40;
    };
    readonly height: {
        readonly type: PropType<string | number>;
        readonly default: 40;
    };
    readonly left: PropType<string | number>;
    readonly right: PropType<string | number>;
    readonly top: PropType<string | number>;
    readonly bottom: PropType<string | number>;
    readonly shape: {
        readonly type: PropType<"circle" | "square">;
        readonly default: "circle";
    };
    readonly position: {
        readonly type: PropType<"fixed" | "absolute" | "relative">;
        readonly default: "fixed";
    };
    readonly type: {
        readonly type: PropType<"default" | "primary">;
        readonly default: "default";
    };
    readonly menuTrigger: PropType<"click" | "hover">;
    readonly showMenu: {
        readonly type: BooleanConstructor;
        readonly default: undefined;
    };
    readonly onUpdateShowMenu: {
        readonly type: PropType<MaybeArray<(value: boolean) => void>>;
        readonly default: undefined;
    };
    readonly 'onUpdate:showMenu': {
        readonly type: PropType<MaybeArray<(value: boolean) => void>>;
        readonly default: undefined;
    };
    readonly theme: PropType<import("../../_mixins").Theme<"FloatButton", {
        color: string;
        colorHover: string;
        colorPressed: string;
        colorPrimary: string;
        colorPrimaryHover: string;
        colorPrimaryPressed: string;
        textColor: string;
        boxShadow: string;
        boxShadowHover: string;
        boxShadowPressed: string;
        textColorPrimary: string;
        borderRadiusSquare: string;
    }, any>>;
    readonly themeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"FloatButton", {
        color: string;
        colorHover: string;
        colorPressed: string;
        colorPrimary: string;
        colorPrimaryHover: string;
        colorPrimaryPressed: string;
        textColor: string;
        boxShadow: string;
        boxShadowHover: string;
        boxShadowPressed: string;
        textColorPrimary: string;
        borderRadiusSquare: string;
    }, any>>>;
    readonly builtinThemeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"FloatButton", {
        color: string;
        colorHover: string;
        colorPressed: string;
        colorPrimary: string;
        colorPrimaryHover: string;
        colorPrimaryPressed: string;
        textColor: string;
        boxShadow: string;
        boxShadowHover: string;
        boxShadowPressed: string;
        textColorPrimary: string;
        borderRadiusSquare: string;
    }, any>>>;
}, {
    inlineStyle: import("vue").ComputedRef<CSSProperties>;
    cssVars: import("vue").ComputedRef<Record<string, string>> | undefined;
    mergedClsPrefix: import("vue").Ref<string>;
    mergedShape: import("vue").ComputedRef<"circle" | "square">;
    mergedShowMenu: import("vue").ComputedRef<boolean>;
    themeClass: import("vue").Ref<string> | undefined;
    onRender: (() => void) | undefined;
    Mouseenter: () => void;
    handleMouseleave: () => void;
    handleClick: (e: MouseEvent) => void;
}, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, {}, string, import("vue").PublicProps, Readonly<import("vue").ExtractPropTypes<{
    readonly width: {
        readonly type: PropType<string | number>;
        readonly default: 40;
    };
    readonly height: {
        readonly type: PropType<string | number>;
        readonly default: 40;
    };
    readonly left: PropType<string | number>;
    readonly right: PropType<string | number>;
    readonly top: PropType<string | number>;
    readonly bottom: PropType<string | number>;
    readonly shape: {
        readonly type: PropType<"circle" | "square">;
        readonly default: "circle";
    };
    readonly position: {
        readonly type: PropType<"fixed" | "absolute" | "relative">;
        readonly default: "fixed";
    };
    readonly type: {
        readonly type: PropType<"default" | "primary">;
        readonly default: "default";
    };
    readonly menuTrigger: PropType<"click" | "hover">;
    readonly showMenu: {
        readonly type: BooleanConstructor;
        readonly default: undefined;
    };
    readonly onUpdateShowMenu: {
        readonly type: PropType<MaybeArray<(value: boolean) => void>>;
        readonly default: undefined;
    };
    readonly 'onUpdate:showMenu': {
        readonly type: PropType<MaybeArray<(value: boolean) => void>>;
        readonly default: undefined;
    };
    readonly theme: PropType<import("../../_mixins").Theme<"FloatButton", {
        color: string;
        colorHover: string;
        colorPressed: string;
        colorPrimary: string;
        colorPrimaryHover: string;
        colorPrimaryPressed: string;
        textColor: string;
        boxShadow: string;
        boxShadowHover: string;
        boxShadowPressed: string;
        textColorPrimary: string;
        borderRadiusSquare: string;
    }, any>>;
    readonly themeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"FloatButton", {
        color: string;
        colorHover: string;
        colorPressed: string;
        colorPrimary: string;
        colorPrimaryHover: string;
        colorPrimaryPressed: string;
        textColor: string;
        boxShadow: string;
        boxShadowHover: string;
        boxShadowPressed: string;
        textColorPrimary: string;
        borderRadiusSquare: string;
    }, any>>>;
    readonly builtinThemeOverrides: PropType<import("../../_mixins/use-theme").ExtractThemeOverrides<import("../../_mixins").Theme<"FloatButton", {
        color: string;
        colorHover: string;
        colorPressed: string;
        colorPrimary: string;
        colorPrimaryHover: string;
        colorPrimaryPressed: string;
        textColor: string;
        boxShadow: string;
        boxShadowHover: string;
        boxShadowPressed: string;
        textColorPrimary: string;
        borderRadiusSquare: string;
    }, any>>>;
}>>, {
    readonly type: "default" | "primary";
    readonly position: "fixed" | "absolute" | "relative";
    readonly height: string | number;
    readonly width: string | number;
    readonly shape: "circle" | "square";
    readonly showMenu: boolean;
    readonly onUpdateShowMenu: MaybeArray<(value: boolean) => void>;
    readonly 'onUpdate:showMenu': MaybeArray<(value: boolean) => void>;
}, {}>;
export default _default;
