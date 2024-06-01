/// <reference types="vue/jsx" />
import { type PropType } from 'vue';
declare const _default: import("vue").DefineComponent<{
    size: {
        type: PropType<"small" | "medium" | "large">;
        required: true;
    };
    selectAllText: StringConstructor;
    clearText: StringConstructor;
    source: BooleanConstructor;
    onCheckedAll: PropType<() => void>;
    onClearAll: PropType<() => void>;
    title: StringConstructor;
}, () => JSX.Element, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, {}, string, import("vue").PublicProps, Readonly<import("vue").ExtractPropTypes<{
    size: {
        type: PropType<"small" | "medium" | "large">;
        required: true;
    };
    selectAllText: StringConstructor;
    clearText: StringConstructor;
    source: BooleanConstructor;
    onCheckedAll: PropType<() => void>;
    onClearAll: PropType<() => void>;
    title: StringConstructor;
}>>, {
    source: boolean;
}, {}>;
export default _default;
