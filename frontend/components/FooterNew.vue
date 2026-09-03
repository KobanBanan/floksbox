<template>
  <footer class="footer-new">
    <div class="footer-content">
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

    <div class="footer-bottom">
      <div class="footer-bottom-content">
        <p class="copyright">
          © {{ currentYear }} Floksbox. Все права защищены.
        </p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { computed } from 'vue'

const currentYear = computed(() => new Date().getFullYear())
</script>

<style lang="scss" scoped>
@use '~/assets/styles/variables.scss' as vars;

.footer-new {
  --footer-font-scale: 1;
  background: #e0ebff;
  color: vars.$color-black;
  padding: 30px 0 0;
  margin-top: auto;
  border-top: 1px solid #e5e7eb;
  position: relative;
  overflow: visible;

  &::before {
    content: '';
    position: absolute;
    top: -60px;
    left: 0;
    right: 0;
    height: 60px;
    background: url('/assets/images/wave.png') no-repeat center center;
    background-size: 100% 100%;
    pointer-events: none;
    z-index: 1;
  }
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 16px 5px;
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 5px;
  align-items: flex-start;
}

.footer-left {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5px;
}

.footer-title {
  font-size: calc(18px * var(--footer-font-scale));
  font-weight: 700;
  margin: 0 0 5px;
  color: vars.$color-black;
  text-transform: uppercase;
  letter-spacing: 0.21px;
}

.links-list {
  list-style: none;
  padding: 0;
  margin: 0;

  li {
    margin: 0;
    padding: 0;
    line-height: 1.2;
  }
}

.footer-link {
  color: #666666;
  text-decoration: none;
  font-size: calc(14px * var(--footer-font-scale));
  font-weight: 500;
  line-height: 1.2;
  transition: color vars.$transition-medium;
  padding: 0;
  margin: 0;
  display: block;

  &:hover {
    color: vars.$color-primary;
  }
}

.footer-right {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 5px;
}

.logo-container {
  margin-bottom: 5px;
}

.footer-logo {
  max-width: 90px;
  height: auto;
}

.footer-tagline {
  font-size: calc(16px * var(--footer-font-scale));
  color: #666666;
  margin: 0 0 5px;
  font-style: italic;
  max-width: 140px;
  line-height: 1.35;
}

.social-links {
  width: 100%;
}

.social-title {
  font-size: calc(16px * var(--footer-font-scale));
  font-weight: 600;
  margin: 0 0 5px;
  color: vars.$color-black;
}

.social-icons {
  display: flex;
  justify-content: center;
  gap: 5px;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  background: rgba(71, 0, 159, 0.1);
  border-radius: 50%;
  text-decoration: none;
  transition: all vars.$transition-medium;
  border: 1px solid rgba(71, 0, 159, 0.2);
  position: relative;
  z-index: 2;

  &:hover {
    background: rgba(71, 0, 159, 0.2);
    transform: translateY(-1px);
  }

  &:nth-child(1):hover {
    background: #4680c2;
    border-color: #4680c2;
  }

  &:nth-child(2):hover {
    background: #0088cc;
    border-color: #0088cc;
  }

  &:nth-child(3):hover {
    background: #25d366;
    border-color: #25d366;
  }
}

.social-icon {
  width: 10px;
  height: 10px;
}

.footer-bottom {
  background: #e0ebff;
  margin-top: 5px;
  padding: 10px 0;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}

.footer-bottom-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 16px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.copyright {
  color: #666666;
  font-size: calc(14px * var(--footer-font-scale));
  margin: 0;
  text-align: center;
}

@media (max-width: 968px) {
  .footer-content {
    grid-template-columns: 1fr;
    padding: 0 12px 5px;
  }

  .footer-right {
    order: -1;
  }
}

@media (max-width: 768px) {
  .footer-new {
    padding-top: 20px;

    &::before {
      top: -40px;
      height: 40px;
    }
  }

  .footer-title {
    font-size: calc(16px * var(--footer-font-scale));
  }

  .footer-tagline {
    font-size: calc(14px * var(--footer-font-scale));
  }

  .footer-logo {
    max-width: 70px;
  }

  .footer-bottom-content {
    padding: 0 12px;
  }
}

@media (max-width: 480px) {
  .footer-content {
    padding: 0 8px 5px;
  }

  .footer-bottom-content {
    padding: 0 8px;
  }

  .footer-title {
    font-size: calc(14px * var(--footer-font-scale));
  }

  .footer-link {
    font-size: calc(13px * var(--footer-font-scale));
  }

  .footer-tagline {
    font-size: calc(13px * var(--footer-font-scale));
  }

  .social-title {
    font-size: calc(14px * var(--footer-font-scale));
  }

  .copyright {
    font-size: calc(12px * var(--footer-font-scale));
  }

  .footer-logo {
    max-width: 65px;
  }
}
</style>
