import { getPadding } from 'seemly';
export function rtlInset(inset) {
  const {
    left,
    right,
    top,
    bottom
  } = getPadding(inset);
  return `${top} ${right} ${bottom} ${left}`;
}