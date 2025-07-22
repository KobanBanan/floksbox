<template>
  <header class="header">
    <!-- Video Background -->
    <div class="video-background">
      <video autoplay muted loop playsinline>
        <source src="/assets/hero/tudasuda.mp4" type="video/mp4">
      </video>
    </div>
    
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
        <a href="tel:+74952345678" class="contact-phone">+7 (495) 234-56-78</a>
        <a href="mailto:floksbox@mail.ru" class="contact-email">floksbox@mail.ru</a>
        <!-- Иконки соцсетей -->
        <div class="social-icons">
          <a href="#" class="social-link">📧</a>
          <a href="#" class="social-link">📱</a>
          <a href="#" class="social-link">🔍</a>
        </div>
      </div>
      <button class="request-btn" @click="showModal = true">Оставить заявку</button>
    </div>
  </header>

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
          <input type="tel" v-model="form.phone" required @input="onPhoneInput" placeholder="+7 (___) ___-__-__" maxlength="18" />
        </label>
        <label>
          <span>Email</span>
          <input type="email" v-model="form.email" required />
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
const showModal = ref(false)
const form = ref({ name: '', phone: '', email: '', message: '' })

function formatPhone(value) {
  // Оставляем только цифры
  let digits = value.replace(/\D/g, '')
  if (digits.startsWith('8')) digits = '7' + digits.slice(1)
  if (!digits.startsWith('7')) digits = '7' + digits
  let result = '+7'
  if (digits.length > 1) result += ' (' + digits.slice(1, 4)
  if (digits.length >= 4) result += ') ' + digits.slice(4, 7)
  if (digits.length >= 7) result += '-' + digits.slice(7, 9)
  if (digits.length >= 9) result += '-' + digits.slice(9, 11)
  return result
}

function onPhoneInput(e) {
  form.value.phone = formatPhone(e.target.value)
}

function submitRequest() {
  // Здесь будет логика отправки формы
  showModal.value = false
  form.value = { name: '', phone: '', email: '', message: '' }
}
</script>

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
.request-btn {
  margin-left: 30px;
  padding: 12px 28px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #fff;
  font-size: 1.1rem;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s, transform 0.2s;
  box-shadow: 0 2px 8px rgba(71,0,159,0.08);
}
.request-btn:hover {
  background: linear-gradient(135deg, #47009f 0%, #764ba2 100%);
  transform: translateY(-2px) scale(1.04);
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
</style> 