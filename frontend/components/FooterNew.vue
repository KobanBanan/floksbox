<template>
  <footer class="footer-new">
    <div class="footer-content">
      <!-- Левая сторона - Навигационные ссылки -->
      <div class="footer-left">
        <div class="footer-links">
          <h3 class="footer-title">Навигация</h3>
          <ul class="links-list">
            <li><NuxtLink to="/" class="footer-link">Главная</NuxtLink></li>
            <li><NuxtLink to="/catalog" class="footer-link">Каталог</NuxtLink></li>
            <li><NuxtLink to="/about" class="footer-link">О компании</NuxtLink></li>
            <li><NuxtLink to="/delivery" class="footer-link">Доставка</NuxtLink></li>
            <li><NuxtLink to="/contacts" class="footer-link">Контакты</NuxtLink></li>
          </ul>
        </div>
        
        <div class="footer-services">
          <h3 class="footer-title">Услуги</h3>
          <ul class="links-list">
            <li><NuxtLink to="/packaging" class="footer-link">Упаковка</NuxtLink></li>
            <li><NuxtLink to="/design" class="footer-link">Дизайн</NuxtLink></li>
            <li><NuxtLink to="/branding" class="footer-link">Брендинг</NuxtLink></li>
            <li><NuxtLink to="/consultation" class="footer-link">Консультация</NuxtLink></li>
          </ul>
        </div>
      </div>

      <!-- Правая сторона - Логотип и соцсети -->
      <div class="footer-right">
        <div class="footer-brand">
          <div class="logo-container">
            <img 
              src="/assets/logo/floksbox лого.png" 
              alt="Floksbox Logo" 
              class="footer-logo"
            />
          </div>
          
          <p class="footer-tagline">
            Упакуем ваш бизнес профессионально
          </p>
          
          <div class="social-links">
            <h4 class="social-title">Мы в соцсетях</h4>
            <div class="social-icons">
              <a href="mailto:info@floksbox.ru" class="social-link" aria-label="Email">
                <img src="/assets/icons/p_email.png" alt="Email" class="social-icon" />
              </a>
              
              <a href="https://t.me/floksbox" target="_blank" class="social-link" aria-label="Telegram">
                <img src="/assets/icons/p_tg.png" alt="Telegram" class="social-icon" />
              </a>
              
              <a href="https://wa.me/79602543323" target="_blank" class="social-link" aria-label="WhatsApp">
                <img src="/assets/icons/p_wa.png" alt="WhatsApp" class="social-icon" />
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Нижняя строка с копирайтом -->
    <div class="footer-bottom">
      <div class="footer-bottom-content">
        <p class="copyright">
          © {{ currentYear }} Floksbox. Все права защищены.
        </p>
        <div class="footer-legal">
          <NuxtLink to="/privacy" class="legal-link">Политика конфиденциальности</NuxtLink>
          <NuxtLink to="/terms" class="legal-link">Условия использования</NuxtLink>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref, computed } from 'vue'

// Получаем текущий год для копирайта
const currentYear = computed(() => new Date().getFullYear())
</script>

<style lang="scss" scoped>
@use '~/assets/styles/variables.scss' as vars;

.footer-new {
  background: #e0ebff;
  color: vars.$color-black;
  padding: 60px 0 0 0;
  margin-top: auto;
  border-top: 1px solid #e5e7eb;
  position: relative;
  overflow: visible;
  
  &::before {
    content: '';
    position: absolute;
    top: -120px;
    left: 0;
    right: 0;
    height: 120px;
    background: url('/assets/images/wave.png') no-repeat center center;
    background-size: 100% 100%;
    pointer-events: none;
    z-index: 1;
  }
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 32px 48px;
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 40px;
  align-items: flex-start;
}

.footer-left {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 28px;
}

.footer-title {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 16px;
  color: vars.$color-black;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.links-list {
  list-style: none;
  padding: 0;
  margin: 0;
  
  li {
    margin-bottom: 10px;
  }
}

.footer-link {
  color: #666666;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: all vars.$transition-medium;
  border-radius: vars.$border-radius-small;
  padding: 6px 8px;
  margin: -6px -8px;
  display: inline-block;
  
  &:hover {
    color: vars.$color-primary;
    background-color: rgba(71, 0, 159, 0.1);
    transform: translateX(5px);
  }
}

.footer-right {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 12px;
}

.logo-container {
  margin-bottom: 20px;
}

.footer-logo {
  max-width: 180px;
  height: auto;
}

.footer-tagline {
  font-size: 16px;
  color: #666666;
  margin-bottom: 20px;
  font-style: italic;
  max-width: 280px;
  line-height: 1.4;
}

.social-links {
  width: 100%;
}

.social-title {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 14px;
  color: vars.$color-black;
}

.social-icons {
  display: flex;
  justify-content: center;
  gap: 12px;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  background: rgba(71, 0, 159, 0.1);
  border-radius: 50%;
  color: vars.$color-primary;
  text-decoration: none;
  transition: all vars.$transition-medium;
  border: 1px solid rgba(71, 0, 159, 0.2);
  position: relative; // чтобы быть поверх декоративных слоев
  z-index: 2;
  
  &:hover {
    background: rgba(71, 0, 159, 0.2);
    color: vars.$color-primary;
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(71, 0, 159, 0.3);
  }
  
  &:nth-child(1):hover {
    background: #4680c2;
    color: vars.$color-white;
    border-color: #4680c2;
  }
  
  &:nth-child(2):hover {
    background: #0088cc;
    color: vars.$color-white;
    border-color: #0088cc;
  }
  
  &:nth-child(3):hover {
    background: #25d366;
    color: vars.$color-white;
    border-color: #25d366;
  }
  
  &:nth-child(4):hover {
    background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
    color: vars.$color-white;
    border-color: transparent;
  }
}

.social-icon {
  width: 20px;
  height: 20px;
}

.footer-bottom {
  background: #e0ebff;
  margin-top: 32px;
  padding: 20px 0;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}

.footer-bottom-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 32px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.copyright {
  color: #666666;
  font-size: 14px;
  margin: 0;
}

.footer-legal {
  display: flex;
  gap: 24px;
}

.legal-link {
  color: #666666;
  text-decoration: none;
  font-size: 14px;
  transition: color vars.$transition-medium;
  padding: 4px 8px;
  border-radius: vars.$border-radius-small;
  
  &:hover {
    color: vars.$color-primary;
    background-color: rgba(71, 0, 159, 0.1);
  }
}

// Адаптивность
@media (max-width: 968px) {
  .footer-content {
    grid-template-columns: 1fr;
    gap: 32px;
    padding: 0 24px 40px;
  }
  
  .footer-left {
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }
  
  .footer-right {
    order: -1;
  }
}

@media (max-width: 768px) {
  .footer-new {
    padding: 40px 0 0 0;
  }
  
  .footer-content {
    gap: 24px;
    padding: 0 20px 32px;
  }
  
  .footer-left {
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }
  
  .footer-title {
    font-size: 16px;
    margin-bottom: 12px;
  }
  
  .footer-logo {
    max-width: 140px;
  }
  
  .footer-tagline {
    font-size: 14px;
    margin-bottom: 16px;
  }
  
  .social-icons {
    gap: 12px;
  }
  
  .social-link {
    width: 40px;
    height: 40px;
  }
  
  .social-icon {
    width: 18px;
    height: 18px;
  }
  
  .footer-bottom-content {
    flex-direction: column;
    gap: 16px;
    text-align: center;
    padding: 0 20px;
  }
  
  .footer-legal {
    gap: 16px;
  }
}

@media (max-width: 480px) {
  .footer-content {
    padding: 0 16px 28px;
  }
  
  .footer-bottom-content {
    padding: 0 16px;
  }
  
  .footer-left {
    gap: 12px;
  }
  
  .footer-title {
    font-size: 14px;
    margin-bottom: 10px;
  }
  
  .footer-link {
    font-size: 13px;
  }
  
  .footer-logo {
    max-width: 130px;
  }
  
  .footer-tagline {
    font-size: 13px;
    margin-bottom: 14px;
  }
  
  .social-title {
    font-size: 14px;
    margin-bottom: 12px;
  }
  
  .social-icons {
    gap: 8px;
  }
  
  .social-link {
    width: 36px;
    height: 36px;
  }
  
  .social-icon {
    width: 16px;
    height: 16px;
  }
  
  .footer-legal {
    flex-direction: column;
    gap: 8px;
  }
  
  .copyright,
  .legal-link {
    font-size: 12px;
  }
}
</style>
