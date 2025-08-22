<template>
  <div class="contacts-page">
    <!-- Header с такой же шапкой -->
    <HeaderSimple />
    
    <!-- Основной контент страницы контактов -->
    <main class="contacts-main">
      <!-- Заголовок страницы -->
      <section class="page-header">
        <div class="page-header-container">
          <h1 class="page-title">Контакты</h1>
          <p class="page-subtitle">Свяжитесь с нами любым удобным способом</p>
        </div>
      </section>
      
      <!-- Раздел с картой и контактами (такой же как на главной) -->
      <div class="scroll-reveal scroll-reveal-fade-up map-section-wrapper">
        <MapSection />
      </div>
    </main>
    
    <!-- Footer такой же как на главной -->
    <div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-1">
      <FooterNew />
    </div>
  </div>
</template>

<script setup>
import HeaderSimple from '../components/HeaderSimple.vue'
import MapSection from '../components/MapSection.vue'
import FooterNew from '../components/FooterNew.vue'

// SEO мета-теги для страницы контактов
useHead({
  title: 'Контакты - Floksbox',
  meta: [
    { 
      name: 'description', 
      content: 'Контактная информация Floksbox. Адрес, телефон, email. Свяжитесь с нами для заказа упаковочных решений.' 
    },
    {
      name: 'keywords',
      content: 'контакты, floksbox, адрес, телефон, email, связаться'
    }
  ]
})
</script>

<style scoped>
.contacts-page {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.contacts-main {
  flex: 1;
}

.page-header {
  background: transparent;
  color: #333;
  padding: 100px 0 80px 0;
  position: relative;
  text-align: center;
}



.page-header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
  position: relative;
  z-index: 2;
}

.page-title {
  font-size: 48px;
  font-weight: 700;
  margin-bottom: 20px;
  line-height: 1.2;
  color: #000;
  text-shadow: none;
}

.page-subtitle {
  font-size: 20px;
  font-weight: 400;
  color: #000;
  opacity: 0.8;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.4;
  text-shadow: none;
}

.map-section-wrapper {
  margin-top: -40px;
  margin-bottom: 120px;
}

/* Адаптивность */
@media (max-width: 768px) {
  .page-header {
    padding: 80px 0 60px 0;
  }
  
  .page-header-container {
    padding: 0 20px;
  }
  
  .page-title {
    font-size: 36px;
    margin-bottom: 16px;
  }
  
  .page-subtitle {
    font-size: 18px;
  }
  
  .map-section-wrapper {
    margin-bottom: 80px;
  }
}

@media (max-width: 480px) {
  .page-header {
    padding: 60px 0 40px 0;
  }
  
  .page-title {
    font-size: 28px;
    margin-bottom: 12px;
  }
  
  .page-subtitle {
    font-size: 16px;
  }
  
  .map-section-wrapper {
    margin-bottom: 60px;
  }
}
</style>
