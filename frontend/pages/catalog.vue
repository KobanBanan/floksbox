<template>
  <div class="catalog-page">
    <!-- Шапка сайта -->
    <HeaderSimple />
    
    <!-- Компонент меню из главной страницы -->
    <div class="scroll-reveal scroll-reveal-fade-up menu-section">
      <MenuGrid />
    </div>
    
    <!-- Ссылка на FEFCO -->
    <div class="scroll-reveal scroll-reveal-fade-up fefco-link-section">
      <nuxt-link to="/fefco" class="fefco-link">
        <div class="fefco-link-content">
          <!-- <img src="/assets/images/fefco_bg.png" alt="FEFCO background" class="fefco-bg-image" /> -->
          <span class="fefco-text">поиск товара по каталогу FEFCO</span>
        </div>
      </nuxt-link>
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

/* Стили для блока ссылки на FEFCO */
.fefco-link-section {
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  margin-bottom: 60px;
  padding: 0;
}

.fefco-link {
  display: block;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  text-decoration: none;
  outline: none;
}

.fefco-link-content {
  position: relative;
  width: 100%;
  height: 120px;
  background-image: url('/assets/fefco/fefco_bg1.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  /* border: 2px solid #5e3085; */ /* Убрали границу */
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0.8;
  transition: opacity 0.3s ease;
  overflow: hidden;
}

.fefco-bg-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
}

.fefco-link:hover .fefco-link-content {
  opacity: 1;
}

.fefco-text {
  font-family: 'Days One', cursive;
  font-size: 24px;
  font-weight: 400;
  color: #5e3085;
  text-align: center;
  text-transform: lowercase;
  position: relative;
  z-index: 2; /* Поверх изображения */
  transition: all 0.3s ease;
  padding: 0 20px;
  background-color: rgba(255, 255, 255, 0.8); /* Добавляем фон для текста */
  border-radius: 8px;
}

.fefco-link:hover .fefco-text {
  text-decoration: underline;
}

/* Отступ для раздела товаров */
.products-section {
  margin-bottom: 120px; /* Увеличенный отступ снизу от товаров */
  padding-bottom: 60px; /* Увеличенный внутренний отступ */
}

/* Обеспечиваем правильные отступы между компонентами */
.catalog-page > div:not(:last-child):not(.menu-section):not(.products-section):not(.fefco-link-section) {
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
  
  .fefco-link-section {
    margin-bottom: 40px;
  }
  
  .fefco-link-content {
    height: 100px;
  }
  
  .fefco-text {
    font-size: 20px;
    padding: 0 15px;
  }
  
  .products-section {
    margin-bottom: 80px; /* Увеличенный отступ на планшетах */
    padding-bottom: 40px;
  }
  
  .catalog-page > div:not(:last-child):not(.menu-section):not(.products-section):not(.fefco-link-section) {
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
  
  .fefco-link-section {
    margin-bottom: 30px;
  }
  
  .fefco-link {
    padding: 0 15px;
  }
  
  .fefco-link-content {
    height: 80px;
    border-radius: 8px;
  }
  
  .fefco-text {
    font-size: 16px;
    padding: 0 10px;
  }
  
  .products-section {
    margin-bottom: 60px; /* Увеличенный отступ на мобильных */
    padding-bottom: 30px;
  }
}
</style>
