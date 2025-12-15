<template>
  <div class="fefco-page">
    <!-- Шапка -->
    <div class="scroll-reveal scroll-reveal-fade-up">
      <HeaderSimple />
    </div>
    
    <!-- Основной контент -->
    <main class="main-content">
      <!-- Текстовая часть -->
      <section class="text-section">
        <div class="container">
                     <ScrollRevealWrapper type="fade-up">
             <h1>FEFCO - это сокращение от французского «Fédération Européenne des Fabricants de Carton Ondulé»</h1>
           </ScrollRevealWrapper>
           <ScrollRevealWrapper type="fade-up" :delay="1">
             <p>что означает Европейская федерация производителей гофрированного картона.</p>
           </ScrollRevealWrapper>
           <ScrollRevealWrapper type="fade-up" :delay="2">
             <p>Организация была основана в 1952 году и занимается стандартизацией упаковочных решений из гофрированного картона. Здесь вы можете найти необходимые чертежи и заказать продукцию.</p>
           </ScrollRevealWrapper>
        </div>
      </section>
      
      <!-- Область с двумя разделами -->
      <section class="content-section">
        <div class="container">
          <div class="content-wrapper">
            <!-- Левое меню -->
            <aside class="sidebar">
              <ScrollRevealWrapper type="fade-left">
                <div class="menu-container">
                  <div class="menu-item" 
                       v-for="(item, index) in menuItems" 
                       :key="item.id"
                       :class="{ active: selectedSection === item.id }"
                       @click="selectSection(item.id)">
                    <div class="menu-icon">
                      <img :src="item.icon" :alt="item.title" />
                    </div>
                                       <div class="menu-text">
                     <span>{{ item.title }}</span>
                   </div>
                  </div>
                </div>
              </ScrollRevealWrapper>
              
              
            </aside>
            
            <!-- Активная область -->
            <div class="active-area">
              <!-- Название раздела -->
              <ScrollRevealWrapper type="fade-right">
                <h2 class="section-title">{{ currentSection.title }}</h2>
              </ScrollRevealWrapper>
              
              <!-- Область слайдера -->
               <ScrollRevealWrapper type="fade-up" :delay="1">
                 <div class="slider-area" ref="sliderRef">
                   <div
                     class="slider-container"
                     :class="{ 'inactive': !selectedDrawing }"
                     @mouseenter="pauseAutoSlide(5000)"
                     @mouseleave="startAutoSlide"
                   >
                     <div v-if="!selectedDrawing" class="slider-placeholder">
                       <p>Выберите чертеж для просмотра</p>
                     </div>
                     <div v-else class="slider-wrapper" :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
                       <div v-for="(image, index) in currentImages" 
                            :key="index" 
                            class="slider-slide"
                            @click="openFullscreen(image)">
                         <img :src="image" :alt="`Чертеж ${selectedDrawing}`" />
                       </div>
                     </div>
                     
                     <!-- Навигация слайдера -->
                     <div v-if="selectedDrawing && currentImages.length > 1" class="slider-nav">
                       <button @click="prevSlide" class="nav-btn prev">‹</button>
                       <button @click="nextSlide" class="nav-btn next">›</button>
                     </div>
                     
                     <!-- Индикаторы -->
                     <div v-if="selectedDrawing && currentImages.length > 1" class="slider-indicators">
                       <span v-for="(_, index) in currentImages" 
                             :key="index"
                             :class="{ active: currentSlide === index }"
                             @click="goToSlide(index)">
                       </span>
                     </div>
                   </div>
                 </div>
               </ScrollRevealWrapper>
              
              <!-- Номер предмета -->
               <ScrollRevealWrapper type="fade-up" :delay="2">
                 <div class="item-number" :class="{ 'inactive': !selectedDrawing }">
                   <span v-if="selectedDrawing">№{{ selectedDrawing }}</span>
                   <span v-else class="no-selection">Номер чертежа</span>
                 </div>
               </ScrollRevealWrapper>
              
              <!-- Кнопки заказа -->
              <ScrollRevealWrapper type="fade-up" :delay="3">
                <div class="order-buttons">
                  <button class="order-btn primary" @click="openOrderForm">
                    Заказать у менеджера
                  </button>
                  <button class="order-btn secondary" @click="addToOrder" :disabled="!selectedDrawing">
                    Добавить к обращению
                  </button>
                </div>
              </ScrollRevealWrapper>
              
                             <!-- Область чертежей -->
               <ScrollRevealWrapper type="fade-up" :delay="4">
                 <div class="drawings-area">
                   <h3>Доступные чертежи ({{ availableDrawings.length }} всего)</h3>
                   <div class="drawings-grid">
                     <ScrollRevealWrapper 
                       v-for="(drawing, index) in paginatedDrawings" 
                       :key="drawing"
                       type="scale"
                       :delay="Math.min(index, 5)"
                       class="drawing-wrapper"
                     >
                       <div class="drawing-item"
                            :class="{ active: selectedDrawing === drawing }"
                            @click="selectDrawing(drawing)">
                         <div class="drawing-icon">
                           <img :src="`/assets/fefco/preview/${drawing}_thumb.jpg`" :alt="drawing" />
                         </div>
                         <span class="drawing-number">{{ drawing }}</span>
                       </div>
                     </ScrollRevealWrapper>
                   </div>
                   
                   <!-- Пагинация -->
                   <div v-if="totalPages > 1" class="pagination">
                     <div class="pagination-info">
                       Страница {{ currentPage }} из {{ totalPages }}
                     </div>
                     <div class="pagination-dots">
                       <span 
                         v-for="page in totalPages" 
                         :key="page"
                         :class="{ active: currentPage === page }"
                         @click="goToPage(page)"
                         class="pagination-dot"
                       >
                       </span>
                     </div>
                   </div>
                 </div>
               </ScrollRevealWrapper>
            </div>
          </div>
        </div>
      </section>
    </main>
    
    <!-- Подвал -->
    <div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-3">
      <FooterNew />
    </div>
    
    <!-- Модальное окно заказа -->
    <div v-if="showOrderForm" class="modal-overlay" @click.self="showOrderForm = false">
      <div class="modal-content">
        <OrderForm @close="showOrderForm = false" :prefilled-message="orderMessage" />
        <button class="close-btn" @click="showOrderForm = false">×</button>
      </div>
    </div>
    
    <!-- Полноэкранный режим -->
    <div v-if="fullscreenImage" class="fullscreen-overlay" @click="closeFullscreen">
      <img :src="fullscreenImage" :alt="`Чертеж ${selectedDrawing}`" />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue'
import HeaderSimple from '../components/HeaderSimple.vue'
import FooterNew from '../components/FooterNew.vue'

// Состояние
const selectedSection = ref('commercial')
const selectedDrawing = ref(null)
const currentSlide = ref(0)
const showOrderForm = ref(false)
const fullscreenImage = ref(null)
const selectedItems = ref([]) // Для накопления выбранных позиций
const currentPage = ref(1) // Текущая страница пагинации
const itemsPerPage = 15 // Количество чертежей на странице
const sliderRef = ref(null)
let scrollTimer = null
let slideInterval = null
let resumeTimer = null

// Меню
const menuItems = [
  {
    id: 'commercial',
    title: 'КОММЕРЧЕСКИЕ\nРУЛОНЫ И ЛИСТЫ',
    icon: '/assets/fefco/img/icon_roll.png',
    folder: '1'
  },
  {
    id: 'boxes',
    title: 'КОРОБКИ\nС ПРОРЕЗЯМИ',
    icon: '/assets/fefco/img/icon_box1.png',
    folder: '2'
  },
  {
    id: 'telescopic',
    title: 'ТЕЛЕСКОПИЧЕСКИЕ\nКОРОБКИ',
    icon: '/assets/fefco/img/icon_box2.png',
    folder: '3'
  },
  {
    id: 'folders',
    title: 'КОРОБКИ-ПАПКИ\nИ ЛОТКИ',
    icon: '/assets/fefco/img/icon_box3.png',
    folder: '4'
  },
  {
    id: 'sliding',
    title: 'ВЫДВИЖНЫЕ\nКОРОБКИ',
    icon: '/assets/fefco/img/icon_box4.png',
    folder: '5'
  },
  {
    id: 'rigid',
    title: 'ЖЁСТКИЕ\nКОРОБКИ',
    icon: '/assets/fefco/img/icon_box5.png',
    folder: '6'
  },
  {
    id: 'ready',
    title: 'ГОТОВЫЕ\nСКЛЕЕННЫЕ КОРОБКИ',
    icon: '/assets/fefco/img/icon_box6.png',
    folder: '7'
  },
  {
    id: 'retail',
    title: 'УПАКОВКА ДЛЯ РОЗНИЦЫ\nИ ЭЛ. КОММЕРЦИИ',
    icon: '/assets/fefco/img/icon_box7.png',
    folder: '8'
  },
  {
    id: 'interior',
    title: 'ВНУТРЕННЕЕ\nОСНАЩЕНИЕ',
    icon: '/assets/fefco/img/icon_box8.png',
    folder: '9'
  }
]

// Доступные чертежи по разделам
const drawingsBySection = {
  'commercial': [
    '0100', '0110', '0111', '0112', '0113', '0119',
    '0121', '0122', '0123', '0129', '0130'
  ],
  'boxes': [
    '0200', '0201', '0202', '0203', '0204', '0205', '0206', '0207', '0208', '0209',
    '0210', '0211', '0212', '0214', '0215', '0216', '0217', '0218', '0219', '0220',
    '0221', '0222', '0225', '0226', '0227', '0228', '0229', '0229.1', '0230', '0231',
    '0232', '0233', '0233.1', '0240', '0241', '0242'
  ],
  'telescopic': [
    '0301', '0302', '0303', '0304', '0306', '0307', '0308', '0309', '0310', '0312',
    '0313', '0314', '0319', '0320', '0321', '0322', '0323', '0325', '0330', '0331',
    '0350', '0351', '0352', '0360'
  ],
  'folders': [
    '0400', '0401', '0402', '0403', '0404', '0405', '0406', '0407', '0409', '0410',
    '0411', '0412', '0413', '0414', '0415', '0416', '0418', '0420', '0421', '0422',
    '0423', '0424', '0425', '0425.1', '0426', '0427', '0427.1', '0428', '0429', '0430',
    '0431', '0432', '0433', '0434', '0435', '0435.1', '0436', '0436.1', '0436.2', '0437',
    '0438', '0439', '0440', '0441', '0442', '0443', '0444', '0445', '0446', '0447',
    '0448', '0449', '0449.1', '0450', '0451', '0451.1', '0452', '0453', '0454', '0455',
    '0456', '0457', '0458', '0459', '0459.1', '0460', '0461', '0462', '0463', '0464',
    '0465', '0466', '0469', '0470', '0471', '0472', '0473', '0474', '0475', '0476',
    '0480', '0481', '0482', '0483', '0484', '0485'
  ],
  'sliding': [
    '0501', '0502', '0503', '0504', '0505', '0507', '0509', '0510', '0511', '0512'
  ],
  'rigid': [
    '0601', '0602', '0605', '0606', '0607', '0608', '0610', '0615', '0616', '0620', '0621'
  ],
  'ready': [
    '0700', '0701', '0702', '0703', '0704', '0705', '0706', '0707', '0708', '0709',
    '0710', '0711', '0712', '0713', '0714', '0715', '0716', '0717', '0718', '0719',
    '0720', '0721', '0722', '0723', '0724', '0725', '0726', '0727', '0728', '0730',
    '0740', '0747', '0748', '0760', '0771', '0772', '0773', '0774', '770'
  ],
  'retail': [
    '0801', '0802', '0803', '0804', '0808', '0809', '0815', '0816', '0817', '0818',
    '0819', '0825', '0826', '0830', '0831', '0832', '0833', '0834', '0840', '0841',
    '0842', '0843', '0845', '0846', '0847', '0848', '0849', '0850', '0851', '0852',
    '0853', '0854', '0858', '0859', '0860', '0861', '0865', '0866', '0870', '0871',
    '0872', '0873', '0874', '0880', '0881', '0882', '0885', '0886', '0887'
  ],
  'interior': [
    '0900', '0901', '0902', '0903', '0904', '0905', '0906', '0907', '0908', '0909',
    '0910', '0911', '0912', '0913', '0914', '0920', '0921', '0929', '0930', '0931',
    '0932', '0933', '0934', '0935', '0936', '0937', '0938', '0939', '0940', '0941',
    '0942', '0943', '0944', '0945', '0946', '0947', '0948', '0949', '0950', '0951',
    '0952', '0953', '0954', '0955', '0960', '0965', '0966', '0967', '0970', '0971',
    '0972', '0973', '0974', '0975', '0976'
  ]
}

// Доступные чертежи для текущего раздела
const availableDrawings = computed(() => {
  return drawingsBySection[selectedSection.value] || []
})

// Пагинация
const totalPages = computed(() => {
  return Math.ceil(availableDrawings.value.length / itemsPerPage)
})

const paginatedDrawings = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return availableDrawings.value.slice(start, end)
})

// Текущий раздел
const currentSection = computed(() => {
  return menuItems.find(item => item.id === selectedSection.value) || menuItems[0]
})

// Текущие изображения для слайдера
const currentImages = computed(() => {
  if (!selectedDrawing.value) return []
  
  const drawing = selectedDrawing.value
  const folder = currentSection.value.folder
  const images = []
  
  // Проверяем наличие изображений по номеру
  if (drawing === '0100') {
    // Для 0100 только одно изображение
    images.push(`/assets/fefco/${folder}/0100.jpg`)
  } else {
    // Для остальных два изображения
    images.push(`/assets/fefco/${folder}/${drawing}_1.jpg`)
    images.push(`/assets/fefco/${folder}/${drawing}_2.jpg`)
  }
  
  return images
})

// Методы
const selectSection = (sectionId) => {
  selectedSection.value = sectionId
  selectedDrawing.value = null
  currentSlide.value = 0
  currentPage.value = 1 // Сбрасываем на первую страницу
  
  // Автоматически выбираем первый чертеж нового раздела
  const drawings = drawingsBySection[sectionId] || []
  if (drawings.length > 0) {
    const initial = drawings[0] === '0100' && drawings.length > 1 ? drawings[1] : drawings[0]
    selectDrawing(initial)
  }
  startAutoSlide()
}

// Методы пагинации
const goToPage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page
  }
}

const selectDrawing = (drawing) => {
  selectedDrawing.value = drawing
  currentSlide.value = 0
  scrollToSlider()
  startAutoSlide()
}

const prevSlide = () => {
  if (currentSlide.value > 0) {
    currentSlide.value--
  } else {
    currentSlide.value = currentImages.value.length - 1
  }
  pauseAutoSlide(10000)
}

const nextSlide = () => {
  if (currentSlide.value < currentImages.value.length - 1) {
    currentSlide.value++
  } else {
    currentSlide.value = 0
  }
  pauseAutoSlide(10000)
}

const goToSlide = (index) => {
  currentSlide.value = index
  pauseAutoSlide(10000)
}

const scrollToSlider = () => {
  if (scrollTimer) {
    clearTimeout(scrollTimer)
  }
  scrollTimer = setTimeout(async () => {
    await nextTick()
    if (sliderRef.value) {
      sliderRef.value.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      })
    }
    scrollTimer = null
  }, 900)
}

// Автослайд с паузами
const startAutoSlide = () => {
  stopAutoSlide()
  if (selectedDrawing.value && currentImages.value.length > 1) {
    slideInterval = setInterval(() => {
      nextSlide()
    }, 3000)
  }
}

const stopAutoSlide = () => {
  if (slideInterval) {
    clearInterval(slideInterval)
    slideInterval = null
  }
}

const pauseAutoSlide = (delayMs) => {
  stopAutoSlide()
  if (resumeTimer) {
    clearTimeout(resumeTimer)
    resumeTimer = null
  }
  resumeTimer = setTimeout(() => {
    startAutoSlide()
    resumeTimer = null
  }, delayMs)
}

const openFullscreen = (image) => {
  fullscreenImage.value = image
}

const closeFullscreen = () => {
  fullscreenImage.value = null
}

// Методы для работы с заказами
const addToOrder = () => {
  if (selectedDrawing.value && !selectedItems.value.includes(selectedDrawing.value)) {
    selectedItems.value.push(selectedDrawing.value)
  }
}

const openOrderForm = () => {
  showOrderForm.value = true
}

// Формируем сообщение для заказа
const orderMessage = computed(() => {
  if (selectedItems.value.length === 0 && selectedDrawing.value) {
    return `FEFCO ${selectedDrawing.value}`
  }
  return selectedItems.value.map(item => `FEFCO ${item}`).join(', ')
})





onMounted(() => {
  // Автоматически выбираем первый чертеж из текущего раздела
  if (availableDrawings.value.length > 0) {
    const first = availableDrawings.value[0]
    const initial = first === '0100' && availableDrawings.value.length > 1 ? availableDrawings.value[1] : first
    selectDrawing(initial)
  }
  startAutoSlide()
})

onUnmounted(() => {
  stopAutoSlide()
  if (resumeTimer) {
    clearTimeout(resumeTimer)
  }
  if (scrollTimer) {
    clearTimeout(scrollTimer)
  }
})

// SEO мета-теги для страницы FEFCO
useHead({
  title: 'FEFCO - Floksbox',
  meta: [
    { 
      name: 'description', 
      content: 'FEFCO - стандартизированные решения для упаковочной промышленности. Чертежи и заказ продукции по международным стандартам.' 
    },
    {
      name: 'keywords',
      content: 'FEFCO, гофрокартон, стандарты, чертежи, упаковка, floksbox'
    }
  ]
})
</script>

<style lang="scss" scoped>
.fefco-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

// Текстовая часть
.text-section {
  background: #fff;
  padding: 40px 0;
  text-align: left;
  margin-top: 40px; /* Отступ от хедера */
  
  h1 {
    font-size: 1.8rem;
    color: #333;
    margin-bottom: 15px;
    font-weight: 600;
    line-height: 1.3;
  }
  
  p {
    font-size: 1rem;
    color: #333;
    max-width: 800px;
    margin: 0 0 15px 0;
    line-height: 1.5;
  }
}

// Основная область контента
.content-section {
  padding: 60px 0 200px 0; /* Увеличенный отступ снизу для футера */
  background: #fff;
}

.content-wrapper {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 0;
  align-items: start;
  position: relative;
}

// Боковое меню
.sidebar {
  position: sticky;
  top: 20px;
}

.menu-container {
  background: #fff;
  padding: 20px;
  margin-bottom: 30px;
  border: none;
  box-shadow: none;
}

.menu-item {
  display: flex;
  align-items: center;
  padding: 8px;
  margin-bottom: 0;
  border: none;
  border-radius: 0;
  cursor: pointer;
  background: transparent;
  transition: opacity 0.3s ease;
  position: relative;
  opacity: 0.5; // Неактивные разделы прозрачные на 50%
  
  &:hover {
    opacity: 1; // При наведении полностью видимые
  }
  
  &.active {
    opacity: 1; // Активный раздел полностью видимый
    
    .menu-text {
      color: #333;
    }
  }
}

.menu-icon {
  width: 50px;
  height: 50px;
  margin-right: 15px;
  flex-shrink: 0;
  background: transparent;
  border-radius: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  box-shadow: none;
  
  img {
    width: 50px;
    height: 50px;
    object-fit: contain;
  }
}

.menu-text {
  font-family: 'Montserrat', sans-serif;
  font-size: 12px;
  font-weight: 600;
  line-height: 1.4;
  color: #333;
  text-transform: uppercase;
  white-space: pre-line; /* Сохраняет переносы строк */
  text-shadow: none;
}



// Активная область
.active-area {
  padding-left: 60px;
  
  .section-title {
    font-size: 1.5rem;
    color: #333;
    margin-bottom: 30px;
    font-weight: 600;
    text-transform: uppercase;
  }
}

// Слайдер
.slider-area {
  margin-bottom: 30px;
}

.slider-container {
  position: relative;
  width: 100%;
  height: 400px;
  border: 1px solid #e9ecef;
  border-radius: 0;
  overflow: hidden;
  background: #fff;
  
  &.inactive {
    border-color: #dee2e6;
    background: #f8f9fa;
    
    .slider-placeholder {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100%;
      
      p {
        color: #6c757d;
        font-size: 1.1rem;
        font-style: italic;
        margin: 0;
      }
    }
  }
}

.slider-wrapper {
  display: flex;
  transition: transform 0.5s ease;
  height: 100%;
}

.slider-slide {
  min-width: 100%;
  height: 100%;
  cursor: pointer;
  
  img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }
}

.slider-nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding: 0 20px;
  pointer-events: none;
}

.nav-btn {
  width: 50px;
  height: 50px;
  border: none;
  background: rgba(94, 48, 133, 0.8);
  color: white;
  border-radius: 50%;
  cursor: pointer;
  font-size: 24px;
  pointer-events: auto;
  transition: all 0.3s ease;
  
  &:hover {
    background: rgba(94, 48, 133, 1);
  }
}

.slider-indicators {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
}

.slider-indicators span {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.5);
  cursor: pointer;
  transition: all 0.3s ease;
  
  &.active {
    background: #5e3085;
  }
}

// Номер предмета
.item-number {
  font-size: 1.5rem;
  font-weight: 600;
  color: #5e3085;
  margin-bottom: 20px;
  
  &.inactive {
    color: #6c757d;
    
    .no-selection {
      color: #6c757d;
      font-style: italic;
    }
  }
  
  .no-selection {
    color: #6c757d;
    font-style: italic;
  }
}

// Кнопки заказа
.order-buttons {
  display: flex;
  gap: 15px;
  margin-bottom: 30px;
  flex-wrap: wrap;
  justify-content: center;
}

.order-btn {
  border: none;
  padding: 15px 30px;
  border-radius: 6px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  
  &.primary {
    background: #5e3085;
    color: white;
    
    &:hover {
      background: #4a2a6b;
      transform: translateY(-2px);
    }
  }
  
  &.secondary {
    background: #d5ff92;
    color: #333;
    
    &:hover:not(:disabled) {
      background: #c5ef82;
      transform: translateY(-2px);
    }
    
    &:disabled {
      background: #ccc;
      cursor: not-allowed;
      opacity: 0.6;
    }
  }
}

// Область чертежей
.drawings-area {
  h3 {
    font-size: 1.1rem;
    color: #333;
    margin-bottom: 20px;
    font-weight: 600;
  }
}

// Пагинация
.pagination {
  margin-top: 30px;
  text-align: center;
}

.pagination-info {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 15px;
}

.pagination-dots {
  display: flex;
  justify-content: center;
  gap: 8px;
  flex-wrap: wrap;
}

.pagination-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #ddd;
  cursor: pointer;
  transition: all 0.3s ease;
  
  &:hover {
    background: #5e3085;
    transform: scale(1.2);
  }
  
  &.active {
    background: #5e3085;
    transform: scale(1.3);
  }
}


.drawings-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 20px;
  max-height: 400px;
  overflow-y: auto;
  padding-right: 10px;
}

.drawing-wrapper {
  display: contents;
}

.drawing-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 15px;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  
  &:hover {
    border-color: #5e3085;
    transform: translateY(-2px);
  }
  
  &.active {
    border-color: #5e3085;
    background: rgba(94, 48, 133, 0.1);
  }
}

.drawing-icon {
  width: 60px;
  height: 60px;
  margin-bottom: 10px;
  overflow: hidden;
  
  img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    transition: transform 0.3s ease;
  }
}

.drawing-item:hover .drawing-icon img {
  transform: scale(1.2);
}

.drawing-number {
  font-family: 'Montserrat', sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: #333;
  text-align: center;
}

// Модальное окно
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 12px;
  padding: 30px;
  max-width: 90vw;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
}

.close-btn {
  position: absolute;
  top: 15px;
  right: 20px;
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #6c757d;
  
  &:hover {
    color: #333;
  }
}

// Полноэкранный режим
.fullscreen-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2000;
  cursor: pointer;
  
  img {
    max-width: 90vw;
    max-height: 90vh;
    object-fit: contain;
  }
}

// Адаптивность
@media (max-width: 1024px) {
  .content-wrapper {
    grid-template-columns: 1fr;
    gap: 40px;
    
    &::before {
      display: none;
    }
  }
  
  .sidebar {
    position: static;
  }
  
  .menu-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .active-area {
    padding-left: 0;
  }
}

@media (max-width: 768px) {
  .container {
    padding: 0 15px;
  }
  
  .text-section {
    padding: 30px 0;
    
    h1 {
      font-size: 1.5rem;
    }
    
    p {
      font-size: 0.9rem;
    }
  }
  
  .content-section {
    padding: 30px 0 120px 0; /* Отступ снизу для футера на мобильных */
  }
  
  .drawings-grid {
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
  }
  
  .slider-container {
    height: 300px;
  }
}
</style>
