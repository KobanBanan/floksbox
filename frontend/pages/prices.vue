<template>
  <div class="prices-page">
    <!-- Header с такой же шапкой -->
    <HeaderSimple />
    
    <!-- Основной контент страницы цен -->
    <main class="prices-main">
      <!-- Заголовок страницы -->
      <section class="page-header">
        <div class="page-header-container">
          <h1 class="page-title">Цены</h1>
          <p class="page-subtitle">Актуальные цены на нашу продукцию</p>
        </div>
      </section>
      
      <!-- Раздел с PDF прайсом -->
      <div class="scroll-reveal scroll-reveal-fade-up prices-section">
        <div class="prices-container">
          <div class="pdf-viewer-wrapper">
            <div class="pdf-header">
              <h2 class="pdf-title">Прайс-лист FloksBox</h2>
              <div class="pdf-actions">
                <a 
                  :href="pdfUrl" 
                  download="Прайс FloksBox.pdf" 
                  class="download-btn"
                >
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M21 15V19C21 19.5304 20.7893 20.0391 20.4142 20.4142C20.0391 20.7893 19.5304 21 19 21H5C4.46957 21 3.96086 20.7893 3.58579 20.4142C3.21071 20.0391 3 19.5304 3 19V15" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <polyline points="7,10 12,15 17,10" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <line x1="12" y1="15" x2="12" y2="3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  Скачать PDF
                </a>
              </div>
            </div>
            
            <div class="pdf-viewer">
              <iframe 
                :src="pdfUrl" 
                type="application/pdf"
                class="pdf-iframe"
                title="Прайс-лист FloksBox"
              >
                <p>Ваш браузер не поддерживает отображение PDF файлов. 
                  <a :href="pdfUrl" target="_blank">Скачайте файл</a> для просмотра.
                </p>
              </iframe>
            </div>
          </div>
        </div>
      </div>
      
    </main>
    
    <!-- Footer такой же как на главной -->
    <div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-2 footer-wrapper">
      <FooterNew />
    </div>

    <!-- Модальное окно формы обратной связи -->
    <div v-if="showModal" class="modal-overlay" @click.self="showModal = false">
      <div class="modal-content">
        <form class="request-form" @submit.prevent="submitRequest">
          <h2 class="form-title">Оставить заявку</h2>
          <label>
            <span>Ваше имя</span>
            <input type="text" v-model="form.name" required />
          </label>
          <label>
            <span>Ваш телефон</span>
            <input type="tel" v-model="form.phone" required />
          </label>
          <label>
            <span>Опишите ваш запрос</span>
            <textarea v-model="form.message" required></textarea>
          </label>
          <button type="submit" class="submit-btn">Отправить</button>
        </form>
        <button class="close-btn" @click="showModal = false">×</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import HeaderSimple from '../components/HeaderSimple.vue'
import FooterNew from '../components/FooterNew.vue'

// Путь к PDF файлу
const pdfUrl = '/assets/images/price_floksbox.pdf'

// Состояние модального окна формы
const showModal = ref(false)
const form = ref({ name: '', phone: '', message: '' })

// Функция для открытия формы
const openContactForm = () => {
  showModal.value = true
}

// Функция для отправки формы
const submitRequest = () => {
  // Здесь будет логика отправки формы
  showModal.value = false
  form.value = { name: '', phone: '', message: '' }
}

// SEO мета-теги для страницы цен
useHead({
  title: 'Цены - Floksbox',
  meta: [
    { 
      name: 'description', 
      content: 'Актуальные цены на упаковочную продукцию Floksbox. Скачайте прайс-лист или свяжитесь с нами для индивидуального расчета.' 
    },
    {
      name: 'keywords',
      content: 'цены, прайс, стоимость, упаковка, floksbox, коробки, пакеты, гофроупаковка'
    }
  ]
})
</script>

<style scoped>
.prices-page {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.prices-main {
  flex: 1;
}

.page-header {
  background: transparent;
  color: #333;
  padding: 60px 0 80px 0;
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

.prices-section {
  margin-bottom: 80px;
}

.prices-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
}

.pdf-viewer-wrapper {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  border: 1px solid #e0e0e0;
}

.pdf-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px 32px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.pdf-title {
  font-size: 24px;
  font-weight: 600;
  margin: 0;
}

.pdf-actions {
  display: flex;
  gap: 16px;
}

.download-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  background: rgba(255, 255, 255, 0.2);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 500;
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.download-btn:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.pdf-viewer {
  position: relative;
  width: 100%;
  height: 600px;
  background: #f8f9fa;
}

.pdf-iframe {
  width: 100%;
  height: 100%;
  border: none;
  display: block;
}


/* Адаптивность */
@media (max-width: 768px) {
  .page-header {
    padding: 80px 0 60px 0;
  }
  
  .page-header-container,
  .prices-container,
  .info-container {
    padding: 0 20px;
  }
  
  .page-title {
    font-size: 36px;
    margin-bottom: 16px;
  }
  
  .page-subtitle {
    font-size: 18px;
  }
  
  .pdf-header {
    flex-direction: column;
    gap: 16px;
    text-align: center;
    padding: 20px;
  }
  
  .pdf-title {
    font-size: 20px;
  }
  
  .pdf-viewer {
    height: 500px;
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
  
  .pdf-viewer {
    height: 400px;
  }
  
}

/* Отступ перед футером */
.footer-wrapper {
  margin-top: 120px;
}

@media (max-width: 768px) {
  .footer-wrapper {
    margin-top: 60px;
  }
}

@media (max-width: 480px) {
  .footer-wrapper {
    margin-top: 40px;
  }
}


/* Стили для модального окна */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.45);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: #f8f9fa;
  border-radius: 18px;
  box-shadow: 0 8px 32px rgba(71, 0, 159, 0.18);
  padding: 40px 36px 32px 36px;
  min-width: 350px;
  max-width: 95vw;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-title {
  font-size: 24px;
  font-weight: 600;
  color: #333;
  margin-bottom: 24px;
  text-align: center;
}

.request-form {
  display: flex;
  flex-direction: column;
  gap: 22px;
  width: 340px;
  max-width: 80vw;
}

.request-form label {
  display: flex;
  flex-direction: column;
  font-size: 1.2rem;
  color: #222;
  font-weight: 500;
  gap: 7px;
}

.request-form input,
.request-form textarea {
  border: 1.5px solid #bdbdbd;
  border-radius: 7px;
  padding: 10px 12px;
  font-size: 1.1rem;
  font-family: inherit;
  background: #fff;
  resize: none;
  transition: border-color 0.3s ease;
}

.request-form input:focus,
.request-form textarea:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.request-form textarea {
  min-height: 90px;
  max-height: 200px;
}

.submit-btn {
  margin-top: 18px;
  padding: 12px 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #fff;
  font-size: 1.1rem;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s, transform 0.2s;
}

.submit-btn:hover {
  background: linear-gradient(135deg, #47009f 0%, #764ba2 100%);
  transform: translateY(-2px) scale(1.04);
}

.close-btn {
  position: absolute;
  top: 12px;
  right: 18px;
  background: none;
  border: none;
  font-size: 2.1rem;
  color: #764ba2;
  cursor: pointer;
  transition: color 0.2s;
}

.close-btn:hover {
  color: #47009f;
}

/* Адаптивность для модального окна */
@media (max-width: 480px) {
  .modal-content {
    padding: 30px 24px 24px 24px;
    min-width: 300px;
  }
  
  .form-title {
    font-size: 20px;
    margin-bottom: 20px;
  }
  
  .request-form {
    width: 280px;
    gap: 18px;
  }
  
  .request-form label {
    font-size: 1.1rem;
  }
  
  .request-form input,
  .request-form textarea {
    font-size: 1rem;
    padding: 8px 10px;
  }
}
</style>
