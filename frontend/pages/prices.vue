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
      
      <!-- Дополнительная информация -->
      <div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-1 info-section">
        <div class="info-container">
          <div class="info-card">
            <div class="info-icon">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M2 17L12 22L22 17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M2 12L12 17L22 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <h3>Индивидуальные цены</h3>
            <p>Для крупных заказов и постоянных клиентов мы предоставляем специальные условия и скидки</p>
          </div>
          
          <div class="info-card">
            <div class="info-icon">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
                <polyline points="12,6 12,12 16,14" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <h3>Актуальные цены</h3>
            <p>Прайс-лист обновляется регулярно. Для получения точной стоимости свяжитесь с нами</p>
          </div>
          
          <div class="info-card consultation-card" @click="openContactForm">
            <div class="info-icon">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M9 12L11 14L15 10" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12Z" stroke="currentColor" stroke-width="2"/>
              </svg>
            </div>
            <h3>Бесплатная консультация</h3>
            <p>Наши специалисты помогут подобрать оптимальное решение и рассчитать стоимость</p>
            <div class="consultation-hint">Нажмите для связи с нами</div>
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
const pdfUrl = '/assets/images/Прайс FloksBox.pdf'

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

.info-section {
  margin-bottom: 80px;
}

.info-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 32px;
}

.info-card {
  background: #fff;
  padding: 32px 24px;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid #f0f0f0;
}

.info-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
}

.info-icon {
  width: 64px;
  height: 64px;
  margin: 0 auto 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.info-card h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 16px;
  color: #333;
}

.info-card p {
  font-size: 16px;
  line-height: 1.6;
  color: #666;
  margin: 0;
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
  
  .info-container {
    grid-template-columns: 1fr;
    gap: 24px;
  }
  
  .info-card {
    padding: 24px 20px;
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
  
  .info-card {
    padding: 20px 16px;
  }
  
  .info-card h3 {
    font-size: 18px;
  }
  
  .info-card p {
    font-size: 14px;
  }
}

/* Отступ перед футером */
.footer-wrapper {
  margin-top: 80px;
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

/* Стили для интерактивной карточки консультации */
.consultation-card {
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.consultation-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.1), transparent);
  transition: left 0.5s ease;
}

.consultation-card:hover::before {
  left: 100%;
}

.consultation-hint {
  margin-top: 12px;
  font-size: 14px;
  color: #667eea;
  font-weight: 500;
  opacity: 0;
  transform: translateY(10px);
  transition: all 0.3s ease;
}

.consultation-card:hover .consultation-hint {
  opacity: 1;
  transform: translateY(0);
}

.consultation-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 40px rgba(102, 126, 234, 0.15);
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
