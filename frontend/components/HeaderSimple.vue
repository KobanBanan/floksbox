<template>
  <header class="header">
    <div class="header-content">
      <!-- Логотип с изображением -->
      <div class="logo">
        <a href="/" class="logo-link">
          <img src="/assets/logo/floksbox лого.png" alt="Floksbox" class="logo-image" />
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
              <span class="icon-email">📧</span>
            </a>
            <a href="https://t.me/floksbox" class="contact-icon" title="Telegram" target="_blank">
              <span class="icon-telegram">📱</span>
            </a>
            <a href="https://wa.me/79602543323" class="contact-icon" title="WhatsApp" target="_blank">
              <span class="icon-whatsapp">💬</span>
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
  background: white;
  border-bottom: 1px solid #e5e7eb;
  padding: 20px 40px;
  position: relative;
  z-index: 10;
}

.header-content {
  width: 100%;
  display: flex;
  align-items: flex-end;
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
  gap: 20px;
  align-items: flex-end;
  margin: 0;
  padding: 0;
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
  color: #000000;
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
  color: #666;
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

/* Адаптивность */
@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    gap: 20px;
    padding: 15px 20px;
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
}







</style> 