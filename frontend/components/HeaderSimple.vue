<template>
  <header class="header">
    <!-- Video Background -->
    <div class="video-background">
      <!-- Временная заглушка изображением пока нет видео -->
      <img src="/assets/hero/banner1.png" alt="Background" class="background-image" />
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
        <div class="contact-info">
          <div class="contact-phone">
            <span class="contact-label">Контакты</span>
            <a href="tel:+74952345678" class="phone-number">+7 (495) 234-56-78</a>
          </div>
          <a href="mailto:floksbox@mail.ru" class="contact-email">floksbox@mail.ru</a>
        </div>
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
      <div class="modal-header">
        <h3>Остались вопросы? Мы ответим!</h3>
        <p>Напишите нам, задайте вопрос по необходимой упаковке</p>
      </div>
      <form class="request-form" @submit.prevent="submitRequest">
        <div class="form-group">
          <label for="modal-name">Ваше имя</label>
          <input id="modal-name" type="text" v-model="form.name" required />
        </div>
        <div class="form-group">
          <label for="modal-phone">Ваш номер телефона</label>
          <input id="modal-phone" type="tel" v-model="form.phone" required @input="onPhoneInput" placeholder="+7 (___) ___-__-__" maxlength="18" />
        </div>
        <div class="form-group">
          <label for="modal-email">Ваша почта</label>
          <input id="modal-email" type="email" v-model="form.email" required />
        </div>
        <div class="form-group">
          <label for="modal-message">Дополн. средства связи (TG, Whatsapp, VK)</label>
          <textarea id="modal-message" v-model="form.message" required rows="4"></textarea>
        </div>
        <button type="submit" class="submit-btn">ОТПРАВИТЬ</button>
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

const submitRequest = async () => {
  try {
    const response = await $fetch('http://127.0.0.1:8000/api/sent_request/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: form.value.name.trim(),
        phone: form.value.phone.trim(),
        email: form.value.email.trim() || null,
        message: form.value.message.trim() || null
      })
    })
    
    if (response.success) {
      alert('Заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.')
      showModal.value = false
      form.value = { name: '', phone: '', email: '', message: '' }
    } else {
      throw new Error(response.error || 'Ошибка отправки заявки')
    }
  } catch (error) {
    console.error('Error submitting form:', error)
    alert('Произошла ошибка при отправке заявки. Попробуйте позже.')
  }
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

.video-background video,
.video-background .background-image {
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
  align-items: center;
  gap: 15px;
}

.contact-info {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.contact-phone {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.contact-label {
  font-size: 12px;
  color: #666;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.phone-number {
  color: #000000;
  text-decoration: none;
  font-weight: 600;
  font-size: 16px;
  transition: color 0.3s ease;
}

.phone-number:hover {
  color: #47009f;
}

.contact-email {
  color: #000000;
  text-decoration: none;
  font-size: 14px;
  transition: color 0.3s ease;
}

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
    flex-direction: column;
    gap: 10px;
  }
  
  .contact-info {
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
  background: white;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
  padding: 40px;
  min-width: 500px;
  max-width: 95vw;
  position: relative;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  text-align: center;
  margin-bottom: 30px;
}

.modal-header h3 {
  font-size: 28px;
  font-weight: bold;
  color: #6B4C93;
  margin-bottom: 10px;
  line-height: 1.2;
}

.modal-header p {
  font-size: 16px;
  color: #333;
  margin: 0;
}
.request-form {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  font-size: 14px;
  color: #666;
  margin-bottom: 8px;
  font-weight: 500;
}

.form-group input,
.form-group textarea {
  padding: 15px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 16px;
  transition: border-color 0.3s ease;
  font-family: inherit;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #6B4C93;
}

.form-group textarea {
  resize: vertical;
}
.submit-btn {
  background: linear-gradient(135deg, #c8e6c9 0%, #a5d6a7 100%);
  color: #2e7d32;
  border: none;
  padding: 18px 40px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-top: 10px;
}
.submit-btn:hover:not(:disabled) {
  background: linear-gradient(135deg, #a5d6a7 0%, #81c784 100%);
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
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