"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.rtlInset = void 0;
const seemly_1 = require("seemly");
function rtlInset(inset) {
    const { left, right, top, bottom } = (0, seemly_1.getPadding)(inset);
    return `${top} ${right} ${bottom} ${left}`;
}
exports.rtlInset = rtlInset;
