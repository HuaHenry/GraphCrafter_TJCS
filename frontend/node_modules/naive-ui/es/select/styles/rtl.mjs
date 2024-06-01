import { internalSelectMenuRtl } from "../../_internal/select-menu/styles/index.mjs";
import { internalSelectionRtl } from "../../_internal/selection/styles/index.mjs";
import { scrollbarRtl } from "../../_internal/scrollbar/styles/index.mjs";
import { tagRtl } from "../../tag/styles/index.mjs";
import { c } from "../../_utils/cssr/index.mjs";
export const selectRtl = {
  name: 'Select',
  style: c([]),
  peers: [internalSelectionRtl, internalSelectMenuRtl, tagRtl, scrollbarRtl]
};