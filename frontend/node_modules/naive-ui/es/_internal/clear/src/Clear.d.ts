import { type PropType } from 'vue';
declare const _default: import("vue").DefineComponent<{
    clsPrefix: {
        type: StringConstructor;
        required: true;
    };
    show: BooleanConstructor;
    onClear: PropType<(e: MouseEvent) => void>;
}, {
    handleMouseDown(e: MouseEvent): void;
}, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, {}, string, import("vue").PublicProps, Readonly<import("vue").ExtractPropTypes<{
    clsPrefix: {
        type: StringConstructor;
        required: true;
    };
    show: BooleanConstructor;
    onClear: PropType<(e: MouseEvent) => void>;
}>>, {
    show: boolean;
}, {}>;
export default _default;
