<template>
  <header class="header">
    <!-- Фоновое видео -->
    <div class="header-background">
      <!-- Заглушка для видео, пока не добавлен файл tudasuda.mp4 -->
      <div class="video-placeholder"></div>
    </div>
    
    <div class="header-content">
      <!-- Логотип -->
      <div class="logo">
        <NuxtLink to="/" class="logo-link">
          <img src="/assets/floksbox лого.png" alt="Floksbox" class="logo-image" />
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
        <a href="tel:+1234567890" class="contact-phone">+7 (123) 456-78-90</a>
        <a href="mailto:floksbox@mail.ru" class="contact-email">floksbox@mail.ru</a>
      </div>
    </div>
  </header>
</template>

<script setup>
// Логика для видео будет добавлена после получения файла
</script>

<style lang="scss" scoped>
.header {
  position: relative;
  width: 100%;
  height: auto;
  z-index: 10;
}

.header-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  
  .video-placeholder {
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  }
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 40px;
  position: relative;
  z-index: 1;
}

// Логотип
.logo {
  .logo-link {
    display: block;
    transition: opacity 1s ease;
    
    &:hover {
      opacity: 0.05;
    }
  }
  
  .logo-image {
    height: 60px;
    width: auto;
  }
}

// Навигация
.navigation {
  .nav-list {
    display: flex;
    list-style: none;
    gap: 40px;
  }
  
  .nav-item {
    position: relative;
  }
  
  .nav-link {
    display: block;
    padding: 10px 15px;
    color: #000000;
    text-decoration: none;
    font-weight: 500;
    position: relative;
    border-radius: 5px;
    transition: color 1s ease, background-color 0.1s ease;
    
    &:hover {
      color: #47009f;
      background-color: rgba(71, 0, 159, 0.1);
    }
    
    &::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: rgba(71, 0, 159, 0.1);
      border-radius: 5px;
      opacity: 0;
      transition: opacity 0.1s ease;
      z-index: -1;
    }
    
    &:hover::before {
      opacity: 1;
    }
  }
}

// Контакты
.contacts {
  display: flex;
  flex-direction: column;
  gap: 10px;
  
  .contact-phone,
  .contact-email {
    color: #000000;
    text-decoration: none;
    transition: color 1s ease;
    
    &:hover {
      color: #47009f;
    }
  }
}

// Адаптивность
@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    gap: 20px;
    padding: 15px 20px;
  }
  
  .navigation .nav-list {
    gap: 20px;
  }
  
  .contacts {
    align-items: center;
  }
}
</style> 