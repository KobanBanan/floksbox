<template>
  <section class="product-carousel">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Наши товары</h2>
        <p class="section-description">Откройте для себя широкий ассортимент упаковочных решений</p>
      </div>
      
      <div class="carousel-wrapper">
        <button 
          v-if="showPrevButton"
          @click="scrollPrev" 
          class="carousel-button carousel-button-prev"
          :disabled="isScrolling"
        >
          ‹
        </button>
        
        <div 
          ref="carouselContainer" 
          class="carousel-container"
          @scroll="handleScroll"
        >
          <div class="carousel-track">
            <div 
              v-for="product in products" 
              :key="product.id" 
              class="carousel-item"
            >
              <ProductCard :product="product" />
            </div>
            
            <!-- Показать спиннер загрузки если есть еще товары -->
            <div v-if="loading" class="carousel-item">
              <div class="loading-placeholder">
                <div class="spinner"></div>
                <p>Загрузка...</p>
              </div>
            </div>
          </div>
        </div>
        
        <button 
          v-if="showNextButton"
          @click="scrollNext" 
          class="carousel-button carousel-button-next"
          :disabled="isScrolling"
        >
          ›
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
import ProductCard from './ProductCard.vue'

const carouselContainer = ref(null)
const products = ref([])
const loading = ref(false)
const currentPage = ref(1)
const hasNextPage = ref(true)
const isScrolling = ref(false)
const showPrevButton = ref(false)
const showNextButton = ref(true)

// Используем относительные пути благодаря прокси

// Загрузка товаров
const loadProducts = async (page = 1, append = false) => {
  try {
    loading.value = true
    const config = useRuntimeConfig()
    const apiBase = config.public.apiBase
    const response = await $fetch(`${apiBase}/api/products/`, {
      params: {
        page: page,
        page_size: 5,
        active_only: true
      }
    })
    
    if (append) {
      products.value = [...products.value, ...response.results]
    } else {
      products.value = response.results
    }
    
    hasNextPage.value = !!response.next
    currentPage.value = page
  } catch (error) {
    console.error('Ошибка загрузки товаров:', error)
  } finally {
    loading.value = false
  }
}

// Загрузить следующую страницу
const loadNextPage = async () => {
  if (hasNextPage.value && !loading.value) {
    await loadProducts(currentPage.value + 1, true)
  }
}

// Прокрутка карусели
const scrollNext = () => {
  const container = carouselContainer.value
  if (!container || isScrolling.value) return
  
  isScrolling.value = true
  const scrollAmount = container.clientWidth * 0.8
  
  container.scrollTo({
    left: container.scrollLeft + scrollAmount,
    behavior: 'smooth'
  })
  
  // Проверить нужно ли загрузить следующую страницу
  setTimeout(() => {
    const { scrollLeft, scrollWidth, clientWidth } = container
    if (scrollLeft + clientWidth >= scrollWidth * 0.8) {
      loadNextPage()
    }
    isScrolling.value = false
  }, 300)
}

const scrollPrev = () => {
  const container = carouselContainer.value
  if (!container || isScrolling.value) return
  
  isScrolling.value = true
  const scrollAmount = container.clientWidth * 0.8
  
  container.scrollTo({
    left: container.scrollLeft - scrollAmount,
    behavior: 'smooth'
  })
  
  setTimeout(() => {
    isScrolling.value = false
  }, 300)
}

// Обработка прокрутки
const handleScroll = () => {
  const container = carouselContainer.value
  if (!container) return
  
  const { scrollLeft, scrollWidth, clientWidth } = container
  
  // Показать/скрыть кнопки
  showPrevButton.value = scrollLeft > 10
  showNextButton.value = hasNextPage.value || scrollLeft < scrollWidth - clientWidth - 10
  
  // Автозагрузка при приближении к концу
  if (scrollLeft + clientWidth >= scrollWidth * 0.8 && hasNextPage.value && !loading.value) {
    loadNextPage()
  }
}

// Инициализация
onMounted(() => {
  loadProducts()
})
</script>

<style scoped>
.product-carousel {
  padding: 80px 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.section-header {
  text-align: center;
  margin-bottom: 50px;
}

.section-title {
  font-size: 48px;
  font-weight: 700;
  margin: 0 0 16px 0;
  font-family: 'Days One', cursive;
}

.section-description {
  font-size: 18px;
  margin: 0;
  max-width: 600px;
  margin: 0 auto;
}

.carousel-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  gap: 20px;
}

.carousel-container {
  flex: 1;
  overflow-x: auto;
  overflow-y: hidden;
  scroll-behavior: smooth;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.carousel-container::-webkit-scrollbar {
  display: none;
}

.carousel-track {
  display: flex;
  gap: 20px;
  padding: 10px 0;
}

.carousel-item {
  flex: 0 0 280px;
  height: 350px;
}

.carousel-button {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: none;
  background: white;
  color: #4a5568;
  font-size: 24px;
  font-weight: bold;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transition: all 0.3s ease;
  z-index: 2;
}

.carousel-button:hover:not(:disabled) {
  background: #4a5568;
  color: white;
  transform: scale(1.1);
}

.carousel-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

.loading-placeholder {
  width: 280px;
  height: 350px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #e2e8f0;
  border-top: 4px solid #4a5568;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 16px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@media (max-width: 768px) {
  .product-carousel {
    padding: 60px 0;
  }
  
  .container {
    padding: 0 15px;
  }
  
  .section-title {
    font-size: 36px;
  }
  
  .section-description {
    font-size: 16px;
  }
  
  .carousel-wrapper {
    gap: 10px;
  }
  
  .carousel-item {
    flex: 0 0 250px;
    height: 320px;
  }
  
  .carousel-button {
    width: 40px;
    height: 40px;
    font-size: 20px;
  }
  
  .loading-placeholder {
    width: 250px;
    height: 320px;
  }
}

@media (max-width: 480px) {
  .carousel-button {
    display: none;
  }
  
  .carousel-wrapper {
    gap: 0;
  }
  
  .carousel-track {
    gap: 15px;
    padding-left: 5px;
    padding-right: 5px;
  }
  
  .carousel-item {
    flex: 0 0 220px;
    height: 300px;
  }
  
  .loading-placeholder {
    width: 220px;
    height: 300px;
  }
}
</style> 