<template>
  <div class="promotions-page">
    <!-- Шапка сайта -->
    <HeaderSimple />
    
    <!-- Основной контент страницы акций -->
    <div class="scroll-reveal scroll-reveal-fade-up promotions-content">
      <div class="container">
        <h1 class="page-title">Акции и специальные предложения</h1>
        
        <!-- Секция с активными акциями -->
        <div class="promotions-grid">
          <div class="promotion-card">
            <div class="promotion-image">
              <img src="/assets/images/icecream.png" alt="Скидка на первый заказ" />
            </div>
            <div class="promotion-content">
              <h3 class="promotion-title">Скидка 15% на первый заказ</h3>
              <p class="promotion-description">
                Новым клиентам предоставляется скидка 15% на первый заказ упаковки. 
                Воспользуйтесь промокодом FIRST15 при оформлении заказа.
              </p>
              <div class="promotion-code">
                <span class="code-label">Промокод:</span>
                <span class="code-value">FIRST15</span>
              </div>
              <div class="promotion-validity">
                Действует до 31.12.2024
              </div>
            </div>
          </div>

          <div class="promotion-card">
            <div class="promotion-image">
              <img src="/assets/images/gmanman4.png" alt="Скидка при заказе от 10000 рублей" />
            </div>
            <div class="promotion-content">
              <h3 class="promotion-title">Скидка 10% при заказе от 10 000₽</h3>
              <p class="promotion-description">
                При заказе упаковки на сумму от 10 000 рублей действует автоматическая 
                скидка 10%. Скидка применяется в корзине при достижении суммы заказа.
              </p>
              <div class="promotion-code">
                <span class="code-label">Условие:</span>
                <span class="code-value">Сумма заказа от 10 000₽</span>
              </div>
              <div class="promotion-validity">
                Постоянная акция
              </div>
            </div>
          </div>

          <div class="promotion-card">
            <div class="promotion-image">
              <img src="/assets/images/gmanman7.png" alt="Бесплатная доставка" />
            </div>
            <div class="promotion-content">
              <h3 class="promotion-title">Бесплатная доставка от 5 000₽</h3>
              <p class="promotion-description">
                Бесплатная доставка по Москве и области при заказе упаковки 
                на сумму от 5 000 рублей. Доставка осуществляется в течение 2-3 дней.
              </p>
              <div class="promotion-code">
                <span class="code-label">Условие:</span>
                <span class="code-value">Сумма заказа от 5 000₽</span>
              </div>
              <div class="promotion-validity">
                Постоянная акция
              </div>
            </div>
          </div>

          <div class="promotion-card special">
            <div class="promotion-image">
              <img src="/assets/images/gmanman8.jpg" alt="Индивидуальный дизайн" />
            </div>
            <div class="promotion-content">
              <h3 class="promotion-title">Бесплатная разработка дизайна</h3>
              <p class="promotion-description">
                При заказе брендированной упаковки от 20 000 рублей - разработка 
                индивидуального дизайна абсолютно бесплатно!
              </p>
              <div class="promotion-code">
                <span class="code-label">Условие:</span>
                <span class="code-value">Заказ от 20 000₽</span>
              </div>
              <div class="promotion-validity">
                Ограниченное предложение
              </div>
            </div>
          </div>
        </div>

        <!-- Дополнительная информация -->
        <div class="promotions-info">
          <h2>Условия акций</h2>
          <ul>
            <li>Акции не суммируются между собой</li>
            <li>Скидки действуют только на новые заказы</li>
            <li>Промокоды действительны только при оформлении заказа через сайт</li>
            <li>Компания оставляет за собой право изменить условия акций</li>
          </ul>
        </div>

        <!-- Призыв к действию -->
        <div class="cta-section">
          <h2>Готовы воспользоваться выгодным предложением?</h2>
          <p>Свяжитесь с нами для консультации и оформления заказа</p>
          <div class="cta-buttons">
            <NuxtLink to="/catalog" class="cta-btn primary">Перейти в каталог</NuxtLink>
            <a href="tel:+79602543323" class="cta-btn secondary">Позвонить</a>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Футер сайта -->
    <div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-2">
      <FooterNew />
    </div>
  </div>
</template>

<script setup>
import HeaderSimple from '../components/HeaderSimple.vue'
import FooterNew from '../components/FooterNew.vue'

// Настройка мета-данных страницы
useHead({
  title: 'Акции и скидки - Floksbox',
  meta: [
    { 
      name: 'description', 
      content: 'Актуальные акции и специальные предложения от Floksbox. Скидки на упаковку, бесплатная доставка, промокоды для новых клиентов.' 
    },
    {
      name: 'keywords',
      content: 'акции, скидки, промокоды, floksbox, упаковка, специальные предложения, бесплатная доставка'
    }
  ]
})
</script>

<style scoped>
.promotions-page {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.promotions-content {
  margin-top: 40px;
  margin-bottom: 80px;
  padding: 40px 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.page-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 60px;
  color: #47009f;
  background: linear-gradient(135deg, #47009f 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.promotions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-bottom: 80px;
}

.promotion-card {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(71, 0, 159, 0.12);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 2px solid transparent;
}

.promotion-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 16px 48px rgba(71, 0, 159, 0.2);
}

.promotion-card.special {
  border: 2px solid #47009f;
  background: linear-gradient(145deg, #fff 0%, #f8f6ff 100%);
}

.promotion-image {
  height: 200px;
  overflow: hidden;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
}

.promotion-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.promotion-card:hover .promotion-image img {
  transform: scale(1.05);
}

.promotion-content {
  padding: 24px;
}

.promotion-title {
  font-size: 1.4rem;
  font-weight: 600;
  color: #47009f;
  margin-bottom: 16px;
  line-height: 1.3;
}

.promotion-description {
  color: #666;
  line-height: 1.6;
  margin-bottom: 20px;
  font-size: 0.95rem;
}

.promotion-code {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 12px;
  padding: 12px;
  background: #f8f6ff;
  border-radius: 8px;
  border-left: 4px solid #47009f;
}

.code-label {
  font-weight: 600;
  color: #47009f;
  font-size: 0.9rem;
}

.code-value {
  font-family: 'Courier New', monospace;
  background: #47009f;
  color: #fff;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.85rem;
  font-weight: bold;
}

.promotion-validity {
  font-size: 0.85rem;
  color: #999;
  font-style: italic;
  text-align: right;
}

.promotions-info {
  background: #f8f9fa;
  padding: 40px;
  border-radius: 16px;
  margin-bottom: 60px;
  border-left: 6px solid #47009f;
}

.promotions-info h2 {
  color: #47009f;
  font-size: 1.8rem;
  margin-bottom: 24px;
  font-weight: 600;
}

.promotions-info ul {
  list-style: none;
  padding: 0;
}

.promotions-info li {
  padding: 12px 0;
  border-bottom: 1px solid #e9ecef;
  position: relative;
  padding-left: 24px;
  color: #555;
  line-height: 1.5;
}

.promotions-info li:before {
  content: '✓';
  position: absolute;
  left: 0;
  color: #47009f;
  font-weight: bold;
  font-size: 1.1rem;
}

.promotions-info li:last-child {
  border-bottom: none;
}

.cta-section {
  text-align: center;
  padding: 60px 40px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 20px;
  color: #fff;
}

.cta-section h2 {
  font-size: 2rem;
  margin-bottom: 16px;
  font-weight: 600;
}

.cta-section p {
  font-size: 1.1rem;
  margin-bottom: 32px;
  opacity: 0.9;
}

.cta-buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
  flex-wrap: wrap;
}

.cta-btn {
  padding: 14px 32px;
  border-radius: 10px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.05rem;
  transition: all 0.3s ease;
  display: inline-block;
  min-width: 160px;
}

.cta-btn.primary {
  background: #fff;
  color: #47009f;
  border: 2px solid #fff;
}

.cta-btn.primary:hover {
  background: transparent;
  color: #fff;
  transform: translateY(-2px);
}

.cta-btn.secondary {
  background: transparent;
  color: #fff;
  border: 2px solid #fff;
}

.cta-btn.secondary:hover {
  background: #fff;
  color: #47009f;
  transform: translateY(-2px);
}

/* Адаптивность */
@media (max-width: 768px) {
  .promotions-content {
    margin-top: 30px;
    margin-bottom: 60px;
    padding: 20px 0;
  }

  .page-title {
    font-size: 2rem;
    margin-bottom: 40px;
  }

  .promotions-grid {
    grid-template-columns: 1fr;
    gap: 20px;
    margin-bottom: 60px;
  }

  .promotion-content {
    padding: 20px;
  }

  .promotion-title {
    font-size: 1.2rem;
  }

  .promotions-info {
    padding: 30px 20px;
    margin-bottom: 40px;
  }

  .promotions-info h2 {
    font-size: 1.5rem;
  }

  .cta-section {
    padding: 40px 20px;
  }

  .cta-section h2 {
    font-size: 1.6rem;
  }

  .cta-buttons {
    flex-direction: column;
    align-items: center;
  }

  .cta-btn {
    width: 100%;
    max-width: 280px;
  }
}

@media (max-width: 480px) {
  .container {
    padding: 0 15px;
  }

  .page-title {
    font-size: 1.8rem;
    margin-bottom: 30px;
  }

  .promotion-image {
    height: 160px;
  }

  .promotion-content {
    padding: 16px;
  }

  .promotion-title {
    font-size: 1.1rem;
  }

  .promotion-description {
    font-size: 0.9rem;
  }

  .promotions-info {
    padding: 20px 16px;
  }

  .cta-section {
    padding: 30px 16px;
    border-radius: 16px;
  }

  .cta-section h2 {
    font-size: 1.4rem;
  }
}
</style>
