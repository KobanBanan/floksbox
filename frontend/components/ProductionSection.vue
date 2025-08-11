<template>
  <section class="production-section">
    <!-- Слайдер с производственными помещениями -->
    <div class="production-slider">
      <div class="slider-container">
        <button class="slider-btn prev" @click="previousSlide">
          <span>←</span>
        </button>
        
        <div class="slider-content">
          <div 
            v-for="(slide, index) in productionSlides" 
            :key="index"
            class="production-slide"
            :class="{ 'active': index === currentProductionSlide }"
          >
            <img :src="slide.image" :alt="slide.alt" class="production-image" />
          </div>
        </div>
        
        <button class="slider-btn next" @click="nextSlide">
          <span>→</span>
        </button>
      </div>
    </div>
    

  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const currentProductionSlide = ref(0)
let slideInterval = null

const productionSlides = [
  { image: '/assets/production/controlkillslove1.jpg', alt: 'Производственное помещение 1' },
  { image: '/assets/production/controlkillslove2.jpg', alt: 'Производственное помещение 2' },
  { image: '/assets/production/controlkillslove3.jpg', alt: 'Производственное помещение 3' },
  { image: '/assets/production/controlkillslove4.jpg', alt: 'Производственное помещение 4' }
]

const nextSlide = () => {
  currentProductionSlide.value = (currentProductionSlide.value + 1) % productionSlides.length
}

const previousSlide = () => {
  currentProductionSlide.value = currentProductionSlide.value === 0 
    ? productionSlides.length - 1 
    : currentProductionSlide.value - 1
}

const startSlideShow = () => {
  slideInterval = setInterval(() => {
    nextSlide()
  }, 4000) // 4 секунды автосмена
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
.production-section {
  padding: 60px 20px;
  background-color: #ffffff;
  color: white;
}

/* Производственный слайдер */
.production-slider {
  max-width: 1200px;
  margin: 0 auto 60px auto;
}

.slider-container {
  position: relative;
  height: 400px;
  border-radius: 15px;
  overflow: hidden;
}

.slider-content {
  position: relative;
  width: 100%;
  height: 100%;
}

.production-slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 0.5s ease;
}

.production-slide.active {
  opacity: 1;
}

.production-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.slider-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.9);
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: #333;
  transition: all 0.3s ease;
  z-index: 2;
}

.slider-btn:hover {
  background: white;
  transform: translateY(-50%) scale(1.1);
}

.slider-btn.prev {
  left: 20px;
}

.slider-btn.next {
  right: 20px;
}



/* Адаптивность */
@media (max-width: 768px) {
  .production-section {
    padding: 40px 15px;
  }
  
  .slider-container {
    height: 250px;
  }
  

}

@media (max-width: 480px) {
  .slider-btn {
    width: 40px;
    height: 40px;
    font-size: 1.2rem;
  }
  
  .slider-btn.prev {
    left: 10px;
  }
  
  .slider-btn.next {
    right: 10px;
  }
  

}
</style> 