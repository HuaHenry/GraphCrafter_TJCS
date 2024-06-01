"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.useModalReactiveList = exports.useModal = void 0;
const vue_1 = require("vue");
const context_1 = require("./context");
const _utils_1 = require("../../_utils");
function useModal() {
    const modal = (0, vue_1.inject)(context_1.modalApiInjectionKey, null);
    if (modal === null) {
        (0, _utils_1.throwError)('use-modal', 'No outer <n-modal-provider /> founded.');
    }
    return modal;
}
exports.useModal = useModal;
function useModalReactiveList() {
    const modalReactiveList = (0, vue_1.inject)(context_1.modalReactiveListInjectionKey, null);
    if (modalReactiveList === null) {
        (0, _utils_1.throwError)('use-modal-reactive-list', 'No outer <n-modal-provider /> founded.');
    }
    return modalReactiveList;
}
exports.useModalReactiveList = useModalReactiveList;
