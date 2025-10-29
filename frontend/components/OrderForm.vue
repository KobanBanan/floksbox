<template>
  <section id="order-form" class="order-form-section">
    <div class="container">
      <div class="form-wrapper">
        <!-- СНАЧАЛА текст -->
        <div class="form-content">
          <div class="form-header">
            <h2>Остались вопросы?<br/>Мы ответим!</h2>
            <p>Напишите нам, задайте вопрос по необходимой упаковке</p>
            <p class="response-info">
              Ответ придет вам на указанный контакты.
            </p>
            <p class="contact-info">
              В обращении укажите как удобнее с вами связаться: Whatsapp, Telegram, по e-mail или телефонным звонком.
            </p>
            <p class="working-hours">
              Отвечаем с 9 до 18, в случае срочности просим обращаться по телефону
            </p>
            <a href="tel:+79602543323" class="phone">+7 (960) 254-33-23</a>
          </div>
        </div>
        
        <!-- ПОТОМ форма -->
        <div class="form-container">
          <form @submit.prevent="submitForm" class="order-form">
            <div class="form-group">
              <label for="name">Ваше имя</label>
              <input 
                id="name"
                v-model="form.name" 
                type="text" 
                placeholder=""
                :class="{ 'error': errors.name }"
                @blur="validateName"
                required
              />
              <span v-if="errors.name" class="error-message">{{ errors.name }}</span>
            </div>

            <div class="form-group">
              <label for="phone">Ваш номер телефона</label>
              <input 
                id="phone"
                v-model="form.phone" 
                type="tel" 
                placeholder="+7 123 456 7890"
                :class="{ 'error': errors.phone }"
                @input="formatPhone"
                @blur="validatePhone"
              />
              <span v-if="errors.phone" class="error-message">{{ errors.phone }}</span>
            </div>

            <div class="form-group">
              <label for="email">Ваша почта</label>
              <input 
                id="email"
                v-model="form.email" 
                type="email" 
                placeholder="example@gmail.com"
                :class="{ 'error': errors.email }"
                @blur="validateEmail"
              />
              <span v-if="errors.email" class="error-message">{{ errors.email }}</span>
            </div>

            <div class="form-group">
              <label for="message">Дополн. средства связи (TG, Whatsapp, VK)</label>
              <input 
                id="message"
                v-model="form.socialContact" 
                type="text"
                placeholder="Укажите ваш никнейм или ссылку"
                :class="{ 'error': errors.socialContact }"
                @blur="validateSocialContact"
              />
              <span v-if="errors.socialContact" class="error-message">{{ errors.socialContact }}</span>
            </div>

            <div class="form-group">
              <label for="question">Опишите ваш вопрос</label>
              <textarea 
                id="question"
                v-model="form.question" 
                placeholder="Расскажите подробнее о вашем вопросе или требованиях"
                rows="4"
                :class="{ 'error': errors.question }"
                @blur="validateQuestion"
                required
              ></textarea>
              <span v-if="errors.question" class="error-message">{{ errors.question }}</span>
            </div>

            <div class="form-group checkbox-group">
              <label class="checkbox-label">
                <input 
                  type="checkbox" 
                  v-model="form.agreement"
                  :class="{ 'error': errors.agreement }"
                  required
                />
                <span class="checkmark"></span>
                <span class="checkbox-text">
                  Нажимая на кнопку вы даете согласие на обработку 
                  ваших персональных данных в соответствии с 
                  <a href="#" class="privacy-link">политикой конфиденциальности</a>. 
                  Данные не подлежат распространению в соответствии с ФЗ 152.
                </span>
              </label>
              <span v-if="errors.agreement" class="error-message">{{ errors.agreement }}</span>
            </div>

            <button 
              type="submit" 
              class="submit-btn"
              :disabled="loading || !canSubmit"
            >
              {{ loading ? 'Отправляем...' : 'ОТПРАВИТЬ' }}
            </button>
          </form>
        </div>
      </div>
    </div>

    <!-- Success Modal -->
    <div v-if="showSuccess" class="modal-overlay" @click="closeSuccess">
      <div class="modal-content" @click.stop>
        <div class="success-icon">✓</div>
        <h3>Заявка отправлена!</h3>
        <p>Мы свяжемся с вами в ближайшее время.</p>
        <button @click="closeSuccess" class="modal-btn">Закрыть</button>
      </div>
    </div>

    <!-- Error Modal -->
    <div v-if="showError" class="modal-overlay" @click="closeError">
      <div class="modal-content error" @click.stop>
        <div class="error-icon">✕</div>
        <h3>Ошибка отправки</h3>
        <p>{{ errorMessage }}</p>
        <button @click="closeError" class="modal-btn">Закрыть</button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive, computed, onMounted, watch } from 'vue'

// Props для автозаполнения формы
const props = defineProps({
  prefilledMessage: {
    type: String,
    default: ''
  }
})

const form = reactive({
  name: '',
  phone: '',
  email: '',
  socialContact: '',
  question: '',
  agreement: false
})

const errors = reactive({})
const loading = ref(false)
const showSuccess = ref(false)
const showError = ref(false)
const errorMessage = ref('')

// Функции для работы с localStorage
const saveUserData = () => {
  if (process.client) {
    const userData = {
      name: form.name,
      phone: form.phone,
      email: form.email,
      socialContact: form.socialContact
    }
    localStorage.setItem('floksbox_user_data', JSON.stringify(userData))
  }
}

const loadUserData = () => {
  if (process.client) {
    try {
      const savedData = localStorage.getItem('floksbox_user_data')
      if (savedData) {
        const userData = JSON.parse(savedData)
        form.name = userData.name || ''
        form.phone = userData.phone || ''
        form.email = userData.email || ''
        form.socialContact = userData.socialContact || ''
      }
    } catch (error) {
      console.error('Ошибка загрузки данных пользователя:', error)
    }
  }
}

// Следим за изменениями в полях пользователя и сохраняем их
watch([() => form.name, () => form.phone, () => form.email, () => form.socialContact], () => {
  saveUserData()
}, { deep: true })

// Загружаем данные при монтировании и устанавливаем предзаполненное сообщение
onMounted(() => {
  loadUserData()
  if (props.prefilledMessage) {
    form.question = props.prefilledMessage
  }
})

// Следим за изменениями в prefilledMessage
watch(() => props.prefilledMessage, (newMessage) => {
  if (newMessage) {
    form.question = newMessage
  }
})

const canSubmit = computed(() => {
  return form.name.trim() && 
         form.question.trim().length >= 3 && 
         (form.phone.trim() || form.email.trim() || form.socialContact.trim()) &&
         form.agreement &&
         Object.keys(errors).length === 0
})

const validateName = () => {
  if (!form.name.trim()) {
    errors.name = 'Поле "Имя" обязательно для заполнения'
  } else {
    delete errors.name
  }
}

const formatPhone = (event) => {
  let value = event.target.value.replace(/\D/g, '')
  
  if (!value.startsWith('7') && value.length > 0) {
    if (value.startsWith('8')) {
      value = '7' + value.slice(1)
    } else {
      value = '7' + value
    }
  }
  
  let formatted = ''
  if (value.length > 0) {
    formatted = '+7'
    if (value.length > 1) {
      formatted += ' ' + value.slice(1, 4)
    }
    if (value.length > 4) {
      formatted += ' ' + value.slice(4, 7)
    }
    if (value.length > 7) {
      formatted += ' ' + value.slice(7, 11)
    }
  }
  
  form.phone = formatted
  validatePhone()
}

const validatePhone = () => {
  if (form.phone.trim()) {
    const phoneDigits = form.phone.replace(/\D/g, '')
    if (phoneDigits.length !== 11 || !phoneDigits.startsWith('7')) {
      errors.phone = 'Номер телефона должен содержать 10 цифр после +7'
    } else {
      delete errors.phone
    }
  } else {
    delete errors.phone
  }
}

const validateEmail = () => {
  if (form.email.trim()) {
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
    if (!emailRegex.test(form.email)) {
      errors.email = 'Введите корректный email (example@gmail.com)'
    } else {
      delete errors.email
    }
  } else {
    delete errors.email
  }
}

const validateSocialContact = () => {
  // Поле не обязательное, но если заполнено, должно содержать хотя бы 2 символа
  if (form.socialContact.trim() && form.socialContact.trim().length < 2) {
    errors.socialContact = 'Укажите корректный никнейм или ссылку'
  } else {
    delete errors.socialContact
  }
}

const validateQuestion = () => {
  if (!form.question.trim()) {
    errors.question = 'Поле "Вопрос" обязательно для заполнения'
  } else if (form.question.trim().length < 3) {
    errors.question = 'Вопрос должен содержать минимум 3 символа'
  } else {
    delete errors.question
  }
}

const validateContactFields = () => {
  const hasPhone = form.phone.trim() && !errors.phone
  const hasEmail = form.email.trim() && !errors.email
  const hasSocial = form.socialContact.trim() && !errors.socialContact
  
  if (!hasPhone && !hasEmail && !hasSocial) {
    if (!form.phone.trim() && !form.email.trim() && !form.socialContact.trim()) {
      errors.contact = 'Укажите хотя бы один способ связи: телефон, email или социальную сеть'
    }
  } else {
    delete errors.contact
  }
}

const validateForm = () => {
  validateName()
  validatePhone()
  validateEmail()
  validateSocialContact()
  validateQuestion()
  validateContactFields()
  
  if (!form.agreement) {
    errors.agreement = 'Необходимо согласие на обработку данных'
  } else {
    delete errors.agreement
  }
  
  return Object.keys(errors).length === 0
}

const submitForm = async () => {
  if (!validateForm()) return
  
  loading.value = true
  
  try {
    const config = useRuntimeConfig()
    const apiBase = (config.public.apiBase || '').replace(/\/+$/, '')
    const url = `${apiBase}/api/sent_request/`
    const response = await $fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: form.name.trim(),
        phone: form.phone.trim() || null,
        email: form.email.trim() || null,
        message: `Дополнительная связь: ${form.socialContact.trim() || 'Не указано'}\n\nВопрос: ${form.question.trim()}`
      })
    })
    
    if (response.success) {
      showSuccess.value = true
      // Очищаем форму
      Object.keys(form).forEach(key => {
        if (typeof form[key] === 'boolean') {
          form[key] = false
        } else {
          form[key] = ''
        }
      })
      // Очищаем ошибки
      Object.keys(errors).forEach(key => delete errors[key])
    } else {
      throw new Error(response.error || 'Ошибка отправки заявки')
    }
  } catch (error) {
    console.error('Error submitting form:', error)
    errorMessage.value = error.message || 'Произошла ошибка при отправке заявки'
    showError.value = true
  } finally {
    loading.value = false
  }
}

const closeSuccess = () => {
  showSuccess.value = false
}

const closeError = () => {
  showError.value = false
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Days+One&display=swap');

.order-form-section {
  background: transparent;
  padding: 120px 0;
  min-height: 800px;
}

.container {
  max-width: 1200px; /* единая ширина для всех компонентов */
  margin: 0 auto;
  padding: 0 20px; /* внутренние отступы */
}

.form-wrapper {
  display: grid;
  grid-template-columns: 2fr 1.3fr;
  gap: 40px;
  align-items: flex-start;
}

.form-header {
  padding-right: 50px;
}

.form-header h2 {
  font-family: 'Days One', cursive;
  font-size: 56px;
  font-weight: normal;
  color: #6B3F8C;
  line-height: 1.2;
  margin-bottom: 25px;
}

.form-header p {
  font-family: 'Montserrat', sans-serif;
  font-weight: 300;
  font-size: 16px;
  color: #333;
  margin-bottom: 18px;
  line-height: 1.5;
}

.response-info {
  margin-top: 30px !important; /* возвращено к исходному размеру */
}

.contact-info {
  margin-top: 20px !important; /* возвращено к исходному размеру */
}

.working-hours {
  margin-top: 30px !important; /* возвращено к исходному размеру */
  font-weight: 400;
}

.phone {
  font-family: 'Montserrat', sans-serif;
  font-size: 32px !important;
  font-weight: 600 !important;
  color: #6B3F8C !important;
  margin-top: 35px !important;
  text-decoration: none;
  display: inline-block;
  transition: color 0.3s ease;
}

.phone:hover {
  color: #5a3e7c !important;
}

.form-container {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  padding: 20px;
  overflow: hidden;
  /* Добавить эффект свечения */
  box-shadow: 
    0 0 0 2px rgba(255, 255, 255, 0.3), /* белая обводка */
    0 0 15px rgba(196, 255, 97, 0.3), /* салатовое свечение */
    0 5px 20px rgba(0, 0, 0, 0.08); /* обычная тень */
  
  /* Альтернативный вариант с градиентной рамкой */
  position: relative;
  background: linear-gradient(white, white) padding-box,
              linear-gradient(135deg, rgba(255,255,255,0.8) 0%, rgba(196,255,97,0.2) 100%) border-box;
  border: 2px solid transparent; /* уменьшено с 3px */
}

.order-form {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 0; /* убрать дополнительный отступ */
}

.form-group label {
  font-family: 'Montserrat', sans-serif;
  font-size: 14px;
  font-weight: 500;
  color: #333;
  margin-bottom: 6px;
}

.form-group input,
.form-group textarea {
  font-family: 'Montserrat', sans-serif;
  font-weight: 300;
  border-radius: 8px;
  background: #FAFAFA;
  border: 1px solid #E8E8E8;
  padding: 12px 16px;
  font-size: 14px;
  transition: border-color 0.3s ease;
}

.form-group textarea {
  min-height: 80px;
  resize: vertical;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #6B4C93;
}

.form-group input.error,
.form-group textarea.error {
  border-color: #ff4444;
  color: #ff4444;
}

.error-message {
  color: #ff4444;
  font-family: 'Montserrat', sans-serif;
  font-weight: 300;
  font-size: 12px;
  margin-top: 4px;
}

.checkbox-group {
  margin-top: 8px;
}

.checkbox-label {
  display: flex;
  align-items: flex-start;
  cursor: pointer;
  font-family: 'Montserrat', sans-serif;
  font-weight: 300;
  font-size: 12px;
  line-height: 1.4;
}

.checkbox-label input[type="checkbox"] {
  display: none;
}

.checkmark {
  width: 16px;
  height: 16px;
  border: 2px solid #e0e0e0;
  border-radius: 4px;
  margin-right: 8px;
  margin-top: 2px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  transition: all 0.3s ease;
}

.checkbox-label input[type="checkbox"]:checked + .checkmark {
  background-color: #6B4C93;
  border-color: #6B4C93;
}

.checkbox-label input[type="checkbox"]:checked + .checkmark::after {
  content: '✓';
  color: white;
  font-size: 10px;
  font-weight: bold;
}

.checkbox-text {
  color: #666;
  flex: 1;
}

.privacy-link {
  color: #6B4C93;
  text-decoration: underline;
}

.submit-btn {
  background: #B8FF00 !important;
  color: #333 !important;
  border-radius: 8px;
  font-weight: 700;
  box-shadow: 0 2px 8px rgba(184, 255, 0, 0.3);
  padding: 14px 20px;
  width: 100%;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  border: none;
  font-family: 'Montserrat', sans-serif;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 12px;
}

.submit-btn:hover:not(:disabled) {
  background: #A8EF00 !important;
  transform: translateY(-1px);
  box-shadow: 0 3px 10px rgba(184, 255, 0, 0.4);
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
  background: #ccc;
  color: #666;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 8px; /* уменьшено с 15px */
  padding: 20px; /* уменьшено с 40px */
  text-align: center;
  max-width: 250px; /* уменьшено с 400px */
  margin: 10px; /* уменьшено с 20px */
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2); /* уменьшено */
}

.modal-content.error {
  border-left: 5px solid #ff4444;
}

.success-icon {
  width: 30px; /* уменьшено с 60px */
  height: 30px; /* уменьшено с 60px */
  border-radius: 50%;
  background: #4caf50;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px; /* уменьшено с 30px */
  margin: 0 auto 10px; /* уменьшено с 20px */
}

.error-icon {
  width: 30px; /* уменьшено с 60px */
  height: 30px; /* уменьшено с 60px */
  border-radius: 50%;
  background: #ff4444;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px; /* уменьшено с 30px */
  margin: 0 auto 10px; /* уменьшено с 20px */
}

.modal-content h3 {
  margin-bottom: 8px; /* уменьшено с 15px */
  color: #333;
  font-family: 'Montserrat', sans-serif;
  font-size: 14px; /* добавлен маленький размер */
}

.modal-content p {
  margin-bottom: 12px; /* уменьшено с 25px */
  color: #666;
  line-height: 1.5;
  font-family: 'Montserrat', sans-serif;
  font-size: 10px; /* уменьшено с 14px */
}

.modal-btn {
  background: #6B4C93;
  color: white;
  border: none;
  padding: 6px 15px; /* уменьшено с 12px 30px */
  border-radius: 4px; /* уменьшено с 8px */
  cursor: pointer;
  font-family: 'Montserrat', sans-serif;
  font-size: 10px; /* уменьшено с 12px */
  font-weight: 500;
  transition: background 0.3s ease;
}

.modal-btn:hover {
  background: #5a3e7c;
}

/* Responsive Design */
@media (max-width: 768px) {
  .container {
    max-width: 95%;
    padding: 0 10px; /* добавлено */
  }
  
  .form-wrapper {
    grid-template-columns: 1fr;
    gap: 15px; /* уменьшено с 40px */
  }
  
  .form-header {
    padding-right: 0;
    text-align: center;
  }
  
  .form-header h2 {
    font-size: 24px; /* возвращено к среднему размеру для планшетов */
  }
  
  .form-container {
    padding: 12px 8px; /* уменьшено с 30px 20px */
  }
  
  .order-form-section {
    padding: 15px 0; /* уменьшено с 40px */
  }
}

@media (max-width: 480px) {
  .form-header h2 {
    font-size: 20px; /* возвращено к нормальному размеру для мобильных */
  }
  
  .form-container {
    padding: 10px 6px; /* уменьшено с 25px 15px */
  }
  
  .modal-content {
    margin: 5px; /* уменьшено с 10px */
    padding: 15px 10px; /* уменьшено с 30px 20px */
  }
  
  .form-header p {
    font-size: 11px; /* увеличено для читаемости */
  }
  
  .phone {
    font-size: 18px !important; /* увеличено для читаемости */
  }
}
</style> 