<template>
  <section class="love-section">
    <div class="section-title">
      <h2>Наше Производство</h2>
    </div>
    
    <div class="content-grid">
      <!-- Левая часть с основным изображением -->
      <div class="main-content">
        <div 
          class="image-wrapper"
          @mouseenter="setHovered(true)"
          @mouseleave="setHovered(false)"
        >
          <img 
            src="/assets/images/gmanman1.jpg" 
            alt="Производство упаковки" 
            class="love-image"
            :class="{ 'active': isHovered }"
          />
          <div class="image-overlay">
            <button class="overlay-button">
              <span class="arrow">→</span>
            </button>
          </div>
        </div>
        
        <div class="info-block">
          <h3>Наше производство</h3>
          <p>Современное оборудование и технологии для создания качественной упаковки</p>
        </div>
      </div>
      
      <!-- Правые колонки -->
      <div class="side-columns">
        <div class="column" v-for="(item, index) in sideItems" :key="index">
          <div class="column-content" :style="{ backgroundColor: item.color }">
            <button class="column-button">
              <span class="arrow">↓</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const isHovered = ref(false)

const sideItems = [
  { color: '#60a5fa' },
  { color: '#84cc16' },
  { color: '#60a5fa' }
]

const setHovered = (value) => {
  isHovered.value = value
}
</script>

<style scoped>
.love-section {
  padding: 60px 20px;
  background-color: #ffffff;
  color: white;
}

.section-title {
  text-align: left;
  margin-bottom: 30px;
  padding-left: 40px;
}

.section-title h2 {
  font-size: 2.5rem;
  font-weight: bold;
  color: white;
}

.content-grid {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  gap: 20px;
  align-items: stretch;
}

.main-content {
  flex: 2;
  position: relative;
}

.image-wrapper {
  position: relative;
  width: 94%;
  transition: width 0.5s ease;
  cursor: pointer;
  border-radius: 20px;
  overflow: hidden;
}

.image-wrapper:hover {
  width: 100%;
}

.love-image {
  width: 100%;
  height: 400px;
  object-fit: cover;
  display: block;
  opacity: 0.87;
  transition: opacity 0.5s ease, transform 0.5s ease;
}

.love-image.active {
  opacity: 1;
  transform: scale(1.02);
}

.image-overlay {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 2;
}

.overlay-button {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: white;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  transition: all 0.3s ease;
}

.overlay-button:hover {
  transform: scale(1.1);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.info-block {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(135deg, #8b5cf6, #7c3aed);
  color: white;
  padding: 20px;
  border-radius: 0 0 20px 20px;
}

.info-block h3 {
  font-size: 1.5rem;
  margin-bottom: 5px;
}

.info-block p {
  opacity: 0.9;
  font-size: 0.9rem;
}

.side-columns {
  flex: 1;
  display: flex;
  gap: 15px;
}

.column {
  flex: 1;
  height: 400px;
}

.column-content {
  width: 100%;
  height: 100%;
  border-radius: 50px;
  position: relative;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.column-content:hover {
  transform: translateY(-5px);
}

.column-button {
  position: absolute;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: white;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  transition: all 0.3s ease;
}

.column-button:hover {
  transform: translateX(-50%) scale(1.1);
}

.arrow {
  color: #333;
}

@media (max-width: 768px) {
  .content-grid {
    flex-direction: column;
  }
  
  .side-columns {
    flex-direction: row;
    height: 200px;
  }
  
  .column {
    height: 100%;
  }
  
  .love-image {
    height: 300px;
  }
  
  .section-title {
    padding-left: 20px;
  }
  
  .section-title h2 {
    font-size: 2rem;
  }
}

@media (max-width: 480px) {
  .love-section {
    padding: 40px 15px;
  }
  
  .content-grid {
    gap: 15px;
  }
  
  .side-columns {
    gap: 10px;
    height: 150px;
  }
  
  .love-image {
    height: 250px;
  }
}
</style> 