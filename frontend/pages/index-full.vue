<template>
  <div class="homepage">
    <!-- Hero Section с слайдером -->
    <HeroSlider />
    
    <!-- Menu Section с сеткой товаров -->
    <MenuGrid />
    
    <!-- Love Section с интерактивным изображением -->
    <LoveSection />
  </div>
</template>

<script setup>
import HeroSlider from '../components/HeroSlider.vue'
import MenuGrid from '../components/MenuGrid.vue'
import LoveSection from '../components/LoveSection.vue'

// SEO мета-теги
useHead({
  title: 'Floksbox - Главная',
  meta: [
    {
      name: 'description',
      content: 'Floksbox - ваш надежный партнер. Широкий каталог товаров и услуг.'
    },
    {
      name: 'keywords',
      content: 'floksbox, товары, каталог, акции, цены'
    },
    {
      property: 'og:title',
      content: 'Floksbox - Главная'
    },
    {
      property: 'og:description',
      content: 'Floksbox - ваш надежный партнер. Широкий каталог товаров и услуг.'
    },
    {
      property: 'og:type',
      content: 'website'
    }
  ]
})
</script>

<style lang="scss" scoped>
.homepage {
  width: 100%;
  min-height: 100vh;
}

// Общие стили для плавного скролла
html {
  scroll-behavior: smooth;
}

// Дополнительные стили могут быть добавлены здесь
</style> 