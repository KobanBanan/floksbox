<template>
  <div
    ref="rootRef"
    class="kat-float"
    :class="{ 'kat-float--compact': compact }"
    :style="wrapperStyle"
    @mouseenter="onPointerEnter"
    @mouseleave="onPointerLeave"
    @mousemove="onPointerMove"
  >
    <img :src="src" :alt="alt" class="kat-float__img" />
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
  src: { type: String, required: true },
  alt: { type: String, default: '' },
  compact: { type: Boolean, default: false },
})

const rootRef = ref(null)
const wrapperStyle = ref({ transform: 'translate3d(0, -30px, 0)' })

const hovering = ref(false)
const reducedMotion = ref(false)

const target = { x: 0, y: 0 }
const current = { x: 0, y: 0 }

const BASE_Y = props.compact ? 0 : -30
const FLOAT_AMP = props.compact ? 6 : 9
const FLOAT_PERIOD_MS = props.compact ? 4800 : 5200
const PARALLAX_X = props.compact ? 8 : 14
const PARALLAX_Y = props.compact ? 5 : 9
const TILT_DEG = props.compact ? 0.12 : 0.18
const EASE = 0.075

let rafId = null
let startTime = 0

function applyTransform(floatY) {
  const tilt = current.x * TILT_DEG
  wrapperStyle.value = {
    transform: `translate3d(${current.x.toFixed(2)}px, ${(BASE_Y + floatY + current.y).toFixed(2)}px, 0) rotate(${tilt.toFixed(2)}deg)`
  }
}

function tick(timestamp) {
  if (!startTime) startTime = timestamp

  const floatY = reducedMotion.value
    ? 0
    : Math.sin(((timestamp - startTime) / FLOAT_PERIOD_MS) * Math.PI * 2) * FLOAT_AMP

  current.x += (target.x - current.x) * EASE
  current.y += (target.y - current.y) * EASE

  if (!hovering.value) {
    target.x *= 0.9
    target.y *= 0.9
  }

  applyTransform(floatY)
  rafId = requestAnimationFrame(tick)
}

function onPointerEnter() {
  hovering.value = true
}

function onPointerLeave() {
  hovering.value = false
  target.x = 0
  target.y = 0
}

function onPointerMove(event) {
  if (reducedMotion.value) return
  const el = rootRef.value
  if (!el) return

  const rect = el.getBoundingClientRect()
  if (!rect.width || !rect.height) return

  const nx = ((event.clientX - rect.left) / rect.width - 0.5) * 2
  const ny = ((event.clientY - rect.top) / rect.height - 0.5) * 2

  target.x = nx * PARALLAX_X
  target.y = ny * PARALLAX_Y
}

onMounted(() => {
  if (!import.meta.client) return

  reducedMotion.value = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  rafId = requestAnimationFrame(tick)
})

onBeforeUnmount(() => {
  if (rafId) cancelAnimationFrame(rafId)
})
</script>

<style scoped>
.kat-float {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  will-change: transform;
  cursor: default;
}

.kat-float--compact {
  width: 100%;
  height: 100%;
  align-items: center;
}

.kat-float--compact .kat-float__img {
  max-height: 100%;
  max-width: 100%;
}

.kat-float__img {
  display: block;
  max-height: var(--kat-max-height, 450px);
  max-width: 100%;
  width: auto;
  height: auto;
  object-fit: contain;
  object-position: center bottom;
  pointer-events: none;
  user-select: none;
}
</style>
