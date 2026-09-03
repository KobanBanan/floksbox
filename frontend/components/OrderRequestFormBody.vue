<template>
  <div class="order-form-body" :class="{ 'order-form-body--modal': variant === 'modal' }">
    <form class="order-form" @submit.prevent="submitForm">
      <div class="form-group">
        <label for="order-name">Ваше имя</label>
        <input
          id="order-name"
          v-model="form.name"
          type="text"
          :class="{ error: errors.name }"
          @blur="validateName"
          required
        />
        <span v-if="errors.name" class="error-message">{{ errors.name }}</span>
      </div>

      <div class="form-group">
        <label for="order-phone">Ваш номер телефона</label>
        <input
          id="order-phone"
          v-model="form.phone"
          type="tel"
          placeholder="+7 123 456 7890"
          :class="{ error: errors.phone }"
          @input="formatPhone"
          @blur="validatePhone"
        />
        <span v-if="errors.phone" class="error-message">{{ errors.phone }}</span>
      </div>

      <div class="form-group">
        <label for="order-email">Ваша почта</label>
        <input
          id="order-email"
          v-model="form.email"
          type="email"
          placeholder="example@gmail.com"
          :class="{ error: errors.email }"
          @blur="validateEmail"
        />
        <span v-if="errors.email" class="error-message">{{ errors.email }}</span>
      </div>

      <div class="form-group">
        <label for="order-social">Дополн. средства связи (TG, Whatsapp, VK)</label>
        <input
          id="order-social"
          v-model="form.socialContact"
          type="text"
          placeholder="Укажите ваш никнейм или ссылку"
          :class="{ error: errors.socialContact }"
          @blur="validateSocialContact"
        />
        <span v-if="errors.socialContact" class="error-message">{{ errors.socialContact }}</span>
      </div>

      <div class="form-group">
        <label for="order-question">Опишите ваш вопрос</label>
        <textarea
          id="order-question"
          v-model="form.question"
          placeholder="Расскажите подробнее о вашем вопросе или требованиях"
          rows="4"
          :class="{ error: errors.question }"
          @blur="validateQuestion"
          required
        />
        <span v-if="errors.question" class="error-message">{{ errors.question }}</span>
      </div>

      <div v-if="errors.contact" class="error-message contact-error">{{ errors.contact }}</div>

      <div class="form-group checkbox-group">
        <label class="checkbox-label">
          <input v-model="form.agreement" type="checkbox" :class="{ error: errors.agreement }" required />
          <span class="checkmark" />
          <span class="checkbox-text">
            Нажимая на кнопку вы даете согласие на обработку ваших персональных данных в соответствии с
            <a href="#" class="privacy-link">политикой конфиденциальности</a>.
            Данные не подлежат распространению в соответствии с ФЗ 152.
          </span>
        </label>
        <span v-if="errors.agreement" class="error-message">{{ errors.agreement }}</span>
      </div>

      <button type="submit" class="submit-btn" :disabled="loading || !canSubmit">
        {{ loading ? 'Отправляем...' : 'ОТПРАВИТЬ' }}
      </button>
    </form>

    <div v-if="showSuccess" class="status-overlay" @click="handleCloseSuccess">
      <div class="status-card" @click.stop>
        <div class="success-icon">✓</div>
        <h3>Заявка отправлена!</h3>
        <p>Мы свяжемся с вами в ближайшее время.</p>
        <button type="button" class="status-btn" @click="handleCloseSuccess">Закрыть</button>
      </div>
    </div>

    <div v-if="showError" class="status-overlay" @click="closeError">
      <div class="status-card error" @click.stop>
        <div class="error-icon">✕</div>
        <h3>Ошибка отправки</h3>
        <p>{{ errorMessage }}</p>
        <button type="button" class="status-btn" @click="closeError">Закрыть</button>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  prefilledMessage: {
    type: String,
    default: '',
  },
  variant: {
    type: String,
    default: 'section',
  },
  closeOnSuccess: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['sent'])

const prefilledRef = toRef(props, 'prefilledMessage')

const {
  form,
  errors,
  loading,
  showSuccess,
  showError,
  errorMessage,
  canSubmit,
  formatPhone,
  validateName,
  validatePhone,
  validateEmail,
  validateSocialContact,
  validateQuestion,
  submitForm,
  closeSuccess,
  closeError,
  applyPrefill,
  loadUserData,
} = useOrderRequestForm(prefilledRef)

watch(
  () => props.prefilledMessage,
  (msg) => {
    if (msg) applyPrefill(msg)
  },
)

const handleCloseSuccess = () => {
  closeSuccess()
  if (props.closeOnSuccess) {
    emit('sent')
  }
}
</script>

<style scoped>
.order-form-body {
  width: 100%;
}

.order-form {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.form-group {
  margin-bottom: 16px;
}

.form-group label {
  display: block;
  font-family: 'Montserrat', sans-serif;
  font-weight: 500;
  font-size: 13px;
  color: #333;
  margin-bottom: 6px;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 12px 14px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-family: 'Montserrat', sans-serif;
  font-size: 14px;
  box-sizing: border-box;
  transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #6b4c93;
}

.form-group input.error,
.form-group textarea.error {
  border-color: #ff4444;
}

.error-message {
  color: #ff4444;
  font-size: 12px;
  margin-top: 4px;
  display: block;
  font-family: 'Montserrat', sans-serif;
}

.contact-error {
  margin-bottom: 12px;
}

.checkbox-group {
  margin-bottom: 8px;
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

.checkbox-label input[type='checkbox'] {
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

.checkbox-label input[type='checkbox']:checked + .checkmark {
  background-color: #6b4c93;
  border-color: #6b4c93;
}

.checkbox-label input[type='checkbox']:checked + .checkmark::after {
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
  color: #6b4c93;
  text-decoration: underline;
}

.submit-btn {
  background: #b8ff00 !important;
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
  margin-top: 4px;
}

.submit-btn:hover:not(:disabled) {
  background: #a8ef00 !important;
  transform: translateY(-1px);
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.status-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10001;
}

.status-card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  text-align: center;
  max-width: 320px;
  margin: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.status-card.error {
  border-left: 5px solid #ff4444;
}

.success-icon,
.error-icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 12px;
  font-size: 20px;
  font-weight: bold;
}

.success-icon {
  background: #4caf50;
  color: white;
}

.error-icon {
  background: #ff4444;
  color: white;
}

.status-card h3 {
  font-family: 'Montserrat', sans-serif;
  margin-bottom: 8px;
}

.status-card p {
  font-family: 'Montserrat', sans-serif;
  font-size: 14px;
  color: #666;
  margin-bottom: 16px;
}

.status-btn {
  background: #6b4c93;
  color: white;
  border: none;
  padding: 10px 24px;
  border-radius: 8px;
  cursor: pointer;
  font-family: 'Montserrat', sans-serif;
}
</style>
