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
          <h1 class="banner-title" :class="{ 'banner-title-first': index === 0, 'banner-title-small': index === 1, 'banner-title-preline': banner.title && banner.title.includes('\n') }">{{ banner.title }}</h1>
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
    title: 'Пусть о Вас говорит Ваша упаковка',
    description: 'Коробки и упаковка для общепита. Не кусается!',
    cta: 'Перейти',
    href: '#',
    productName: 'коробка для пиццы'
  },
  {
    fon: '/assets/hero/fon4.png',
    char: '/assets/hero/char4.png',
    title: 'Шляпные коробки\nна любой вкус',
    description: 'Создайте свою!',
    cta: 'Создать',
    href: '/category/hat-boxes'
  },
  {
    fon: '/assets/hero/fon6.jpg',
    char: '/assets/hero/char6.png',
    title: 'Доставляем\nдо двери',
    description: 'По Москве, регионам \nи всей России!',
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
  z-index: 2;
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
  white-space: normal;
  text-shadow: 0 3px 10px rgba(0,0,0,0.25);
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
  white-space: normal; /* разрешаем перенос для второго баннера */
  line-height: 1.1; /* уменьшаем межстрочный интервал */
  max-width: 500px; /* ограничиваем ширину для переноса */
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

.banner-title-preline {
  white-space: pre-line;
}

.banner-button-lower {
  margin-top: 4px;
}

/* Специальные стили для второго баннера */
  .hero-slide:nth-child(2) .banner-content {
    padding-right: 120px; /* компактнее, без искусственного переноса */
  }

/* Специальные стили для баннера 4 (с fon6.jpg) - разрешаем перенос заголовка */
.hero-slide:nth-child(4) .banner-content {
  padding-right: 200px; /* добавляем отступ справа для персонажа */
}

.hero-slide:nth-child(4) .banner-title {
  white-space: normal; /* разрешаем перенос для четвертого баннера */
  line-height: 1.1; /* уменьшаем межстрочный интервал */
  max-width: 500px; /* ограничиваем ширину для переноса */
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

/* Усиливаем читаемость описания на баннере 4 (fon6.jpg) чёрным свечением */
.hero-slide:nth-child(4) .banner-description {
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.65), 0 0 8px rgba(0, 0, 0, 0.7), 0 0 14px rgba(0, 0, 0, 0.5);
}

.hero-slide:nth-child(4) .banner-char {
  right: 20px; /* сдвигаем персонажа еще правее */
}

/* Специальные стили для баннера 3 (с fon4.png) - разрешаем перенос заголовка */
.hero-slide:nth-child(3) .banner-content {
  padding-right: 200px; /* добавляем отступ справа для персонажа */
  padding-left: 80px; /* сдвигаем текст правее */
}

.hero-slide:nth-child(3) .banner-title {
  white-space: pre-line; /* перенос по \n для третьего баннера */
  line-height: 1.1; /* уменьшаем межстрочный интервал */
  max-width: 500px; /* ограничиваем ширину для переноса */
  font-size: 48px; /* уменьшенный размер шрифта */
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
  z-index: 2; /* над фоном, под шапкой */
  pointer-events: none; /* не перекрывает клики по меню */
}


@media (max-width: 900px) {
  .hero-banner {
    margin-top: 60px;
    margin-bottom: 50px;
  }
  .hero-container {
    max-width: 100%;
    height: 330px;
  }
  .banner-background {
    width: 100%;
    left: 0;
    border-radius: 32px;
  }
  .banner-content {
    width: 60%;
    padding: 24px 160px 14px 24px;
  }
  .hero-slide:nth-child(1) .banner-content {
    padding-right: 120px;
  }
  .banner-char {
    right: 14px;
    height: 320px;
  }
  .banner-title { font-size: 40px; }
  .banner-description { font-size: 18px; }
  .banner-button { font-size: 22px; padding: 6px 12px; border-radius: 16px; }
}

@media (max-width: 768px) {
  .hero-banner {
    margin-top: 46px;
    margin-bottom: 42px;
  }
  .hero-container { width: 100%; height: 300px; }
  .banner-content { width: 62%; padding: 18px 120px 12px 20px; }
  .hero-slide:nth-child(1) .banner-content { padding-right: 90px; }
  .banner-char { right: 6px; height: 270px; bottom: 0; }
  .banner-title { font-size: 34px; }
  .banner-description { font-size: 17px; }
  .banner-button { font-size: 19px; padding: 6px 12px; border-radius: 14px; }

  .banner-background {
    border-radius: 26px;
  }

  /* Адаптивные стили для второго баннера */
  .hero-slide:nth-child(2) .banner-content {
    padding-right: 16px; /* убираем лишний отступ на мобильных */
  }
  
  /* Адаптивные стили для третьего баннера */
  .hero-slide:nth-child(3) .banner-content {
    padding-right: 16px; /* убираем лишний отступ на мобильных */
  }
  
  /* Адаптивные стили для четвертого баннера */
  .hero-slide:nth-child(4) .banner-content {
    padding-right: 16px; /* убираем лишний отступ на мобильных */
  }
  
  .banner-title-small {
    max-width: 100%; /* на мобильных используем всю доступную ширину */
  }
  
  .hero-slide:nth-child(3) .banner-title {
    max-width: 100%; /* на мобильных используем всю доступную ширину */
    font-size: 30px; /* адаптивный размер для планшетов */
  }
  
  .hero-slide:nth-child(4) .banner-title {
    max-width: 100%; /* на мобильных используем всю доступную ширину */
  }
}

@media (max-width: 480px) {
  .hero-banner {
    margin-top: 32px;
    margin-bottom: 32px;
  }
  .hero-container { height: 260px; }
  .banner-content { width: 64%; padding: 14px 100px 10px 14px; }
  .hero-slide:nth-child(1) .banner-content { padding-right: 80px; }
  .banner-char { height: 210px; right: 0; }
  .banner-title { font-size: 26px; }
  .banner-description { font-size: 15px; }
  .banner-button { font-size: 16px; padding: 5px 10px; border-radius: 12px; }
  .banner-background { border-radius: 22px; }
  
  /* Адаптивные стили для второго баннера */
  .hero-slide:nth-child(2) .banner-content {
    padding-right: 12px;
  }
  
  /* Адаптивные стили для третьего баннера */
  .hero-slide:nth-child(3) .banner-content {
    padding-right: 12px;
  }
  
  /* Адаптивные стили для четвертого баннера */
  .hero-slide:nth-child(4) .banner-content {
    padding-right: 12px;
  }
  
  .banner-title-small {
    max-width: 100%;
  }
  
  .hero-slide:nth-child(3) .banner-title {
    max-width: 100%;
    font-size: 24px; /* адаптивный размер для мобильных */
  }
  
  .hero-slide:nth-child(4) .banner-title {
    max-width: 100%;
  }
}
</style>