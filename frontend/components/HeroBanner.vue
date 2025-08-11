<template>
  <section class="hero-banner">
    <div class="hero-container">
      <div
        v-for="(banner, index) in banners"
        :key="index"
        class="hero-slide"
        :class="{ active: index === currentSlide }"
      >
        <div class="banner-background" :style="{ backgroundImage: `url(${banner.fon})` }"></div>
        
        <div class="banner-content">
          <h1 class="banner-title">{{ banner.title }}</h1>
          <p class="banner-description">{{ banner.description }}</p>
          <a href="#" class="banner-button">{{ banner.cta }}</a>
        </div>

        <img :src="banner.char" alt="Персонаж" class="banner-char" />
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// Новый формат баннеров
const banners = [
  {
    fon: '/assets/hero/fon1.png',
    char: '/assets/hero/char1.png',
    title: 'Упакуем ваш бизнес!',
    description: 'Работаем на клиента',
    cta: 'Узнать подробности'
  }
]

const currentSlide = ref(0)
let slideInterval = null

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % banners.length
}

const startSlideShow = () => {
  slideInterval = setInterval(() => {
    nextSlide()
  }, 6000)
}

onMounted(() => {
  startSlideShow()
})

onUnmounted(() => {
  if (slideInterval) clearInterval(slideInterval)
})
</script>

<style scoped>
.hero-banner {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  overflow: visible; /* персонаж может выходить вверх */
  margin-top: 100px; /* опускаем баннер ниже шапки */
}

.hero-container {
  position: relative;
  width: min(1300px, 100%);
  height: 250px; /* фиксированная высота */
}

.hero-slide {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity 1s ease-in-out;
}

.hero-slide.active {
  opacity: 1;
  z-index: 1;
}

.banner-background {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  filter: none;
}

.banner-content {
  position: relative;
  z-index: 2;
  width: 450px; /* область текста */
  height: 100%;
  padding: 20px 24px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.banner-title {
  font-family: 'Days', sans-serif;
  font-size: 14px;
  color: #111;
  margin: 0 0 8px 0;
}

.banner-description {
  font-family: 'Montserrat', Arial, sans-serif;
  font-weight: 500; /* Medium */
  font-size: 9px;
  color: #222;
  margin: 0 0 14px 0;
}

.banner-button {
  width: fit-content;
  background: #60d394; /* зеленая кнопка */
  color: #0b3d2e;
  font-family: 'Montserrat', Arial, sans-serif;
  font-weight: 700; /* Bold */
  font-size: 12px;
  padding: 8px 16px;
  border-radius: 8px;
  text-decoration: none;
  transition: transform 0.2s ease, background-color 0.2s ease;
}

.banner-button:hover {
  transform: translateY(-1px);
  background: #4fc187;
}

.banner-char {
  position: absolute;
  right: 40px;
  bottom: 0; /* по нижней границе баннера */
  height: 320px; /* увеличиваем размер для правильной посадки */
  object-fit: contain;
  z-index: 2; /* над фоном, под шапкой */
  pointer-events: none; /* не перекрывает клики по меню */
}

@media (max-width: 768px) {
  .hero-container { width: 95%; }
  .banner-content { width: 55%; padding: 16px; }
  .banner-char { right: 10px; height: 300px; bottom: 0; }
}

@media (max-width: 480px) {
  .banner-content { width: 60%; }
  .banner-title { font-size: 13px; }
  .banner-description { font-size: 9px; }
  .banner-button { font-size: 12px; padding: 6px 12px; }
}
</style>