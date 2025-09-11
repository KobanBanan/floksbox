<template>
  <section class="production-section">
    <div class="video-container">
      <video 
        autoplay 
        muted 
        loop 
        playsinline
        class="production-video"
      >
        <source src="/assets/production/Автоматическая_линия_для_гофроящиков_｜_2_флексопечати_+_ротор_слоттер.mp4" type="video/mp4">
        Ваш браузер не поддерживает видео.
      </video>
    </div>
  </section>
</template>

<script setup>
// Компонент теперь не требует никакой логики
</script>

<style scoped>
.production-section {
  padding: 60px 20px;
  background-color: transparent;
  color: white;
}

.video-container {
  max-width: 1200px; /* единая ширина */
  margin: 0 auto;
  border-radius: 15px;
  overflow: hidden;
  height: 400px;
}

.production-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* Адаптивность */
@media (max-width: 768px) {
  .production-section {
    padding: 40px 15px;
  }
  
  .video-container {
    height: 250px;
  }
}

@media (max-width: 480px) {
  .video-container {
    height: 200px;
  }
}
</style> 