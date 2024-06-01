import { type PropType } from 'vue';
import type { KatexOptions } from 'katex';
import type { ExtractPublicPropTypes } from '../../_utils';
export declare const equationProps: {
    readonly value: StringConstructor;
    readonly katex: PropType<typeof import("katex")>;
    readonly katexOptions: PropType<KatexOptions>;
};
export type EquationProps = ExtractPublicPropTypes<typeof equationProps>;
export declare const Equation: import("vue").DefineComponent<{
    readonly value: StringConstructor;
    readonly katex: PropType<typeof import("katex")>;
    readonly katexOptions: PropType<KatexOptions>;
}, () => import("vue").VNode<import("vue").RendererNode, import("vue").RendererElement, {
    [key: string]: any;
}>, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, {}, string, import("vue").PublicProps, Readonly<import("vue").ExtractPropTypes<{
    readonly value: StringConstructor;
    readonly katex: PropType<typeof import("katex")>;
    readonly katexOptions: PropType<KatexOptions>;
}>>, {}, {}>;
