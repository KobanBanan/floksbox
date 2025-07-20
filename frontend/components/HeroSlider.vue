<template>
  <section class="hero-slider">
    <div class="slider-container">
      <div 
        v-for="(banner, index) in banners" 
        :key="index"
        class="slide"
        :class="{ 
          'active': index === currentSlide,
          'prev': index === prevSlide 
        }"
      >
        <img 
          :src="banner.src" 
          :alt="banner.alt" 
          class="slide-image"
        />
      </div>
      
      <!-- Индикаторы слайдов -->
      <div class="slide-indicators">
        <button 
          v-for="(banner, index) in banners"
          :key="index"
          class="indicator"
          :class="{ 'active': index === currentSlide }"
          @click="goToSlide(index)"
        ></button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const banners = [
      { src: '/assets/images/banner1.png', alt: 'Баннер 1' },
    { src: '/assets/images/banner2.png', alt: 'Баннер 2' }
]

const currentSlide = ref(0)
const prevSlide = ref(0)
let slideInterval = null

const nextSlide = () => {
  prevSlide.value = currentSlide.value
  currentSlide.value = (currentSlide.value + 1) % banners.length
}

const goToSlide = (index) => {
  if (index !== currentSlide.value) {
    prevSlide.value = currentSlide.value
    currentSlide.value = index
    // Перезапуск интервала
    clearInterval(slideInterval)
    startSlideShow()
  }
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

<style lang="scss" scoped>
.hero-slider {
  width: 100%;
  display: flex;
  justify-content: center;
  padding: 40px 20px;
}

.slider-container {
  position: relative;
  width: 80%; // 70-85% от viewport
  max-width: 1200px;
  aspect-ratio: 16/9; // Пропорциональная высота
  overflow: hidden;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 2s ease-in-out; // 2 секунды перетекания
  
  &.active {
    opacity: 1;
    z-index: 2;
  }
  
  &.prev {
    opacity: 0;
    z-index: 1;
  }
}

.slide-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.slide-indicators {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
  z-index: 3;
}

.indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 2px solid white;
  background: transparent;
  cursor: pointer;
  transition: background-color 0.3s ease;
  
  &.active {
    background-color: white;
  }
  
  &:hover {
    background-color: rgba(255, 255, 255, 0.7);
  }
}

// Адаптивность
@media (max-width: 768px) {
  .slider-container {
    width: 95%;
  }
  
  .hero-slider {
    padding: 20px 10px;
  }
}

@media (max-width: 480px) {
  .slider-container {
    width: 100%;
    border-radius: 0;
  }
  
  .hero-slider {
    padding: 0;
  }
}
</style> 