<template>
  <section class="hero-banner">
    <div class="hero-container">
      <div
        v-for="(banner, index) in banners"
        :key="index"
        class="hero-slide"
        :class="{ active: index === currentSlide }"
      >
        <div class="banner-background" :style="{ backgroundImage: `url(${banner.fon})` }" @click="handleBannerClick"></div>
        
        <div class="banner-content" @click="handleBannerClick">
          <h1 class="banner-title" :class="{ 'banner-title-small': index === 1 }">{{ banner.title }}</h1>
          <p class="banner-description">{{ banner.description }}</p>
          <a v-if="banner.cta !== 'Узнать подробности'" :href="banner.href" class="banner-button" :class="{ 'banner-button-lower': index === 1 }" @click.stop="handleButtonClick(banner)">{{ banner.cta }}</a>
        </div>
      </div>

      <img
        :src="banners[currentSlide].char"
        alt="Персонаж"
        class="banner-char"
        :class="{ 'banner-char--slide-4': currentSlide === 3 }"
        @click="handleBannerClick"
      />
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
    cta: 'Узнать подробности',
    href: '#'
  },
  {
    fon: '/assets/hero/fon2.png',
    char: '/assets/hero/char2.png',
    title: 'Эта\u00A0Упаковка\nСкажет\u00A0за\nВас!',
    description: 'Упаковка для общепита',
    cta: 'Перейти',
    href: '#',
    productName: 'коробка для пиццы'
  },
  {
    fon: '/assets/hero/fon4.png',
    char: '/assets/hero/char4.png',
    title: 'Шляпные коробки',
    description: 'Создайте свою!',
    cta: 'Создать',
    href: '/category/hat-boxes'
  },
  {
    fon: '/assets/hero/fon6.jpg',
    char: '/assets/hero/char6.png',
    title: 'Доставляем до\u00A0двери',
    description: 'По Москве, регионам и всей России!',
    cta: 'Узнать подробности',
    href: '#'
  }
  
]

const currentSlide = ref(0)
let slideInterval = null
const router = useRouter()

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % banners.length
}

const startSlideShow = () => {
  slideInterval = setInterval(() => {
    nextSlide()
  }, 4000)
}

const resetSlideShow = () => {
  if (slideInterval) {
    clearInterval(slideInterval)
  }
  startSlideShow()
}

const handleBannerClick = () => {
  nextSlide()
  resetSlideShow() // сбрасываем таймер автопереключения после клика
}

const handleButtonClick = async (bannerOrHref) => {
  let href = null
  let productName = null
  if (typeof bannerOrHref === 'string') {
    href = bannerOrHref
  } else if (bannerOrHref && typeof bannerOrHref === 'object') {
    href = bannerOrHref.href
    productName = bannerOrHref.productName
  }

  if (productName) {
    try {
      const config = useRuntimeConfig()
      const apiBase = config.public.apiBase
      let response = await $fetch(`${apiBase}/api/products/`, {
        params: {
          search: productName,
          active_only: true,
          page_size: 1
        }
      })
      let productId = response?.results?.[0]?.id

      if (!productId) {
        response = await $fetch(`${apiBase}/api/products/`, {
          params: { active_only: true, page_size: 100 }
        })
        const found = (response?.results || []).find(p => (p.name || '').toLowerCase().includes(productName.toLowerCase()))
        productId = found?.id
      }

      if (productId) {
        router.push(`/product/${productId}`)
        return
      }
    } catch (e) {
      console.error('Не удалось найти товар по названию', e)
    }
  }

  if (href && href !== '#') {
    router.push(href)
    resetSlideShow()
  }
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
  --hero-overlap: 140px;
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  overflow: visible;
  margin-top: 45px;
  margin-bottom: 45px;
  padding-top: var(--hero-overlap);
  z-index: 15;
}

.hero-container {
  --hero-gutter: 40px;
  position: relative;
  max-width: calc(1200px - var(--hero-gutter) * 2);
  width: calc(100% - var(--hero-gutter) * 2);
  margin: calc(-1 * var(--hero-overlap)) auto 0;
  height: 405px;
  overflow: visible;
}

.hero-slide {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity 1s ease-in-out;
  overflow: visible;
  pointer-events: none;
}

.hero-slide.active {
  opacity: 1;
  z-index: 1;
  pointer-events: auto;
}

.banner-background {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  filter: none;
  border-radius: 50px;
  width: 100%;
  left: 0;
}

.banner-content {
  position: relative;
  z-index: 10;
  width: 55%;
  max-width: 600px;
  height: 100%;
  padding: 40px 210px 20px 44px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
}

.banner-title {
  font-family: 'Days One', cursive;
  font-size: 56px;
  color: #cbff07;
  margin: 0 0 10px 0;
  line-height: 1.1;
  max-width: 580px;
  white-space: normal;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.65), 0 0 8px rgba(0, 0, 0, 0.7), 0 0 14px rgba(0, 0, 0, 0.5);
  -webkit-text-stroke: 0 !important;
  text-stroke: 0 !important;
  -webkit-text-stroke-width: 0 !important;
  -webkit-text-stroke-color: transparent !important;
  text-stroke-width: 0 !important;
  text-stroke-color: transparent !important;
  paint-order: fill !important;
  outline: none !important;
  text-outline: none !important;
}

.banner-title-small {
  font-size: 44px;
  white-space: pre-line; /* для переносов \n */
  line-height: 1.1; /* уменьшаем межстрочный интервал */
  max-width: 580px; /* ограничиваем ширину для переноса */
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.65), 0 0 8px rgba(0, 0, 0, 0.7), 0 0 14px rgba(0, 0, 0, 0.5);
  -webkit-text-stroke: 0 !important;
  text-stroke: 0 !important;
  -webkit-text-stroke-width: 0 !important;
  -webkit-text-stroke-color: transparent !important;
  text-stroke-width: 0 !important;
  text-stroke-color: transparent !important;
  paint-order: fill !important;
  outline: none !important;
  text-outline: none !important;
}


.banner-button-lower {
  margin-top: 4px;
}

.banner-description {
  font-family: 'Montserrat', Arial, sans-serif;
  font-weight: 500; /* Medium */
  font-size: 27px;
  color: #ffffff;
  margin: 0 0 14px 0;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.65), 0 0 8px rgba(0, 0, 0, 0.7), 0 0 14px rgba(0, 0, 0, 0.5);
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
  bottom: 0;
  height: 486px;
  width: auto;
  object-fit: contain;
  object-position: bottom center;
  z-index: 30;
  pointer-events: none;
  cursor: default;
}

.banner-char--slide-4 {
  right: 20px;
}


/* Мобильная версия - пропорциональное уменьшение всех элементов */
@media (max-width: 1024px) {
  .hero-container {
    --hero-gutter: 20px;
    max-width: calc(1200px - var(--hero-gutter) * 2);
    width: calc(100% - var(--hero-gutter) * 2);
  }
}

@media (max-width: 900px) {
  .hero-banner {
    --hero-overlap: calc(140px * 0.7);
    margin-top: calc(45px * 0.7);
    margin-bottom: calc(45px * 0.7);
  }
  .hero-container {
    height: calc(405px * 0.7);
  }
  .banner-background {
    width: 100%;
    left: 0;
    border-radius: calc(50px * 0.7);
  }
  .banner-content {
    width: 55%;
    max-width: calc(600px * 0.7);
    padding: calc(40px * 0.7) calc(210px * 0.7) calc(20px * 0.7) calc(44px * 0.7);
  }
  .banner-char {
    right: calc(40px * 0.7);
    height: calc(486px * 0.7);
  }
  .banner-char--slide-4 {
    right: calc(20px * 0.7);
  }
  .banner-title { 
    font-size: calc(56px * 0.7);
  }
  .banner-title-small {
    font-size: calc(44px * 0.7);
  }
  .banner-description { 
    font-size: calc(27px * 0.7); /* 18.9px */
  }
  .banner-button { 
    font-size: calc(36px * 0.7); /* 25.2px */
    padding: calc(8px * 0.7) calc(16px * 0.7);
    border-radius: calc(24px * 0.7); /* 16.8px */
  }
}

@media (max-width: 768px) {
  .hero-container {
    --hero-gutter: 18px;
    max-width: calc(1200px - var(--hero-gutter) * 2);
    width: calc(100% - var(--hero-gutter) * 2);
  }
  .hero-banner {
    --hero-overlap: calc(140px * 0.6);
    margin-top: calc(45px * 0.6);
    margin-bottom: calc(45px * 0.6);
  }
  .hero-container { 
    height: calc(405px * 0.6);
  }
  .banner-background {
    width: 100%;
    left: 0;
    border-radius: calc(50px * 0.6);
  }
  .banner-content { 
    width: 55%;
    max-width: calc(600px * 0.6);
    padding: calc(40px * 0.6) calc(210px * 0.6) calc(20px * 0.6) calc(44px * 0.6);
  }
  .banner-char { 
    right: calc(40px * 0.6);
    height: calc(486px * 0.6);
    bottom: 0;
  }
  .banner-char--slide-4 {
    right: calc(20px * 0.6);
  }
  .banner-title { 
    font-size: calc(56px * 0.6);
  }
  .banner-title-small {
    font-size: calc(44px * 0.6);
  }
  .banner-description { 
    font-size: calc(27px * 0.6); /* 16.2px */
  }
  .banner-button { 
    font-size: calc(36px * 0.6); /* 21.6px */
    padding: calc(8px * 0.6) calc(16px * 0.6);
    border-radius: calc(24px * 0.6); /* 14.4px */
  }
}

@media (max-width: 480px) {
  .hero-container {
    --hero-gutter: 14px;
    max-width: calc(1200px - var(--hero-gutter) * 2);
    width: calc(100% - var(--hero-gutter) * 2);
  }
  .hero-banner {
    --hero-overlap: calc(140px * 0.5);
    margin-top: calc(45px * 0.5);
    margin-bottom: calc(45px * 0.5);
  }
  .hero-container { 
    height: calc(405px * 0.5);
  }
  .banner-background {
    width: 100%;
    left: 0;
    border-radius: calc(50px * 0.5);
  }
  .banner-content { 
    width: 55%;
    max-width: calc(600px * 0.5);
    padding: calc(40px * 0.5) calc(210px * 0.5) calc(20px * 0.5) calc(44px * 0.5);
  }
  .banner-char { 
    height: calc(486px * 0.5);
    right: calc(40px * 0.5);
  }
  .banner-char--slide-4 {
    right: calc(20px * 0.5);
  }
  .banner-title { 
    font-size: calc(56px * 0.5);
  }
  .banner-title-small {
    font-size: calc(44px * 0.5);
  }
  .banner-description { 
    font-size: calc(27px * 0.5); /* 13.5px */
  }
  .banner-button { 
    font-size: calc(36px * 0.5); /* 18px */
    padding: calc(8px * 0.5) calc(16px * 0.5);
    border-radius: calc(24px * 0.5); /* 12px */
  }
}
</style>