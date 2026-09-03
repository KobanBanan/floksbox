<template>
  <div class="crm-page">
    <header class="crm-header">
      <button type="button" class="crm-back" @click="router.push('/crm')">← К списку</button>
      <span v-if="order" class="crm-badge" :class="`crm-badge--${order.status}`">{{ order.status_label }}</span>
    </header>

    <section v-if="loading" class="crm-state">Загрузка заявки...</section>
    <section v-else-if="!order" class="crm-state">Заявка не найдена</section>

    <section v-else class="crm-detail">
      <div class="crm-detail-main">
        <h1>#{{ order.id }} · {{ order.name }}</h1>
        <p class="crm-date">Создана: {{ formatDate(order.created_at) }}</p>

        <div class="crm-fields">
          <div class="crm-field">
            <span>Телефон</span>
            <strong>
              <a v-if="order.phone" :href="`tel:${order.phone}`">{{ order.phone }}</a>
              <template v-else>Не указан</template>
            </strong>
          </div>
          <div class="crm-field">
            <span>Email</span>
            <strong>
              <a v-if="order.email" :href="`mailto:${order.email}`">{{ order.email }}</a>
              <template v-else>Не указан</template>
            </strong>
          </div>
          <div class="crm-field">
            <span>Источник</span>
            <strong>{{ order.source || 'Сайт' }}</strong>
          </div>
        </div>

        <div class="crm-message-box">
          <h2>Сообщение клиента</h2>
          <p>{{ order.message || 'Без сообщения' }}</p>
        </div>
      </div>

      <aside class="crm-sidebar">
        <h2>Обработка</h2>

        <label>
          <span>Статус</span>
          <select v-model="form.status">
            <option value="new">Новая</option>
            <option value="in_progress">В работе</option>
            <option value="completed">Завершена</option>
            <option value="cancelled">Отменена</option>
          </select>
        </label>

        <label>
          <span>Заметки менеджера</span>
          <textarea v-model="form.manager_notes" rows="8" placeholder="Комментарий для команды..." />
        </label>

        <p v-if="saveError" class="crm-error">{{ saveError }}</p>
        <p v-if="saveSuccess" class="crm-success">Сохранено</p>

        <button type="button" :disabled="saving" @click="saveOrder">
          {{ saving ? 'Сохранение...' : 'Сохранить' }}
        </button>
      </aside>
    </section>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'crm',
  middleware: 'crm-auth',
})

const route = useRoute()
const router = useRouter()
const { fetchOrder, updateOrder } = useCrm()

const order = ref(null)
const loading = ref(true)
const saving = ref(false)
const saveError = ref('')
const saveSuccess = ref(false)

const form = reactive({
  status: 'new',
  manager_notes: '',
})

const loadOrder = async () => {
  loading.value = true
  try {
    const data = await fetchOrder(route.params.id)
    order.value = data
    form.status = data.status
    form.manager_notes = data.manager_notes || ''
  } catch (error) {
    console.error(error)
    order.value = null
  } finally {
    loading.value = false
  }
}

const saveOrder = async () => {
  saving.value = true
  saveError.value = ''
  saveSuccess.value = false
  try {
    const updated = await updateOrder(route.params.id, {
      status: form.status,
      manager_notes: form.manager_notes,
    })
    order.value = updated
    saveSuccess.value = true
    setTimeout(() => {
      saveSuccess.value = false
    }, 2000)
  } catch (error) {
    saveError.value = error?.data?.error || 'Не удалось сохранить изменения'
  } finally {
    saving.value = false
  }
}

const formatDate = (value) => {
  if (!value) return ''
  return new Date(value).toLocaleString('ru-RU')
}

onMounted(loadOrder)

useHead({
  title: computed(() => (order.value ? `Заявка #${order.value.id} — Floksbox CRM` : 'Заявка — Floksbox CRM')),
})
</script>

<style scoped>
.crm-page {
  max-width: 1100px;
  margin: 0 auto;
  padding: 28px 20px 48px;
}

.crm-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.crm-back {
  border: none;
  background: transparent;
  color: #5e3085;
  font: inherit;
  font-weight: 600;
  cursor: pointer;
}

.crm-detail {
  display: grid;
  grid-template-columns: 1.4fr 0.8fr;
  gap: 20px;
}

.crm-detail-main,
.crm-sidebar {
  background: #fff;
  border-radius: 20px;
  padding: 24px;
  box-shadow: 0 8px 24px rgba(94, 48, 133, 0.06);
}

.crm-detail-main h1 {
  margin: 0;
  font-family: 'Days One', cursive;
  color: #5e3085;
  font-size: 1.8rem;
}

.crm-date {
  margin: 8px 0 20px;
  color: #9ca3af;
}

.crm-fields {
  display: grid;
  gap: 12px;
  margin-bottom: 24px;
}

.crm-field {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.crm-field span {
  color: #9ca3af;
  font-size: 0.85rem;
}

.crm-field a {
  color: #5e3085;
  text-decoration: none;
}

.crm-message-box h2,
.crm-sidebar h2 {
  margin: 0 0 12px;
  font-size: 1rem;
}

.crm-message-box p {
  margin: 0;
  white-space: pre-wrap;
  line-height: 1.6;
}

.crm-sidebar {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.crm-sidebar label {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.crm-sidebar select,
.crm-sidebar textarea {
  border: 1px solid #d8cfe6;
  border-radius: 12px;
  padding: 12px 14px;
  font: inherit;
}

.crm-sidebar button {
  border: none;
  border-radius: 12px;
  padding: 14px 16px;
  background: #5e3085;
  color: #fff;
  font: inherit;
  font-weight: 600;
  cursor: pointer;
}

.crm-sidebar button:disabled {
  opacity: 0.7;
}

.crm-state {
  padding: 40px 0;
  text-align: center;
  color: #6b7280;
}

.crm-error {
  margin: 0;
  color: #b42318;
}

.crm-success {
  margin: 0;
  color: #15803d;
}

.crm-badge {
  border-radius: 999px;
  padding: 4px 10px;
  font-size: 0.8rem;
  font-weight: 600;
}

.crm-badge--new { background: #ede9fe; color: #5b21b6; }
.crm-badge--in_progress { background: #fef3c7; color: #b45309; }
.crm-badge--completed { background: #dcfce7; color: #15803d; }
.crm-badge--cancelled { background: #fee2e2; color: #b91c1c; }

@media (max-width: 900px) {
  .crm-detail {
    grid-template-columns: 1fr;
  }
}
</style>
