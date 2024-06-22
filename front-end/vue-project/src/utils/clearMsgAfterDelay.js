import store from '@/store';

export function clearMsgAfterDelay(delay) {
    setTimeout(() => {
      store.dispatch('clearMessage');
    }, delay);
  }
