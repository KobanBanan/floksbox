<template>
  <section id="ident" class="ident-section">
    <video
      ref="videoRef"
      class="video-bg"
      src="/assets/task/stripes.mp4"
      autoplay
      muted
      loop
      playsinline
      preload="auto"
    />

    <div class="content-center">
      <div class="square-slider" @click="goNext">
        <img :src="slides[current]" alt="ident slide" class="slide-image" />
      </div>
    </div>
  </section>
  
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const slides = [
  '/assets/task/1.png',
  '/assets/task/2.png',
  '/assets/task/3.png',
  '/assets/task/4.png',
  '/assets/task/5.png'
]

const current = ref(0)
let timerId = null

const goNext = () => {
  current.value = (current.value + 1) % slides.length
}

const start = () => {
  stop()
  timerId = setInterval(goNext, 11000)
}

const stop = () => {
  if (timerId) {
    clearInterval(timerId)
    timerId = null
  }
}

const videoRef = ref(null)

onMounted(() => {
  start()
  const v = videoRef.value
  if (v) {
    // Ensure autoplay on iOS/Safari
    const playPromise = v.play?.()
    if (playPromise && typeof playPromise.then === 'function') {
      playPromise.catch(() => {})
    }
  }
})

onUnmounted(() => {
  stop()
})
</script>

<style scoped>
.ident-section {
  position: relative;
  width: 100%;
  min-height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.video-bg {
  position: absolute;
  left: 0;
  right: 0;
  top: 20%;
  width: 100%;
  height: 60%; /* еще тоньше полоса */
  object-fit: cover;
  z-index: -1;
}

.content-center {
  position: relative;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px 0;
}

.square-slider {
  width: min(80vw, 720px);
  aspect-ratio: 1 / 1;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.slide-image {
  width: 100%;
  height: 100%;
  object-fit: contain; /* без обрезаний */
  display: block;
}

@media (max-width: 768px) {
  .ident-section { min-height: 180px; }
  .video-bg { top: 22%; height: 56%; }
  .square-slider { width: min(86vw, 520px); }
}

@media (max-width: 480px) {
  .ident-section { min-height: 170px; }
  .video-bg { top: 24%; height: 52%; }
  .square-slider { width: min(92vw, 420px); }
}
</style>


