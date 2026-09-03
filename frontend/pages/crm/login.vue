<template>
  <div class="crm-login-page">
    <div class="crm-login-card">
      <div class="crm-login-brand">
        <h1>Floksbox CRM</h1>
        <p>Приём и обработка заявок с сайта</p>
      </div>

      <form class="crm-login-form" @submit.prevent="handleLogin">
        <label>
          <span>Логин</span>
          <input v-model="username" type="text" autocomplete="username" required />
        </label>

        <label>
          <span>Пароль</span>
          <input v-model="password" type="password" autocomplete="current-password" required />
        </label>

        <p v-if="error" class="crm-error">{{ error }}</p>

        <button type="submit" :disabled="loading">
          {{ loading ? 'Вход...' : 'Войти' }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'crm',
})

const router = useRouter()
const { login, fetchMe } = useCrm()

const username = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')

onMounted(async () => {
  const me = await fetchMe()
  if (me) {
    await router.replace('/crm')
  }
})

const handleLogin = async () => {
  loading.value = true
  error.value = ''
  try {
    const response = await login(username.value.trim(), password.value)
    if (response.success) {
      await router.push('/crm')
      return
    }
    error.value = response.error || 'Не удалось войти'
  } catch (e) {
    error.value = e?.data?.error || 'Неверный логин или пароль'
  } finally {
    loading.value = false
  }
}

useHead({ title: 'Вход — Floksbox CRM' })
</script>

<style scoped>
.crm-login-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.crm-login-card {
  width: 100%;
  max-width: 420px;
  background: #fff;
  border-radius: 20px;
  padding: 32px;
  box-shadow: 0 20px 50px rgba(94, 48, 133, 0.12);
}

.crm-login-brand h1 {
  font-family: 'Days One', cursive;
  font-size: 2rem;
  color: #5e3085;
  margin: 0 0 8px;
}

.crm-login-brand p {
  margin: 0 0 28px;
  color: #6b7280;
}

.crm-login-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.crm-login-form label {
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 0.9rem;
  color: #374151;
}

.crm-login-form input {
  border: 1px solid #d8cfe6;
  border-radius: 12px;
  padding: 12px 14px;
  font: inherit;
}

.crm-login-form input:focus {
  outline: none;
  border-color: #8b4fb8;
  box-shadow: 0 0 0 3px rgba(139, 79, 184, 0.15);
}

.crm-login-form button {
  margin-top: 8px;
  border: none;
  border-radius: 12px;
  padding: 14px 16px;
  background: #5e3085;
  color: #fff;
  font: inherit;
  font-weight: 600;
  cursor: pointer;
}

.crm-login-form button:disabled {
  opacity: 0.7;
  cursor: default;
}

.crm-error {
  margin: 0;
  color: #b42318;
  font-size: 0.9rem;
}
</style>
