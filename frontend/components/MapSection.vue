<template>
  <section class="map-section">
    <div class="map-container">
      <!-- Заголовок секции -->
      <div class="map-header">
        <div class="map-header-content">
          <h2 class="map-title">Как нас найти</h2>
          <p class="map-subtitle">Мы находимся в удобном месте с хорошей транспортной доступностью</p>
        </div>
      </div>

      <!-- Контейнер с картой и контактной информацией -->
      <div class="map-content">
        <!-- Яндекс карта -->
        <div class="map-wrapper">
          <div class="yandex-map">
            <iframe 
              src="https://yandex.ru/map-widget/v1/org/floksboks/182640389494/?ll=37.009835%2C55.593991&z=16" 
              width="100%" 
              height="100%" 
              frameborder="0" 
              allowfullscreen="true"
              loading="lazy"
            ></iframe>
          </div>
        </div>

        <!-- Контактная информация -->
        <div class="contact-info">
          <div class="contact-card">
            <h3 class="contact-title">Контактная информация</h3>
            
            <div class="contact-items">
              <div class="contact-item">
                <div class="contact-icon">
                  <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
                  </svg>
                </div>
                <div class="contact-details">
                  <h4>Адрес</h4>
                  <p>г. Москва, ул. Промышленная, д. 123</p>
                </div>
              </div>

              <div class="contact-item">
                <div class="contact-icon">
                  <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/>
                  </svg>
                </div>
                <div class="contact-details">
                  <h4>Телефон</h4>
                  <p><a href="tel:+79602543323">+7 (960) 254-33-23</a></p>
                </div>
              </div>

              <div class="contact-item">
                <div class="contact-icon">
                  <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.89 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
                  </svg>
                </div>
                <div class="contact-details">
                  <h4>Email</h4>
                  <p><a href="mailto:info@floksbox.ru">info@floksbox.ru</a></p>
                </div>
              </div>

              <div class="contact-item">
                <div class="contact-icon">
                  <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/>
                  </svg>
                </div>
                <div class="contact-details">
                  <h4>Время работы</h4>
                  <p>Пн-Вс: 9:00 - 19:00</p>
                </div>
              </div>
            </div>

            <!-- Кнопка для построения маршрута -->
            <div class="route-button">
              <a href="https://yandex.ru/maps/?rtext=~55.593991,37.009835" target="_blank" class="btn-route">
                <svg viewBox="0 0 24 24" fill="currentColor">
                  <path d="M21.71 11.29l-9-9c-.39-.39-1.02-.39-1.41 0l-9 9c-.39.39-.39 1.02 0 1.41l9 9c.39.39 1.02.39 1.41 0l9-9c.39-.39.39-1.02 0-1.41zM14 14.5V12h-4v3H8l4-4 4 4h-2z"/>
                </svg>
                Построить маршрут
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
// Компонент карты не требует дополнительной логики
</script>

<style lang="scss" scoped>
@use 'sass:color';
@use '~/assets/styles/variables.scss' as vars;

.map-section {
  background: transparent;
  padding: 80px 0;
  position: relative;
}

.map-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
}

.map-header {
  text-align: center;
  margin-bottom: 50px;
}

.map-title {
  font-size: 36px;
  font-weight: 700;
  color: vars.$color-black;
  margin-bottom: 16px;
  line-height: 1.2;
}

.map-subtitle {
  font-size: 18px;
  color: #666666;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.5;
}

.map-content {
  display: grid;
  grid-template-columns: 1fr 400px;
  gap: 40px;
  align-items: start;
}

.map-wrapper {
  border-radius: vars.$border-radius-large;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  background: rgba(248, 249, 250, 0.9);
}

.yandex-map {
  width: 100%;
  height: 500px;
  min-height: 400px;
  
  iframe {
    border-radius: vars.$border-radius-large;
  }
}

.contact-info {
  position: sticky;
  top: 100px;
}

.contact-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: vars.$border-radius-large;
  padding: 32px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  border: 1px solid #e5e7eb;
}

.contact-title {
  font-size: 24px;
  font-weight: 700;
  color: vars.$color-black;
  margin-bottom: 24px;
  text-align: center;
}

.contact-items {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 32px;
}

.contact-item {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 16px;
  border-radius: vars.$border-radius-medium;
  transition: all vars.$transition-medium;
  
  &:hover {
    background: rgba(71, 0, 159, 0.05);
    transform: translateX(5px);
  }
}

.contact-icon {
  width: 48px;
  height: 48px;
  background: rgba(71, 0, 159, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: vars.$color-primary;
  flex-shrink: 0;
  
  svg {
    width: 24px;
    height: 24px;
  }
}

.contact-details {
  flex: 1;
  
  h4 {
    font-size: 16px;
    font-weight: 600;
    color: vars.$color-black;
    margin-bottom: 4px;
  }
  
  p {
    font-size: 14px;
    color: #666666;
    margin: 0;
    line-height: 1.4;
    
    a {
      color: inherit;
      text-decoration: none;
      transition: color vars.$transition-medium;
      
      &:hover {
        color: vars.$color-primary;
      }
    }
  }
}

.route-button {
  text-align: center;
}

.btn-route {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  background: vars.$color-primary;
  color: vars.$color-white;
  text-decoration: none;
  border-radius: vars.$border-radius-medium;
  font-weight: 600;
  font-size: 14px;
  transition: all vars.$transition-medium;
  
  &:hover {
    background: color.scale(vars.$color-primary, $lightness: -10%);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(71, 0, 159, 0.3);
  }
  
  svg {
    width: 18px;
    height: 18px;
  }
}

// Адаптивность
@media (max-width: 1024px) {
  .map-content {
    grid-template-columns: 1fr;
    gap: 30px;
  }
  
  .contact-info {
    position: static;
  }
}

@media (max-width: 768px) {
  .map-section {
    padding: 60px 0;
  }
  
  .map-container {
    padding: 0 20px;
  }
  
  .map-header {
    margin-bottom: 40px;
  }
  
  .map-title {
    font-size: 28px;
    margin-bottom: 12px;
  }
  
  .map-subtitle {
    font-size: 16px;
  }
  
  .yandex-map {
    height: 400px;
  }
  
  .contact-card {
    padding: 24px;
  }
  
  .contact-title {
    font-size: 20px;
    margin-bottom: 20px;
  }
  
  .contact-item {
    padding: 12px;
  }
  
  .contact-icon {
    width: 40px;
    height: 40px;
    
    svg {
      width: 20px;
      height: 20px;
    }
  }
}

@media (max-width: 480px) {
  .map-section {
    padding: 40px 0;
  }
  
  .map-container {
    padding: 0 15px;
  }
  
  .map-title {
    font-size: 24px;
  }
  
  .map-subtitle {
    font-size: 14px;
  }
  
  .yandex-map {
    height: 300px;
  }
  
  .contact-card {
    padding: 20px;
  }
  
  .contact-title {
    font-size: 18px;
  }
  
  .contact-items {
    gap: 16px;
    margin-bottom: 24px;
  }
  
  .contact-item {
    padding: 8px;
    flex-direction: column;
    text-align: center;
    gap: 12px;
  }
  
  .contact-details {
    h4 {
      font-size: 14px;
    }
    
    p {
      font-size: 13px;
    }
  }
  
  .btn-route {
    font-size: 13px;
    padding: 10px 20px;
  }
}
</style>

