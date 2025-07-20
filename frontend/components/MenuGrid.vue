<template>
  <section class="menu-section">
    <div class="menu-grid">
      <div 
        v-for="(item, index) in menuItems" 
        :key="index"
        class="menu-item"
        @mouseenter="setHover(index, true)"
        @mouseleave="setHover(index, false)"
      >
        <div class="item-frame">
          <!-- Изображение товара -->
          <div class="item-image-container">
            <img 
              :src="hoveredItems[index] ? '/assets/but_on.png' : '/assets/but_off.png'" 
              :alt="item.name"
              class="item-image"
              :class="{ 'lifted': hoveredItems[index] }"
            />
          </div>
          
          <!-- Текст товара -->
          <div class="item-text" :class="{ 'active': hoveredItems[index] }">
            {{ item.name }}
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive } from 'vue'

// 8 товаров для сетки 2x4
const menuItems = [
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

<style lang="scss" scoped>
.menu-section {
  padding: 60px 20px;
  background-color: #f8f9fa;
}

.menu-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(2, 1fr);
  gap: 15px;
  max-width: 1400px;
  margin: 0 auto;
  
  // Ячейки 340x210px как указано в ТЗ
  .menu-item {
    width: 340px;
    height: 210px;
    justify-self: center;
  }
}

.item-frame {
  width: 100%;
  height: 100%;
  background-image: url('/assets/back.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.3s ease;
  
  &:hover {
    transform: translateY(-2px);
  }
}

.item-image-container {
  position: relative;
  width: 100%;
  height: 60%;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding-top: 0; // Изначально впритык к верхнему краю
}

.item-image {
  width: 160px;
  height: 160px;
  object-fit: contain;
  transition: transform 0.3s ease;
  
  // Активная фаза - подъем на 12px вверх
  &.lifted {
    transform: translateY(-12px);
  }
}

.item-text {
  position: absolute;
  bottom: 15px;
  left: 50%;
  transform: translateX(-50%);
  font-family: 'Roboto', sans-serif;
  font-weight: bold;
  font-size: 23px;
  color: #000000;
  transition: color 0.3s ease;
  text-align: center;
  
  &.active {
    color: #47009f;
  }
}

// Адаптивность
@media (max-width: 1440px) {
  .menu-grid {
    grid-template-columns: repeat(4, minmax(280px, 1fr));
    
    .menu-item {
      width: 100%;
      max-width: 340px;
      height: 180px;
    }
  }
}

@media (max-width: 1200px) {
  .menu-grid {
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(3, 1fr);
    gap: 12px;
    
    .menu-item {
      height: 160px;
    }
  }
  
  .item-text {
    font-size: 20px;
  }
}

@media (max-width: 768px) {
  .menu-grid {
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(4, 1fr);
    gap: 10px;
    
    .menu-item {
      height: 140px;
    }
  }
  
  .item-text {
    font-size: 18px;
    bottom: 10px;
  }
}

@media (max-width: 480px) {
  .menu-grid {
    grid-template-columns: 1fr;
    grid-template-rows: repeat(8, 1fr);
    
    .menu-item {
      height: 120px;
    }
  }
  
  .menu-section {
    padding: 40px 15px;
  }
}
</style> 