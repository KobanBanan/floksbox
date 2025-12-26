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
          <h1 class="banner-title" :class="{ 'banner-title-first': index === 0, 'banner-title-small': index === 1 }">{{ banner.title }}</h1>
          <p class="banner-description">{{ banner.description }}</p>
          <a v-if="banner.cta !== 'Узнать подробности'" :href="banner.href" class="banner-button" :class="{ 'banner-button-lower': index === 1 }" @click.stop="handleButtonClick(banner)">{{ banner.cta }}</a>
        </div>

        <img :src="banner.char" alt="Персонаж" class="banner-char" @click="handleBannerClick" />
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
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  overflow: visible; /* персонаж может выходить вверх */
  margin-top: 85px; /* поднят на 15px (было 100px) */
  margin-bottom: 80px; /* увеличенный отступ до следующего раздела */
}

.hero-container {
  position: relative;
  max-width: 990px; /* уменьшена на 10% (было 1100px) */
  margin: 0 auto; /* центрирование */
  width: 100%;
  height: 405px; /* уменьшена на 10% (было 450px) */
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
  width: 110%; /* делаем фон шире */
  left: -5%; /* центрируем расширенный фон */
}

.banner-content {
  position: relative;
  z-index: 10; /* Текст поверх персонажа */
  width: 55%;
  max-width: 540px;
  height: 100%;
  padding: 40px 220px 20px 44px; /* справа оставляем место под персонажа */
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* Первый слайд: уменьшаем правый отступ, чтобы текст не уходил слишком влево */
.hero-slide:nth-child(1) .banner-content {
  padding-right: 160px;
}

.banner-title {
  font-family: 'Days One', cursive;
  font-size: 56px;
  color: #cbff07;
  margin: 0 0 10px 0;
  white-space: pre-line; /* для переносов \n */
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

.banner-title-first {
  font-size: 50px;
}

.banner-title-small {
  font-size: 44px;
  white-space: pre-line; /* для переносов \n */
  line-height: 1.1; /* уменьшаем межстрочный интервал */
  max-width: 500px; /* ограничиваем ширину для переноса */
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

/* Специальные стили для второго баннера */
.hero-slide:nth-child(2) .banner-content {
  padding-right: 200px; /* единый стиль со всеми баннерами */
  padding-left: 44px; /* единый стиль */
}

/* Специальные стили для баннера 4 (с fon6.jpg) - разрешаем перенос заголовка */
.hero-slide:nth-child(4) .banner-content {
  padding-right: 200px; /* добавляем отступ справа для персонажа */
}

.hero-slide:nth-child(4) .banner-title {
  white-space: pre-line; /* для переносов \n */
  line-height: 1.1; /* уменьшаем межстрочный интервал */
  max-width: 500px; /* ограничиваем ширину для переноса */
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


.hero-slide:nth-child(4) .banner-char {
  right: 20px; /* сдвигаем персонажа еще правее */
}

/* Специальные стили для баннера 3 (с fon4.png) - единый стиль */
.hero-slide:nth-child(3) .banner-content {
  padding-right: 200px; /* единый стиль со всеми баннерами */
  padding-left: 44px; /* единый стиль */
}

.hero-slide:nth-child(3) .banner-title {
  white-space: normal; /* автоматический перенос */
  line-height: 1.1; /* уменьшаем межстрочный интервал */
  max-width: 500px; /* ограничиваем ширину для переноса */
  font-size: 56px; /* единый размер как у всех */
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
  bottom: 0; /* по нижней границе баннера */
  height: 486px; /* уменьшена на 10% (было 540px) */
  object-fit: contain;
  z-index: 1; /* под текстом, но над фоном */
  pointer-events: none; /* не перекрывает клики по меню */
}


/* Мобильная версия - пропорциональное уменьшение всех элементов */
@media (max-width: 900px) {
  /* Коэффициент масштабирования: ~0.7 для экранов до 900px */
  .hero-banner {
    margin-top: calc(85px * 0.7);
    margin-bottom: calc(80px * 0.7);
  }
  .hero-container {
    max-width: 100%;
    height: calc(405px * 0.7); /* 283.5px */
  }
  .banner-background {
    width: 110%;
    left: -5%;
    border-radius: calc(50px * 0.7); /* 35px */
  }
  .banner-content {
    width: 55%;
    max-width: calc(540px * 0.7);
    padding: calc(40px * 0.7) calc(220px * 0.7) calc(20px * 0.7) calc(44px * 0.7);
  }
  .hero-slide:nth-child(1) .banner-content {
    padding-right: calc(160px * 0.7);
  }
  .hero-slide:nth-child(2) .banner-content {
    padding-right: calc(200px * 0.7);
    padding-left: calc(44px * 0.7);
  }
  .hero-slide:nth-child(3) .banner-content {
    padding-right: calc(200px * 0.7);
    padding-left: calc(44px * 0.7);
  }
  .hero-slide:nth-child(4) .banner-content {
    padding-right: calc(200px * 0.7);
  }
  .banner-char {
    right: calc(40px * 0.7);
    height: calc(486px * 0.7); /* 340.2px */
  }
  .banner-title { 
    font-size: calc(56px * 0.7); /* 39.2px */
  }
  /* Первый баннер: уменьшенные размеры */
  .hero-slide:nth-child(1) .banner-title {
    font-size: calc(50px * 0.65); /* 32.5px - меньше чем обычно */
  }
  .hero-slide:nth-child(1) .banner-description {
    font-size: calc(27px * 0.65); /* 17.55px - меньше чем обычно */
  }
  .hero-slide:nth-child(1) .banner-button {
    font-size: calc(36px * 0.65); /* 23.4px - меньше чем обычно */
  }
  .banner-title-first {
    font-size: calc(50px * 0.7); /* 35px */
  }
  .banner-title-small {
    font-size: calc(44px * 0.7); /* 30.8px */
  }
  .hero-slide:nth-child(3) .banner-title {
    font-size: calc(56px * 0.7); /* 39.2px - единый размер */
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
  /* Коэффициент масштабирования: ~0.6 для экранов до 768px */
  .hero-banner {
    margin-top: calc(85px * 0.6);
    margin-bottom: calc(80px * 0.6);
  }
  .hero-container { 
    width: 100%; 
    height: calc(405px * 0.6); /* 243px */
  }
  .banner-background {
    width: 110%;
    left: -5%;
    border-radius: calc(50px * 0.6); /* 30px */
  }
  .banner-content { 
    width: 55%;
    max-width: calc(540px * 0.6);
    padding: calc(40px * 0.6) calc(220px * 0.6) calc(20px * 0.6) calc(44px * 0.6);
  }
  .hero-slide:nth-child(1) .banner-content { 
    padding-right: calc(160px * 0.6);
  }
  .hero-slide:nth-child(2) .banner-content {
    padding-right: calc(200px * 0.6);
    padding-left: calc(44px * 0.6);
  }
  .hero-slide:nth-child(3) .banner-content {
    padding-right: calc(200px * 0.6);
    padding-left: calc(44px * 0.6);
  }
  .hero-slide:nth-child(4) .banner-content {
    padding-right: calc(200px * 0.6);
  }
  .banner-char { 
    right: calc(40px * 0.6);
    height: calc(486px * 0.6); /* 291.6px */
    bottom: 0;
  }
  .hero-slide:nth-child(4) .banner-char {
    right: calc(20px * 0.6);
  }
  .banner-title { 
    font-size: calc(56px * 0.6); /* 33.6px */
  }
  /* Первый баннер: уменьшенные размеры */
  .hero-slide:nth-child(1) .banner-title {
    font-size: calc(50px * 0.55); /* 27.5px - меньше чем обычно */
  }
  .hero-slide:nth-child(1) .banner-description {
    font-size: calc(27px * 0.55); /* 14.85px - меньше чем обычно */
  }
  .hero-slide:nth-child(1) .banner-button {
    font-size: calc(36px * 0.55); /* 19.8px - меньше чем обычно */
  }
  .banner-title-first {
    font-size: calc(50px * 0.6); /* 30px */
  }
  .banner-title-small {
    font-size: calc(44px * 0.6); /* 26.4px */
  }
  .hero-slide:nth-child(3) .banner-title {
    font-size: calc(56px * 0.6); /* 33.6px - единый размер */
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
  /* Коэффициент масштабирования: ~0.5 для экранов до 480px */
  .hero-banner {
    margin-top: calc(85px * 0.5);
    margin-bottom: calc(80px * 0.5);
  }
  .hero-container { 
    height: calc(405px * 0.5); /* 202.5px */
  }
  .banner-background {
    width: 110%;
    left: -5%;
    border-radius: calc(50px * 0.5); /* 25px */
  }
  .banner-content { 
    width: 55%;
    max-width: calc(540px * 0.5);
    padding: calc(40px * 0.5) calc(220px * 0.5) calc(20px * 0.5) calc(44px * 0.5);
  }
  .hero-slide:nth-child(1) .banner-content { 
    padding-right: calc(160px * 0.5);
  }
  .hero-slide:nth-child(2) .banner-content {
    padding-right: calc(200px * 0.5);
    padding-left: calc(44px * 0.5);
  }
  .hero-slide:nth-child(3) .banner-content {
    padding-right: calc(200px * 0.5);
    padding-left: calc(44px * 0.5);
  }
  .hero-slide:nth-child(4) .banner-content {
    padding-right: calc(200px * 0.5);
  }
  .banner-char { 
    height: calc(486px * 0.5); /* 243px */
    right: calc(40px * 0.5);
  }
  .hero-slide:nth-child(4) .banner-char {
    right: calc(20px * 0.5);
  }
  .banner-title { 
    font-size: calc(56px * 0.5); /* 28px */
  }
  /* Первый баннер: уменьшенные размеры */
  .hero-slide:nth-child(1) .banner-title {
    font-size: calc(50px * 0.45); /* 22.5px - меньше чем обычно */
  }
  .hero-slide:nth-child(1) .banner-description {
    font-size: calc(27px * 0.45); /* 12.15px - меньше чем обычно */
  }
  .hero-slide:nth-child(1) .banner-button {
    font-size: calc(36px * 0.45); /* 16.2px - меньше чем обычно */
  }
  .banner-title-first {
    font-size: calc(50px * 0.5); /* 25px */
  }
  .banner-title-small {
    font-size: calc(44px * 0.5); /* 22px */
  }
  .hero-slide:nth-child(3) .banner-title {
    font-size: calc(56px * 0.5); /* 28px - единый размер */
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