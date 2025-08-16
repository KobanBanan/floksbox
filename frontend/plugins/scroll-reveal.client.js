export default defineNuxtPlugin(() => {
  // Этот плагин будет запускаться только на клиенте
  if (process.client) {
    // Создаем глобальную функцию для инициализации scroll reveal
    const initScrollReveal = () => {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('scroll-reveal-visible')
            observer.unobserve(entry.target)
          }
        })
      }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
      })

      // Находим все элементы с классом scroll-reveal
      const elements = document.querySelectorAll('.scroll-reveal')
      elements.forEach((el) => {
        observer.observe(el)
      })

      return observer
    }

    // Инициализируем при загрузке страницы
    let observer = null
    
    const router = useRouter()
    
    // Инициализация при первой загрузке
    onMounted(() => {
      setTimeout(() => {
        observer = initScrollReveal()
      }, 100)
    })

    // Переинициализация при изменении маршрута
    router.afterEach(() => {
      nextTick(() => {
        if (observer) {
          observer.disconnect()
        }
        setTimeout(() => {
          observer = initScrollReveal()
        }, 100)
      })
    })

    // Очистка при размонтировании
    onUnmounted(() => {
      if (observer) {
        observer.disconnect()
      }
    })
  }
})
