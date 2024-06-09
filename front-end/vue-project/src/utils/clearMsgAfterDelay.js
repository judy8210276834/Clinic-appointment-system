export function clearMsgAfterDelay(msg, delay) {
    setTimeout(() => {
      msg.value = '';
    }, delay);
  }
