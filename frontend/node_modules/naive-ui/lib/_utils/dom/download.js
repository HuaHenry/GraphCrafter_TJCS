"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.download = void 0;
const download = (url, name) => {
    if (!url)
        return;
    const a = document.createElement('a');
    a.href = url;
    if (name !== undefined) {
        a.download = name;
    }
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
};
exports.download = download;
