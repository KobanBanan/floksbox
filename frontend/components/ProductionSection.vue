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
            v-for="(slide, index) in shuffledSlides" 
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
const shuffledSlides = ref([])

const productionSlides = [
  { image: '/assets/production/00009052.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/12399_dizain-korobok-dlia-pitstsy-round-the-clock_640s.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/1460812309_14327757-1000x1000.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/1989984_upakovka_slozhnoj_vysechki.jpeg', alt: 'Производственное изображение' },
  { image: '/assets/production/36b8e41aabab2ebe00f6d0ddab820723.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/5.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/ad20b9cef8ecbee4e2d33102696dc73d.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/caf19f2ed5f34444df5429a11636336c.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/controlkillslove1.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/controlkillslove2.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/controlkillslove3.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/controlkillslove4.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/gmanman1.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/gmanman3.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/gofrokarton-korobki-gofrokoroba-gofrolotki_foto_largest.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/IMG_5513.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/le-tim_7X.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/pod-ovoshi.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/top-view-fresh-delicious-whole-pizza-pizza-box_114579-88419.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/Vegancuts-02.jpg', alt: 'Производственное изображение' },
  { image: '/assets/production/пакет_большой.jpg', alt: 'Производственное изображение' }
]

const nextSlide = () => {
  currentProductionSlide.value = (currentProductionSlide.value + 1) % shuffledSlides.value.length
}

const previousSlide = () => {
  currentProductionSlide.value = currentProductionSlide.value === 0 
    ? shuffledSlides.value.length - 1 
    : currentProductionSlide.value - 1
}

const shuffleArray = (array) => {
  const result = array.slice()
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[result[i], result[j]] = [result[j], result[i]]
  }
  return result
}

const startSlideShow = () => {
  slideInterval = setInterval(() => {
    nextSlide()
  }, 3000) // 3 секунды автосмена
}

onMounted(() => {
  shuffledSlides.value = shuffleArray(productionSlides)
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
  background-color: transparent;
  color: white;
}

/* Производственный слайдер */
.production-slider {
  max-width: 1200px; /* единая ширина */
  margin: 0 auto 60px auto;
  padding: 0 20px; /* внутренние отступы */
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