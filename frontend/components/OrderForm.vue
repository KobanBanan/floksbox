<template>
  <section id="order-form" class="order-form-section">
    <div class="container">
      <div class="form-wrapper">
        <div class="form-content">
          <div class="form-header">
            <h2>Остались вопросы?<br />Мы ответим!</h2>
            <p>Напишите нам, задайте вопрос по необходимой упаковке</p>
            <p class="response-info">Ответ придет вам на указанный контакты.</p>
            <p class="contact-info">
              В обращении укажите как удобнее с вами связаться: Whatsapp, Telegram, по e-mail или
              телефонным звонком.
            </p>
            <p class="working-hours">
              Отвечаем с 9 до 18, в случае срочности просим обращаться по телефону
            </p>
            <a href="tel:+79602543323" class="phone">+7 (960) 254-33-23</a>
          </div>
        </div>

        <div class="form-container">
          <OrderRequestFormBody :prefilled-message="prefilledMessage" variant="section" />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({
  prefilledMessage: {
    type: String,
    default: '',
  },
})
</script>

<style scoped>
.order-form-section {
  padding: 80px 0;
  background: transparent;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.form-wrapper {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: start;
}

.form-content {
  padding-right: 20px;
}

.form-header h2 {
  font-family: 'Days One', cursive;
  font-size: 2.5rem;
  font-weight: 400;
  color: #5e3085;
  margin-bottom: 20px;
  line-height: 1.2;
}

.form-header p {
  font-family: 'Montserrat', sans-serif;
  font-size: 1rem;
  color: #666;
  line-height: 1.6;
  margin-bottom: 15px;
}

.response-info,
.contact-info,
.working-hours {
  font-size: 0.9rem;
}

.phone {
  display: inline-block;
  font-family: 'Montserrat', sans-serif;
  font-size: 1.5rem;
  font-weight: 700;
  color: #5e3085;
  text-decoration: none;
  margin-top: 10px;
}

.phone:hover {
  text-decoration: underline;
}

.form-container {
  background: white;
  border-radius: 15px;
  padding: 30px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

@media (max-width: 968px) {
  .form-wrapper {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .form-content {
    padding-right: 0;
    text-align: center;
  }

  .form-header h2 {
    font-size: 2rem;
  }
}

@media (max-width: 768px) {
  .order-form-section {
    padding: 60px 0;
  }

  .form-container {
    padding: 20px;
  }
}
</style>
