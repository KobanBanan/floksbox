/** Короткие сообщения о результате действия. Не перекрывают страницу. */
export function useToast() {
  const toasts = useState('app-toasts', () => [])

  const dismiss = (id) => {
    const current = toasts.value.find((item) => item.id === id)
    if (!current || current.leaving) return
    current.leaving = true
    if (import.meta.client) {
      window.setTimeout(() => {
        toasts.value = toasts.value.filter((item) => item.id !== id)
      }, 280)
    } else {
      toasts.value = toasts.value.filter((item) => item.id !== id)
    }
  }

  const push = ({ type = 'success', title, text, duration }) => {
    const id = `${Date.now()}-${Math.random().toString(16).slice(2)}`
    toasts.value = [...toasts.value, { id, type, title, text, leaving: false }].slice(-3)
    const ms = duration ?? (type === 'error' ? 6500 : 4800)
    if (import.meta.client) {
      window.setTimeout(() => dismiss(id), ms)
    }
    return id
  }

  return {
    toasts,
    push,
    dismiss,
    success: (title, text) => push({ type: 'success', title, text }),
    error: (title, text) => push({ type: 'error', title, text }),
    info: (title, text) => push({ type: 'info', title, text }),
  }
}
