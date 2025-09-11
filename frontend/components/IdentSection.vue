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
  min-height: 400px; /* увеличено до 400px для большего пространства вокруг видео */
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.video-bg {
  position: absolute;
  left: 50%; /* центрируем относительно левого края */
  top: 20%; /* скорректирован отступ для центрирования увеличенного видео */
  width: 100vw; /* ширина во весь viewport */
  transform: translateX(-50%); /* центрируем по горизонтали */
  height: 60%; /* увеличена высота для полного отображения видео */
  object-fit: contain;
  z-index: -1;
  display: none; /* ВРЕМЕННО СКРЫТО: видео stripes.mp4 скрыто, но не удалено */
  /* 
  НАСТРОЙКИ ВИДЕО ДЛЯ ВОССТАНОВЛЕНИЯ:
  - src: /assets/task/stripes.mp4
  - autoplay: true
  - muted: true  
  - loop: true
  - playsinline: true
  - preload: auto
  - position: absolute, left: 50%, top: 20%
  - width: 100vw, height: 60%
  - transform: translateX(-50%)
  - object-fit: contain
  - z-index: -1
  */
}

.content-center { display: none; }

@media (max-width: 768px) {
  .ident-section { min-height: 320px; } /* увеличено до 320px для большего пространства */
  .video-bg { top: 30%; height: 40%; } /* еще больше уменьшенный размер */
  
}

@media (max-width: 480px) {
  .ident-section { min-height: 280px; } /* увеличено до 280px для большего пространства */
  .video-bg { top: 30%; height: 40%; } /* еще больше уменьшенный размер */
  
}
</style>


