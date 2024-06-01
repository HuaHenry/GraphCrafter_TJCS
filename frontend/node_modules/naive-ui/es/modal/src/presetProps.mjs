import { dialogProps } from "../../dialog/src/dialogProps.mjs";
import { cardBaseProps } from "../../card/src/Card.mjs";
import { keysOf } from "../../_utils/index.mjs";
const presetProps = Object.assign(Object.assign({}, cardBaseProps), dialogProps);
const presetPropsKeys = keysOf(presetProps);
export { presetProps, presetPropsKeys };