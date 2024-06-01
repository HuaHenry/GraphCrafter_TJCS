/// <reference types="vue/jsx" />
import { type PropType } from 'vue';
declare const _default: import("vue").DefineComponent<{
    clsPrefix: {
        type: StringConstructor;
        required: true;
    };
    showArrow: {
        type: BooleanConstructor;
        default: undefined;
    };
    showClear: {
        type: BooleanConstructor;
        default: undefined;
    };
    loading: {
        type: BooleanConstructor;
        default: boolean;
    };
    onClear: PropType<(e: MouseEvent) => void>;
}, () => JSX.Element, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, {}, string, import("vue").PublicProps, Readonly<import("vue").ExtractPropTypes<{
    clsPrefix: {
        type: StringConstructor;
        required: true;
    };
    showArrow: {
        type: BooleanConstructor;
        default: undefined;
    };
    showClear: {
        type: BooleanConstructor;
        default: undefined;
    };
    loading: {
        type: BooleanConstructor;
        default: boolean;
    };
    onClear: PropType<(e: MouseEvent) => void>;
}>>, {
    loading: boolean;
    showArrow: boolean;
    showClear: boolean;
}, {}>;
export default _default;
