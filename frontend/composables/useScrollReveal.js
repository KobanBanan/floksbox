import { onMounted, onUnmounted } from 'vue'

export const useScrollReveal = (options = {}) => {
  const {
    threshold = 0.1,
    rootMargin = '0px 0px -50px 0px',
    animationClass = 'scroll-reveal-visible',
    targetSelector = '.scroll-reveal'
  } = options

  let observer = null

  const initScrollReveal = () => {
    // Создаем observer только на клиенте
    if (process.client) {
      observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            // Добавляем класс для анимации появления
            entry.target.classList.add(animationClass)
            // Прекращаем наблюдение за элементом после появления
            observer.unobserve(entry.target)
          }
        })
      }, {
        threshold,
        rootMargin
      })

      // Находим и наблюдаем за всеми элементами с классом scroll-reveal
      const elements = document.querySelectorAll(targetSelector)
      elements.forEach((el) => {
        observer.observe(el)
      })
    }
  }

  const disconnectObserver = () => {
    if (observer) {
      observer.disconnect()
      observer = null
    }
  }

  onMounted(() => {
    // Небольшая задержка для загрузки DOM
    setTimeout(initScrollReveal, 100)
  })

  onUnmounted(() => {
    disconnectObserver()
  })

  // Возвращаем функцию для повторной инициализации (если нужно)
  return {
    initScrollReveal,
    disconnectObserver
  }
}
