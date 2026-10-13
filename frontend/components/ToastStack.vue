<template>
  <div class="toast-stack" aria-live="polite" aria-relevant="additions">
    <article
      v-for="item in toasts"
      :key="item.id"
      class="toast"
      :class="[`toast--${item.type}`, { 'toast--leaving': item.leaving }]"
      role="status"
    >
      <span class="toast-icon" aria-hidden="true">
        <svg v-if="item.type === 'success'" viewBox="0 0 24 24" fill="none">
          <path d="M6 12.5l4 4 8-9" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <svg v-else-if="item.type === 'error'" viewBox="0 0 24 24" fill="none">
          <path d="M8 8l8 8M16 8l-8 8" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
        </svg>
        <svg v-else viewBox="0 0 24 24" fill="none">
          <path d="M12 8.2v.2M12 11.2V16" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>
        </svg>
      </span>
      <div class="toast-copy">
        <strong>{{ item.title }}</strong>
        <p v-if="item.text">{{ item.text }}</p>
      </div>
      <button type="button" class="toast-close" aria-label="Закрыть" @click="dismiss(item.id)">×</button>
    </article>
  </div>
</template>

<script setup>
const { toasts, dismiss } = useToast()
</script>

<style scoped>
.toast-stack {
  position: fixed;
  right: 20px;
  bottom: 20px;
  z-index: 11000;
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: min(360px, calc(100vw - 32px));
  pointer-events: none;
}

.toast {
  --toast-glow: #5e3085;
  --toast-icon: #5e3085;
  position: relative;
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 14px 12px 14px 14px;
  border-radius: 14px;
  background: #fff;
  color: #1c1c1c;
  box-shadow: 0 12px 32px rgba(30, 12, 50, 0.16);
  overflow: hidden;
  pointer-events: auto;
  animation: toast-in 420ms cubic-bezier(0.22, 1, 0.36, 1);
}

.toast--success {
  --toast-glow: #b8ff00;
  --toast-icon: #2f6b00;
}

.toast--error {
  --toast-glow: #ff5a5a;
  --toast-icon: #fff;
}

.toast--info {
  --toast-glow: #5e3085;
  --toast-icon: #fff;
}

.toast::before {
  content: '';
  position: absolute;
  left: -6px;
  top: 50%;
  width: 54px;
  height: 54px;
  border-radius: 50%;
  background: var(--toast-glow);
  filter: blur(16px);
  opacity: 0.9;
  transform: translateY(-50%);
  pointer-events: none;
}

.toast-icon {
  position: relative;
  z-index: 1;
  flex-shrink: 0;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--toast-glow);
  color: var(--toast-icon);
  box-shadow: 0 0 0 4px rgba(255, 255, 255, 0.7);
}

.toast--error .toast-icon {
  background: #ff4d4f;
}

.toast--info .toast-icon {
  background: #5e3085;
}

.toast-icon svg {
  width: 18px;
  height: 18px;
}

.toast-copy {
  position: relative;
  z-index: 1;
  flex: 1;
  min-width: 0;
  padding-top: 1px;
}

.toast-copy strong {
  display: block;
  font-family: 'Montserrat', sans-serif;
  font-size: 15px;
  font-weight: 700;
  line-height: 1.25;
}

.toast-copy p {
  margin: 3px 0 0;
  font-family: 'Montserrat', sans-serif;
  font-size: 13px;
  line-height: 1.4;
  color: #5c5c5c;
}

.toast-close {
  position: relative;
  z-index: 1;
  flex-shrink: 0;
  width: 28px;
  height: 28px;
  border: none;
  border-radius: 50%;
  background: transparent;
  color: #888;
  font-size: 20px;
  line-height: 1;
  cursor: pointer;
}

.toast-close:hover {
  background: rgba(0, 0, 0, 0.06);
  color: #222;
}

.toast--leaving {
  animation: toast-out 260ms ease forwards;
}

@keyframes toast-in {
  from {
    opacity: 0;
    transform: translateX(28px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes toast-out {
  to {
    opacity: 0;
    transform: translateX(20px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .toast,
  .toast--leaving {
    animation: none;
  }
}

@media (max-width: 640px) {
  .toast-stack {
    right: 12px;
    left: 12px;
    bottom: 12px;
    width: auto;
  }
}
</style>
