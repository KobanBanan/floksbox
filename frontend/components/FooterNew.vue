<template>
  <footer class="footer-new">
    <div class="footer-content">
      <!-- Левая сторона - Навигационные ссылки -->
      <div class="footer-left">
        <div class="footer-links">
          <h3 class="footer-title">Навигация</h3>
          <ul class="links-list">
            <li><a href="/" class="footer-link">Главная</a></li>
            <li><a href="/catalog" class="footer-link">Каталог</a></li>
            <li><a href="/about" class="footer-link">О компании</a></li>
            <li><a href="/delivery" class="footer-link">Доставка</a></li>
            <li><a href="/contacts" class="footer-link">Контакты</a></li>
          </ul>
        </div>
        
        <div class="footer-services">
          <h3 class="footer-title">Услуги</h3>
          <ul class="links-list">
            <li><a href="/packaging" class="footer-link">Упаковка</a></li>
            <li><a href="/design" class="footer-link">Дизайн</a></li>
            <li><a href="/branding" class="footer-link">Брендинг</a></li>
            <li><a href="/consultation" class="footer-link">Консультация</a></li>
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
              <a href="#" class="social-link" aria-label="ВКонтакте">
                <svg class="social-icon" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12.785 16.241s.288-.032.436-.194c.136-.148.132-.427.132-.427s-.02-1.307.587-1.5c.6-.19 1.369.864 2.184 1.248.615.291 1.082.227 1.082.227l2.175-.03s1.139-.071.599-.966c-.044-.073-.314-.662-1.612-1.87-1.361-1.264-1.179-.106.461-3.248.999-1.914 1.398-3.084 1.272-3.584-.12-.477-.857-.351-.857-.351l-2.45.015s-.181-.025-.315.056c-.131.079-.215.263-.215.263s-.387 1.031-.903 1.909c-1.087 1.849-1.521 1.947-1.699 1.832-.413-.267-.31-1.073-.31-1.645 0-1.79.271-2.537-.529-2.729-.265-.064-.46-.106-1.138-.113-.87-.009-1.605.003-2.021.206-.277.135-.49.437-.36.454.161.021.526.099.72.362.251.341.242 1.108.242 1.108s.144 2.108-.336 2.372c-.331.182-.785-.189-1.758-1.873-.498-.848-.875-1.785-.875-1.785s-.072-.177-.201-.272c-.157-.115-.377-.151-.377-.151l-2.327.015s-.349.01-.477.161c-.114.135-.009.413-.009.413s1.816 4.25 3.873 6.393c1.886 1.963 4.025 1.834 4.025 1.834z"/>
                </svg>
              </a>
              
              <a href="#" class="social-link" aria-label="Telegram">
                <svg class="social-icon" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 0C5.374 0 0 5.373 0 12s5.374 12 12 12 12-5.373 12-12S18.626 0 12 0zm5.568 8.16c-.169 1.958-.896 6.728-.896 6.728-.302 1.572-.893 1.726-1.492 1.726-.636 0-1.369-.279-1.929-.78-.5-.447-5.017-3.171-5.017-3.171-.636-.447-.571-.894 0-1.342 0 0 4.085-3.642 4.63-4.132.113-.102-.024-.153-.168-.051-.738.522-5.188 3.428-5.188 3.428s-.57.362-1.64.362c-.413 0-.846-.131-1.238-.337-.98-.516-2.207-1.191-2.207-1.191s-.82-.513.579-.78c.744-.142 6.797-2.754 9.001-3.686.848-.36 1.782-.428 1.782.645z"/>
                </svg>
              </a>
              
              <a href="#" class="social-link" aria-label="WhatsApp">
                <svg class="social-icon" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.893 3.486"/>
                </svg>
              </a>
              
              <a href="#" class="social-link" aria-label="Instagram">
                <svg class="social-icon" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                </svg>
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
          <a href="/privacy" class="legal-link">Политика конфиденциальности</a>
          <a href="/terms" class="legal-link">Условия использования</a>
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
@import '~/assets/styles/variables.scss';

.footer-new {
  background: #e0ebff;
  color: $color-black;
  padding: 60px 0 0 0;
  margin-top: auto;
  border-top: 1px solid #e5e7eb;
  position: relative;
  overflow: visible;
  
  &::before {
    content: '';
    position: absolute;
    top: -100px;
    left: 0;
    right: 0;
    height: 100px;
    background: rgba(224, 235, 255, 0.8) url('/assets/images/wave.png') no-repeat center bottom;
    background-size: 120% auto;
    pointer-events: none;
    z-index: 1;
  }
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: start;
}

.footer-left {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
}

.footer-title {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 24px;
  color: $color-black;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.links-list {
  list-style: none;
  padding: 0;
  margin: 0;
  
  li {
    margin-bottom: 12px;
  }
}

.footer-link {
  color: #666666;
  text-decoration: none;
  font-size: 16px;
  font-weight: 500;
  transition: all $transition-medium;
  border-radius: $border-radius-small;
  padding: 8px 12px;
  margin: -8px -12px;
  display: inline-block;
  
  &:hover {
    color: $color-primary;
    background-color: rgba(71, 0, 159, 0.1);
    transform: translateX(5px);
  }
}

.footer-right {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.logo-container {
  margin-bottom: 20px;
}

.footer-logo {
  max-width: 200px;
  height: auto;
}

.footer-tagline {
  font-size: 18px;
  color: #666666;
  margin-bottom: 32px;
  font-style: italic;
  max-width: 280px;
  line-height: 1.4;
}

.social-links {
  width: 100%;
}

.social-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 20px;
  color: $color-black;
}

.social-icons {
  display: flex;
  justify-content: center;
  gap: 16px;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  background: rgba(71, 0, 159, 0.1);
  border-radius: 50%;
  color: $color-primary;
  text-decoration: none;
  transition: all $transition-medium;
  border: 1px solid rgba(71, 0, 159, 0.2);
  
  &:hover {
    background: rgba(71, 0, 159, 0.2);
    color: $color-primary;
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(71, 0, 159, 0.3);
  }
  
  &:nth-child(1):hover {
    background: #4680c2;
    color: $color-white;
    border-color: #4680c2;
  }
  
  &:nth-child(2):hover {
    background: #0088cc;
    color: $color-white;
    border-color: #0088cc;
  }
  
  &:nth-child(3):hover {
    background: #25d366;
    color: $color-white;
    border-color: #25d366;
  }
  
  &:nth-child(4):hover {
    background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
    color: $color-white;
    border-color: transparent;
  }
}

.social-icon {
  width: 24px;
  height: 24px;
}

.footer-bottom {
  background: #f8f9fa;
  margin-top: 48px;
  padding: 24px 0;
  border-top: 1px solid #e5e7eb;
}

.footer-bottom-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
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
  transition: color $transition-medium;
  padding: 4px 8px;
  border-radius: $border-radius-small;
  
  &:hover {
    color: $color-primary;
    background-color: rgba(71, 0, 159, 0.1);
  }
}

// Адаптивность
@media (max-width: 968px) {
  .footer-content {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  
  .footer-left {
    grid-template-columns: 1fr 1fr;
    gap: 30px;
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
    gap: 32px;
    padding: 0 20px;
  }
  
  .footer-left {
    grid-template-columns: 1fr;
    gap: 24px;
  }
  
  .footer-title {
    font-size: 18px;
    margin-bottom: 16px;
  }
  
  .footer-logo {
    max-width: 160px;
  }
  
  .footer-tagline {
    font-size: 16px;
    margin-bottom: 24px;
  }
  
  .social-icons {
    gap: 12px;
  }
  
  .social-link {
    width: 44px;
    height: 44px;
  }
  
  .social-icon {
    width: 20px;
    height: 20px;
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
    padding: 0 20px;
  }
  
  .footer-bottom-content {
    padding: 0 20px;
  }
  
  .footer-left {
    gap: 20px;
  }
  
  .footer-title {
    font-size: 16px;
    margin-bottom: 12px;
  }
  
  .footer-link {
    font-size: 14px;
  }
  
  .footer-logo {
    max-width: 140px;
  }
  
  .footer-tagline {
    font-size: 14px;
    margin-bottom: 20px;
  }
  
  .social-title {
    font-size: 16px;
    margin-bottom: 16px;
  }
  
  .social-icons {
    gap: 10px;
  }
  
  .social-link {
    width: 40px;
    height: 40px;
  }
  
  .social-icon {
    width: 18px;
    height: 18px;
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
