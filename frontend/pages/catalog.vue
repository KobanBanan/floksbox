<template>
  <div class="catalog-page">
    <!-- Шапка сайта -->
    <HeaderSimple />
    
    <!-- Компонент меню из главной страницы -->
    <div class="scroll-reveal scroll-reveal-fade-up menu-section">
      <MenuGrid />
    </div>
    
    <!-- Раздел с товарами -->
    <div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-1 products-section">
      <ProductCarousel />
    </div>
    
    <!-- Футер сайта -->
    <div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-2">
      <FooterNew />
    </div>
  </div>
</template>

<script setup>
import HeaderSimple from '../components/HeaderSimple.vue'
import MenuGrid from '../components/MenuGrid.vue'
import ProductCarousel from '../components/ProductCarousel.vue'
import FooterNew from '../components/FooterNew.vue'

// Настройка мета-данных страницы
useHead({
  title: 'Каталог - Floksbox',
  meta: [
    { 
      name: 'description', 
      content: 'Каталог продукции Floksbox - упаковочные решения для вашего бизнеса. Коробки, пакеты, гофроупаковка и многое другое.' 
    },
    {
      name: 'keywords',
      content: 'каталог, упаковка, коробки, пакеты, floksbox, гофроупаковка, печать'
    }
  ]
})
</script>

<style scoped>
.catalog-page {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Добавляем отступ для меню */
.menu-section {
  margin-top: 40px; /* Умеренный отступ сверху от шапки */
  padding-top: 20px; /* Умеренный внутренний отступ сверху */
  margin-bottom: 40px; /* Уменьшенный отступ снизу от меню */
  padding-bottom: 20px; /* Уменьшенный внутренний отступ */
}

/* Отступ для раздела товаров */
.products-section {
  margin-bottom: 120px; /* Увеличенный отступ снизу от товаров */
  padding-bottom: 60px; /* Увеличенный внутренний отступ */
}

/* Обеспечиваем правильные отступы между компонентами */
.catalog-page > div:not(:last-child):not(.menu-section):not(.products-section) {
  margin-bottom: 40px;
}

/* Адаптивность */
@media (max-width: 768px) {
  .menu-section {
    margin-top: 30px; /* Умеренный отступ сверху на планшетах */
    padding-top: 15px;
    margin-bottom: 30px; /* Уменьшенный отступ на планшетах */
    padding-bottom: 15px;
  }
  
  .products-section {
    margin-bottom: 80px; /* Увеличенный отступ на планшетах */
    padding-bottom: 40px;
  }
  
  .catalog-page > div:not(:last-child):not(.menu-section):not(.products-section) {
    margin-bottom: 20px;
  }
}

@media (max-width: 480px) {
  .menu-section {
    margin-top: 20px; /* Умеренный отступ сверху на мобильных */
    padding-top: 10px;
    margin-bottom: 25px; /* Уменьшенный отступ на мобильных */
    padding-bottom: 10px;
  }
  
  .products-section {
    margin-bottom: 60px; /* Увеличенный отступ на мобильных */
    padding-bottom: 30px;
  }
}
</style>
