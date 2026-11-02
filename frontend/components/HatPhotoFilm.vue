<template>
  <section class="hat-film" aria-label="Фото круглых коробок">
    <div class="hat-film-window">
      <div class="hat-film-track" :class="{ paused: paused }">
        <div
          v-for="copy in 2"
          :key="copy"
          class="hat-film-group"
          :aria-hidden="copy === 2 ? 'true' : undefined"
        >
          <button
            v-for="(src, index) in photos"
            :key="`${copy}-${index}`"
            type="button"
            class="hat-film-card"
            :tabindex="copy === 2 ? -1 : 0"
            @click="open(index)"
          >
            <img :src="src" alt="Круглая коробка" draggable="false" />
          </button>
        </div>
      </div>
    </div>

    <div
      v-if="active !== null"
      class="hat-viewer"
      role="dialog"
      aria-modal="true"
      aria-label="Фото на весь экран"
      @click.self="close"
    >
      <button type="button" class="hat-viewer-close" aria-label="Закрыть" @click="close">×</button>
      <button type="button" class="hat-viewer-nav prev" aria-label="Предыдущее фото" @click="step(-1)">‹</button>
      <img :src="photos[active]" alt="Круглая коробка" />
      <button type="button" class="hat-viewer-nav next" aria-label="Следующее фото" @click="step(1)">›</button>
    </div>
  </section>
</template>

<script setup>
const photos = Array.from({ length: 29 }, (_, index) => {
  return `/hat-boxes/${String(index + 1).padStart(2, '0')}.jpg`
})

const active = ref(null)
const paused = computed(() => active.value !== null)

const open = (index) => {
  active.value = index
}

const close = () => {
  active.value = null
}

const step = (direction) => {
  if (active.value === null) return
  active.value = (active.value + direction + photos.length) % photos.length
}

const onKey = (event) => {
  if (active.value === null) return
  if (event.key === 'Escape') close()
  if (event.key === 'ArrowRight') step(1)
  if (event.key === 'ArrowLeft') step(-1)
}

onMounted(() => {
  window.addEventListener('keydown', onKey)
})

onBeforeUnmount(() => {
  window.removeEventListener('keydown', onKey)
})
</script>

<style scoped>
.hat-film {
  width: 100%;
  padding: 8px 0 72px;
}

.hat-film-window {
  width: 100%;
  overflow: hidden;
}

.hat-film-window:hover .hat-film-track {
  animation-play-state: paused;
}

.hat-film-track {
  display: flex;
  width: max-content;
  animation: hat-film-move 110s linear infinite;
}

.hat-film-track.paused {
  animation-play-state: paused;
}

.hat-film-group {
  display: flex;
  gap: 14px;
  padding-right: 14px;
}

.hat-film-card {
  height: 120px;
  padding: 0;
  border: 0;
  border-radius: 10px;
  background: #fff;
  box-shadow: 0 8px 22px rgba(28, 25, 21, 0.12);
  overflow: hidden;
  cursor: pointer;
  flex: none;
}

.hat-film-card img {
  display: block;
  height: 120px;
  width: auto;
}

.hat-viewer {
  position: fixed;
  inset: 0;
  z-index: 4000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 72px;
  background: rgba(18, 16, 14, 0.92);
}

.hat-viewer img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  border-radius: 8px;
}

.hat-viewer-close,
.hat-viewer-nav {
  position: absolute;
  border: 0;
  background: transparent;
  color: #fff;
  cursor: pointer;
  line-height: 1;
}

.hat-viewer-close {
  top: 16px;
  right: 20px;
  font-size: 40px;
}

.hat-viewer-nav {
  top: 50%;
  transform: translateY(-50%);
  font-size: 56px;
  padding: 0 8px;
}

.hat-viewer-nav.prev { left: 12px; }
.hat-viewer-nav.next { right: 12px; }

@keyframes hat-film-move {
  from { transform: translateX(-50%); }
  to { transform: translateX(0); }
}

@media (prefers-reduced-motion: reduce) {
  .hat-film-track {
    animation: none;
  }
}

@media (max-width: 640px) {
  .hat-viewer {
    padding: 56px 16px;
  }

  .hat-viewer-nav {
    font-size: 40px;
  }
}
</style>
