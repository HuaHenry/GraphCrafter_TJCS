/// <reference types="vue/jsx" />
import { type PropType } from 'vue';
import { type TmNode } from './interface';
declare const _default: import("vue").DefineComponent<{
    clsPrefix: {
        type: StringConstructor;
        required: true;
    };
    indent: {
        type: NumberConstructor;
        required: true;
    };
    expanded: BooleanConstructor;
    selected: BooleanConstructor;
    hide: BooleanConstructor;
    loading: BooleanConstructor;
    onClick: PropType<(e: MouseEvent) => void>;
    tmNode: {
        type: PropType<TmNode>;
        required: true;
    };
}, () => JSX.Element, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, {}, string, import("vue").PublicProps, Readonly<import("vue").ExtractPropTypes<{
    clsPrefix: {
        type: StringConstructor;
        required: true;
    };
    indent: {
        type: NumberConstructor;
        required: true;
    };
    expanded: BooleanConstructor;
    selected: BooleanConstructor;
    hide: BooleanConstructor;
    loading: BooleanConstructor;
    onClick: PropType<(e: MouseEvent) => void>;
    tmNode: {
        type: PropType<TmNode>;
        required: true;
    };
}>>, {
    hide: boolean;
    expanded: boolean;
    loading: boolean;
    selected: boolean;
}, {}>;
export default _default;
