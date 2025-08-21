<template>
  <div class="scroll-demo">
    <div class="demo-header">
      <h1 class="scroll-reveal scroll-reveal-fade-up">
        Демонстрация Scroll Reveal Эффектов
      </h1>
      <p class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-1">
        Прокрутите страницу вниз, чтобы увидеть различные анимации
      </p>
    </div>

    <!-- Fade Up эффекты -->
    <section class="demo-section">
      <h2 class="scroll-reveal scroll-reveal-fade-up">Fade Up (Появление снизу)</h2>
      <div class="demo-grid">
        <div class="demo-card scroll-reveal scroll-reveal-fade-up">
          Карточка 1
        </div>
        <div class="demo-card scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-1">
          Карточка 2 (задержка 0.1s)
        </div>
        <div class="demo-card scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-2">
          Карточка 3 (задержка 0.2s)
        </div>
      </div>
    </section>

    <!-- Fade Left/Right эффекты -->
    <section class="demo-section">
      <h2 class="scroll-reveal scroll-reveal-scale">Боковые эффекты</h2>
      <div class="demo-horizontal">
        <div class="demo-card scroll-reveal scroll-reveal-fade-left">
          Появляется слева
        </div>
        <div class="demo-card scroll-reveal scroll-reveal-scale scroll-reveal-delay-1">
          Масштабируется
        </div>
        <div class="demo-card scroll-reveal scroll-reveal-fade-right scroll-reveal-delay-2">
          Появляется справа
        </div>
      </div>
    </section>

    <!-- Компонент-обертка -->
    <section class="demo-section">
      <h2 class="scroll-reveal scroll-reveal-fade-up">Использование компонента-обертки</h2>
      <ScrollRevealWrapper type="fade-up" :delay="0">
        <div class="demo-card">
          Обернуто в ScrollRevealWrapper
        </div>
      </ScrollRevealWrapper>
      
      <ScrollRevealWrapper type="scale" :delay="1">
        <div class="demo-card">
          С масштабированием и задержкой
        </div>
      </ScrollRevealWrapper>
    </section>

    <!-- Большая секция для прокрутки -->
    <section class="demo-section tall-section">
      <h2 class="scroll-reveal scroll-reveal-fade-up">Финальная секция</h2>
      <div class="scroll-reveal scroll-reveal-scale scroll-reveal-delay-1">
        <p>Поздравляем! Вы увидели все эффекты scroll reveal.</p>
        <NuxtLink to="/" class="back-link scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-2">
          ← Вернуться на главную
        </NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup>
import ScrollRevealWrapper from '~/components/ScrollRevealWrapper.vue'

useHead({
  title: 'Scroll Reveal Demo - Floksbox',
  meta: [
    { name: 'description', content: 'Демонстрация scroll reveal эффектов' }
  ]
})
</script>

<style scoped>
.scroll-demo {
  min-height: 100vh;
  padding: 40px 20px;
}

.demo-header {
  text-align: center;
  margin-bottom: 80px;
  padding: 60px 0;
}

.demo-header h1 {
  font-size: 3rem;
  font-family: 'Days', sans-serif;
  color: #5e3085;
  margin-bottom: 20px;
}

.demo-header p {
  font-size: 1.2rem;
  color: #666;
  max-width: 600px;
  margin: 0 auto;
}

.demo-section {
  max-width: 1200px;
  margin: 0 auto 120px auto;
}

.demo-section h2 {
  font-size: 2rem;
  margin-bottom: 40px;
  text-align: center;
  color: #333;
}

.demo-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-bottom: 40px;
}

.demo-horizontal {
  display: flex;
  justify-content: space-between;
  gap: 30px;
  flex-wrap: wrap;
}

.demo-card {
  background: white;
  padding: 40px 30px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
  font-size: 1.1rem;
  font-weight: 500;
  color: #333;
  min-height: 150px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.3s ease;
}

.demo-card:hover {
  transform: translateY(-5px);
}

.tall-section {
  min-height: 80vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.tall-section p {
  font-size: 1.2rem;
  margin-bottom: 30px;
  color: #555;
}

.back-link {
  display: inline-block;
  padding: 12px 24px;
  background: #5e3085;
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.back-link:hover {
  background: #4a2568;
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .demo-header h1 {
    font-size: 2rem;
  }
  
  .demo-horizontal {
    flex-direction: column;
  }
  
  .demo-card {
    min-height: 120px;
    padding: 30px 20px;
  }
}
</style>
