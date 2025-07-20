<template>
  <section class="product-grid-section">
    <div class="container">
      <div class="product-grid">
        <div 
          v-for="(item, index) in productItems" 
          :key="index"
          class="product-item"
          @mouseenter="setHover(index, true)"
          @mouseleave="setHover(index, false)"
        >
          <div class="product-card">
            <!-- Фон ячейки -->
            <div class="card-background"></div>
            
            <!-- Изображение товара -->
            <div class="product-image-container">
              <img 
                :src="hoveredItems[index] ? '/assets/but_on.png' : '/assets/but_off.png'" 
                :alt="item.name"
                class="product-image"
                :class="{ 'lifted': hoveredItems[index] }"
              />
            </div>
            
            <!-- Текст товара -->
            <div class="product-text" :class="{ 'active': hoveredItems[index] }">
              {{ item.name }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive } from 'vue'

// 8 товаров для сетки 2x4
const productItems = [
  { name: 'товар' },
  { name: 'товар' },
  { name: 'товар' },
  { name: 'товар' },
  { name: 'товар' },
  { name: 'товар' },
  { name: 'товар' },
  { name: 'товар' }
]

// Состояние hover для каждого элемента
const hoveredItems = reactive({})

const setHover = (index, isHovered) => {
  hoveredItems[index] = isHovered
}
</script>

<style scoped>
.product-grid-section {
  padding: 40px 20px;
  background-color: #f8f9fa;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(2, 1fr);
  gap: 15px;
  justify-items: center;
}

.product-item {
  width: 100%;
  max-width: 340px;
  height: 210px;
}

.product-card {
  width: 100%;
  height: 100%;
  position: relative;
  background-image: url('/assets/back.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.card-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
  border-radius: 12px;
}

.product-image-container {
  position: absolute;
  top: 15px;
  left: 50%;
  transform: translateX(-50%);
  transition: transform 0.3s ease;
}

.product-image {
  width: 160px;
  height: 160px;
  object-fit: contain;
  transition: transform 0.3s ease;
}

.product-image.lifted {
  transform: translateY(-12px);
}

.product-text {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  font-family: 'Roboto', sans-serif;
  font-weight: bold;
  font-size: 23px;
  color: #000000;
  transition: color 0.3s ease;
  text-align: center;
  background: rgba(255, 255, 255, 0.9);
  padding: 5px 15px;
  border-radius: 15px;
  backdrop-filter: blur(5px);
}

.product-text.active {
  color: #47009f;
  background: rgba(255, 255, 255, 0.95);
}

/* Адаптивность */
@media (max-width: 1400px) {
  .product-grid {
    gap: 12px;
  }
  
  .product-item {
    max-width: 280px;
    height: 180px;
  }
}

@media (max-width: 1200px) {
  .product-grid {
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(3, 1fr);
    gap: 15px;
  }
  
  .product-item {
    height: 160px;
  }
  
  .product-text {
    font-size: 20px;
  }
}

@media (max-width: 768px) {
  .product-grid {
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(4, 1fr);
    gap: 12px;
  }
  
  .product-item {
    height: 150px;
  }
  
  .product-text {
    font-size: 18px;
    bottom: 15px;
  }
  
  .product-image {
    width: 60px;
    height: 60px;
  }
}

@media (max-width: 480px) {
  .product-grid {
    grid-template-columns: 1fr;
    grid-template-rows: repeat(8, 1fr);
    gap: 10px;
  }
  
  .product-item {
    height: 130px;
  }
  
  .product-grid-section {
    padding: 30px 15px;
  }
}
</style> 