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
    
    <!-- Конструктор для круглых коробок -->
    <section v-if="categorySlug === 'hat-boxes'" class="constructor-page-section">
      <div class="constructor-page-container">
        <h2 class="constructor-page-title">Конструктор круглых коробок</h2>
        <p class="constructor-page-subtitle">Создайте коробку по вашим размерам</p>
        <div class="constructor-wrapper">
          <div class="constructor-container">
            <div class="constructor-content">
              <div class="constructor-left">
                <!-- Параметры коробки -->
                <div class="parameter-group">
                  <div class="parameter">
                    <label class="parameter-label">высота коробки</label>
                    <div class="slider-container">
                      <input 
                        type="range" 
                        v-model="constructorHeight" 
                        :min="4" 
                        :max="50" 
                        step="1"
                        class="slider"
                      />
                      <div class="slider-value">{{ constructorHeight }}см</div>
                      <div class="input-with-unit">
                        <input 
                          type="number" 
                          v-model="constructorHeight" 
                          :min="4" 
                          :max="50" 
                          step="1"
                          class="manual-input"
                        />
                        <span class="unit-label">см</span>
                      </div>
                    </div>
                  </div>
                  
                  <div class="parameter">
                    <label class="parameter-label">диаметр коробки</label>
                    <div class="slider-container">
                      <input 
                        type="range" 
                        v-model="constructorDiameter" 
                        :min="12" 
                        :max="30" 
                        step="2"
                        class="slider"
                      />
                      <div class="slider-value">{{ constructorDiameter }}см</div>
                      <div class="input-with-unit">
                        <input 
                          type="number" 
                          v-model="constructorDiameter" 
                          :min="12" 
                          :max="30" 
                          step="2"
                          class="manual-input"
                        />
                        <span class="unit-label">см</span>
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Материалы -->
                <div class="material-group">
                  <label class="material-label">Материал</label>
                  <div class="material-options">
                    <label class="material-option">
                      <input type="radio" v-model="constructorMaterial" value="d" />
                      <span>Дизайнерская бумага</span>
                    </label>
                    <label class="material-option">
                      <input type="radio" v-model="constructorMaterial" value="b" />
                      <span>Бархатная</span>
                    </label>
                  </div>
                </div>
                
                <!-- Дополнительные опции -->
                <div class="options-group">
                  <label class="option-label">
                    <input type="checkbox" v-model="constructorWithLid" />
                    <span>С крышкой</span>
                  </label>
                </div>
                
                <!-- Тираж -->
                <div class="circulation-group">
                  <label class="circulation-label">Тираж (от 300 штук)</label>
                  <div class="circulation-input">
                    <input 
                      type="number" 
                      v-model="constructorCirculation" 
                      :min="300" 
                      class="circulation-field"
                    />
                    <span class="unit-label">шт.</span>
                  </div>
                </div>
                
                <!-- Кнопка заказа -->
                <button class="order-button">
                  Оформить заказ у менеджера
                </button>
              </div>
              
              <!-- Визуализация коробки -->
              <div class="constructor-right">
                <div class="box-visualization">
                  <div class="constructor-image-wrapper" :style="imageWrapperStyle">
                    <img
                      class="constructor-image"
                      :style="imageStyle"
                      :src="displayedImageSrc"
                      alt="Круглая коробка"
                      @click="openFullImage"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
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

// Данные конструктора
const constructorHeight = ref(25)
const constructorDiameter = ref(22) // ширина временно фиксирована на 22
const constructorMaterial = ref('b') // d: дизайнерская, b: бархатная (по умолчанию есть полный набор b)
const constructorWithLid = ref(true)
const constructorCirculation = ref(300)

const config = useRuntimeConfig()
const apiBaseUrl = config.public.apiBase

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

// Вспомогательные вычисления для выбора изображения и кропа
const effectiveHeightStep = computed(() => {
  // Округление вниз к ближайшему четному из последовательности [4,6,...,50]
  const h = Math.max(4, Math.min(50, Math.floor(constructorHeight.value)))
  const stepped = h % 2 === 0 ? h : h - 1
  return Math.max(4, Math.min(50, stepped))
})

// Подготовка к активации логики ширины: шаги [12,14,...,30]
const effectiveWidthStep = computed(() => {
  const w = Math.max(12, Math.min(30, Math.floor(constructorDiameter.value)))
  const stepped = w % 2 === 0 ? w : w - 1
  return Math.max(12, Math.min(30, stepped))
})

const currentImageSrc = computed(() => {
  // width (w) пока фиксирован через контрол, но уже поддерживаем все наборы
  const w = effectiveWidthStep.value
  const mat = constructorMaterial.value || 'd' // d | b
  const lid = constructorWithLid.value ? 'on' : 'off'
  const h = effectiveHeightStep.value
  const baseDir = '/assets/images/22 крышка д'
  const dir = encodeURI(baseDir)
  return `${dir}/${mat}_${lid}_w${w}_h${h}.png`
})

// Плавная смена изображения без белого фона
const displayedImageSrc = ref('')

const preloadAndSwap = (src) => {
  if (!src) return
  if (process.client && typeof Image !== 'undefined') {
    const img = new Image()
    img.onload = () => { displayedImageSrc.value = src }
    img.onerror = () => { /* остаёмся на предыдущем */ }
    img.src = src
  } else {
    // SSR/рендер на сервере — просто выставляем без предзагрузки
    displayedImageSrc.value = src
  }
}

watch(() => currentImageSrc.value, (src) => {
  preloadAndSwap(src)
}, { immediate: true })

// Процент видимой высоты: от 60% (h4) до 100% (h50)
const visiblePercentHeight = computed(() => 100)

// Процент видимой ширины: от 60% (w12) до 100% (w30)
const visiblePercentWidth = computed(() => 100)

// Дополнительный авто-масштаб для гармоничности:
// маленькие размеры визуально крупнее, большие — чуть меньше
const autoSizeScale = computed(() => 1)

// Контейнер фиксированного размера (единый масштаб для всех изображений)
const imageWrapperStyle = computed(() => {
  return {
    width: '100%',
    maxWidth: '520px',
    height: '520px',
    overflow: 'hidden',
    margin: '0 auto',
    display: 'flex',
    alignItems: 'flex-end',
    justifyContent: 'center',
    background: 'transparent'
  }
})

// Само изображение: зум от нижнего края по высоте и ширине
const imageStyle = computed(() => {
  return {
    width: '100%',
    height: '100%',
    objectFit: 'contain',
    objectPosition: 'center bottom',
    transform: 'none',
    transformOrigin: 'center bottom',
    background: 'transparent',
    cursor: 'zoom-in'
  }
})

const imageErrorStage = ref(0)

const resetImageErrorStage = () => {
  imageErrorStage.value = 0
}

watch([constructorHeight, constructorWithLid, constructorMaterial, constructorDiameter], resetImageErrorStage)

const handleConstructorImageError = (e) => {
  const w = effectiveWidthStep.value
  const h = effectiveHeightStep.value
  const mat = constructorMaterial.value || 'd' // d | b
  const baseDir = encodeURI('/assets/images/22 крышка д')
  if (imageErrorStage.value === 0) {
    // Первая попытка: сменить только параметр крышки, не меняя материал
    const altLid = constructorWithLid.value ? 'off' : 'on'
    const fallback1 = `${baseDir}/${mat}_${altLid}_w${w}_h${h}.png`
    // пробуем подменить только если текущий источник совпадает с currentImageSrc,
    // чтобы не сорвать плавную подмену displayedImageSrc
    if (currentImageSrc.value === displayedImageSrc.value) {
      displayedImageSrc.value = fallback1
    }
    imageErrorStage.value = 1
    return
  }
  if (imageErrorStage.value === 1) {
    // Вторая попытка: минимальная высота в этом же материале и с крышкой
    const fallback2 = `${baseDir}/${mat}_on_w${w}_h4.png`
    if (currentImageSrc.value === displayedImageSrc.value) {
      displayedImageSrc.value = fallback2
    }
    imageErrorStage.value = 2
    return
  }
  // Больше не пытаемся — оставляем как есть, чтобы было видно некорректное сочетание
}

const openFullImage = () => {
  const src = currentImageSrc.value
  window.open(src, '_blank')
}

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

/* Секция конструктора на странице */
.constructor-page-section {
  padding: 80px 0;
  background: transparent;
  width: 100%;
}

.constructor-page-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
}

.constructor-page-title {
  font-family: 'Days One', cursive;
  font-size: 2.5rem;
  font-weight: 400;
  color: #5e3085;
  text-align: center;
  margin-bottom: 15px;
  text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.8);
}

.constructor-page-subtitle {
  font-family: 'Montserrat', sans-serif;
  font-size: 1.2rem;
  font-weight: 400;
  color: #666;
  text-align: center;
  margin-bottom: 50px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.6;
}

/* Стили конструктора */
.constructor-wrapper {
  background: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.constructor-container {
  width: 100%;
  background: white;
  border-radius: 20px;
  overflow: hidden;
}

.constructor-content {
  display: flex;
  min-height: 500px;
}

.constructor-left {
  flex: 1;
  padding: 40px;
  background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
  border-right: 1px solid #e9ecef;
}

.constructor-right {
  flex: 1;
  padding: 40px;
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Параметры */
.parameter-group {
  margin-bottom: 30px;
}

.parameter {
  margin-bottom: 25px;
}

.parameter-label {
  display: block;
  font-family: 'Montserrat', sans-serif;
  font-size: 1rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 10px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.slider-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.slider {
  width: 100%;
  height: 6px;
  border-radius: 3px;
  background: #e9ecef;
  outline: none;
  -webkit-appearance: none;
  
  &::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #5e3085;
    cursor: pointer;
    box-shadow: 0 2px 6px rgba(94, 48, 133, 0.3);
  }
  
  &::-moz-range-thumb {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #5e3085;
    cursor: pointer;
    border: none;
    box-shadow: 0 2px 6px rgba(94, 48, 133, 0.3);
  }
}

.slider-value {
  font-family: 'Montserrat', sans-serif;
  font-size: 1.1rem;
  font-weight: 600;
  color: #5e3085;
  text-align: center;
}

.input-with-unit {
  display: flex;
  align-items: center;
  gap: 8px;
  justify-content: center;
}

.manual-input {
  width: 80px;
  padding: 8px 12px;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  font-family: 'Montserrat', sans-serif;
  font-size: 1rem;
  text-align: center;
  transition: border-color 0.3s ease;
  
  &:focus {
    outline: none;
    border-color: #5e3085;
  }
}

.unit-label {
  font-family: 'Montserrat', sans-serif;
  font-size: 0.9rem;
  color: #666;
  font-weight: 500;
}

/* Материалы */
.material-group {
  margin-bottom: 25px;
}

.material-label {
  display: block;
  font-family: 'Montserrat', sans-serif;
  font-size: 1rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 15px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.material-options {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.material-option {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  padding: 10px;
  border-radius: 8px;
  transition: background-color 0.3s ease;
  
  &:hover {
    background: #f8f9fa;
  }
  
  input[type="radio"] {
    width: 18px;
    height: 18px;
    accent-color: #5e3085;
  }
  
  span {
    font-family: 'Montserrat', sans-serif;
    font-size: 1rem;
    color: #333;
  }
}

/* Опции */
.options-group {
  margin-bottom: 25px;
}

.option-label {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  padding: 10px;
  border-radius: 8px;
  transition: background-color 0.3s ease;
  
  &:hover {
    background: #f8f9fa;
  }
  
  input[type="checkbox"] {
    width: 18px;
    height: 18px;
    accent-color: #5e3085;
  }
  
  span {
    font-family: 'Montserrat', sans-serif;
    font-size: 1rem;
    color: #333;
    font-weight: 500;
  }
}

/* Тираж */
.circulation-group {
  margin-bottom: 30px;
}

.circulation-label {
  display: block;
  font-family: 'Montserrat', sans-serif;
  font-size: 1rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 10px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.circulation-input {
  display: flex;
  align-items: center;
  gap: 8px;
  justify-content: center;
}

.circulation-field {
  width: 120px;
  padding: 8px 12px;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  font-family: 'Montserrat', sans-serif;
  font-size: 1rem;
  text-align: center;
  transition: border-color 0.3s ease;
  
  &:focus {
    outline: none;
    border-color: #5e3085;
  }
}

/* Кнопка заказа */
.order-button {
  width: 100%;
  padding: 15px 25px;
  background: linear-gradient(135deg, #5e3085 0%, #8B4FB8 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-family: 'Montserrat', sans-serif;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(94, 48, 133, 0.3);
  
  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(94, 48, 133, 0.4);
    background: linear-gradient(135deg, #6d3a9a 0%, #9a5fc8 100%);
  }
  
  &:active {
    transform: translateY(0);
  }
}

/* Визуализация цилиндра */
.box-visualization {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  min-height: 400px;
}

.constructor-image {
  display: block;
  background: transparent;
}

.constructor-image-wrapper {
  background: transparent;
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
  
  /* Адаптивные стили для конструктора на странице */
  .constructor-page-section {
    padding: 60px 0;
  }
  
  .constructor-page-container {
    padding: 0 20px;
  }
  
  .constructor-page-title {
    font-size: 2rem;
  }
  
  .constructor-page-subtitle {
    font-size: 1rem;
    margin-bottom: 40px;
  }
  
  .constructor-content {
    flex-direction: column;
    min-height: auto;
  }
  
  .constructor-left {
    border-right: none;
    border-bottom: 1px solid #e9ecef;
    padding: 30px 20px;
  }
  
  .constructor-right {
    padding: 20px;
    min-height: 300px;
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
  
  /* Дополнительные адаптивные стили для конструктора на маленьких экранах */
  .constructor-page-section {
    padding: 40px 0;
  }
  
  .constructor-page-container {
    padding: 0 15px;
  }
  
  .constructor-page-title {
    font-size: 1.8rem;
  }
  
  .constructor-page-subtitle {
    font-size: 0.9rem;
    margin-bottom: 30px;
  }
  
  .constructor-left {
    padding: 20px 15px;
  }
  
  .constructor-right {
    padding: 15px;
    min-height: 250px;
  }
  
  .parameter-label,
  .material-label,
  .circulation-label {
    font-size: 0.9rem;
  }
  
  .manual-input,
  .circulation-field {
    width: 70px;
    font-size: 0.9rem;
  }
  
  .circulation-field {
    width: 100px;
  }
  
  .order-button {
    padding: 12px 20px;
    font-size: 1rem;
  }
}
</style>
