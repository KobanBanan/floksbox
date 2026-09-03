export default defineNuxtPlugin((nuxtApp) => {
  let observer = null

  const revealIfVisible = (el) => {
    const rect = el.getBoundingClientRect()
    const inView = rect.top < window.innerHeight && rect.bottom > 0
    if (inView) {
      el.classList.add('scroll-reveal-visible')
      return true
    }
    return false
  }

  const initScrollReveal = () => {
    if (observer) {
      observer.disconnect()
      observer = null
    }

    observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('scroll-reveal-visible')
          observer.unobserve(entry.target)
        }
      })
    }, {
      threshold: 0.05,
      rootMargin: '0px 0px -20px 0px'
    })

    document.querySelectorAll('.scroll-reveal:not(.scroll-reveal-visible)').forEach((el) => {
      if (!revealIfVisible(el)) {
        observer.observe(el)
      }
    })

    // Fallback: не оставляем контент невидимым, если observer не сработал
    window.setTimeout(() => {
      document.querySelectorAll('.scroll-reveal:not(.scroll-reveal-visible)').forEach((el) => {
        el.classList.add('scroll-reveal-visible')
      })
    }, 800)
  }

  nuxtApp.hook('page:finish', () => {
    nextTick(() => {
      window.setTimeout(initScrollReveal, 50)
    })
  })

  nuxtApp.hook('app:mounted', () => {
    window.setTimeout(initScrollReveal, 100)
  })
})
