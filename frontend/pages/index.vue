<template>
  <div class="homepage">
    <!-- Header -->
    <HeaderSimple />
    
    <!-- Hero Banner с слайдером -->
    <HeroBanner />
    
    <!-- Сетка товаров -->
    <ProductGrid />
    
    <!-- Love Section -->
    <LoveSection />
    
    <!-- Production Section -->
    <ProductionSection />
    
    <!-- Order Form -->
    <OrderForm />
    
    <!-- Footer с картой -->
    <FooterMap />
  </div>
</template>

<script setup>
import HeaderSimple from '../components/HeaderSimple.vue'
import HeroBanner from '../components/HeroBanner.vue'
import ProductGrid from '../components/ProductGrid.vue'
import LoveSection from '../components/LoveSection.vue'
import ProductionSection from '../components/ProductionSection.vue'
import OrderForm from '../components/OrderForm.vue'
import FooterMap from '../components/FooterMap.vue'

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