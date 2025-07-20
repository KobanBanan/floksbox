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
    
    <!-- Карточки записей -->
    <div class="records-grid">
      <div class="record-card large-card">
        <div class="card-content blue-card">
          <h3>Наше производство</h3>
          <p>Современное оборудование и технологии для создания качественной упаковки</p>
        </div>
      </div>
      
      <div class="record-cards-column">
        <div class="record-card small-card">
          <div class="card-content purple-card">
            <h3>Работаем ради вас</h3>
            <p>Каждый заказ выполняем с особым вниманием к деталям</p>
          </div>
        </div>
        
        <div class="record-card small-card">
          <div class="card-content green-card">
            <h3>Почему стоит выбрать нас</h3>
            <p>Опыт, качество и индивидуальный подход к каждому клиенту</p>
          </div>
        </div>
        
        <div class="record-card small-card">
          <div class="card-content orange-card">
            <h3>Мы гордимся нашей работой!</h3>
            <p>Каждая коробка - это результат профессионального мастерства</p>
          </div>
        </div>
      </div>
      
      <div class="record-card medium-card">
        <div class="card-content beige-card">
          <h3>Все для вашего бизнеса</h3>
          <p>Комплексные решения упаковки для любых задач и масштабов</p>
        </div>
        <div class="card-image">
          <img src="/assets/images/gmanman3.jpg" alt="Упаковочные материалы" />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const currentProductionSlide = ref(0)
let slideInterval = null

const productionSlides = [
  { image: '/assets/images/controlkillslove1.jpg', alt: 'Производственное помещение 1' },
  { image: '/assets/images/controlkillslove2.jpg', alt: 'Производственное помещение 2' },
  { image: '/assets/images/controlkillslove3.jpg', alt: 'Производственное помещение 3' },
  { image: '/assets/images/controlkillslove4.jpg', alt: 'Производственное помещение 4' }
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

/* Сетка записей */
.records-grid {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 3fr 1.5fr;
  grid-template-rows: 450px;
  gap: 15px;
}

.record-card {
  border-radius: 20px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.record-card:hover {
  transform: translateY(-5px);
}

.large-card {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.medium-card {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.small-card {
  height: 100%;
}

.record-cards-column {
  display: flex;
  flex-direction: column;
  gap: 15px;
  height: 100%;
}

.record-cards-column .small-card {
  flex: 1;
}

.card-content {
  padding: 20px;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.large-card .card-content {
  flex: 1;
}

.medium-card .card-content {
  flex: 1;
}

.card-content h3 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  color: white;
}

.card-content p {
  font-size: 0.9rem;
  opacity: 0.9;
  line-height: 1.4;
}

.card-image {
  height: 150px;
  overflow: hidden;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Цветовые схемы карточек */
.blue-card {
  background: linear-gradient(135deg, #3b82f6, #1d4ed8);
}

.purple-card {
  background: linear-gradient(135deg, #8b5cf6, #7c3aed);
}

.green-card {
  background: linear-gradient(135deg, #84cc16, #65a30d);
}

.orange-card {
  background: linear-gradient(135deg, #f97316, #ea580c);
}

.beige-card {
  background: linear-gradient(135deg, #f3f4f6, #d1d5db);
  color: #333;
}

.beige-card h3 {
  color: #333;
}

/* Адаптивность */
@media (max-width: 768px) {
  .production-section {
    padding: 40px 15px;
  }
  
  .slider-container {
    height: 250px;
  }
  
  .records-grid {
    grid-template-columns: 1fr;
    grid-template-rows: auto;
    gap: 15px;
  }
  
  .large-card,
  .medium-card,
  .small-card {
    grid-row: span 1;
    min-height: 200px;
  }
  
  .record-cards-column {
    grid-column: 1;
  }
  
  .card-image {
    height: 120px;
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
  
  .records-grid {
    gap: 10px;
  }
  
  .card-content {
    padding: 15px;
  }
  
  .card-content h3 {
    font-size: 1rem;
  }
  
  .card-content p {
    font-size: 0.8rem;
  }
}
</style> 