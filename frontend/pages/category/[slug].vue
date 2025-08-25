<template>
  <div class="category-page">
    <!-- Шапка сайта -->
    <HeaderSimple />
    
    <!-- Главный баннер категории -->
    <section class="category-hero">
      <!-- Слой 1: Фоновое изображение с слайдшоу f1.png и f2.png -->
      <div class="background-layer">
        <img 
          src="/assets/images/f1.png" 
          alt="Фон 1" 
          class="bg-image" 
          :class="{ 'fade-out': !showF1 }"
        />
        <img 
          src="/assets/images/f2.png" 
          alt="Фон 2" 
          class="bg-image bg-image-overlay" 
          :class="{ 'fade-in': !showF1 }"
        />
      </div>
      
      <!-- Слой 2: Облако oblako.png -->
      <div class="cloud-layer">
        <img src="/assets/images/oblako.png" alt="Облако" class="cloud-image" />
      </div>
      
      <!-- Слой 3: Полоса floksbox - diag.png -->
      <div class="diagonal-layer">
        <img src="/assets/images/diag.png" alt="Полоса FloksBox" class="diagonal-image" />
      </div>
      

      
      <!-- Контейнер для контента с ограничением ширины -->
      <div class="content-container">
        <!-- Слой 5: Текст - выше всего, если длинный, то опускается на диагональную полосу -->
        <div class="text-layer">
          <div class="text-content">
            <h1 class="category-title">{{ categoryName }}</h1>
            <p class="category-description">
              {{ categoryDescription }}
            </p>
          </div>
        </div>
        
        <!-- Слой 4: Картинка kat1.png внутри контейнера -->
        <div class="product-layer">
          <img :src="categoryImage" :alt="categoryName" class="product-image" />
        </div>
      </div>
    </section>
    
    <!-- Раздел с товарами -->
    <section class="products-section">
      <div v-if="loading" class="loading-container">
        <div class="spinner"></div>
        <p>Загрузка товаров...</p>
      </div>
      
      <div v-else-if="products.length > 0" class="products-grid">
        <div 
          v-for="product in products" 
          :key="product.id" 
          class="product-card"
          @click="navigateToProduct(product.id)"
        >
          <div class="product-image-container">
            <img 
              v-if="product.image_url"
              :src="product.image_url" 
              :alt="product.name"
              class="product-image"
              @error="handleImageError"
            />
            <div v-else class="product-image-placeholder">
              <span>{{ product.name }}</span>
            </div>
          </div>
          <div class="product-info">
            <h3>{{ product.name }}</h3>
            <p v-if="product.price">{{ formatPrice(product.price) }} ₽</p>
            <p v-else>Цена по запросу</p>
            <small v-if="product.dimensions">{{ product.dimensions }}</small>
          </div>
        </div>
      </div>
      
      <div v-else class="no-products">
        <h3>В этой категории пока нет товаров</h3>
        <p>Мы работаем над пополнением каталога</p>
      </div>
    </section>
    
    <!-- Футер сайта -->
    <FooterNew />
  </div>
</template>

<script setup>
import HeaderSimple from '../../components/HeaderSimple.vue'
import FooterNew from '../../components/FooterNew.vue'

const route = useRoute()
const router = useRouter()

// Реактивные данные
const products = ref([])
const loading = ref(true)
const showF1 = ref(true)

const apiBaseUrl = 'http://localhost:8000'

// Получаем slug категории из URL
const categorySlug = computed(() => route.params.slug)

// Маппинг slug-ов в данные категорий
const categoryConfig = {
  'four-flap-boxes': {
    name: 'Четырехклапанные коробки',
    description: 'Это универсальное решение для упаковки, хранения и транспортировки различных товаров. Наша компания предлагает высококачественные гофрокороба, изготовленные по современным технологиям из экологичного материала.',
    image: '/assets/images/kat1.png'
  },
  'corrugated-sheets': {
    name: 'Гофролисты',
    description: 'Высококачественные гофрированные листы для создания упаковки любой сложности. Экологичный материал с отличными защитными свойствами.',
    image: '/assets/images/kat2.png'
  },
  'complex-cutting': {
    name: 'Сложная высечка',
    description: 'Индивидуальные упаковочные решения с использованием технологии сложной высечки. Создаем уникальную упаковку под ваши потребности.',
    image: '/assets/images/kat3.png'
  },
  'offset-printing': {
    name: 'Офсетная печать',
    description: 'Высококачественная офсетная печать на упаковке. Яркие цвета, четкие изображения и стойкость к внешним воздействиям.',
    image: '/assets/images/kat4.png'
  },
  'gift-bags': {
    name: 'Подарочные пакеты',
    description: 'Стильные и прочные подарочные пакеты для любых случаев. Широкий выбор размеров, цветов и дизайнов.',
    image: '/assets/images/kat5.png'
  },
  'hat-boxes': {
    name: 'Шляпные коробки',
    description: 'Элегантные круглые коробки для хранения и подарков. Идеальны для цветов, аксессуаров и эксклюзивных товаров.',
    image: '/assets/images/kat6.png'
  },
  'designer-packaging': {
    name: 'Дизайнерская упаковка',
    description: 'Эксклюзивная дизайнерская упаковка, созданная специально для вашего бренда. Уникальный дизайн и премиальные материалы.',
    image: '/assets/images/kat7.png'
  },
  'laminated-corrugated': {
    name: 'Кашированная гофроупаковка',
    description: 'Премиальная упаковка с ламинированным покрытием. Сочетает прочность гофрокартона с красивым внешним видом.',
    image: '/assets/images/kat8.png'
  },
  'flexo-corrugated': {
    name: 'Гофроупаковка с флексопечатью',
    description: 'Качественная печать на гофрокартоне методом флексографии. Экономичное решение для больших тиражей упаковки.',
    image: '/assets/images/kat9.png'
  }
}

// Получаем данные текущей категории
const currentCategory = computed(() => {
  return categoryConfig[categorySlug.value] || categoryConfig['four-flap-boxes']
})

const categoryName = computed(() => currentCategory.value.name)
const categoryDescription = computed(() => currentCategory.value.description)
const categoryImage = computed(() => currentCategory.value.image)

// Загрузка товаров по категории
const loadCategoryProducts = async () => {
  try {
    loading.value = true
    
    // Получаем товары, фильтруя по названию категории
    const response = await $fetch(`${apiBaseUrl}/api/products/`, {
      params: {
        category_name: categoryName.value,
        active_only: true,
        page_size: 50
      }
    })
    
    products.value = response.results || []
  } catch (error) {
    console.error('Ошибка загрузки товаров категории:', error)
    products.value = []
  } finally {
    loading.value = false
  }
}

// Форматирование цены
const formatPrice = (price) => {
  return new Intl.NumberFormat('ru-RU').format(price)
}

// Обработка ошибки загрузки изображения
const handleImageError = (event) => {
  event.target.src = '/assets/images/mainpage.png'
}

// Навигация к товару
const navigateToProduct = (productId) => {
  router.push(`/product/${productId}`)
}

// Слайдшоу фона
let backgroundInterval
const startBackgroundSlideshow = () => {
  backgroundInterval = setInterval(() => {
    showF1.value = !showF1.value
  }, 4000) // 1 секунда показ + 3 секунды переход = 4 секунды
}

const stopBackgroundSlideshow = () => {
  if (backgroundInterval) {
    clearInterval(backgroundInterval)
  }
}

// Загрузка данных при монтировании
onMounted(() => {
  loadCategoryProducts()
  startBackgroundSlideshow()
})

// Очистка интервала при размонтировании
onUnmounted(() => {
  stopBackgroundSlideshow()
})

// Обновление товаров при изменении маршрута
watch(() => route.params.slug, () => {
  loadCategoryProducts()
})

// Настройка мета-данных страницы
useHead({
  title: computed(() => `${categoryName.value} - Floksbox`),
  meta: [
    { 
      name: 'description', 
      content: computed(() => categoryDescription.value.slice(0, 160))
    },
    {
      name: 'keywords',
      content: computed(() => `${categoryName.value.toLowerCase()}, упаковка, floksbox, картонные коробки`)
    }
  ]
})
</script>

<style lang="scss" scoped>
.category-page {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.category-hero {
  position: relative;
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  height: 450px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Слой 1: Фоновое изображение */
.background-layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  
  .bg-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: opacity 3s ease-in-out;
    
    &.bg-image-overlay {
      position: absolute;
      top: 0;
      left: 0;
      opacity: 0;
    }
    
    &.fade-out {
      opacity: 0;
    }
    
    &.fade-in {
      opacity: 1;
    }
  }
}

/* Слой 2: Облако */
.cloud-layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 2;
  
  .cloud-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
}

/* Слой 3: Диагональная полоса */
.diagonal-layer {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  z-index: 3;
  
  .diagonal-image {
    width: 100%;
    height: auto;
    display: block;
  }
}

/* Контейнер для контента с ограничением ширины */
.content-container {
  position: relative;
  max-width: 1200px; /* такая же ширина как у hero-banner */
  width: 100%;
  height: 100%;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  z-index: 4; /* выше фоновых слоев */
}

/* Слой 4: Картинка товара - залезает на диагональную полосу */
.product-layer {
  width: 50%;
  height: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  
  .product-image {
    max-height: 450px; /* больше высоты блока, чтобы залезал на полосу */
    max-width: 100%;
    width: auto;
    height: auto;
    object-fit: contain;
    transform: translateY(-30px); /* поднимаем изображение вверх */
  }
}

/* Слой 5: Текст */
.text-layer {
  width: 50%;
  height: 100%;
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 40px 20px 20px 20px;
  
  .text-content {
    width: 100%;
    max-width: 100%;
    padding: 0;
    
    .category-title {
      font-family: 'Days One', cursive;
      font-size: 2.5rem;
      font-weight: 400;
      color: #5e3085;
      margin-bottom: 1.5rem;
      line-height: 1.2;
      text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.8);
    }
    
    .category-description {
      font-family: 'Montserrat', sans-serif;
      font-size: 1rem;
      font-weight: 400;
      color: #555;
      line-height: 1.6;
      text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8);
      /* Если текст длинный, он может опускаться на диагональную полосу */
      z-index: 5; /* выше всех слоев */
      position: relative;
    }
  }
}

/* Раздел товаров */
.products-section {
  padding: 80px 0 160px 0;
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
  padding: 0 40px;
}

.product-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
  
  &:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
  }
}

.product-image-container {
  height: 250px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  background: linear-gradient(135deg, #f8f9fa, #e9ecef);
}

.product-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
  
  &:hover {
    transform: scale(1.05);
  }
}

.product-image-placeholder {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #f5f5f5, #e0e0e0);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Montserrat', sans-serif;
  color: #666;
  font-size: 1.1rem;
  text-align: center;
  padding: 20px;
}

.product-info {
  padding: 20px;
  
  h3 {
    font-family: 'Days One', cursive;
    font-size: 1.2rem;
    color: #333;
    margin-bottom: 10px;
    line-height: 1.3;
  }
  
  p {
    font-family: 'Montserrat', sans-serif;
    font-size: 1.1rem;
    font-weight: 600;
    color: #8B4FB8;
    margin-bottom: 5px;
  }
  
  small {
    font-family: 'Montserrat', sans-serif;
    font-size: 0.9rem;
    color: #666;
  }
}

/* Стили для состояний загрузки и пустого списка */
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 80px 20px;
  text-align: center;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid #e2e8f0;
  border-top: 4px solid #8B4FB8;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-container p {
  font-family: 'Montserrat', sans-serif;
  font-size: 1.1rem;
  color: #666;
  margin: 0;
}

.no-products {
  text-align: center;
  padding: 80px 20px;
  
  h3 {
    font-family: 'Days One', cursive;
    font-size: 1.8rem;
    color: #333;
    margin-bottom: 15px;
  }
  
  p {
    font-family: 'Montserrat', sans-serif;
    font-size: 1.1rem;
    color: #666;
    margin: 0;
  }
}

/* Адаптивность */
@media (max-width: 1200px) {
  .category-hero {
    height: 450px; /* сохраняем фиксированную высоту */
    width: 90%; /* увеличиваем ширину для больших экранов */
  }
  
  .text-layer .text-content {
    .category-title {
      font-size: 2.2rem;
    }
    
    .category-description {
      font-size: 0.95rem;
    }
  }
  
  .product-layer .product-image {
    max-height: 420px;
  }
  
  .products-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 25px;
    padding: 0 30px;
  }
}

@media (max-width: 992px) {
  .category-hero {
    height: 450px; /* сохраняем фиксированную высоту */
  }
  
  .content-container {
    max-width: 95%;
    flex-direction: column;
  }
  
  .text-layer {
    width: 100%;
    height: 50%;
    padding: 15px;
    
    .text-content {
      .category-title {
        font-size: 2rem;
        margin-bottom: 1rem;
      }
      
      .category-description {
        font-size: 0.9rem;
      }
    }
  }
  
  .product-layer {
    width: 100%;
    height: 50%;
    
    .product-image {
      max-height: 200px;
    }
  }
  
  .products-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }
}

@media (max-width: 768px) {
  .category-hero {
    height: 450px; /* сохраняем фиксированную высоту */
  }
  
  .content-container {
    max-width: 98%;
    flex-direction: column;
  }
  
  .text-layer {
    width: 100%;
    height: 60%;
    padding: 15px;
    
    .text-content {
      .category-title {
        font-size: 1.8rem;
        margin-bottom: 0.8rem;
      }
      
      .category-description {
        font-size: 0.85rem;
      }
    }
  }
  
  .product-layer {
    width: 100%;
    height: 40%;
    
    .product-image {
      max-height: 160px;
    }
  }
  
  .products-section {
    padding: 60px 0 130px 0;
  }
  
  .products-grid {
    padding: 0 20px;
  }
}

@media (max-width: 480px) {
  .category-hero {
    height: 450px; /* сохраняем фиксированную высоту */
  }
  
  .content-container {
    max-width: 100%;
    flex-direction: column;
  }
  
  .text-layer {
    width: 100%;
    height: 65%;
    padding: 10px;
    
    .text-content {
      .category-title {
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
      }
      
      .category-description {
        font-size: 0.8rem;
      }
    }
  }
  
  .product-layer {
    width: 100%;
    height: 35%;
    
    .product-image {
      max-height: 140px;
    }
  }
  
  .products-grid {
    grid-template-columns: 1fr;
    gap: 15px;
  }
  
  .products-section {
    padding: 40px 0 110px 0;
  }
}
</style>
