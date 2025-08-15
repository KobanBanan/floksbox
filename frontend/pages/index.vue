<template>
  <div class="homepage">
    <!-- Header -->
    <HeaderSimple />
    
    <!-- Hero Banner с слайдером -->
    <HeroBanner />
    
    <!-- Меню (заменяет старую сетку товаров) -->
    <MenuGrid />
    
    <!-- Ident Section (видеофон + 1:1 слайдер) -->
    <IdentSection />
    
    <!-- Process Section (над производством) -->
    <ProcessSection />

    <!-- Production Section -->
    <ProductionSection />
    
    <!-- Product Carousel -->
    <ProductCarousel />
    
    <!-- Order Form -->
    <OrderForm />
    
    <!-- Карта и контакты -->
    <MapSection />
    
    <!-- Новый современный футер -->
    <FooterNew />
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
</style> 