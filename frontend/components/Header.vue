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
      <!-- Логотип -->
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
            <NuxtLink to="/fefco" class="nav-link">FEFCO</NuxtLink>
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
          <a href="tel:+79602543323" class="contact-phone">+7 (960) 254-33-23</a>
          <a href="mailto:info@floksbox.ru" class="contact-email">info@floksbox.ru</a>
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
      <div class="action-buttons">
        <button class="constructor-btn" @click="showConstructor = true">Конструктор</button>
        <button class="request-btn" @click="showModal = true">Оставить заявку</button>
      </div>
    </div>
  </header>

  <!-- Модальное окно конструктора -->
  <div v-if="showConstructor" class="modal-overlay" @click.self="showConstructor = false">
    <div class="constructor-modal">
      <BoxConstructor @close="showConstructor = false" />
    </div>
  </div>

  <!-- Модальное окно заявки -->
  <div v-if="showModal" class="modal-overlay" @click.self="showModal = false">
    <div class="modal-content">
      <form class="request-form" @submit.prevent="submitRequest">
        <label>
          <span>Ваше имя</span>
          <input type="text" v-model="form.name" required />
        </label>
        <label>
          <span>Ваш телефон</span>
          <input type="tel" v-model="form.phone" required />
        </label>
        <label>
          <span>Опишите ваш запрос</span>
          <textarea v-model="form.message" required></textarea>
        </label>
        <button type="submit" class="submit-btn">Отправить</button>
      </form>
      <button class="close-btn" @click="showModal = false">×</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import BoxConstructor from './BoxConstructor.vue'
const showModal = ref(false)
const showConstructor = ref(false)
const form = ref({ name: '', phone: '', message: '' })
function submitRequest() {
  // Здесь будет логика отправки формы
  showModal.value = false
  form.value = { name: '', phone: '', message: '' }
}
// Видео добавлено в фон шапки
</script>

<style lang="scss" scoped>
.header {
  position: relative;
  width: 100%;
  min-height: 120px; /* минимальная высота для отображения видео */
  z-index: 10;
}

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
  display: flex;
  align-items: flex-end; /* Выравнивание по нижнему краю */
  gap: 0px;
  padding: 30px 40px; /* увеличиваем padding для лучшего отображения видео */
  position: relative;
  z-index: 1;
  font-size: 0; /* Убираем отступы между элементами */
  
  /* Убираем все отступы между flex элементами */
  > * {
    margin: 0;
    padding: 0;
    font-size: 1rem; /* Восстанавливаем размер шрифта для дочерних элементов */
  }
  
  .navigation {
    margin: 0; /* Убираем все отступы навигации */
    padding: 0; /* Убираем все внутренние отступы навигации */
    margin-left: -70px; /* Максимальный отрицательный отступ */
    flex-shrink: 0; /* Предотвращаем сжатие */
    font-size: 1rem; /* Восстанавливаем размер шрифта */
    align-self: flex-end; /* Дополнительное выравнивание навигации по нижнему краю */
  }
  
  .contacts {
    margin-left: auto;
    font-size: 1rem; /* Восстанавливаем размер шрифта */
  }
}

// Логотип
.logo {
  margin: 0; /* Убираем все отступы логотипа */
  padding: 0; /* Убираем все внутренние отступы логотипа */
  
  .logo-link {
    display: block;
    margin: 0; /* Убираем отступы ссылки */
    padding: 0; /* Убираем внутренние отступы ссылки */
  }
  
  .logo-image {
    height: 42px;
    width: auto;
    margin: 0; /* Убираем отступы изображения */
    padding: 0; /* Убираем внутренние отступы изображения */
    display: block; /* Убираем возможные отступы inline элемента */
  }
}

// Навигация
.navigation {
  .nav-list {
    display: flex;
    list-style: none;
    gap: 8px; /* Уменьшенные отступы между пунктами меню */
    margin: 0; /* Убираем стандартные отступы списка */
    padding: 0; /* Убираем стандартные отступы списка */
  }
  
  .nav-item {
    position: relative;
  }
  
  .nav-link {
    display: block;
    padding: 8px 6px; /* Еще более минимальные внутренние отступы */
    color: #000000;
    text-decoration: none;
    font-weight: 500;
    position: relative;
    border-radius: 5px;
    transition: color 1s ease, background-color 0.1s ease;
    
    /* Убираем левый отступ у первого элемента */
    &:first-child {
      padding-left: 0;
    }
    
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
  
  .nav-item:first-child .nav-link {
    padding-left: 0; /* Убираем левый отступ у ссылки "Главная" */
  }
}

// Контакты
.contacts {
  display: flex;
  flex-direction: column;
  gap: 10px;
  
  .contact-info {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .contact-phone,
  .contact-email {
    color: #000000;
    text-decoration: none;
    transition: color 1s ease;
    
    &:hover {
      color: #47009f;
    }
  }
  
  .contact-icons {
    display: flex;
    gap: 8px;
    justify-content: flex-end;
  }
  
  .contact-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.8);
    text-decoration: none;
    transition: all 0.3s ease;
    
    &:hover {
      background: rgba(71, 0, 159, 0.1);
      transform: translateY(-2px);
    }
  }
  
  .contact-icon-img {
    width: 18px;
    height: 18px;
    object-fit: contain;
  }
}

.action-buttons {
  display: flex;
  gap: 15px;
  margin-left: 60px;
}

.constructor-btn,
.request-btn {
  padding: 12px 28px;
  font-size: 1.1rem;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s, transform 0.2s;
  box-shadow: 0 2px 8px rgba(71,0,159,0.08);
}

.constructor-btn {
  background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
  color: #fff;
}

.constructor-btn:hover {
  background: linear-gradient(135deg, #218838 0%, #1ba085 100%);
  transform: translateY(-2px) scale(1.04);
}

.request-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #fff;
}

.request-btn:hover {
  background: linear-gradient(135deg, #47009f 0%, #764ba2 100%);
  transform: translateY(-2px) scale(1.04);
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

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0,0,0,0.45);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}
.modal-content {
  background: #f8f9fa;
  border-radius: 18px;
  box-shadow: 0 8px 32px rgba(71,0,159,0.18);
  padding: 40px 36px 32px 36px;
  min-width: 350px;
  max-width: 95vw;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.request-form {
  display: flex;
  flex-direction: column;
  gap: 22px;
  width: 340px;
  max-width: 80vw;
}
.request-form label {
  display: flex;
  flex-direction: column;
  font-size: 1.2rem;
  color: #222;
  font-weight: 500;
  gap: 7px;
}
.request-form input,
.request-form textarea {
  border: 1.5px solid #bdbdbd;
  border-radius: 7px;
  padding: 10px 12px;
  font-size: 1.1rem;
  font-family: inherit;
  background: #fff;
  resize: none;
}
.request-form textarea {
  min-height: 90px;
  max-height: 200px;
}
.submit-btn {
  margin-top: 18px;
  padding: 12px 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #fff;
  font-size: 1.1rem;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s, transform 0.2s;
}
.submit-btn:hover {
  background: linear-gradient(135deg, #47009f 0%, #764ba2 100%);
  transform: translateY(-2px) scale(1.04);
}
.close-btn {
  position: absolute;
  top: 12px;
  right: 18px;
  background: none;
  border: none;
  font-size: 2.1rem;
  color: #764ba2;
  cursor: pointer;
  transition: color 0.2s;
}
.close-btn:hover {
  color: #47009f;
}

.constructor-modal {
  background: #fff;
  border-radius: 20px;
  max-width: 90vw;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}
</style> 