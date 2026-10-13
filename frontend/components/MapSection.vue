<template>
  <section class="map-section">
    <div class="map-stage">
      <iframe
        class="map-frame"
        src="https://yandex.ru/map-widget/v1/org/floksboks/182640389494/?ll=36.9965%2C55.593991&z=16"
        title="Карта Floksbox"
        allowfullscreen
        loading="lazy"
      ></iframe>

      <aside class="contact-card">
        <h2 class="contact-title">Как нас найти</h2>
        <p class="contact-subtitle">Удобный заезд и хорошая транспортная доступность</p>

        <div class="contact-items">
          <a
            class="contact-link"
            href="https://yandex.ru/maps/org/floksboks/182640389494/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <span class="fancy-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
              </svg>
            </span>
            <span class="contact-copy">
              <span class="contact-label">Адрес</span>
              <span class="contact-value">г. Москва, ул. Промышленная, д. 123</span>
            </span>
          </a>

          <a class="contact-link" href="tel:+79602543323">
            <span class="fancy-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/>
              </svg>
            </span>
            <span class="contact-copy">
              <span class="contact-label">Телефон</span>
              <span class="contact-value">+7 (960) 254-33-23</span>
            </span>
          </a>

          <a class="contact-link" href="mailto:info@floksbox.ru">
            <span class="fancy-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.89 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
              </svg>
            </span>
            <span class="contact-copy">
              <span class="contact-label">Email</span>
              <span class="contact-value">info@floksbox.ru</span>
            </span>
          </a>

          <a
            class="contact-link"
            href="https://yandex.ru/maps/org/floksboks/182640389494/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <span class="fancy-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/>
              </svg>
            </span>
            <span class="contact-copy">
              <span class="contact-label">Время работы</span>
              <span class="contact-value">Пн-Вс: 9:00 - 19:00</span>
            </span>
          </a>
        </div>

        <a
          class="route-btn"
          href="https://yandex.ru/maps/?rtext=~55.593991,37.009835"
          target="_blank"
          rel="noopener noreferrer"
        >
          <span class="fancy-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M21.71 11.29l-9-9c-.39-.39-1.02-.39-1.41 0l-9 9c-.39.39-.39 1.02 0 1.41l9 9c.39.39 1.02.39 1.41 0l9-9c.39-.39.39-1.02 0-1.41zM14 14.5V12h-4v3H8l4-4 4 4h-2z"/>
            </svg>
          </span>
          <span class="route-label">Построить маршрут</span>
        </a>
      </aside>
    </div>
  </section>
</template>

<script setup>
</script>

<style lang="scss" scoped>
$brand: #5e3085;
$map-height: 400px; // было 500px, минус 20%

.map-section {
  position: relative;
  z-index: 2;
  width: 100%;
  background: transparent;
}

.map-stage {
  position: relative;
  width: 100%;
  height: $map-height;
  overflow: hidden;
}

.map-frame {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: 0;
}

.contact-card {
  position: absolute;
  z-index: 2;
  left: 40px;
  top: calc(50% - 12px);
  transform: translateY(-50%);
  width: 400px;
  max-height: calc(100% - 28px);
  box-sizing: border-box;
  padding: 14px 16px 12px;
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.96);
  box-shadow: 0 18px 40px rgba(20, 8, 40, 0.22);
  overflow: auto;
}

.contact-title {
  margin: 0;
  font-family: 'Days One', cursive;
  font-size: 26px;
  font-weight: 400;
  line-height: 1.15;
  color: $brand;
}

.contact-subtitle {
  margin: 2px 0 6px;
  font-family: 'Montserrat', sans-serif;
  font-size: 13px;
  line-height: 1.35;
  color: #666;
}

.contact-items {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.contact-link,
.route-btn {
  text-decoration: none;
  color: inherit;
}

.contact-link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 4px 6px;
  border-radius: 14px;
  transition: background 0.3s ease;

  &:hover,
  &:focus-visible {
    background: rgba(94, 48, 133, 0.06);
    outline: none;
  }
}

.contact-copy {
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.contact-label {
  font-family: 'Montserrat', sans-serif;
  font-size: 13px;
  font-weight: 700;
  color: #1a1a1a;
}

.contact-value {
  font-family: 'Montserrat', sans-serif;
  font-size: 13px;
  line-height: 1.35;
  color: #666;
}

// Эффект #14: круг заливается цветом, иконка переворачивается
.fancy-icon {
  position: relative;
  z-index: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #fff;
  color: $brand;
  box-shadow: 0 6px 14px rgba(94, 48, 133, 0.18);
  overflow: hidden;
  perspective: 400px;

  &::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: inherit;
    background: $brand;
    transform: scale(0);
    transition: transform 0.45s ease;
    z-index: 0;
  }

  svg {
    position: relative;
    z-index: 1;
    width: 18px;
    height: 18px;
    transition: transform 0.55s ease, color 0.35s ease;
  }
}

.contact-link:hover .fancy-icon,
.contact-link:focus-visible .fancy-icon,
.route-btn:hover .fancy-icon,
.route-btn:focus-visible .fancy-icon {
  color: #fff;

  &::before {
    transform: scale(1);
  }

  svg {
    transform: rotateY(360deg);
  }
}

.route-btn {
  position: relative;
  z-index: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  width: 100%;
  margin-top: 8px;
  padding: 6px 14px 6px 6px;
  box-sizing: border-box;
  border-radius: 999px;
  background: #fff;
  color: $brand;
  border: 2px solid $brand;
  overflow: hidden;
  font-family: 'Montserrat', sans-serif;
  font-size: 14px;
  font-weight: 700;

  &::before {
    content: '';
    position: absolute;
    left: 50%;
    top: 50%;
    width: 140%;
    height: 280%;
    border-radius: 50%;
    background: $brand;
    transform: translate(-50%, -50%) scale(0);
    transition: transform 0.45s ease;
    z-index: 0;
  }

  .fancy-icon,
  .route-label {
    position: relative;
    z-index: 1;
  }
}

.route-btn:hover,
.route-btn:focus-visible {
  color: #fff;
  outline: none;

  &::before {
    transform: translate(-50%, -50%) scale(1);
  }
}

@media (max-width: 1024px) {
  .map-stage {
    height: 320px;
  }

  .contact-card {
    left: 20px;
    width: 340px;
  }
}

@media (max-width: 768px) {
  .map-stage {
    height: auto;
  }

  .map-frame {
    position: relative;
    height: 240px;
  }

  .contact-card {
    position: relative;
    left: auto;
    top: auto;
    transform: none;
    width: auto;
    max-height: none;
    margin: 16px 16px 0;
  }
}
</style>
