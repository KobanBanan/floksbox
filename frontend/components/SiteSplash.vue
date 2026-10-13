<template>
  <div
    v-if="shown"
    class="site-splash"
    :class="{ 'is-hiding': hiding }"
    role="status"
    aria-live="polite"
    aria-label="Сайт загружается"
  >
    <div class="site-splash__stage">
      <span class="site-splash__wave" />
      <span class="site-splash__wave" />
      <span class="site-splash__wave" />
      <div class="site-splash__disc">
        <img
          class="site-splash__logo"
          src="/assets/logo/floksbox лого.png"
          alt="Floksbox"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
const shown = ref(true)
const hiding = ref(false)
const THRESHOLD = 0.2
const MAX_WAIT_MS = 12000

const contentRatio = () => {
  const images = Array.from(document.images).filter((img) => {
    const src = img.currentSrc || img.getAttribute('src') || ''
    return src && !src.startsWith('data:')
  })
  const eager = images.filter((img) => img.getAttribute('loading') !== 'lazy')
  const set = eager.length ? eager : images

  if (set.length) {
    const loaded = set.filter((img) => img.complete).length
    return loaded / set.length
  }

  const resources = performance.getEntriesByType('resource')
  if (!resources.length) {
    return document.readyState === 'loading' ? 0 : 1
  }
  const loaded = resources.filter((entry) => entry.responseEnd > 0).length
  return loaded / resources.length
}

const finish = () => {
  if (hiding.value || !shown.value) return
  hiding.value = true
  document.documentElement.classList.remove('splash-open')
  window.setTimeout(() => {
    shown.value = false
  }, 700)
}

let stopped = false
let started = 0

const tick = () => {
  if (stopped || hiding.value) return
  const elapsed = performance.now() - started
  if (contentRatio() >= THRESHOLD || elapsed >= MAX_WAIT_MS) {
    stopped = true
    document.removeEventListener('load', tick, true)
    finish()
    return
  }
  window.setTimeout(tick, 120)
}

onMounted(() => {
  document.documentElement.classList.add('splash-open')
  started = performance.now()
  document.addEventListener('load', tick, true)
  tick()
})

onUnmounted(() => {
  stopped = true
  document.removeEventListener('load', tick, true)
  document.documentElement.classList.remove('splash-open')
})
</script>

<style scoped>
.site-splash {
  position: fixed;
  inset: 0;
  z-index: 20000;
  display: grid;
  place-items: center;
  background: #fff;
  transition: opacity 0.65s ease, visibility 0.65s ease;
}

.site-splash.is-hiding {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}

.site-splash__stage {
  position: relative;
  width: min(340px, 72vw);
  aspect-ratio: 1;
}

.site-splash__wave,
.site-splash__disc {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: #fff;
}

.site-splash__wave {
  background: transparent;
  box-shadow:
    8px 8px 20px rgba(140, 156, 184, 0.42),
    -8px -8px 18px rgba(255, 255, 255, 0.95),
    inset 7px 7px 14px rgba(140, 156, 184, 0.22),
    inset -7px -7px 14px rgba(255, 255, 255, 0.9);
  animation: neo-wave 20s ease-out infinite;
  pointer-events: none;
}

.site-splash__wave:nth-child(2) {
  animation-delay: 0.75s;
}

.site-splash__wave:nth-child(3) {
  animation-delay: 1.5s;
}

.site-splash__disc {
  display: grid;
  place-items: center;
  box-shadow:
    16px 16px 32px rgba(163, 177, 198, 0.5),
    -16px -16px 32px rgba(255, 255, 255, 0.95),
    inset 1px 1px 2px rgba(255, 255, 255, 0.9);
}

.site-splash__logo {
  width: 72%;
  height: auto;
  object-fit: contain;
  user-select: none;
  pointer-events: none;
}

@keyframes neo-wave {
  0% {
    transform: scale(1);
    opacity: 0.95;
  }
  14% {
    transform: scale(2.35);
    opacity: 0;
  }
  100% {
    transform: scale(2.35);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .site-splash__wave {
    animation: none;
    opacity: 0;
  }
}
</style>
