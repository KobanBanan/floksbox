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
                 <div class="slider-area">
                   <div class="slider-container" :class="{ 'inactive': !selectedDrawing }">
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
              
              <!-- Кнопка заказа -->
              <ScrollRevealWrapper type="fade-up" :delay="3">
                <button class="order-btn" @click="showOrderForm = true">
                  Заказать у менеджера
                </button>
              </ScrollRevealWrapper>
              
                             <!-- Область чертежей -->
               <ScrollRevealWrapper type="fade-up" :delay="4">
                 <div class="drawings-area">
                   <h3>Доступные чертежи</h3>
                   <div class="drawings-grid">
                     <ScrollRevealWrapper 
                       v-for="(drawing, index) in availableDrawings.slice(0, 12)" 
                       :key="drawing"
                       type="scale"
                       :delay="Math.min(index, 5)"
                       class="drawing-wrapper"
                     >
                       <div class="drawing-item"
                            :class="{ active: selectedDrawing === drawing }"
                            @click="selectDrawing(drawing)">
                         <div class="drawing-icon">
                           <img :src="`/assets/fefco/icons/${drawing}.svg`" :alt="drawing" />
                         </div>
                         <span class="drawing-number">{{ drawing }}</span>
                       </div>
                     </ScrollRevealWrapper>
                   </div>
                   <!-- Показать больше чертежей если их больше 12 -->
                   <div v-if="availableDrawings.length > 12" class="show-more-drawings">
                     <button @click="showAllDrawings = !showAllDrawings" class="show-more-btn">
                       {{ showAllDrawings ? 'Скрыть' : `Показать еще ${availableDrawings.length - 12} чертежей` }}
                     </button>
                     <div v-if="showAllDrawings" class="additional-drawings">
                       <ScrollRevealWrapper 
                         v-for="(drawing, index) in availableDrawings.slice(12)" 
                         :key="drawing"
                         type="scale"
                         :delay="Math.min(index, 5)"
                         class="drawing-wrapper"
                       >
                         <div class="drawing-item"
                              :class="{ active: selectedDrawing === drawing }"
                              @click="selectDrawing(drawing)">
                           <div class="drawing-icon">
                             <img :src="`/assets/fefco/icons/${drawing}.svg`" :alt="drawing" />
                           </div>
                           <span class="drawing-number">{{ drawing }}</span>
                         </div>
                       </ScrollRevealWrapper>
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
        <OrderForm @close="showOrderForm = false" />
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
import { ref, computed, onMounted, onUnmounted } from 'vue'
import HeaderSimple from '../components/HeaderSimple.vue'
import FooterNew from '../components/FooterNew.vue'

// Состояние
const selectedSection = ref('commercial')
const selectedDrawing = ref(null)
const currentSlide = ref(0)
const showOrderForm = ref(false)
const fullscreenImage = ref(null)
const showAllDrawings = ref(false)

// Меню
const menuItems = [
  {
    id: 'commercial',
    title: 'КОММЕРЧЕСКИЕ\nРУЛОНЫ И ЛИСТЫ',
    icon: '/assets/fefco/img/icon_roll.png'
  },
  {
    id: 'boxes',
    title: 'ЗАКРЫВАЕМЫЕ\nКОРОБКИ',
    icon: '/assets/fefco/img/icon_box1.png'
  },
  {
    id: 'section3',
    title: 'РАЗДЕЛ 3',
    icon: '/assets/fefco/img/icon_roll.png'
  },
  {
    id: 'section4',
    title: 'РАЗДЕЛ 4',
    icon: '/assets/fefco/img/icon_box1.png'
  },
  {
    id: 'section5',
    title: 'РАЗДЕЛ 5',
    icon: '/assets/fefco/img/icon_roll.png'
  },
  {
    id: 'section6',
    title: 'РАЗДЕЛ 6',
    icon: '/assets/fefco/img/icon_box1.png'
  },
  {
    id: 'section7',
    title: 'РАЗДЕЛ 7',
    icon: '/assets/fefco/img/icon_roll.png'
  }
]

// Доступные чертежи
const availableDrawings = [
  '0100', '0110', '0111', '0112', '0113', '0119',
  '0121', '0122', '0123', '0129', '0130'
]

// Текущий раздел
const currentSection = computed(() => {
  return menuItems.find(item => item.id === selectedSection.value) || menuItems[0]
})

// Текущие изображения для слайдера
const currentImages = computed(() => {
  if (!selectedDrawing.value) return []
  
  const drawing = selectedDrawing.value
  const images = []
  
  // Проверяем наличие изображений по номеру
  if (drawing === '0100') {
    // Для 0100 только одно изображение
    images.push(`/assets/fefco/1/0100.jpg`)
  } else {
    // Для остальных два изображения
    images.push(`/assets/fefco/1/${drawing}_1.jpg`)
    images.push(`/assets/fefco/1/${drawing}_2.jpg`)
  }
  
  return images
})

// Методы
const selectSection = (sectionId) => {
  selectedSection.value = sectionId
  selectedDrawing.value = null
  currentSlide.value = 0
}

const selectDrawing = (drawing) => {
  selectedDrawing.value = drawing
  currentSlide.value = 0
}

const prevSlide = () => {
  if (currentSlide.value > 0) {
    currentSlide.value--
  } else {
    currentSlide.value = currentImages.value.length - 1
  }
}

const nextSlide = () => {
  if (currentSlide.value < currentImages.value.length - 1) {
    currentSlide.value++
  } else {
    currentSlide.value = 0
  }
}

const goToSlide = (index) => {
  currentSlide.value = index
}

const openFullscreen = (image) => {
  fullscreenImage.value = image
}

const closeFullscreen = () => {
  fullscreenImage.value = null
}





// Автоматическое переключение слайдов
let slideInterval = null

onMounted(() => {
  // Автоматически выбираем первый чертеж
  selectDrawing('0100')
  
  // Автоматическое переключение каждые 3 секунды
  slideInterval = setInterval(() => {
    if (selectedDrawing.value && currentImages.value.length > 1) {
      nextSlide()
    }
  }, 3000)
})

onUnmounted(() => {
  if (slideInterval) {
    clearInterval(slideInterval)
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
  transition: none;
  position: relative;
  
  &:hover {
    background: transparent;
  }
  
  &.active {
    background: transparent;
    color: #333;
    
    &::before {
      display: none;
    }
    
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

// Кнопка заказа
.order-btn {
  background: #00d4aa;
  color: white;
  border: none;
  padding: 15px 30px;
  border-radius: 6px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-bottom: 30px;
  
  &:hover {
    background: #00b894;
    transform: translateY(-2px);
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

.show-more-drawings {
  margin-top: 20px;
  text-align: center;
}

.show-more-btn {
  background: #5e3085;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  
  &:hover {
    background: #4a2a6b;
    transform: translateY(-1px);
  }
}

.additional-drawings {
  margin-top: 20px;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 20px;
  max-height: 300px;
  overflow-y: auto;
  padding: 20px;
  background: #f8f9fa;
  border-radius: 8px;
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
  
  img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }
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
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 15px;
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
