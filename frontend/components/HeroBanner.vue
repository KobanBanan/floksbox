<template>
  <section class="hero-banner">
    <div class="hero-container">
      <div 
        v-for="(banner, index) in banners" 
        :key="index"
        class="hero-slide"
        :class="{ 'active': index === currentSlide }"
      >
        <div class="banner-background">
          <img :src="banner.image" :alt="banner.alt" class="banner-image" />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const banners = [
  {
    image: '/assets/banner1.png',
    alt: 'Упакуем ваш бизнес - Баннер 1'
  },
  {
    image: '/assets/banner2.png', 
    alt: 'Упакуем ваш бизнес - Баннер 2'
  }
]

const currentSlide = ref(0)
let slideInterval = null

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % banners.length
}

const startSlideShow = () => {
  slideInterval = setInterval(() => {
    nextSlide()
  }, 6000) // 6 секунд
}

onMounted(() => {
  startSlideShow()
})

onUnmounted(() => {
  if (slideInterval) {
    clearInterval(slideInterval)
  }
})
</script>

<style scoped>
.hero-banner {
  position: relative;
  width: 80%;
  height: 100vh;
  margin: -70px auto 0 auto;
  overflow: hidden;
}

.hero-container {
  position: relative;
  width: 100%;
  height: 100%;
}

.hero-slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 2s ease-in-out;
}

.hero-slide.active {
  opacity: 1;
  z-index: 2;
}

.banner-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.banner-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: center;
}

/* Адаптивность */
@media (max-width: 768px) {
  .hero-banner {
    width: 90%;
    height: 100vh;
  }
}

@media (max-width: 480px) {
  .hero-banner {
    width: 95%;
    height: 100vh;
  }
}
</style> 