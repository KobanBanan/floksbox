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
          @click="handleProductClick(item, index)"
        >
          <div class="product-card">
            <!-- Фон ячейки -->
            <div class="card-background"></div>
            
            <!-- Изображение товара -->
            <div class="product-image-container">
              <img 
                :src="hoveredItems[index] ? '/assets/ui/but_on.png' : '/assets/ui/but_off.png'" 
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

    <!-- Модальное окно конструктора -->
    <div v-if="showConstructor" class="modal-overlay" @click="showConstructor = false">
      <div class="modal-content constructor-modal" @click.stop>
        <div class="modal-header">
          <h2>Конструктор круглых коробок</h2>
          <button class="close-btn" @click="showConstructor = false">×</button>
        </div>
        <BoxConstructor @close="showConstructor = false" />
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive } from 'vue'
import BoxConstructor from './BoxConstructor.vue'

// 8 товаров для сетки 2x4
const productItems = [
  { name: 'круглая коробка' },
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
// Состояние модального окна конструктора
const showConstructor = ref(false)

const setHover = (index, isHovered) => {
  hoveredItems[index] = isHovered
}

const handleProductClick = (item, index) => {
  if (item.name === 'круглая коробка') {
    showConstructor.value = true
  }
  // Для других товаров можно добавить другую логику
}
</script>

<style scoped>
.product-grid-section {
  padding: 40px 20px;
  background-color: transparent;
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
  background-image: url('/assets/ui/back.png');
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

/* Модальные окна */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(5px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: #fff;
  border-radius: 20px;
  padding: 0;
  max-width: 500px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.constructor-modal {
  max-width: 90vw;
  max-height: 90vh;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 25px 30px;
  border-bottom: 1px solid #e5e7eb;
}

.modal-header h2 {
  margin: 0;
  color: #1f2937;
  font-size: 24px;
  font-weight: 600;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #6b7280;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: all 0.2s ease;
}

.close-btn:hover {
  background: #f3f4f6;
  color: #374151;
}

/* Адаптивность модального окна */
@media (max-width: 768px) {
  .modal-content {
    margin: 20px;
    width: calc(100% - 40px);
  }

  .modal-header {
    padding: 20px;
  }
}
</style> 