"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.self = void 0;
const common_1 = require("../../_styles/common");
const self = (vars) => {
    const { primaryColorHover, borderColor } = vars;
    return {
        resizableTriggerColorHover: primaryColorHover,
        resizableTriggerColor: borderColor
    };
};
exports.self = self;
const themeLight = {
    name: 'Split',
    common: common_1.commonLight,
    self: exports.self
};
exports.default = themeLight;
