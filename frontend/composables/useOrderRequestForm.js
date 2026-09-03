import { ref, reactive, computed, onMounted, watch } from 'vue'

export function useOrderRequestForm(prefilledMessageRef) {
  const form = reactive({
    name: '',
    phone: '',
    email: '',
    socialContact: '',
    question: '',
    agreement: false,
  })

  const errors = reactive({})
  const loading = ref(false)
  const showSuccess = ref(false)
  const showError = ref(false)
  const errorMessage = ref('')

  const saveUserData = () => {
    if (!import.meta.client) return
    const userData = {
      name: form.name,
      phone: form.phone,
      email: form.email,
      socialContact: form.socialContact,
    }
    localStorage.setItem('floksbox_user_data', JSON.stringify(userData))
  }

  const loadUserData = () => {
    if (!import.meta.client) return
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

  const applyPrefill = (message) => {
    if (message) {
      form.question = message
    }
  }

  watch(
    [() => form.name, () => form.phone, () => form.email, () => form.socialContact],
    () => saveUserData(),
    { deep: true },
  )

  if (prefilledMessageRef) {
    watch(
      prefilledMessageRef,
      (msg) => applyPrefill(msg),
      { immediate: true },
    )
  }

  onMounted(() => {
    loadUserData()
    if (prefilledMessageRef?.value) {
      applyPrefill(prefilledMessageRef.value)
    }
  })

  const canSubmit = computed(
    () =>
      form.name.trim() &&
      form.question.trim().length >= 3 &&
      (form.phone.trim() || form.email.trim() || form.socialContact.trim()) &&
      form.agreement &&
      Object.keys(errors).length === 0,
  )

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
      value = value.startsWith('8') ? '7' + value.slice(1) : '7' + value
    }
    let formatted = ''
    if (value.length > 0) {
      formatted = '+7'
      if (value.length > 1) formatted += ' ' + value.slice(1, 4)
      if (value.length > 4) formatted += ' ' + value.slice(4, 7)
      if (value.length > 7) formatted += ' ' + value.slice(7, 11)
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
        errors.contact =
          'Укажите хотя бы один способ связи: телефон, email или социальную сеть'
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

  const resetFormFields = () => {
    form.name = ''
    form.phone = ''
    form.email = ''
    form.socialContact = ''
    form.question = ''
    form.agreement = false
    Object.keys(errors).forEach((key) => delete errors[key])
  }

  const submitForm = async () => {
    if (!validateForm()) return

    loading.value = true
    try {
      const config = useRuntimeConfig()
      const apiBase = (config.public.apiBase || '').replace(/\/+$/, '')
      const response = await $fetch(`${apiBase}/api/sent_request/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: form.name.trim(),
          phone: form.phone.trim() || null,
          email: form.email.trim() || null,
          message: `Дополнительная связь: ${form.socialContact.trim() || 'Не указано'}\n\nВопрос: ${form.question.trim()}`,
          source: import.meta.client ? window.location.pathname : '',
        }),
      })

      if (response.success) {
        const { trackLead } = useYandexEcommerce()
        trackLead(form.question.trim())
        showSuccess.value = true
        resetFormFields()
        loadUserData()
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

  return {
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
  }
}
