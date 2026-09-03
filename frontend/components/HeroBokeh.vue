<template>
  <div ref="rootRef" class="hero-bokeh" aria-hidden="true">
    <span
      v-for="dot in dots"
      :key="dot.id"
      class="hero-bokeh__dot"
      :style="{
        width: `${dot.size}px`,
        height: `${dot.size}px`,
        left: `${dot.left}%`,
        bottom: `${dot.bottom}%`,
        background: dot.background,
        '--dx': dot.dx,
        '--dy': dot.dy,
        animationDuration: dot.duration,
        animationDelay: dot.delay
      }"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const BOKEH_COLORS = [
  'rgba(160, 142, 198, 0.55)',
  'rgba(94, 48, 133, 0.48)',
  'rgba(208, 255, 10, 0.42)',
  'rgba(142, 173, 196, 0.5)',
  'rgba(173, 149, 120, 0.46)',
  'rgba(255, 255, 255, 0.65)'
]

const rootRef = ref(null)
const dots = ref([])

function createDots() {
  const zoneH = rootRef.value?.clientHeight || 400
  const count = 32

  dots.value = Array.from({ length: count }, () => {
    const size = 26 + Math.random() * 50
    const duration = 12 + Math.random() * 14
    // почти на всю высоту зоны — долетают до верха
    const rise = zoneH * (0.88 + Math.random() * 0.14)

    return {
      id: Math.random(),
      size,
      left: 2 + Math.random() * 76,
      bottom: Math.random() * 8,
      background: BOKEH_COLORS[Math.floor(Math.random() * BOKEH_COLORS.length)],
      dx: `${(-38 + Math.random() * 52).toFixed(1)}px`,
      dy: `${rise.toFixed(0)}px`,
      duration: `${duration.toFixed(2)}s`,
      delay: `${(-Math.random() * duration).toFixed(2)}s`
    }
  })
}

onMounted(() => {
  if (!import.meta.client) return
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
  requestAnimationFrame(() => createDots())
})
</script>

<style scoped>
.hero-bokeh {
  position: absolute;
  top: var(--bokeh-inset-top, 0);
  bottom: 0;
  left: var(--bokeh-inset-left, 50%);
  right: var(--bokeh-inset-right, 9%);
  z-index: 3;
  overflow: hidden;
  pointer-events: none;
  -webkit-mask-image:
    linear-gradient(to top, transparent 0%, black 8%, black 94%, transparent 100%),
    linear-gradient(to right, transparent 0%, black 5%, black 90%, transparent 100%);
  -webkit-mask-composite: source-in;
  mask-image:
    linear-gradient(to top, transparent 0%, black 8%, black 94%, transparent 100%),
    linear-gradient(to right, transparent 0%, black 5%, black 90%, transparent 100%);
  mask-composite: intersect;
}

.hero-bokeh__dot {
  position: absolute;
  border-radius: 50%;
  filter: blur(2px);
  opacity: 0;
  mix-blend-mode: multiply;
  animation: hero-bokeh-float linear infinite;
  will-change: transform, opacity;
}

@keyframes hero-bokeh-float {
  0% {
    transform: translate3d(0, 0, 0) scale(0.75);
    opacity: 0;
  }
  8% {
    opacity: 0.5;
  }
  82% {
    opacity: 0.46;
  }
  93% {
    opacity: 0.2;
  }
  100% {
    transform: translate3d(var(--dx, 0), calc(-1 * var(--dy, 360px)), 0) scale(1.2);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hero-bokeh__dot {
    animation: none;
    opacity: 0;
  }
}
</style>
