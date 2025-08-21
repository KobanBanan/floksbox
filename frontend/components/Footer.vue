<template>
  <footer class="footer">
    <div class="footer-container">
      <!-- Карта Яндекс (заглушка) -->
      <div class="map-container">
        <div class="map-placeholder">
          <p>Здесь будет размещена Яндекс карта</p>
          <small>Интеграция с Яндекс API будет добавлена позже</small>
        </div>
      </div>
      
      <!-- Изображение footer поверх карты -->
      <div class="footer-overlay">
        <img 
                      src="/assets/footer/footer.png" 
          alt="Footer" 
          class="footer-image"
        />
      </div>
    </div>
  </footer>
</template>

<script setup>
// Здесь будет логика для интеграции с Яндекс картами
// Возможно использование vue-yandex-maps или прямая интеграция через Yandex Maps API
</script>

<style lang="scss" scoped>
.footer {
  position: relative;
  width: 100%;
  margin-top: auto;
  overflow: visible;
}

.footer-container {
  position: relative;
  width: 100%;
  height: 420px; // Высота карты как указано в ТЗ
}

.map-container {
  width: 100%;
  height: 100%;
  background: #e0ebff;
  position: relative;
  
  &::before {
    content: '';
    position: absolute;
    top: -100px;
    left: 0;
    right: 0;
    height: 100px;
    background: rgba(224, 235, 255, 0.8) url('/assets/images/wave.png') no-repeat center bottom;
    background-size: 120% auto;
    pointer-events: none;
    z-index: 1;
  }
}

.map-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
  color: white;
  font-size: 18px;
  text-align: center;
  
  p {
    margin-bottom: 10px;
    font-weight: 600;
  }
  
  small {
    opacity: 0.8;
    font-size: 14px;
  }
}

.footer-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 150px; // Заходит на 150px снизу как указано в ТЗ
  pointer-events: none; // Изображение не интерактивно
  z-index: 2;
}

.footer-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

// Адаптивность
@media (max-width: 768px) {
  .footer-container {
    height: 350px;
  }
  
  .footer-overlay {
    height: 120px;
  }
  
  .map-placeholder {
    font-size: 16px;
    
    small {
      font-size: 12px;
    }
  }
}

@media (max-width: 480px) {
  .footer-container {
    height: 300px;
  }
  
  .footer-overlay {
    height: 100px;
  }
  
  .map-placeholder {
    font-size: 14px;
    padding: 20px;
    
    small {
      font-size: 11px;
    }
  }
}
</style> 