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
          <h1 class="banner-title" :class="{ 'banner-title-small': index === 1, 'banner-title-preline': banner.title && banner.title.includes('\n') }">{{ banner.title }}</h1>
          <p class="banner-description">{{ banner.description }}</p>
          <a :href="banner.href" class="banner-button" :class="{ 'banner-button-lower': index === 1 }" @click.stop="handleButtonClick(banner.href)">{{ banner.cta }}</a>
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
    href: '/akcii' // TODO: обновить когда страница Акции будет создана
  },
  {
    fon: '/assets/hero/fon4.png',
    char: '/assets/hero/char4.png',
    title: 'Сделай шляпную\nкоробку сам',
    description: 'Работаем на клиента',
    cta: 'Попробовать',
    href: '/category/hat-boxes'
  },
  {
    fon: '/assets/hero/fon6.png',
    char: '/assets/hero/char6.png',
    title: 'Доставляем\nдо двери',
    description: 'Работаем на клиента',
    cta: 'Узнать подробности',
    href: '#'
  }
  
]

const currentSlide = ref(0)
let slideInterval = null

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % banners.length
}

const handleBannerClick = () => {
  nextSlide()
}

const handleButtonClick = (href) => {
  if (href && href !== '#') {
    window.location.href = href
  }
}

const startSlideShow = () => {
  slideInterval = setInterval(() => {
    nextSlide()
  }, 4000)
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
  max-width: 1100px; /* уменьшена с 1200px для более компактного вида */
  margin: 0 auto; /* центрирование */
  width: 100%;
  height: 450px; /* увеличена на 40% (было 320px) */
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
  width: 600px; /* увеличиваем область текста для размещения заголовка в одну строку */
  height: 100%;
  padding: 40px 15px 20px 44px; /* увеличиваем верхний отступ для лучшего позиционирования в увеличенном баннере */
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
  text-shadow: none;
  -webkit-text-stroke: 0;
  text-stroke: 0;
  paint-order: fill; /* исключаем отрисовку обводки, если она задана где-то глобально */
}

.banner-title-small {
  font-size: 44px;
  white-space: normal; /* разрешаем перенос для второго баннера */
  line-height: 1.1; /* уменьшаем межстрочный интервал */
  max-width: 500px; /* ограничиваем ширину для переноса */
}

.banner-title-preline {
  white-space: pre-line;
}

.banner-button-lower {
  margin-top: 4px;
}

/* Специальные стили для второго баннера */
.hero-slide:nth-child(2) .banner-content {
  padding-right: 200px; /* добавляем отступ справа для персонажа */
}

.hero-slide:nth-child(2) .banner-title {
  white-space: normal;
  line-height: 1.1;
  max-width: 500px;
}

/* Специальные стили для баннера 4 (с fon6.png) - разрешаем перенос заголовка */
.hero-slide:nth-child(4) .banner-content {
  padding-right: 200px; /* добавляем отступ справа для персонажа */
}

.hero-slide:nth-child(4) .banner-title {
  white-space: normal; /* разрешаем перенос для четвертого баннера */
  line-height: 1.1; /* уменьшаем межстрочный интервал */
  max-width: 500px; /* ограничиваем ширину для переноса */
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
  white-space: normal; /* разрешаем перенос для третьего баннера */
  line-height: 1.1; /* уменьшаем межстрочный интервал */
  max-width: 500px; /* ограничиваем ширину для переноса */
  font-size: 48px; /* уменьшенный размер шрифта */
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
  height: 540px; /* увеличена на 40% (было 384px) */
  object-fit: contain;
  z-index: 2; /* над фоном, под шапкой */
  pointer-events: none; /* не перекрывает клики по меню */
}


@media (max-width: 768px) {
  .hero-container { width: 95%; height: 360px; }
  .banner-content { width: 55%; padding: 16px; }
  .banner-char { right: 10px; height: 432px; bottom: 0; }
  .banner-title { font-size: 44px; }
  .banner-description { font-size: 20px; }
  .banner-button { font-size: 28px; padding: 6px 12px; border-radius: 18px; }
  
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
    font-size: 38px; /* адаптивный размер для планшетов */
  }
  
  .hero-slide:nth-child(4) .banner-title {
    max-width: 100%; /* на мобильных используем всю доступную ширину */
  }
}

@media (max-width: 480px) {
  .hero-container { height: 315px; }
  .banner-content { width: 60%; }
  .banner-char { height: 378px; }
  .banner-title { font-size: 32px; }
  .banner-description { font-size: 16px; }
  .banner-button { font-size: 20px; padding: 4px 8px; border-radius: 12px; }
  
  /* Адаптивные стили для второго баннера */
  .hero-slide:nth-child(2) .banner-content {
    padding-right: 16px;
  }
  
  /* Адаптивные стили для третьего баннера */
  .hero-slide:nth-child(3) .banner-content {
    padding-right: 16px;
  }
  
  /* Адаптивные стили для четвертого баннера */
  .hero-slide:nth-child(4) .banner-content {
    padding-right: 16px;
  }
  
  
  .banner-title-small {
    max-width: 100%;
  }
  
  .hero-slide:nth-child(3) .banner-title {
    max-width: 100%;
    font-size: 28px; /* адаптивный размер для мобильных */
  }
  
  .hero-slide:nth-child(4) .banner-title {
    max-width: 100%;
  }
}
</style>