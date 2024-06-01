import { type Ref } from 'vue';
import type { ModalApiInjection, ModalReactive } from './ModalProvider';
export declare function useModal(): ModalApiInjection;
export declare function useModalReactiveList(): Ref<readonly ModalReactive[]>;
