<template>
  <footer class="footer-new">
    <div class="footer-content">
      <div class="footer-brand">
        <NuxtLink to="/" class="logo-link" aria-label="Floksbox">
          <img
            src="/assets/logo/floksbox лого.png"
            alt="Floksbox"
            class="footer-logo"
          />
        </NuxtLink>
        <p class="footer-tagline">Упакуем ваш бизнес</p>
        <p class="footer-note">Производство упаковки из гофрокартона: от коробки до печати.</p>
      </div>

      <div class="footer-col footer-col--catalog">
        <h3 class="footer-title">Каталог</h3>
        <ul class="footer-catalog">
          <li v-for="item in categories" :key="item.route">
            <NuxtLink :to="item.route" class="footer-link">{{ item.name }}</NuxtLink>
          </li>
        </ul>
      </div>

      <div class="footer-col">
        <h3 class="footer-title">Компания</h3>
        <ul class="links-list">
          <li><NuxtLink to="/" class="footer-link">Главная</NuxtLink></li>
          <li><NuxtLink to="/catalog" class="footer-link">Каталог</NuxtLink></li>
          <li><NuxtLink to="/prices" class="footer-link">Цены</NuxtLink></li>
          <li><NuxtLink to="/promotions" class="footer-link">Доставка</NuxtLink></li>
          <li><NuxtLink to="/fefco" class="footer-link">Каталог FEFCO</NuxtLink></li>
          <li><NuxtLink to="/contacts" class="footer-link">Контакты</NuxtLink></li>
        </ul>
      </div>

      <div class="footer-col footer-contacts">
        <h3 class="footer-title">Контакты</h3>
        <a class="contact-line" href="tel:+79602543323">+7 (960) 254-33-23</a>
        <a class="contact-line" href="mailto:info@floksbox.ru">info@floksbox.ru</a>
        <p class="contact-meta">г. Москва, ул. Промышленная, д. 123</p>
        <p class="contact-meta">Пн–Вс: 9:00–19:00</p>
        <div class="social-icons">
          <a href="mailto:info@floksbox.ru" class="social-link" aria-label="Email">
            <img src="/assets/icons/p_email.png" alt="" class="social-icon" />
          </a>
          <a href="https://t.me/floksbox" target="_blank" rel="noopener" class="social-link" aria-label="Telegram">
            <img src="/assets/icons/p_tg.png" alt="" class="social-icon" />
          </a>
          <a href="https://wa.me/79602543323" target="_blank" rel="noopener" class="social-link" aria-label="WhatsApp">
            <img src="/assets/icons/p_wa.png" alt="" class="social-icon" />
          </a>
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <p class="copyright">© {{ currentYear }} Floksbox. Все права защищены.</p>
    </div>
  </footer>
</template>

<script setup>
import { computed } from 'vue'
import { catalogMenuItems } from '../composables/useCatalogMenuItems'

const currentYear = computed(() => new Date().getFullYear())

const categories = catalogMenuItems
  .filter((item) => item.route !== '/fefco')
  .map((item) => ({
    route: item.route,
    name: item.name.replace(/<br\s*\/?>/gi, ' ').replace(/&nbsp;/g, ' ').replace(/\s+/g, ' ').trim(),
  }))
</script>

<style lang="scss" scoped>
.footer-new {
  background: #e0ebff;
  color: #1c1c1c;
  margin-top: auto;
  position: relative;
  overflow: visible;
  font-family: 'Montserrat', Arial, sans-serif;

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
  padding: 36px 24px 28px;
  display: grid;
  grid-template-columns: 1.05fr 1.35fr 0.75fr 1.05fr;
  gap: 32px 28px;
  align-items: start;
}

.footer-brand {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 8px;
}

.logo-link {
  display: inline-flex;
}

.footer-logo {
  width: 148px;
  height: auto;
}

.footer-tagline {
  margin: 4px 0 0;
  font-family: 'Days One', cursive;
  font-size: 18px;
  line-height: 1.25;
  color: #5e3085;
}

.footer-note {
  margin: 0;
  max-width: 240px;
  font-size: 14px;
  line-height: 1.45;
  color: #4d5566;
}

.footer-title {
  margin: 0 0 12px;
  font-family: 'Days One', cursive;
  font-size: 16px;
  font-weight: 400;
  letter-spacing: 0.02em;
  color: #5e3085;
}

.links-list,
.footer-catalog {
  list-style: none;
  margin: 0;
  padding: 0;
}

.footer-catalog {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 14px;
}

.links-list li {
  margin: 0 0 6px;
}

.footer-link {
  color: #2c3340;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  line-height: 1.35;
}

.footer-link:hover {
  color: #47009f;
}

.footer-contacts {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 6px;
}

.contact-line {
  color: #1c1c1c;
  font-size: 15px;
  font-weight: 700;
  text-decoration: none;
  line-height: 1.35;
}

.contact-line:hover {
  color: #47009f;
}

.contact-meta {
  margin: 0;
  font-size: 14px;
  line-height: 1.4;
  color: #4d5566;
}

.social-icons {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #fff;
  border: 1px solid rgba(94, 48, 133, 0.18);
  text-decoration: none;
}

.social-link:hover {
  background: #f4ffe8;
  border-color: #b8ff00;
}

.social-icon {
  width: 20px;
  height: 20px;
  object-fit: contain;
}

.footer-bottom {
  border-top: 1px solid rgba(94, 48, 133, 0.14);
  padding: 14px 24px 18px;
}

.copyright {
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
  color: #5c6575;
  font-size: 13px;
}

@media (max-width: 992px) {
  .footer-content {
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
    gap: 28px 20px;
    padding: 28px 18px 22px;
  }

  .footer-brand,
  .footer-col--catalog {
    grid-column: 1 / -1;
  }
}

@media (max-width: 640px) {
  .footer-new::before {
    top: -40px;
    height: 40px;
  }

  .footer-content {
    padding: 22px 16px 18px;
    gap: 22px 12px;
  }

  .footer-logo {
    width: 132px;
  }

  .footer-link,
  .contact-line {
    display: inline-flex;
    padding: 3px 0;
  }
}
</style>
