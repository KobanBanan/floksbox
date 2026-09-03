<template>
  <div class="crm-page">
    <header class="crm-header">
      <div>
        <h1>Заявки</h1>
        <p v-if="user">Здравствуйте, {{ user.name }}</p>
      </div>
      <button type="button" class="crm-logout" @click="handleLogout">Выйти</button>
    </header>

    <section class="crm-stats">
      <button
        v-for="item in statusFilters"
        :key="item.value"
        type="button"
        class="crm-stat"
        :class="{ active: activeStatus === item.value }"
        @click="setStatus(item.value)"
      >
        <span class="crm-stat-value">{{ stats[item.value] || 0 }}</span>
        <span class="crm-stat-label">{{ item.label }}</span>
      </button>
    </section>

    <section class="crm-toolbar">
      <input
        v-model="search"
        type="search"
        placeholder="Поиск по имени, телефону, email..."
        @input="debouncedLoad"
      />
      <button type="button" @click="loadOrders">Обновить</button>
    </section>

    <section v-if="loading" class="crm-state">Загрузка заявок...</section>
    <section v-else-if="orders.length === 0" class="crm-state">Заявок пока нет</section>

    <section v-else class="crm-list">
      <article
        v-for="order in orders"
        :key="order.id"
        class="crm-card"
        @click="openOrder(order.id)"
      >
        <div class="crm-card-top">
          <strong>#{{ order.id }} · {{ order.name }}</strong>
          <span class="crm-badge" :class="`crm-badge--${order.status}`">{{ order.status_label }}</span>
        </div>
        <p class="crm-card-contact">
          {{ order.phone || 'Телефон не указан' }}
          <span v-if="order.email"> · {{ order.email }}</span>
        </p>
        <p class="crm-card-message">{{ previewMessage(order.message) }}</p>
        <div class="crm-card-meta">
          <span>{{ formatDate(order.created_at) }}</span>
          <span v-if="order.source">{{ order.source }}</span>
        </div>
      </article>
    </section>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'crm',
  middleware: 'crm-auth',
})

const router = useRouter()
const { user, logout, fetchOrders } = useCrm()

const orders = ref([])
const stats = ref({})
const loading = ref(true)
const search = ref('')
const activeStatus = ref('')

const statusFilters = [
  { value: '', label: 'Все' },
  { value: 'new', label: 'Новые' },
  { value: 'in_progress', label: 'В работе' },
  { value: 'completed', label: 'Завершены' },
  { value: 'cancelled', label: 'Отменены' },
]

let debounceTimer

const loadOrders = async () => {
  loading.value = true
  try {
    const response = await fetchOrders({
      status: activeStatus.value || undefined,
      search: search.value.trim() || undefined,
    })
    orders.value = response.results || []
    stats.value = response.stats || {}
  } catch (error) {
    console.error(error)
    orders.value = []
  } finally {
    loading.value = false
  }
}

const debouncedLoad = () => {
  clearTimeout(debounceTimer)
  debounceTimer = setTimeout(loadOrders, 300)
}

const setStatus = (status) => {
  activeStatus.value = status
  loadOrders()
}

const openOrder = (id) => {
  router.push(`/crm/orders/${id}`)
}

const handleLogout = async () => {
  await logout()
  await router.push('/crm/login')
}

const formatDate = (value) => {
  if (!value) return ''
  return new Date(value).toLocaleString('ru-RU', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  })
}

const previewMessage = (message) => {
  if (!message) return 'Без сообщения'
  return message.length > 140 ? `${message.slice(0, 140)}...` : message
}

onMounted(loadOrders)

useHead({ title: 'Заявки — Floksbox CRM' })
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
  gap: 16px;
  margin-bottom: 24px;
}

.crm-header h1 {
  margin: 0;
  font-family: 'Days One', cursive;
  color: #5e3085;
  font-size: 2rem;
}

.crm-header p {
  margin: 6px 0 0;
  color: #6b7280;
}

.crm-logout {
  border: 1px solid #d8cfe6;
  background: #fff;
  border-radius: 12px;
  padding: 10px 16px;
  cursor: pointer;
  font: inherit;
}

.crm-stats {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 12px;
  margin-bottom: 20px;
}

.crm-stat {
  border: 1px solid #e7ddf2;
  background: #fff;
  border-radius: 16px;
  padding: 14px;
  text-align: left;
  cursor: pointer;
}

.crm-stat.active {
  border-color: #8b4fb8;
  box-shadow: 0 0 0 2px rgba(139, 79, 184, 0.12);
}

.crm-stat-value {
  display: block;
  font-size: 1.4rem;
  font-weight: 700;
  color: #5e3085;
}

.crm-stat-label {
  display: block;
  margin-top: 4px;
  color: #6b7280;
  font-size: 0.85rem;
}

.crm-toolbar {
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
}

.crm-toolbar input {
  flex: 1;
  border: 1px solid #d8cfe6;
  border-radius: 12px;
  padding: 12px 14px;
  font: inherit;
}

.crm-toolbar button {
  border: none;
  border-radius: 12px;
  padding: 0 18px;
  background: #5e3085;
  color: #fff;
  font: inherit;
  cursor: pointer;
}

.crm-state {
  padding: 40px 0;
  text-align: center;
  color: #6b7280;
}

.crm-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.crm-card {
  background: #fff;
  border-radius: 16px;
  padding: 18px 20px;
  box-shadow: 0 8px 24px rgba(94, 48, 133, 0.06);
  cursor: pointer;
  transition: transform 0.2s ease;
}

.crm-card:hover {
  transform: translateY(-2px);
}

.crm-card-top {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: center;
}

.crm-card-contact,
.crm-card-message,
.crm-card-meta {
  margin: 8px 0 0;
  color: #4b5563;
}

.crm-card-message {
  white-space: pre-wrap;
}

.crm-card-meta {
  display: flex;
  gap: 12px;
  font-size: 0.85rem;
  color: #9ca3af;
}

.crm-badge {
  border-radius: 999px;
  padding: 4px 10px;
  font-size: 0.8rem;
  font-weight: 600;
  white-space: nowrap;
}

.crm-badge--new { background: #ede9fe; color: #5b21b6; }
.crm-badge--in_progress { background: #fef3c7; color: #b45309; }
.crm-badge--completed { background: #dcfce7; color: #15803d; }
.crm-badge--cancelled { background: #fee2e2; color: #b91c1c; }

@media (max-width: 900px) {
  .crm-stats {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
</style>
