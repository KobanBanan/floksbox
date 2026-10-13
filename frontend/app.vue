<template>
  <NuxtLayout>
    <NuxtPage :transition="pageTransition" />
    <OrderRequestModal />
    <ToastStack />
    <SiteSplash />
  </NuxtLayout>
</template>

<script setup>
const router = useRouter()
const nuxtApp = useNuxtApp()

const washOn = ref(false)
const washTick = ref(0)
const navDirection = ref('forward')
const transitionName = ref('page-instant')

let generation = 0
let clearTimer = 0
let releaseTries = 0

const prefersReducedMotion = () => {
  if (!import.meta.client) return false
  return window.matchMedia('(prefers-reduced-motion: reduce)').matches
}

const normalizePath = (path) => {
  if (!path) return '/'
  const clean = path.split('?')[0].split('#')[0]
  if (clean.length > 1 && clean.endsWith('/')) return clean.slice(0, -1)
  return clean || '/'
}

// 0 — не каталог; глубже по каталогу — выше ранг (для направления анимации).
const catalogRank = (path) => {
  const value = normalizePath(path)
  if (value.startsWith('/product/')) return 3
  if (value.startsWith('/category/')) return 2
  if (value === '/fefco' || value.startsWith('/fefco/')) return 2
  if (value === '/catalog') return 1
  return 0
}

const clearDirClass = () => {
  document.documentElement.classList.remove(
    'catalog-nav-forward',
    'catalog-nav-back',
    'catalog-nav-switch',
  )
}

const releaseMotion = () => {
  if (!import.meta.client) {
    washOn.value = false
    return
  }
  const busy = document.querySelector('.catalog-fx-enter-active, .catalog-fx-leave-active')
  if (busy && releaseTries < 8) {
    releaseTries += 1
    scheduleRelease(generation, 90)
    return
  }
  releaseTries = 0
  washOn.value = false
  clearDirClass()
  document.documentElement.style.scrollBehavior = ''
}

const scheduleRelease = (token, delay) => {
  window.clearTimeout(clearTimer)
  window.clearTimeout(nuxtApp._catalogFxTimer)
  clearTimer = window.setTimeout(() => {
    if (token !== generation) return
    releaseMotion()
  }, delay)
  nuxtApp._catalogFxTimer = clearTimer
}

const armCatalogMotion = (direction) => {
  const token = ++generation
  releaseTries = 0
  navDirection.value = direction
  washOn.value = false
  clearDirClass()
  document.documentElement.classList.add(`catalog-nav-${direction}`)
  document.documentElement.style.scrollBehavior = 'auto'
  window.scrollTo(0, 0)
  scheduleRelease(token, 280)
}

if (import.meta.client) {
  nuxtApp._catalogFxUnsub?.()
  window.clearTimeout(nuxtApp._catalogFxTimer)
  nuxtApp._catalogFxUnsub = router.beforeResolve((to, from) => {
    if (!from.matched.length) return
    if (normalizePath(to.path) === normalizePath(from.path)) {
      transitionName.value = 'page-instant'
      return
    }

    const toRank = catalogRank(to.path)
    const fromRank = catalogRank(from.path)
    const reduced = prefersReducedMotion()

    if (toRank === 0) {
      generation += 1
      transitionName.value = 'page-instant'
      releaseMotion()
      return
    }

    transitionName.value = reduced ? 'catalog-fx-reduced' : 'catalog-fx'

    if (reduced) {
      const token = ++generation
      releaseMotion()
      document.documentElement.style.scrollBehavior = 'auto'
      window.scrollTo(0, 0)
      scheduleRelease(token, 220)
      return
    }

    let direction = 'switch'
    if (fromRank === 0 || toRank > fromRank) direction = 'forward'
    else if (toRank < fromRank) direction = 'back'
    armCatalogMotion(direction)
  })
}

const pageTransition = computed(() => {
  const name = transitionName.value
  if (name === 'catalog-fx') {
    return {
      name,
      duration: { enter: 240, leave: 180 },
    }
  }
  if (name === 'catalog-fx-reduced') {
    return {
      name,
      duration: { enter: 140, leave: 140 },
    }
  }
  return {
    name: 'page-instant',
    duration: { enter: 30, leave: 30 },
  }
})

onBeforeUnmount(() => {
  window.clearTimeout(clearTimer)
  nuxtApp._catalogFxUnsub?.()
  nuxtApp._catalogFxUnsub = null
})
</script>
