<template>
  <div class="promotions-page">
    <!-- Шапка сайта -->
    <HeaderSimple />
    
    <!-- Основной контент страницы доставки -->
    <div class="scroll-reveal scroll-reveal-fade-up delivery-content">
      <div class="container">
        <h1 class="page-title">Доставка гофроупаковки: быстро, надежно, по всей стране!</h1>
        <div class="delivery-text">
          <p>
            Мы понимаем, насколько важна своевременная и бережная доставка гофроупаковки для вашего бизнеса. Именно поэтому мы предлагаем комплексные логистические решения, охватывающие Москву, Московскую область и всю Россию. Независимо от того, нужен ли вам крупногабаритный груз для производственных нужд или компактная партия для небольшого магазина, мы подберем оптимальный вариант доставки. Наш автопарк включает разнообразные типы транспортных средств – от малотоннажных автомобилей для экспресс-доставки по городу до мощных фур для дальних перевозок. Мы гарантируем, что ваша гофроупаковка будет доставлена точно в срок и в идеальном состоянии, сохраняя свою целостность и функциональность.
          </p>
          <p>
            Наша цель – сделать процесс получения упаковочных материалов максимально простым и удобным для вас. Мы заботимся о каждом этапе доставки, от момента оформления заказа до вручения вам продукции. Благодаря развитой логистической сети и опыту наших специалистов, мы готовы оперативно реагировать на ваши потребности, предлагая гибкие тарифы и прозрачные условия сотрудничества. Выбирая нас, вы выбираете надежного партнера, который поможет вашему бизнесу расти и процветать, обеспечивая бесперебойные поставки качественной гофроупаковки в любую точку страны.
          </p>
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
  title: 'Доставка гофроупаковки - Floksbox',
  meta: [
    {
      name: 'description',
      content: 'Доставка гофроупаковки по Москве, области и всей России: оперативно, бережно, на любом транспорте. Гибкие тарифы и прозрачные условия.'
    },
    {
      name: 'keywords',
      content: 'доставка, гофроупаковка, логистика, Floksbox, Москва, Московская область, Россия, поставки'
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

/* Доставка: отступы и типографика в духе сайта */
.delivery-content {
  margin-top: 40px;
  margin-bottom: 120px; /* дополнительный отступ от футера */
  padding: 40px 0;
}

.delivery-text {
  max-width: 900px;
  margin: 0 auto;
}

.delivery-text p {
  color: #666;
  line-height: 1.7;
  font-size: 1rem;
  margin-bottom: 18px;
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

  .delivery-content {
    margin-top: 30px;
    margin-bottom: 100px; /* чуть меньше на планшетах */
    padding: 20px 0;
  }

  .delivery-text p {
    font-size: 0.95rem;
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

  .delivery-content {
    margin-bottom: 80px; /* компактнее на мобильных */
  }
}
</style>
