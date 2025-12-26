<template>
  <div class="homepage">
    <!-- Header -->
    <HeaderSimple />
    
    <!-- Уведомление о предзаполненной форме -->
    <div v-if="showFormNotification" class="form-notification" @click="scrollToForm">
      <div class="notification-content">
        <span class="notification-text">✓ Форма заказа заполнена. Нажмите, чтобы перейти к форме</span>
        <button @click.stop="showFormNotification = false" class="notification-close">×</button>
      </div>
    </div>
    
    <!-- Hero Banner с слайдером -->
    <div class="scroll-reveal scroll-reveal-fade-up">
      <HeroBanner />
    </div>
    
    <!-- Stories Bar -->
    <div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-1">
      <StoriesBar />
    </div>
    
    <!-- Меню (заменяет старую сетку товаров) -->
    <div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-1">
      <MenuGrid />
    </div>
    

    <!-- Production Section -->
    <div class="scroll-reveal scroll-reveal-fade-right scroll-reveal-delay-2">
      <ProductionSection />
    </div>
    
    <!-- Product Carousel -->
    <div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-1">
      <ProductCarousel />
    </div>
    
    <!-- Order Form -->
    <div class="scroll-reveal scroll-reveal-scale scroll-reveal-delay-2">
      <OrderForm :prefilled-message="prefilledMessage" />
    </div>
    
    
    
    <!-- Карта и контакты -->
    <div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-2 map-wrapper">
      <MapSection />
    </div>
    
    <!-- Новый современный футер -->
    <div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-3">
      <FooterNew />
    </div>
  </div>
</template>

<script setup>
import { computed, ref, onMounted } from 'vue'
import HeaderSimple from '../components/HeaderSimple.vue'
import HeroBanner from '../components/HeroBanner.vue'
import MenuGrid from '../components/MenuGrid.vue'
 
import ProductionSection from '../components/ProductionSection.vue'
import ProductCarousel from '../components/ProductCarousel.vue'
import StoriesBar from '../components/StoriesBar.vue'
import OrderForm from '../components/OrderForm.vue'
import MapSection from '../components/MapSection.vue'
import FooterNew from '../components/FooterNew.vue'

// Scroll reveal эффекты инициализируются автоматически через плагин

// Получаем сообщение из URL параметров
const route = useRoute()
const prefilledMessage = computed(() => {
  return route.query.message ? decodeURIComponent(route.query.message) : ''
})

// Показ уведомления о предзаполненной форме
const showFormNotification = ref(false)

// Агрессивная блокировка скролла и принудительная установка позиции
const forceScrollToTop = () => {
  if (process.client) {
    // Блокируем все возможные способы скролла
    window.scrollTo(0, 0)
    document.documentElement.scrollTop = 0
    document.body.scrollTop = 0
    
    // Дополнительно через CSS
    document.documentElement.style.scrollBehavior = 'auto'
    document.body.style.scrollBehavior = 'auto'
  }
}

// Проверяем, есть ли предзаполненное сообщение и показываем уведомление
onMounted(() => {
  // Очищаем любые флаги скролла
  if (process.client) {
    sessionStorage.removeItem('floksbox_scroll_to_form')
    
    // Агрессивно блокируем скролл
    forceScrollToTop()
    
    // Блокируем скролл еще раз через небольшую задержку (для борьбы со scroll-reveal)
    setTimeout(() => {
      forceScrollToTop()
    }, 50)
    
    // И еще раз через большую задержку
    setTimeout(() => {
      forceScrollToTop()
      
      // Восстанавливаем smooth scroll behavior после принудительной установки позиции
      document.documentElement.style.scrollBehavior = 'smooth'
      document.body.style.scrollBehavior = 'smooth'
    }, 500)
    
    // Показываем уведомление только если есть сообщение
    if (route.query.message) {
      showFormNotification.value = true
      
      // Автоматически скрываем уведомление через 5 секунд
      setTimeout(() => {
        showFormNotification.value = false
      }, 5000)
    }
  }
})

// Функция для скролла к форме по клику на уведомление (ТОЛЬКО ПО КЛИКУ)
const scrollToForm = () => {
  const orderFormElement = document.getElementById('order-form')
  if (orderFormElement) {
    orderFormElement.scrollIntoView({ 
      behavior: 'smooth',
      block: 'start'
    })
  }
  showFormNotification.value = false
}

useHead({
  title: 'Floksbox - Упакуем ваш бизнес',
  meta: [
    { 
      name: 'description', 
      content: 'Floksbox - профессиональная упаковка для вашего бизнеса. Заказать упаковочные решения.' 
    },
    {
      name: 'keywords',
      content: 'упаковка, floksbox, коробки, бизнес, заказать упаковку'
    }
  ]
})
</script>

<style scoped>
.homepage {
  width: 100%;
  max-width: 100%;
  min-height: 100vh;
  overflow-x: hidden;
}

.form-notification {
  position: fixed;
  top: 20px;
  right: 20px;
  background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
  color: white;
  padding: 15px 20px;
  border-radius: 12px;
  box-shadow: 0 8px 25px rgba(76, 175, 80, 0.3);
  cursor: pointer;
  z-index: 1000;
  max-width: 350px;
  animation: slideIn 0.3s ease-out;
  transition: all 0.3s ease;
}

.form-notification:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 35px rgba(76, 175, 80, 0.4);
}

.notification-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 15px;
}

.notification-text {
  font-size: 14px;
  font-weight: 500;
  line-height: 1.4;
}

.notification-close {
  background: none;
  border: none;
  color: white;
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
  padding: 0;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: background 0.2s ease;
}

.notification-close:hover {
  background: rgba(255, 255, 255, 0.2);
}

@keyframes slideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.map-wrapper {
  margin-bottom: 40px;
}

@media (max-width: 768px) {
  .form-notification {
    top: 10px;
    right: 10px;
    left: 10px;
    max-width: none;
  }
}
</style> 