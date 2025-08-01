<template>
  <div class="product-page">
    <!-- Header -->
    <HeaderSimple />
    
    <!-- Product Details -->
    <section class="product-details" v-if="product">
      <div class="container">
        <div class="product-layout">
          <!-- Product Image -->
          <div class="product-image-section">
            <div class="product-image-wrapper">
              <img 
                :src="product.image_url || '/assets/images/mainpage.png'" 
                :alt="product.name"
                class="product-image"
                @error="handleImageError"
              />
            </div>
          </div>
          
          <!-- Product Info -->
          <div class="product-info-section">
            <div class="product-header">
              <h1 class="product-title">{{ product.name }}</h1>
              <div class="product-meta">
                <div class="product-category" v-if="product.category_name">
                  <span>Тип товара:</span> {{ product.category_name }}
                </div>
                <div class="product-article">
                  <span>Артикул товара:</span> {{ product.id }}-{{ product.name.slice(0, 3).toUpperCase() }}
                </div>
              </div>
            </div>
            
            <div class="product-description">
              <p>{{ product.description }}</p>
            </div>
            
            <div class="product-specifications">
              <h3>Характеристики:</h3>
              <div class="specs-grid">
                <div class="spec-item">
                  <span class="spec-label">Размер:</span>
                  <span class="spec-value">{{ product.dimensions }}</span>
                </div>
                <div class="spec-item" v-if="product.volume > 0">
                  <span class="spec-label">Объем:</span>
                  <span class="spec-value">{{ formatVolume(product.volume) }} см³</span>
                </div>
                <div class="spec-item" v-if="product.price">
                  <span class="spec-label">Цена за штуку:</span>
                  <span class="spec-value price">{{ formatPrice(product.price) }} ₽</span>
                </div>
              </div>
            </div>
            
            <div class="product-advantages">
              <p><strong>Назначение:</strong> Организация пространства и упаковка подарков.</p>
              <p><strong>Особенности:</strong> Стильный дизайн, надежная защита содержимого, плотно прилегающая крышка.</p>
              <p><strong>Применение:</strong> Космология, канцелярские принадлежности, бижутерия, чай, сладости.</p>
              <p><strong>Ключевые характеристики:</strong> Отличный дизайн, надежная защита содержимого, плотно прилегающая крышка.</p>
              <p><strong>Примеры применения:</strong> Косметика, канцелярские принадлежности, бижутерия, чай, сладости.</p>
              <p><strong>Размер:</strong> {{ product.dimensions }}</p>
              <p><strong>Цвет на выбор:</strong></p>
              <p>Эта коробка станет не только функциональным элементом вашего интерьера, но и прекрасным способом преподнести подарок. Благодаря плотно прилегающей крышке, содержимое будет надежно защищено от пыли и влаги, а эстетичный внешний вид коробки добавит особую торжественность любому сюрпризу.</p>
            </div>
            
            <div class="product-action">
              <button class="order-button" @click="openOrderModal">
                заказать у менеджера
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    <!-- Recommended Products -->
    <section class="recommended-products" v-if="recommendedProducts.length">
      <div class="container">
        <h2 class="section-title">Рекомендуемые товары</h2>
        <div class="products-grid">
          <div 
            v-for="recommendedProduct in recommendedProducts" 
            :key="recommendedProduct.id"
            class="product-item"
          >
            <ProductCard :product="recommendedProduct" />
          </div>
        </div>
      </div>
    </section>
    
    <!-- Loading State -->
    <div v-if="pending" class="loading-container">
      <div class="spinner"></div>
      <p>Загрузка товара...</p>
    </div>
    
    <!-- Error State -->
    <div v-if="error" class="error-container">
      <h2>Товар не найден</h2>
      <p>К сожалению, запрашиваемый товар не существует или был удален.</p>
      <NuxtLink to="/" class="back-button">Вернуться на главную</NuxtLink>
    </div>
    
    <!-- Footer -->
    <FooterMap />
  </div>
</template>

<script setup>
import HeaderSimple from '~/components/HeaderSimple.vue'
import ProductCard from '~/components/ProductCard.vue'
import FooterMap from '~/components/FooterMap.vue'

const route = useRoute()
const router = useRouter()

const apiBaseUrl = 'http://localhost:8000'
const productId = route.params.id

// Reactive data
const product = ref(null)
const recommendedProducts = ref([])
const pending = ref(true)
const error = ref(false)

// Загрузка товара
const loadProduct = async () => {
  try {
    pending.value = true
    error.value = false
    
    const response = await $fetch(`${apiBaseUrl}/api/products/${productId}/`)
    product.value = response
    
    // Обновляем meta-теги
    if (response) {
      useHead({
        title: `${response.name} - Floksbox`,
        meta: [
          { name: 'description', content: response.description.slice(0, 160) },
          { name: 'keywords', content: `${response.name}, ${response.category_name || ''}, упаковка, floksbox` }
        ]
      })
    }
  } catch (err) {
    console.error('Ошибка загрузки товара:', err)
    error.value = true
  } finally {
    pending.value = false
  }
}

// Загрузка рекомендуемых товаров
const loadRecommendedProducts = async () => {
  try {
    const response = await $fetch(`${apiBaseUrl}/api/products/`, {
      params: {
        active_only: true,
        page_size: 4
      }
    })
    recommendedProducts.value = response.results || []
  } catch (err) {
    console.error('Ошибка загрузки рекомендуемых товаров:', err)
  }
}

// Форматирование цены
const formatPrice = (price) => {
  return new Intl.NumberFormat('ru-RU').format(price)
}

// Форматирование объема
const formatVolume = (volume) => {
  return new Intl.NumberFormat('ru-RU').format(Math.round(volume))
}

// Обработка ошибки загрузки изображения
const handleImageError = (event) => {
  event.target.src = '/assets/images/mainpage.png'
}

// Открытие модального окна заказа
const openOrderModal = () => {
  // Скроллим к форме заказа на главной странице
  router.push('/#order-form')
}

// Загрузка данных при монтировании
onMounted(async () => {
  await Promise.all([
    loadProduct(),
    loadRecommendedProducts()
  ])
})

// Обработка изменения route (для SPA навигации)
watch(() => route.params.id, async (newId) => {
  if (newId) {
    await loadProduct()
  }
})
</script>

<style scoped>
.product-page {
  min-height: 100vh;
  background: #ffffff;
}

.product-details {
  padding: 40px 0 80px;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.product-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: start;
}

.product-image-section {
  position: sticky;
  top: 20px;
}

.product-image-wrapper {
  width: 100%;
  aspect-ratio: 1;
  border-radius: 20px;
  overflow: hidden;
  background: #f8f9fa;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.product-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product-info-section {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.product-header {
  border-bottom: 1px solid #e2e8f0;
  padding-bottom: 20px;
}

.product-title {
  font-size: 48px;
  font-weight: 700;
  color: #2d3748;
  margin: 0 0 16px 0;
  line-height: 1.2;
  font-family: 'Montserrat', sans-serif;
}

.product-meta {
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 16px;
  color: #4a5568;
}

.product-meta span {
  font-weight: 600;
}

.product-description {
  font-size: 18px;
  line-height: 1.7;
  color: #4a5568;
}

.product-specifications h3 {
  font-size: 24px;
  font-weight: 600;
  color: #2d3748;
  margin: 0 0 20px 0;
}

.specs-grid {
  display: grid;
  gap: 12px;
}

.spec-item {
  display: grid;
  grid-template-columns: 180px 1fr;
  gap: 16px;
  padding: 12px 0;
  border-bottom: 1px solid #f1f5f9;
}

.spec-label {
  font-weight: 600;
  color: #4a5568;
}

.spec-value {
  color: #2d3748;
}

.spec-value.price {
  font-size: 24px;
  font-weight: 700;
  color: #1a365d;
}

.product-advantages {
  font-size: 16px;
  line-height: 1.6;
  color: #4a5568;
}

.product-advantages p {
  margin: 0 0 12px 0;
}

.product-advantages strong {
  color: #2d3748;
}

.product-action {
  margin-top: 20px;
}

.order-button {
  background: #C8FF00;
  color: #000000;
  border: none;
  padding: 18px 40px;
  font-size: 18px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;
  max-width: 400px;
}

.order-button:hover {
  background: #B8EF00;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(200, 255, 0, 0.3);
}

.recommended-products {
  padding: 80px 0;
  background: #f8f9fa;
}

.section-title {
  font-size: 36px;
  font-weight: 700;
  color: #2d3748;
  text-align: center;
  margin: 0 0 50px 0;
  font-family: 'Montserrat', sans-serif;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  max-width: 1000px;
  margin: 0 auto;
}

.product-item {
  height: 280px;
}

.loading-container,
.error-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
  text-align: center;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid #e2e8f0;
  border-top: 4px solid #4a5568;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error-container h2 {
  color: #e53e3e;
  margin-bottom: 16px;
}

.back-button {
  display: inline-block;
  background: #4a5568;
  color: white;
  padding: 12px 24px;
  text-decoration: none;
  border-radius: 6px;
  margin-top: 20px;
  transition: background 0.3s ease;
}

.back-button:hover {
  background: #2d3748;
}

@media (max-width: 968px) {
  .product-layout {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  
  .product-image-section {
    position: static;
  }
  
  .product-title {
    font-size: 36px;
  }
  
  .spec-item {
    grid-template-columns: 1fr;
    gap: 8px;
  }
  
  .products-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
  }
  
  .product-item {
    height: 260px;
  }
}

@media (max-width: 768px) {
  .product-details {
    padding: 20px 0 60px;
  }
  
  .container {
    padding: 0 15px;
  }
  
  .product-layout {
    gap: 30px;
  }
  
  .product-title {
    font-size: 28px;
  }
  
  .products-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
  }
  
  .product-item {
    height: 250px;
  }
}

@media (max-width: 480px) {
  .products-grid {
    grid-template-columns: 1fr;
    gap: 15px;
  }
  
  .product-item {
    height: 220px;
  }
}
</style> 