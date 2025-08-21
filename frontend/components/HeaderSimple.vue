<template>
  <header class="header">
    <!-- Фоновое видео -->
    <div class="header-background">
      <video class="header-video" autoplay muted loop playsinline>
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
      
      <!-- Навигационное меню -->
      <nav class="navigation">
        <ul class="nav-list">
          <li class="nav-item">
            <NuxtLink to="/" class="nav-link">Главная</NuxtLink>
          </li>
          <li class="nav-item">
            <NuxtLink to="/catalog" class="nav-link">Каталог</NuxtLink>
          </li>
          <li class="nav-item">
            <NuxtLink to="/promotions" class="nav-link">Акции</NuxtLink>
          </li>
          <li class="nav-item">
            <NuxtLink to="/prices" class="nav-link">Цены</NuxtLink>
          </li>
          <li class="nav-item">
            <NuxtLink to="/contacts" class="nav-link">Контакты</NuxtLink>
          </li>
        </ul>
      </nav>
      
      <!-- Контактная информация -->
      <div class="contacts">
        <div class="contact-info">
          <!-- Крупный номер телефона -->
          <div class="phone-main">
            <a href="tel:+79602543323" class="phone-large">+7(960)254 33 23</a>
          </div>
          <!-- Время работы -->
          <div class="working-hours">
            <span class="hours-text">каждый день с 9 до 19</span>
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


    </div>


  </header>
</template>

<script setup>
// Пустой скрипт, поскольку вся функциональность удалена
</script>

<style scoped>
.header {
  position: relative;
  padding: 20px 0;
  min-height: 120px; /* минимальная высота для отображения видео */
  z-index: 10;
}

/* Фоновое видео */
.header-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  
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
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    z-index: 0;
  }
}

.header-content {
  max-width: 1200px; /* единая ширина */
  margin: 0 auto; /* центрирование */
  padding: 30px 40px; /* увеличиваем padding для лучшего отображения видео */
  display: flex;
  align-items: flex-end; /* Выравнивание по нижнему краю */
  justify-content: space-between;
  position: relative;
  z-index: 2;
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

/* Адаптивность */
@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    gap: 20px;
    padding: 0 20px; /* обновлено для консистентности */
    align-items: center;
  }
  
  .navigation {
    margin-left: 0;
    justify-content: center;
  }
  
  .navigation .nav-list {
    gap: 15px;
    align-items: center;
  }
  
  .contacts {
    align-items: center;
  }
  
  .contact-info {
    align-items: center;
  }
  
  .phone-large {
    font-size: 20px;
  }
  
  .hours-text {
    text-align: center;
  }
}

@media (max-width: 480px) {
  .navigation .nav-list {
    flex-wrap: wrap;
    justify-content: center;
    gap: 12px;
  }
  
  .navigation .nav-link {
    padding: 8px 12px;
    font-size: 0.9rem;
  }
  
  .phone-large {
    font-size: 18px;
  }
  
  .contact-icons {
    gap: 8px;
  }
  
  .contact-icon {
    width: 28px;
    height: 28px;
  }
  
  .contact-icon span {
    font-size: 14px;
  }
  
  .contact-icon-img {
    width: 18px;
    height: 18px;
  }
}







</style> 