<template>
  <header class="header">
    <!-- Фоновое видео -->
    <div class="header-background">
      <video 
        ref="videoRef"
        class="header-video" 
        autoplay 
        muted 
        loop 
        playsinline
        webkit-playsinline
        x-webkit-airplay="allow"
        preload="auto"
        disablePictureInPicture
        controlsList="nodownload nofullscreen noremoteplayback"
      >
        <source src="/assets/hero/tudasuda.mp4" type="video/mp4">
        Ваш браузер не поддерживает видео.
      </video>
      <!-- Fallback фон если видео не загрузилось -->
      <div class="video-fallback"></div>
    </div>
    
    <div class="header-content">
      <!-- Логотип с изображением -->
      <div class="logo">
        <NuxtLink to="/" class="logo-link">
          <img src="/assets/logo/floksbox лого.png" alt="Floksbox" class="logo-image" />
        </NuxtLink>
      </div>
      
      <!-- Навигационное меню (desktop) -->
      <nav class="navigation desktop-nav">
        <ul class="nav-list">
          <li class="nav-item">
            <NuxtLink to="/" class="nav-link">Главная</NuxtLink>
          </li>
          <li class="nav-item">
            <NuxtLink to="/catalog" class="nav-link">Каталог</NuxtLink>
          </li>
          <li class="nav-item">
            <NuxtLink to="/prices" class="nav-link">Цены</NuxtLink>
          </li>
          <li class="nav-item">
            <NuxtLink to="/promotions" class="nav-link">Доставка</NuxtLink>
          </li>
          <li class="nav-item">
            <NuxtLink to="/contacts" class="nav-link">Контакты</NuxtLink>
          </li>
        </ul>
      </nav>
      
      <!-- Контактная информация -->
      <div class="contacts desktop-contacts">
        <div class="contact-info">
          <!-- Крупный номер телефона -->
          <div class="phone-main">
            <a href="tel:+79602543323" class="phone-large">+7(960)254 33 23</a>
          </div>
          <!-- Время работы -->
          <div class="working-hours">
            <span class="hours-text">ежедневно с 9:00 до 19:00</span>
          </div>
          <!-- Иконки связи -->
          <div class="contact-icons">
            <a href="mailto:info@floksbox.ru" class="contact-icon" title="Email">
              <img src="/assets/icons/p_email.png" alt="Email" class="contact-icon-img">
            </a>
            <a href="https://t.me/floksbox" class="contact-icon" title="Telegram" target="_blank">
              <img src="/assets/icons/p_tg.png" alt="Telegram" class="contact-icon-img">
            </a>
            <a href="https://wa.me/79602543323" class="contact-icon" title="WhatsApp" target="_blank">
              <img src="/assets/icons/p_wa.png" alt="WhatsApp" class="contact-icon-img">
            </a>
          </div>
        </div>
      </div>

      <!-- Бургер для мобильных -->
      <button class="burger" @click="toggleMenu" aria-label="Меню">
        <span :class="{ open: isMenuOpen }"></span>
      </button>
    </div>

    <!-- Мобильное меню -->
    <div v-if="isMenuOpen" class="mobile-menu-overlay" @click.self="isMenuOpen = false">
      <div class="mobile-menu">
        <div class="mobile-menu__header">
          <NuxtLink to="/" class="mobile-logo" @click="closeMenu">
            <img src="/assets/logo/floksbox лого.png" alt="Floksbox" />
          </NuxtLink>
          <button class="close-btn" @click="closeMenu" aria-label="Закрыть меню">×</button>
        </div>

        <nav class="mobile-nav">
          <NuxtLink to="/" class="mobile-link" @click="closeMenu">Главная</NuxtLink>
          <NuxtLink to="/catalog" class="mobile-link" @click="closeMenu">Каталог</NuxtLink>
          <NuxtLink to="/prices" class="mobile-link" @click="closeMenu">Цены</NuxtLink>
          <NuxtLink to="/promotions" class="mobile-link" @click="closeMenu">Доставка</NuxtLink>
          <NuxtLink to="/contacts" class="mobile-link" @click="closeMenu">Контакты</NuxtLink>
        </nav>

        <div class="mobile-contacts">
          <a href="tel:+79602543323" class="mobile-phone">+7(960)254 33 23</a>
          <span class="mobile-hours">ежедневно с 9:00 до 19:00</span>
          <div class="mobile-icons">
            <a href="mailto:info@floksbox.ru" class="contact-icon" title="Email">
              <img src="/assets/icons/p_email.png" alt="Email" class="contact-icon-img">
            </a>
            <a href="https://t.me/floksbox" class="contact-icon" title="Telegram" target="_blank">
              <img src="/assets/icons/p_tg.png" alt="Telegram" class="contact-icon-img">
            </a>
            <a href="https://wa.me/79602543323" class="contact-icon" title="WhatsApp" target="_blank">
              <img src="/assets/icons/p_wa.png" alt="WhatsApp" class="contact-icon-img">
            </a>
          </div>
        </div>
      </div>
    </div>
  </header>
  
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isMenuOpen = ref(false)
const videoRef = ref(null)
let checkVideoPlaybackInterval = null

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = () => {
  isMenuOpen.value = false
}

// Принудительный запуск видео для iOS/Safari
onMounted(() => {
  const video = videoRef.value
  if (!video) return

  // Устанавливаем все необходимые атрибуты для iOS/Safari
  video.setAttribute('playsinline', '')
  video.setAttribute('webkit-playsinline', '')
  video.setAttribute('x-webkit-airplay', 'allow')
  video.muted = true
  video.playsInline = true
  
  // Функция для попытки запуска видео
  const attemptPlay = () => {
    if (!video) return
    
    const playPromise = video.play()
    if (playPromise !== undefined) {
      playPromise
        .then(() => {
          console.log('Video playing successfully')
          // Убеждаемся, что видео продолжает играть
          if (video.paused) {
            video.play().catch(() => {})
          }
        })
        .catch((error) => {
          console.log('Video play attempt failed:', error)
          // Пробуем еще раз через небольшую задержку
          setTimeout(() => {
            if (video && video.paused) {
              video.play().catch(() => {})
            }
          }, 100)
        })
    }
  }

  // Пытаемся запустить сразу
  attemptPlay()

  // Пытаемся запустить после загрузки метаданных
  const onLoadedMetadata = () => {
    attemptPlay()
    video.removeEventListener('loadedmetadata', onLoadedMetadata)
  }
  video.addEventListener('loadedmetadata', onLoadedMetadata)

  // Пытаемся запустить когда видео готово к воспроизведению
  const onCanPlay = () => {
    attemptPlay()
    video.removeEventListener('canplay', onCanPlay)
  }
  video.addEventListener('canplay', onCanPlay)

  // Пытаемся запустить когда загружены первые данные
  const onLoadedData = () => {
    attemptPlay()
    video.removeEventListener('loadeddata', onLoadedData)
  }
  video.addEventListener('loadeddata', onLoadedData)

  // Если видео уже загружено, пытаемся запустить сразу
  if (video.readyState >= 2) {
    attemptPlay()
  }

  // Используем requestAnimationFrame для более надежного запуска
  requestAnimationFrame(() => {
    attemptPlay()
  })

  // Дополнительная попытка через небольшую задержку
  setTimeout(() => {
    attemptPlay()
  }, 200)

  // Слушаем первое взаимодействие пользователя для Safari
  const tryPlayOnInteraction = () => {
    if (video && video.paused) {
      attemptPlay()
    }
    document.removeEventListener('touchstart', tryPlayOnInteraction)
    document.removeEventListener('click', tryPlayOnInteraction)
    document.removeEventListener('scroll', tryPlayOnInteraction)
  }
  
  document.addEventListener('touchstart', tryPlayOnInteraction, { once: true, passive: true })
  document.addEventListener('click', tryPlayOnInteraction, { once: true })
  document.addEventListener('scroll', tryPlayOnInteraction, { once: true, passive: true })

  // Периодически проверяем и перезапускаем видео, если оно остановилось (для Safari)
  checkVideoPlaybackInterval = setInterval(() => {
    if (video && video.paused && video.readyState >= 2) {
      attemptPlay()
    }
  }, 1000)
})

// Очищаем интервал при размонтировании
onUnmounted(() => {
  if (checkVideoPlaybackInterval) {
    clearInterval(checkVideoPlaybackInterval)
    checkVideoPlaybackInterval = null
  }
})
</script>

<style scoped>
.header {
  position: relative;
  padding: 20px 0;
  min-height: 120px; /* минимальная высота для отображения видео */
  z-index: 10;
  width: 100%;
  background: #ffffff;
}

/* Фоновое видео */
.header-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  background: #ffffff;
  
  .header-video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 1;
  }
  
  .video-fallback {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: #ffffff;
    z-index: 0;
  }
}

.header-content {
  max-width: 1200px; /* единая ширина */
  margin: 0 auto; /* центрирование */
  padding: 30px 40px; /* увеличиваем padding для лучшего отображения видео */
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  z-index: 2;
  gap: 20px;
}

.navigation {
  flex: 1;
  display: flex;
  justify-content: flex-start;
  margin-left: 40px;
}

.contacts {
  flex-shrink: 0;
}

.desktop-contacts {
  display: flex;
}

/* Логотип */
.logo {
  flex-shrink: 0;
}

.logo .logo-link {
  display: block;
}

.logo .logo-image {
  height: 60px;
  width: auto;
}

/* Навигация */
.navigation .nav-list {
  display: flex;
  list-style: none;
  gap: 12px; /* Немного увеличенные отступы между пунктами меню */
  align-items: flex-end;
  margin: 0;
  padding: 0;
}

.navigation .nav-item {
  position: relative;
}

.navigation .nav-link {
  display: block;
  padding: 8px 6px; /* Уменьшенные внутренние отступы */
  color: #000000; /* черный цвет для видимости на светлом фоне */
  text-decoration: none;
  font-weight: 500;
  position: relative;
  border-radius: 5px;
  transition: color 1s ease;
}

.navigation .nav-link:hover {
  color: #47009f;
}

/* Убираем левый отступ у первого элемента */
.navigation .nav-item:first-child .nav-link {
  padding-left: 0;
}

/* Контакты */
.contacts {
  display: flex;
  align-items: flex-end;
}

.contact-info {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 8px;
}

.phone-main {
  display: flex;
  justify-content: flex-end;
}

.phone-large {
  color: #000000; /* черный цвет для видимости на светлом фоне */
  text-decoration: none;
  font-weight: 700;
  font-size: 24px;
  font-family: 'Montserrat', sans-serif;
  transition: color 0.3s ease;
  letter-spacing: -0.5px;
  white-space: nowrap;
}

.phone-large:hover {
  color: #47009f;
}

.working-hours {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 2px;
}

.hours-text {
  font-size: 12px;
  color: #666666; /* серый цвет для дополнительной информации */
  font-weight: 400;
  text-align: right;
  line-height: 1.2;
}

.contact-icons {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}

.contact-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(71, 0, 159, 0.1);
  text-decoration: none;
  transition: all 0.3s ease;
}

.contact-icon:hover {
  background: rgba(71, 0, 159, 0.2);
  transform: translateY(-2px);
}

.contact-icon span {
  font-size: 16px;
  line-height: 1;
}

.contact-icon-img {
  width: 20px;
  height: 20px;
  object-fit: contain;
}

.burger {
  display: none;
  width: 42px;
  height: 42px;
  border: none;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 10px;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  padding: 0;
  box-shadow: 0 6px 14px rgba(0, 0, 0, 0.08);
}

.burger span,
.burger span::before,
.burger span::after {
  display: block;
  width: 22px;
  height: 2px;
  background: #222;
  border-radius: 2px;
  position: relative;
  transition: all 0.25s ease;
}

.burger span::before,
.burger span::after {
  content: '';
  position: absolute;
  left: 0;
}

.burger span::before { top: -7px; }
.burger span::after { top: 7px; }

.burger span.open {
  background: transparent;
}

.burger span.open::before {
  top: 0;
  transform: rotate(45deg);
}

.burger span.open::after {
  top: 0;
  transform: rotate(-45deg);
}

.mobile-menu-overlay {
  position: fixed;
  inset: 0;
  background: rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(6px);
  z-index: 999;
  display: flex;
  justify-content: flex-end;
}

.mobile-menu {
  width: min(320px, 100%);
  height: 100%;
  background: #ffffff;
  box-shadow: -8px 0 24px rgba(0, 0, 0, 0.12);
  padding: 24px 20px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  border-left: 1px solid rgba(0, 0, 0, 0.05);
}

.mobile-menu__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.mobile-logo img {
  height: 38px;
  width: auto;
}

.mobile-nav {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.mobile-link {
  font-size: 16px;
  font-weight: 600;
  color: #222;
  padding: 10px 0;
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}

.mobile-contacts {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding-top: 12px;
  border-top: 1px solid rgba(0, 0, 0, 0.06);
}

.mobile-phone {
  font-weight: 700;
  font-size: 18px;
  color: #000;
}

.mobile-hours {
  font-size: 13px;
  color: #555;
}

.mobile-icons {
  display: flex;
  gap: 10px;
}

/* Адаптивность */
@media (max-width: 768px) {
  .header-content {
    flex-direction: row;
    gap: 14px;
    padding: 16px 18px;
  }
  
  .logo .logo-image {
    height: 48px;
  }
}

@media (max-width: 1024px) {
  .desktop-nav,
  .desktop-contacts {
    display: none;
  }

  .burger {
    display: inline-flex;
  }

  .header-content {
    padding: 18px 20px;
  }
}

@media (max-width: 480px) {
  .header {
    padding: 12px 0;
  }

  .header-content {
    padding: 12px 14px;
    gap: 10px;
  }

  .burger {
    width: 38px;
    height: 38px;
  }

  .mobile-menu {
    width: 100%;
  }
}
</style>