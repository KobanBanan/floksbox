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
  margin-top: 85px; /* поднят на 15px (было 100px) */
}

.hero-container {
  position: relative;
  max-width: 1200px; /* единая ширина */
  margin: 0 auto; /* центрирование */
  width: 100%;
  height: 320px; /* уменьшена на 20% (было 400px) */
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
  border-radius: 50px;
}

.banner-content {
  position: relative;
  z-index: 2;
  width: 600px; /* увеличиваем область текста для размещения заголовка в одну строку */
  height: 100%;
  padding: 20px 15px 20px 44px; /* сдвинут вправо на 20px (было 24px) */
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.banner-title {
  font-family: 'Days One', cursive;
  font-size: 56px;
  color: #cbff07;
  margin: 0 0 8px 0;
  white-space: nowrap;
}

.banner-description {
  font-family: 'Montserrat', Arial, sans-serif;
  font-weight: 500; /* Medium */
  font-size: 27px;
  color: #ffffff;
  margin: 0 0 14px 0;
}

.banner-button {
  width: fit-content;
  background: #cbff07; /* ярко-зеленая кнопка */
  color: #0b3d2e;
  font-family: 'Montserrat', Arial, sans-serif;
  font-weight: 700; /* Bold */
  font-size: 36px;
  padding: 8px 16px;
  border-radius: 24px;
  text-decoration: none;
  transition: transform 0.2s ease, background-color 0.2s ease;
}

.banner-button:hover {
  transform: translateY(-1px);
  background: #a8d905;
}

.banner-char {
  position: absolute;
  right: 40px;
  bottom: 0; /* по нижней границе баннера */
  height: 384px; /* уменьшена на 20% (было 480px) */
  object-fit: contain;
  z-index: 2; /* над фоном, под шапкой */
  pointer-events: none; /* не перекрывает клики по меню */
}


@media (max-width: 768px) {
  .hero-container { width: 95%; height: 256px; }
  .banner-content { width: 55%; padding: 16px; }
  .banner-char { right: 10px; height: 304px; bottom: 0; }
  .banner-title { font-size: 44px; }
  .banner-description { font-size: 20px; }
  .banner-button { font-size: 28px; padding: 6px 12px; border-radius: 18px; }
}

@media (max-width: 480px) {
  .hero-container { height: 224px; }
  .banner-content { width: 60%; }
  .banner-char { height: 256px; }
  .banner-title { font-size: 32px; }
  .banner-description { font-size: 16px; }
  .banner-button { font-size: 20px; padding: 4px 8px; border-radius: 12px; }
}
</style>