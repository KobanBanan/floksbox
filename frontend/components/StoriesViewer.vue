<template>
  <div
    v-if="isOpen"
    class="stories-viewer"
    @click="handleClick"
    @mousedown="handleMouseDown"
    @mousemove="handleMouseMove"
    @mouseup="handleMouseUp"
    @mouseleave="handleMouseLeave"
    @touchstart="handleTouchStart"
    @touchmove="handleTouchMove"
    @touchend="handleTouchEnd"
    @keydown="handleKeyDown"
  >
    <!-- Размытый фон -->
    <div class="stories-backdrop" @click="close"></div>
    
      <!-- Контент stories -->
      <div class="stories-content" :key="currentStoryIndex">
        <!-- Верхняя панель с прогресс-барами -->
        <div class="stories-header">
          <div class="progress-container">
            <div
              v-for="(slide, index) in currentStory.slides"
              :key="index"
              class="progress-bar-wrapper"
            >
              <div
                class="progress-bar"
                :class="{ active: index === currentSlideIndex }"
              >
                <div
                  class="progress-fill"
                  :style="{ width: getProgressWidth(index) + '%' }"
                ></div>
              </div>
            </div>
          </div>
          
          <!-- Кнопка закрытия -->
          <button class="close-button" @click="close">×</button>
        </div>
        
        <!-- Область слайдов -->
        <div class="slides-container">
          <div
            class="slide-wrapper"
            :style="{ transform: `translateX(-${currentSlideIndex * 100}%)` }"
          >
            <div
              v-for="(slide, index) in currentStory.slides"
              :key="index"
              class="slide"
            >
            <!-- Изображение -->
            <img
              v-if="slide.type === 'image'"
              :src="slide.src"
              :alt="`Slide ${index + 1}`"
              class="slide-image"
            />
            
            <!-- Видео -->
            <video
              v-if="slide.type === 'video'"
              :src="slide.src"
              :ref="el => { if (el) videoRefs[index] = el }"
              class="slide-video"
              @loadedmetadata="handleVideoLoaded($event, index)"
              @ended="handleVideoEnded"
              autoplay
              muted
              playsinline
            ></video>
            
          </div>
        </div>
      </div>
      
      <!-- Области клика для навигации -->
      <div class="click-area left" @click.stop="prevSlide"></div>
      <div class="click-area right" @click.stop="nextSlide"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted, nextTick } from 'vue'

const props = defineProps({
  stories: {
    type: Array,
    required: true
  },
  initialIndex: {
    type: Number,
    default: 0
  }
})

const emit = defineEmits(['close'])

const isOpen = ref(true)
const currentStoryIndex = ref(props.initialIndex)
const currentSlideIndex = ref(0)
const isPaused = ref(false)
const progress = ref(0)
const slideTimer = ref(null)
const videoRefs = ref([])
const videoDuration = ref(0)
const isMouseDown = ref(false)
const mouseStartY = ref(0)
const mouseStartX = ref(0)
const touchStartY = ref(0)
const touchStartX = ref(0)
const dragOffset = ref(0)

const currentStory = computed(() => props.stories[currentStoryIndex.value] || props.stories[0])

const SLIDE_DURATION = 10000 // 10 секунд для изображений

// Инициализация
onMounted(() => {
  // Блокируем скролл страницы
  document.body.style.overflow = 'hidden'
  document.documentElement.style.overflow = 'hidden'
  // Увеличиваем z-index body чтобы не было конфликтов
  document.body.style.position = 'relative'
  
  window.addEventListener('keydown', handleKeyDown)
  nextTick(() => {
    const slide = currentStory.value.slides[currentSlideIndex.value]
    if (slide?.type === 'video') {
      // Ждем загрузки видео
      setTimeout(() => {
        playVideo()
      }, 100)
    } else {
      startSlideTimer()
    }
  })
})

onUnmounted(() => {
  // Восстанавливаем скролл
  document.body.style.overflow = ''
  document.documentElement.style.overflow = ''
  document.body.style.position = ''
  
  clearTimers()
  window.removeEventListener('keydown', handleKeyDown)
})

watch([currentStoryIndex, currentSlideIndex], () => {
  clearTimers()
  progress.value = 0
  nextTick(() => {
    if (currentStory.value.slides[currentSlideIndex.value]?.type === 'video') {
      playVideo()
    } else {
      startSlideTimer()
    }
  })
})

// Таймер для изображений
const startSlideTimer = () => {
  if (isPaused.value) return
  
  const startTime = Date.now()
  const updateProgress = () => {
    if (isPaused.value) return
    
    const elapsed = Date.now() - startTime
    progress.value = Math.min((elapsed / SLIDE_DURATION) * 100, 100)
    
    if (progress.value >= 100) {
      nextSlide()
    } else {
      slideTimer.value = requestAnimationFrame(updateProgress)
    }
  }
  
  slideTimer.value = requestAnimationFrame(updateProgress)
}

// Видео
const playVideo = () => {
  const video = videoRefs.value[currentSlideIndex.value]
  if (video) {
    if (videoDuration.value === 0) {
      // Ждем загрузки метаданных
      video.addEventListener('loadedmetadata', () => {
        videoDuration.value = video.duration || 0
        video.currentTime = 0
        video.play().catch(() => {})
        updateVideoProgress(video)
      }, { once: true })
    } else {
      video.currentTime = 0
      video.play().catch(() => {})
      updateVideoProgress(video)
    }
  }
}

const handleVideoLoaded = (event, index) => {
  const video = event.target
  if (index === currentSlideIndex.value && video) {
    videoDuration.value = video.duration || 0
    if (!isPaused.value) {
      video.play().catch(() => {})
      updateVideoProgress(video)
    }
  }
}

const updateVideoProgress = (video) => {
  if (video && !isPaused.value && !video.paused && videoDuration.value > 0) {
    progress.value = Math.min((video.currentTime / videoDuration.value) * 100, 100)
    if (progress.value < 100 && !video.ended) {
      requestAnimationFrame(() => updateVideoProgress(video))
    }
  }
}

const handleVideoEnded = () => {
  nextSlide()
}

// Навигация
const nextSlide = () => {
  if (currentSlideIndex.value < currentStory.value.slides.length - 1) {
    // Переход к следующему слайду внутри story - без анимации
    currentSlideIndex.value++
  } else {
    // Переход к следующей story (закрепленке) с анимацией
    if (currentStoryIndex.value < props.stories.length - 1) {
      const contentEl = document.querySelector('.stories-content')
      if (contentEl) {
        contentEl.style.animation = 'storySlideOut 0.3s ease-out'
        setTimeout(() => {
          currentStoryIndex.value++
          currentSlideIndex.value = 0
          contentEl.style.animation = 'storySlideIn 0.3s ease-out'
          setTimeout(() => {
            contentEl.style.animation = ''
          }, 300)
        }, 300)
      } else {
        currentStoryIndex.value++
        currentSlideIndex.value = 0
      }
    } else {
      close()
    }
  }
}

const prevSlide = () => {
  if (currentSlideIndex.value > 0) {
    // Переход к предыдущему слайду внутри story - без анимации
    currentSlideIndex.value--
  } else {
    // Переход к предыдущей story (закрепленке) с анимацией
    if (currentStoryIndex.value > 0) {
      const contentEl = document.querySelector('.stories-content')
      if (contentEl) {
        contentEl.style.animation = 'storySlideOutReverse 0.3s ease-out'
        setTimeout(() => {
          currentStoryIndex.value--
          currentSlideIndex.value = props.stories[currentStoryIndex.value].slides.length - 1
          contentEl.style.animation = 'storySlideInReverse 0.3s ease-out'
          setTimeout(() => {
            contentEl.style.animation = ''
          }, 300)
        }, 300)
      } else {
        currentStoryIndex.value--
        currentSlideIndex.value = props.stories[currentStoryIndex.value].slides.length - 1
      }
    }
  }
}

// Прогресс-бар
const getProgressWidth = (index) => {
  if (index < currentSlideIndex.value) {
    return 100
  } else if (index === currentSlideIndex.value) {
    return progress.value
  } else {
    return 0
  }
}

// Пауза при зажатии и drag вниз
const handleMouseDown = (e) => {
  if (e.button === 0) { // Левая кнопка мыши
    isMouseDown.value = true
    mouseStartY.value = e.clientY
    mouseStartX.value = e.clientX
    dragOffset.value = 0
    pause()
  }
}

const handleMouseMove = (e) => {
  if (isMouseDown.value) {
    const deltaY = e.clientY - mouseStartY.value
    const deltaX = e.clientX - mouseStartX.value
    
    // Если тянем вниз больше чем в сторону
    if (Math.abs(deltaY) > Math.abs(deltaX) && deltaY > 0) {
      dragOffset.value = Math.min(deltaY, 300) // Ограничиваем максимальное смещение
      const contentEl = document.querySelector('.stories-content')
      if (contentEl) {
        const opacity = Math.max(0, 1 - dragOffset.value / 300)
        const scale = Math.max(0.8, 1 - dragOffset.value / 1000)
        contentEl.style.transform = `translateY(${dragOffset.value}px) scale(${scale})`
        contentEl.style.opacity = opacity
      }
    }
  }
}

const handleMouseUp = () => {
  if (isMouseDown.value) {
    const deltaY = dragOffset.value
    
    // Если потянули вниз достаточно далеко - закрываем
    if (deltaY > 100) {
      close()
    } else {
      // Возвращаем на место
      const contentEl = document.querySelector('.stories-content')
      if (contentEl) {
        contentEl.style.transform = ''
        contentEl.style.opacity = ''
      }
      resume()
    }
    
    isMouseDown.value = false
    dragOffset.value = 0
  }
}

const handleMouseLeave = () => {
  if (isMouseDown.value) {
    // Если мышь вышла за пределы, возвращаем на место
    const contentEl = document.querySelector('.stories-content')
    if (contentEl) {
      contentEl.style.transform = ''
      contentEl.style.opacity = ''
    }
    isMouseDown.value = false
    dragOffset.value = 0
    resume()
  }
}

const handleTouchStart = (e) => {
  touchStartY.value = e.touches[0].clientY
  touchStartX.value = e.touches[0].clientX
  dragOffset.value = 0
  pause()
}

const handleTouchMove = (e) => {
  const currentY = e.touches[0].clientY
  const currentX = e.touches[0].clientX
  const deltaY = currentY - touchStartY.value
  const deltaX = currentX - touchStartX.value
  
  // Если тянем вниз больше чем в сторону
  if (Math.abs(deltaY) > Math.abs(deltaX) && deltaY > 0) {
    e.preventDefault() // Предотвращаем скролл страницы
    dragOffset.value = Math.min(deltaY, 300)
    const contentEl = document.querySelector('.stories-content')
    if (contentEl) {
      const opacity = Math.max(0, 1 - dragOffset.value / 300)
      const scale = Math.max(0.8, 1 - dragOffset.value / 1000)
      contentEl.style.transform = `translateY(${dragOffset.value}px) scale(${scale})`
      contentEl.style.opacity = opacity
    }
  }
}

const handleTouchEnd = (e) => {
  const touchEndY = e.changedTouches[0].clientY
  const touchEndX = e.changedTouches[0].clientX
  const deltaY = touchEndY - touchStartY.value
  const deltaX = touchEndX - touchStartX.value
  
  // Свайп вниз для закрытия
  if (Math.abs(deltaY) > Math.abs(deltaX) && deltaY > 100) {
    close()
    return
  }
  
  // Если потянули вниз, но недостаточно - возвращаем на место
  if (Math.abs(deltaY) > Math.abs(deltaX) && deltaY > 0) {
    const contentEl = document.querySelector('.stories-content')
    if (contentEl) {
      contentEl.style.transform = ''
      contentEl.style.opacity = ''
    }
    resume()
    return
  }
  
  // Свайп влево/вправо для навигации
  if (Math.abs(deltaX) > 50) {
    if (deltaX > 0) {
      prevSlide()
    } else {
      nextSlide()
    }
  } else {
    resume()
  }
  
  dragOffset.value = 0
}

const pause = () => {
  isPaused.value = true
  clearTimers()
  const video = videoRefs.value[currentSlideIndex.value]
  if (video) {
    video.pause()
  }
}

const resume = () => {
  isPaused.value = false
  const slide = currentStory.value.slides[currentSlideIndex.value]
  if (slide?.type === 'video') {
    playVideo()
  } else {
    startSlideTimer()
  }
}

const clearTimers = () => {
  if (slideTimer.value) {
    cancelAnimationFrame(slideTimer.value)
    slideTimer.value = null
  }
}

// Клики по краям экрана
const handleClick = (e) => {
  const clickX = e.clientX
  const windowWidth = window.innerWidth
  const clickAreaWidth = windowWidth * 0.3 // 30% с каждой стороны
  
  if (clickX < clickAreaWidth) {
    prevSlide()
  } else if (clickX > windowWidth - clickAreaWidth) {
    nextSlide()
  }
}

// Клавиатура
const handleKeyDown = (e) => {
  if (e.key === 'Escape') {
    close()
  } else if (e.key === 'ArrowLeft') {
    prevSlide()
  } else if (e.key === 'ArrowRight') {
    nextSlide()
  }
}

const close = () => {
  clearTimers()
  const video = videoRefs.value[currentSlideIndex.value]
  if (video) {
    video.pause()
  }
  isOpen.value = false
  emit('close')
}
</script>

<style lang="scss" scoped>
.stories-viewer {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 99999;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  overflow: hidden;
}

.stories-backdrop {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(71, 0, 159, 0.5);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  z-index: 1;
}

@keyframes storyFadeIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes storySlideOut {
  from {
    opacity: 1;
    transform: translateX(0) scale(1);
  }
  to {
    opacity: 0;
    transform: translateX(100px) scale(0.9);
  }
}

@keyframes storySlideIn {
  from {
    opacity: 0;
    transform: translateX(-100px) scale(0.9);
  }
  to {
    opacity: 1;
    transform: translateX(0) scale(1);
  }
}

@keyframes storySlideOutReverse {
  from {
    opacity: 1;
    transform: translateX(0) scale(1);
  }
  to {
    opacity: 0;
    transform: translateX(-100px) scale(0.9);
  }
}

@keyframes storySlideInReverse {
  from {
    opacity: 0;
    transform: translateX(100px) scale(0.9);
  }
  to {
    opacity: 1;
    transform: translateX(0) scale(1);
  }
}

/* Убрали фиксированные max-width - ширина вычисляется автоматически из высоты и соотношения 9:16 */

.stories-header {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  z-index: 10;
  padding: 12px 16px;
  padding-right: 38px; /* Место для кнопки закрытия */
  background: transparent;
  box-sizing: border-box;
  width: 100%;
  overflow: hidden;
}

.stories-content {
  position: relative;
  aspect-ratio: 9 / 16;
  height: 100vh;
  max-height: 100vh;
  width: auto;
  max-width: calc(100vh * 9 / 16); /* Ширина вычисляется из высоты и соотношения 9:16 */
  background: transparent;
  border-radius: 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  z-index: 2;
  animation: storyFadeIn 0.3s ease-out;
  transition: transform 0.2s ease-out, opacity 0.2s ease-out;
  margin: 0 auto; /* Центрирование */
}

.progress-container {
  display: flex;
  gap: 4px;
  margin-bottom: 8px;
  width: 100%;
  box-sizing: border-box;
  padding: 0;
  margin: 0;
  overflow: hidden;
  min-width: 0;
  /* Учитываем padding родителя и gap между элементами */
  max-width: 100%;
}

.progress-bar-wrapper {
  flex: 1;
  min-width: 0; /* Позволяет сжиматься */
  height: 3px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 2px;
  overflow: hidden;
  box-sizing: border-box;
}

.progress-bar {
  width: 100%;
  height: 100%;
  position: relative;
  
  &.active {
    .progress-fill {
      background: #fff;
    }
  }
}

.progress-fill {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  background: rgba(255, 255, 255, 0.5);
  transition: width 0.1s linear;
}

.close-button {
  position: absolute;
  top: 20px;
  right: 12px;
  background: transparent;
  border: none;
  color: #fff;
  font-size: 20px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 11;
  transition: opacity 0.2s ease;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  transform: translateY(-50%); /* Центрируем по вертикали с полоской */
  
  &:hover {
    opacity: 0.8;
  }
  
  &:active {
    transform: translateY(-50%) scale(0.95);
  }
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 11;
  transition: background 0.3s ease;
  
  &:hover {
    background: rgba(0, 0, 0, 0.7);
  }
}

.slides-container {
  flex: 1;
  position: relative;
  overflow: hidden;
  width: 100%;
  height: 100%;
}

.slide-wrapper {
  display: flex;
  width: 100%;
  height: 100%;
  transition: none; /* Убрали анимацию для переключения слайдов внутри story */
}

.slide {
  min-width: 100%;
  height: 100%;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.slide-image,
.slide-video {
  width: 100%;
  height: 100%;
  object-fit: contain;
  background: transparent;
  border: none;
  outline: none;
}

.click-area {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 30%;
  z-index: 5;
  cursor: pointer;
  
  &.left {
    left: 0;
  }
  
  &.right {
    right: 0;
  }
}

@media (min-width: 769px) {
  .stories-content {
    border-radius: 12px;
    aspect-ratio: 9 / 16;
    height: 90vh;
    max-height: 90vh;
  }
  
  .stories-backdrop {
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
  }
}

@media (max-width: 768px) {
  .stories-content {
    max-width: 100%;
    max-height: 100%;
    border-radius: 0;
  }
  
}
</style>

