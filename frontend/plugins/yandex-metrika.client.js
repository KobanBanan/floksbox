const METRIKA_ID = 109642461
const TAG_URL = `https://mc.yandex.ru/metrika/tag.js?id=${METRIKA_ID}`

export default defineNuxtPlugin((nuxtApp) => {
  if (import.meta.server) {
    return
  }

  const initMetrika = () => {
    if (typeof window.ym === 'function') {
      return
    }

    window.dataLayer = window.dataLayer || []

    ;(function (m, e, t, r, i, k, a) {
      m[i] =
        m[i] ||
        function () {
          ;(m[i].a = m[i].a || []).push(arguments)
        }
      m[i].l = 1 * new Date()
      for (let j = 0; j < document.scripts.length; j++) {
        if (document.scripts[j].src === r) {
          return
        }
      }
      k = e.createElement(t)
      a = e.getElementsByTagName(t)[0]
      k.async = 1
      k.src = r
      a.parentNode.insertBefore(k, a)
    })(window, document, 'script', TAG_URL, 'ym')

    window.ym(METRIKA_ID, 'init', {
      ssr: true,
      webvisor: true,
      clickmap: true,
      ecommerce: 'dataLayer',
      referrer: document.referrer,
      url: location.href,
      accurateTrackBounce: true,
      trackLinks: true,
    })
  }

  initMetrika()

  let isFirstPage = true
  nuxtApp.hook('page:finish', () => {
    if (typeof window.ym !== 'function') {
      return
    }
    if (isFirstPage) {
      isFirstPage = false
      return
    }
    window.ym(METRIKA_ID, 'hit', window.location.href, {
      title: document.title,
      referer: document.referrer,
    })
  })
})
