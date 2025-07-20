<template>
  <header class="header">
    <!-- Video Background -->
    <div class="video-background">
      <video autoplay muted loop playsinline>
        <source src="/assets/images/tudasuda.mp4" type="video/mp4">
      </video>
    </div>
    
    <div class="header-content">
      <!-- Логотип с изображением -->
      <div class="logo">
        <a href="/" class="logo-link">
          <img src="/assets/images/floksbox лого.png" alt="Floksbox" class="logo-image" />
        </a>
      </div>
      
      <!-- Навигационное меню -->
      <nav class="navigation">
        <ul class="nav-list">
          <li class="nav-item">
            <a href="/" class="nav-link">Главная</a>
          </li>
          <li class="nav-item">
            <a href="/catalog" class="nav-link">Каталог</a>
          </li>
          <li class="nav-item">
            <a href="/promotions" class="nav-link">Акции</a>
          </li>
          <li class="nav-item">
            <a href="/prices" class="nav-link">Цены</a>
          </li>
          <li class="nav-item">
            <a href="/contacts" class="nav-link">Контакты</a>
          </li>
        </ul>
      </nav>
      
      <!-- Контактная информация -->
      <div class="contacts">
        <a href="tel:+74952345678" class="contact-phone">+7 (495) 234-56-78</a>
        <a href="mailto:floksbox@mail.ru" class="contact-email">floksbox@mail.ru</a>
        <!-- Иконки соцсетей -->
        <div class="social-icons">
          <a href="#" class="social-link">📧</a>
          <a href="#" class="social-link">📱</a>
          <a href="#" class="social-link">🔍</a>
        </div>
      </div>
    </div>
  </header>
</template>

<style scoped>
.header {
  background: white;
  border-bottom: 1px solid #e5e7eb;
  padding: 20px 0;
  position: relative;
  z-index: 10;
  overflow: hidden;
}

.video-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}

.video-background video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.3;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
  z-index: 2;
}

/* Логотип */
.logo .logo-link {
  display: block;
  transition: opacity 1s ease;
}

.logo .logo-link:hover {
  opacity: 0.05;
}

.logo .logo-image {
  height: 60px;
  width: auto;
}

/* Навигация */
.navigation .nav-list {
  display: flex;
  list-style: none;
  gap: 40px;
}

.navigation .nav-item {
  position: relative;
}

.navigation .nav-link {
  display: block;
  padding: 10px 15px;
  color: #000000;
  text-decoration: none;
  font-weight: 500;
  position: relative;
  border-radius: 5px;
  transition: color 1s ease, background-color 0.1s ease;
}

.navigation .nav-link:hover {
  color: #47009f;
  background-color: rgba(71, 0, 159, 0.1);
}

.navigation .nav-link::before {
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

.navigation .nav-link:hover::before {
  opacity: 1;
}

/* Контакты */
.contacts {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.contact-phone,
.contact-email {
  color: #000000;
  text-decoration: none;
  transition: color 1s ease;
}

.contact-phone:hover,
.contact-email:hover {
  color: #47009f;
}

.social-icons {
  display: flex;
  gap: 10px;
  margin-top: 5px;
}

.social-link {
  font-size: 1.2rem;
  text-decoration: none;
  transition: transform 0.2s ease;
}

.social-link:hover {
  transform: scale(1.1);
}

/* Адаптивность */
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

@media (max-width: 480px) {
  .navigation .nav-list {
    flex-wrap: wrap;
    justify-content: center;
    gap: 15px;
  }
  
  .navigation .nav-link {
    padding: 8px 12px;
    font-size: 0.9rem;
  }
}
</style> 