/** Глобальное модальное окно заявки менеджеру */
export function useOrderRequest() {
  const isOpen = useState('order-request-open', () => false)
  const prefilledQuestion = useState('order-request-prefill', () => '')

  const openOrderRequest = (message = '') => {
    prefilledQuestion.value = typeof message === 'string' ? message : ''
    isOpen.value = true
    if (import.meta.client) {
      document.body.style.overflow = 'hidden'
    }
  }

  const closeOrderRequest = () => {
    isOpen.value = false
    if (import.meta.client) {
      document.body.style.overflow = ''
    }
  }

  return {
    isOpen,
    prefilledQuestion,
    openOrderRequest,
    closeOrderRequest,
  }
}
