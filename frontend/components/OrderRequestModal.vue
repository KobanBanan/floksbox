<template>
  <Teleport to="body">
    <div
      v-if="isOpen"
      class="order-request-overlay"
      role="dialog"
      aria-modal="true"
      aria-labelledby="order-request-title"
      @click.self="closeOrderRequest"
    >
      <div class="order-request-modal">
        <button
          type="button"
          class="order-request-modal__close"
          aria-label="Закрыть"
          @click="closeOrderRequest"
        >
          ×
        </button>

        <h2 id="order-request-title" class="order-request-modal__title">Заявка менеджеру</h2>
        <p class="order-request-modal__subtitle">
          Заполните форму — мы свяжемся с вами удобным способом
        </p>

        <OrderRequestFormBody
          :key="formKey"
          :prefilled-message="prefilledQuestion"
          variant="modal"
          close-on-success
          @sent="onSent"
        />
      </div>
    </div>
  </Teleport>
</template>

<script setup>
const { isOpen, prefilledQuestion, closeOrderRequest } = useOrderRequest()
const formKey = ref(0)

watch(isOpen, (open) => {
  if (open) {
    formKey.value += 1
  }
})

const onSent = () => {
  closeOrderRequest()
}

const onEscape = (e) => {
  if (e.key === 'Escape' && isOpen.value) {
    closeOrderRequest()
  }
}

onMounted(() => {
  if (import.meta.client) {
    window.addEventListener('keydown', onEscape)
  }
})

onBeforeUnmount(() => {
  if (import.meta.client) {
    window.removeEventListener('keydown', onEscape)
    document.body.style.overflow = ''
  }
})
</script>

<style scoped>
.order-request-overlay {
  position: fixed;
  inset: 0;
  z-index: 10000;
  background: rgba(0, 0, 0, 0.55);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  overflow-y: auto;
}

.order-request-modal {
  position: relative;
  width: 100%;
  max-width: 520px;
  max-height: calc(100vh - 40px);
  overflow-y: auto;
  background: #fff;
  border-radius: 20px;
  padding: 32px 28px 28px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.25);
}

.order-request-modal__close {
  position: absolute;
  top: 12px;
  right: 14px;
  width: 36px;
  height: 36px;
  border: none;
  background: #f5f0fa;
  color: #5e3085;
  border-radius: 50%;
  font-size: 24px;
  line-height: 1;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}

.order-request-modal__close:hover {
  background: #ebe0f5;
}

.order-request-modal__title {
  font-family: 'Days One', cursive;
  font-size: 1.5rem;
  font-weight: 400;
  color: #5e3085;
  margin: 0 32px 8px 0;
  line-height: 1.2;
}

.order-request-modal__subtitle {
  font-family: 'Montserrat', sans-serif;
  font-size: 0.9rem;
  color: #666;
  margin: 0 0 20px;
  line-height: 1.5;
}

@media (max-width: 480px) {
  .order-request-modal {
    padding: 28px 18px 22px;
    border-radius: 16px;
  }

  .order-request-modal__title {
    font-size: 1.25rem;
  }
}
</style>
