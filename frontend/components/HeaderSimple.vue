<template>
  <header ref="headerRef" class="header">
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
          <li
            v-if="showCatalogMegaMenu"
            class="nav-item nav-item--dropdown"
            @mouseenter="openCatalogDropdown"
            @mouseleave="closeCatalogDropdown"
          >
            <NuxtLink to="/catalog" class="nav-link nav-link--catalog">Каталог</NuxtLink>
          </li>
          <li v-else class="nav-item">
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
          <template v-if="showCatalogMegaMenu">
            <button type="button" class="mobile-link mobile-link--toggle" @click="toggleMobileCatalog">
              Каталог
              <span class="mobile-toggle-icon" :class="{ open: isMobileCatalogOpen }">›</span>
            </button>
            <div v-if="isMobileCatalogOpen" class="mobile-catalog-submenu">
              <NuxtLink
                v-for="item in catalogMenuItems"
                :key="item.route"
                :to="item.route"
                class="mobile-catalog-link"
                @click="closeMenu"
              >
                {{ plainCatalogLabel(item.name) }}
              </NuxtLink>
            </div>
          </template>
          <NuxtLink v-else to="/catalog" class="mobile-link" @click="closeMenu">Каталог</NuxtLink>
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

  <Teleport to="body">
    <div
      v-show="isCatalogDropdownOpen && showCatalogMegaMenu"
      class="catalog-dropdown"
      :style="{ top: `${dropdownTop}px` }"
      @mouseenter="openCatalogDropdown"
      @mouseleave="closeCatalogDropdown"
    >
      <div class="catalog-dropdown-panel">
        <div class="catalog-dropdown-inner">
          <NuxtLink
            v-for="(item, index) in catalogMenuItems"
            :key="item.route"
            :to="item.route"
            class="catalog-dropdown-item"
            @mouseenter="setCatalogHover(index, true)"
            @mouseleave="setCatalogHover(index, false)"
          >
            <span class="catalog-dropdown-icon-wrap">
              <img
                :src="catalogHoveredItems[index] ? item.iconOn : item.iconOff"
                :alt="plainCatalogLabel(item.name)"
                class="catalog-dropdown-icon"
                :class="{
                  'catalog-dropdown-icon--active': catalogHoveredItems[index],
                  'catalog-dropdown-icon--svg': item.iconSvg,
                }"
              />
            </span>
            <span class="catalog-dropdown-label">{{ plainCatalogLabel(item.name) }}</span>
          </NuxtLink>
        </div>
      </div>
    </div>
  </Teleport>
  
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'
import { useCatalogMenuItems } from '../composables/useCatalogMenuItems'

const route = useRoute()
const { catalogMenuItems, plainCatalogLabel } = useCatalogMenuItems()

const isMenuOpen = ref(false)
const isMobileCatalogOpen = ref(false)
const isCatalogDropdownOpen = ref(false)
const isDesktop = ref(true)
const catalogHoveredItems = ref(catalogMenuItems.map(() => false))
const headerRef = ref(null)
const dropdownTop = ref(0)
const videoRef = ref(null)
let checkVideoPlaybackInterval = null
let catalogDropdownCloseTimer = null
let desktopMediaQuery = null

const isHomeOrCatalogPage = computed(() => route.path === '/' || route.path === '/catalog')

const showCatalogMegaMenu = computed(() => isDesktop.value && !isHomeOrCatalogPage.value)

const updateDropdownPosition = () => {
  const headerEl = headerRef.value
  if (!headerEl) return
  dropdownTop.value = headerEl.getBoundingClientRect().bottom
}

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
  if (!isMenuOpen.value) {
    isMobileCatalogOpen.value = false
  }
}

const closeMenu = () => {
  isMenuOpen.value = false
  isMobileCatalogOpen.value = false
}

const toggleMobileCatalog = () => {
  isMobileCatalogOpen.value = !isMobileCatalogOpen.value
}

const openCatalogDropdown = () => {
  if (!showCatalogMegaMenu.value) return
  if (catalogDropdownCloseTimer) {
    clearTimeout(catalogDropdownCloseTimer)
    catalogDropdownCloseTimer = null
  }
  updateDropdownPosition()
  isCatalogDropdownOpen.value = true
}

const closeCatalogDropdown = () => {
  catalogDropdownCloseTimer = setTimeout(() => {
    isCatalogDropdownOpen.value = false
    catalogHoveredItems.value = catalogMenuItems.map(() => false)
  }, 180)
}

const setCatalogHover = (index, isHovered) => {
  catalogHoveredItems.value[index] = isHovered
}

const onViewportChange = () => {
  if (isCatalogDropdownOpen.value) {
    updateDropdownPosition()
  }
}

const updateDesktopMode = () => {
  if (!desktopMediaQuery) return
  isDesktop.value = desktopMediaQuery.matches
  if (!showCatalogMegaMenu.value) {
    isCatalogDropdownOpen.value = false
    isMobileCatalogOpen.value = false
  }
}

watch(() => route.path, () => {
  isCatalogDropdownOpen.value = false
  isMobileCatalogOpen.value = false
})

// Принудительный запуск видео для iOS/Safari (агрессивный подход)
onMounted(() => {
  if (import.meta.client) {
    desktopMediaQuery = window.matchMedia('(min-width: 1025px)')
    updateDesktopMode()
    desktopMediaQuery.addEventListener('change', updateDesktopMode)
  }

  window.addEventListener('resize', onViewportChange)
  window.addEventListener('scroll', onViewportChange, { passive: true })

  const video = videoRef.value
  if (!video) return

  // Устанавливаем все необходимые атрибуты для iOS/Safari
  video.setAttribute('playsinline', '')
  video.setAttribute('webkit-playsinline', '')
  video.setAttribute('x-webkit-airplay', 'allow')
  video.muted = true
  video.playsInline = true
  video.defaultMuted = true
  
  // Принудительно загружаем видео
  video.load()
  
  // Функция для попытки запуска видео (более агрессивная)
  const attemptPlay = () => {
    if (!video) return
    
    // Убеждаемся, что видео muted
    if (!video.muted) {
      video.muted = true
    }
    
    const playPromise = video.play()
    if (playPromise !== undefined) {
      playPromise
        .then(() => {
          console.log('Video playing successfully')
        })
        .catch((error) => {
          console.log('Video play attempt failed:', error)
        })
    }
  }

  // Множественные попытки запуска с разными задержками
  const attempts = [0, 100, 200, 500, 1000, 1500, 2000]
  attempts.forEach((delay) => {
    setTimeout(() => {
      attemptPlay()
    }, delay)
  })

  // Пытаемся запустить после загрузки метаданных
  const onLoadedMetadata = () => {
    attemptPlay()
  }
  video.addEventListener('loadedmetadata', onLoadedMetadata, { once: true })

  // Пытаемся запустить когда видео готово к воспроизведению
  const onCanPlay = () => {
    attemptPlay()
  }
  video.addEventListener('canplay', onCanPlay, { once: true })
  video.addEventListener('canplaythrough', onCanPlay, { once: true })

  // Пытаемся запустить когда загружены первые данные
  const onLoadedData = () => {
    attemptPlay()
  }
  video.addEventListener('loadeddata', onLoadedData, { once: true })

  // Если видео уже загружено, пытаемся запустить сразу
  if (video.readyState >= 2) {
    attemptPlay()
  }

  // Используем requestAnimationFrame для более надежного запуска (несколько раз)
  for (let i = 0; i < 5; i++) {
    requestAnimationFrame(() => {
      setTimeout(() => {
        attemptPlay()
      }, i * 100)
    })
  }

  // Агрессивно слушаем ЛЮБОЕ взаимодействие пользователя для Safari
  const tryPlayOnInteraction = (e) => {
    if (video && video.paused) {
      attemptPlay()
    }
  }
  
  // Слушаем все возможные события взаимодействия
  const events = ['touchstart', 'touchend', 'click', 'scroll', 'mousedown', 'mouseup', 'keydown', 'keyup', 'focus']
  events.forEach(eventType => {
    document.addEventListener(eventType, tryPlayOnInteraction, { once: false, passive: true })
    window.addEventListener(eventType, tryPlayOnInteraction, { once: false, passive: true })
  })

  // Используем Intersection Observer для запуска когда видео видно
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && video.paused) {
          attemptPlay()
        }
      })
    }, { threshold: 0.1 })
    
    observer.observe(video)
  }

  // Периодически проверяем и перезапускаем видео, если оно остановилось (для Safari)
  checkVideoPlaybackInterval = setInterval(() => {
    if (video && video.paused && video.readyState >= 2) {
      attemptPlay()
    }
  }, 500) // Увеличил частоту проверки до 500ms
})

// Очищаем интервал при размонтировании
onUnmounted(() => {
  if (desktopMediaQuery) {
    desktopMediaQuery.removeEventListener('change', updateDesktopMode)
    desktopMediaQuery = null
  }
  window.removeEventListener('resize', onViewportChange)
  window.removeEventListener('scroll', onViewportChange)

  if (checkVideoPlaybackInterval) {
    clearInterval(checkVideoPlaybackInterval)
    checkVideoPlaybackInterval = null
  }
  if (catalogDropdownCloseTimer) {
    clearTimeout(catalogDropdownCloseTimer)
    catalogDropdownCloseTimer = null
  }
})
</script>

<style scoped>
.header {
  position: relative;
  padding: 11px 0;
  min-height: 66px;
  z-index: 5;
  width: 100%;
  background: transparent;
  overflow: visible;
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
  overflow: hidden;
  
  .header-video {
    width: 100%;
    height: 100%;
    min-width: 100%;
    min-height: 100%;
    object-fit: cover;
    object-position: center center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
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
  max-width: 1200px;
  margin: 0 auto;
  padding: 13px 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  z-index: 40;
  gap: 12px;
}

.navigation {
  flex: 1;
  display: flex;
  justify-content: flex-start;
  margin-left: 20px;
}

.contacts {
  flex-shrink: 0;
  display: flex;
  align-items: center;
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
  height: 46px;
  width: auto;
}

/* Навигация */
.navigation .nav-list {
  display: flex;
  list-style: none;
  gap: 8px;
  align-items: center;
  margin: 0;
  padding: 0;
}

.navigation .nav-item {
  position: relative;
}

.navigation .nav-link {
  display: block;
  padding: 4px 5px;
  color: #000000;
  text-decoration: none;
  font-weight: 500;
  position: relative;
  border-radius: 5px;
  transition: color 1s ease;
}

.navigation .nav-link:hover {
  color: #47009f;
}

.nav-item--dropdown {
  position: relative;
}

.nav-link--catalog::after {
  content: '▾';
  display: inline-block;
  margin-left: 4px;
  font-size: 10px;
  opacity: 0.7;
  transform: translateY(-1px);
}

.catalog-dropdown {
  position: fixed;
  left: 0;
  right: 0;
  width: 100%;
  z-index: 10050;
}

.catalog-dropdown::before {
  content: '';
  position: absolute;
  top: -16px;
  left: 0;
  right: 0;
  height: 16px;
}

.catalog-dropdown-panel {
  width: 100%;
  background: #fff;
  border-top: 1px solid rgba(71, 0, 159, 0.1);
  border-bottom: 1px solid rgba(71, 0, 159, 0.08);
  box-shadow: 0 16px 32px rgba(71, 0, 159, 0.14);
}

.catalog-dropdown-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 10px 40px 12px;
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 4px 12px;
}

.catalog-dropdown-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  gap: 6px;
  padding: 6px 8px;
  border-radius: 8px;
  text-decoration: none;
  color: #000;
  text-align: left;
  min-height: 36px;
  transition: background-color 0.2s ease;
}

.catalog-dropdown-item:hover {
  background: rgba(71, 0, 159, 0.06);
}

.catalog-dropdown-icon-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  flex-shrink: 0;
}

.catalog-dropdown-icon {
  width: 26px;
  height: 26px;
  object-fit: contain;
  transition: transform 0.2s ease, filter 0.2s ease, opacity 0.2s ease;
  opacity: 0.82;
  filter: saturate(0.7);
}

.catalog-dropdown-icon--active {
  transform: scale(1.06);
  opacity: 1;
  filter: none;
}

.catalog-dropdown-icon--svg:not(.catalog-dropdown-icon--active) {
  filter: grayscale(1) opacity(0.6);
}

.catalog-dropdown-icon--svg.catalog-dropdown-icon--active {
  filter: none;
}

.catalog-dropdown-label {
  display: block;
  flex: 1;
  min-width: 0;
  font-family: 'Days One', cursive;
  font-size: 10px;
  line-height: 1.2;
  color: #222;
  text-align: left;
}

/* Убираем левый отступ у первого элемента */
.navigation .nav-item:first-child .nav-link {
  padding-left: 0;
}

/* Контакты */
.contact-info {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 2px;
}

.phone-main {
  display: flex;
  justify-content: flex-end;
}

.phone-large {
  color: #000000;
  text-decoration: none;
  font-weight: 700;
  font-size: 18px;
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
  font-size: 10px;
  color: #666666; /* серый цвет для дополнительной информации */
  font-weight: 400;
  text-align: right;
  line-height: 1.2;
}

.contact-icons {
  display: flex;
  gap: 6px;
  justify-content: flex-end;
}

.contact-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
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
  width: 14px;
  height: 14px;
  object-fit: contain;
}

.burger {
  display: none;
  width: 34px;
  height: 34px;
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
  height: 30px;
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
  text-decoration: none;
  background: none;
  border-left: none;
  border-right: none;
  border-top: none;
  width: 100%;
  text-align: left;
  cursor: pointer;
}

.mobile-link--toggle {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.mobile-toggle-icon {
  display: inline-block;
  font-size: 18px;
  line-height: 1;
  transition: transform 0.2s ease;
}

.mobile-toggle-icon.open {
  transform: rotate(90deg);
}

.mobile-catalog-submenu {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 0 0 8px 12px;
}

.mobile-catalog-link {
  font-size: 14px;
  font-weight: 500;
  color: #47009f;
  text-decoration: none;
  padding: 6px 0;
}

.mobile-catalog-link:hover {
  text-decoration: underline;
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
    gap: 10px;
    padding: 9px 18px;
  }
  
  .logo .logo-image {
    height: 37px;
  }
}

@media (max-width: 1024px) {
  .desktop-nav,
  .desktop-contacts {
    display: none;
  }

  .catalog-dropdown {
    display: none;
  }

  .burger {
    display: inline-flex;
  }

  .header-content {
    padding: 9px 20px;
  }
}

@media (max-width: 480px) {
  .header {
    padding: 7px 0;
  }

  .header-content {
    padding: 7px 14px;
    gap: 8px;
  }

  .burger {
    width: 32px;
    height: 32px;
  }

  .mobile-menu {
    width: 100%;
  }
}
</style>