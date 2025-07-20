<template>
  <footer class="footer">
    <div class="footer-container">
      <!-- Яндекс карта -->
      <div class="map-container">
        <div style="position:relative;overflow:hidden;">
          <iframe src="https://yandex.ru/map-widget/v1/org/floksboks/182640389494/?ll=37.009835%2C55.593991&z=16" 
                  width="100%" 
                  height="440" 
                  frameborder="1" 
                  allowfullscreen="true" 
                  style="position:relative;">
          </iframe>
        </div>
      </div>
      
      <!-- Наложение footer.png поверх карты -->
      <div class="footer-overlay">
        <img 
          src="/assets/footer.png" 
          alt="Footer" 
          class="footer-image"
        />
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  position: relative;
  width: 100%;
  margin-top: auto;
}

.footer-container {
  position: relative;
  width: 100%;
  height: 440px;
}

.map-container {
  width: 100%;
  height: 100%;
  background-color: #e9ecef;
}

.footer-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 150px;
  z-index: 2;
}

.footer-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* Адаптивность */
@media (max-width: 768px) {
  .footer-container {
    height: 350px;
  }
  
  .footer-overlay {
    height: 120px;
  }
}

@media (max-width: 480px) {
  .footer-container {
    height: 300px;
  }
  
  .footer-overlay {
    height: 100px;
  }
}
</style> 