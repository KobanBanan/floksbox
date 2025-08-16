<template>
  <div class="homepage">
    <!-- Header -->
    <HeaderSimple />
    
    <!-- Hero Banner с слайдером -->
    <div class="scroll-reveal scroll-reveal-fade-up">
      <HeroBanner />
    </div>
    
    <!-- Меню (заменяет старую сетку товаров) -->
    <div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-1">
      <MenuGrid />
    </div>
    
    <!-- Ident Section (видеофон + 1:1 слайдер) -->
    <div class="scroll-reveal scroll-reveal-fade-left scroll-reveal-delay-2">
      <IdentSection />
    </div>
    
    <!-- Process Section (над производством) -->
    <div class="scroll-reveal scroll-reveal-scale scroll-reveal-delay-1">
      <ProcessSection />
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
      <OrderForm />
    </div>
    
    <!-- Нас выбирают -->
    <section class="choose-section scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-1">
      <img src="/assets/footer/choose.png" alt="Нас выбирают" class="choose-image" />
    </section>
    
    <!-- Карта и контакты -->
    <div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-2">
      <MapSection />
    </div>
    
    <!-- Новый современный футер -->
    <div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-3">
      <FooterNew />
    </div>
  </div>
</template>

<script setup>
import HeaderSimple from '../components/HeaderSimple.vue'
import HeroBanner from '../components/HeroBanner.vue'
import MenuGrid from '../components/MenuGrid.vue'
import IdentSection from '../components/IdentSection.vue'
import ProcessSection from '../components/ProcessSection.vue'
import ProductionSection from '../components/ProductionSection.vue'
import ProductCarousel from '../components/ProductCarousel.vue'
import OrderForm from '../components/OrderForm.vue'
import MapSection from '../components/MapSection.vue'
import FooterNew from '../components/FooterNew.vue'

// Scroll reveal эффекты инициализируются автоматически через плагин

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
  min-height: 100vh;
}

.choose-section {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px 0;
  background: white;
}

.choose-image {
  max-width: 100%;
  height: auto;
  border: none;
  outline: none;
}
</style> 