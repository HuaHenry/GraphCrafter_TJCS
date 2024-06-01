import { inject } from 'vue';
import { notificationApiInjectionKey } from "./NotificationProvider.mjs";
import { throwError } from "../../_utils/index.mjs";
export function useNotification() {
  const api = inject(notificationApiInjectionKey, null);
  if (api === null) {
    throwError('use-notification', 'No outer `n-notification-provider` found.');
  }
  return api;
}