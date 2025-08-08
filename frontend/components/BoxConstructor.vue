<template>
  <div class="constructor-container">
    <button class="close-btn" @click="$emit('close')">×</button>
    
    <div class="constructor-content">
      <div class="constructor-left">
        <h2 class="constructor-title">Конструктор коробок</h2>
        
        <!-- Параметры коробки -->
        <div class="parameter-group">
          <div class="parameter">
            <label class="parameter-label">высота коробки</label>
            <div class="slider-container">
              <input 
                type="range" 
                v-model="height" 
                :min="minHeight" 
                :max="maxHeight" 
                step="1"
                class="slider"
              />
              <div class="slider-value">{{ height }}см</div>
              <div class="input-with-unit">
                <input 
                  type="number" 
                  v-model="height" 
                  :min="minHeight" 
                  :max="maxHeight" 
                  step="1"
                  class="manual-input"
                />
                <span class="unit-label">см</span>
              </div>
            </div>
          </div>
          
          <div class="parameter">
            <label class="parameter-label">диаметр коробки</label>
            <div class="slider-container">
              <input 
                type="range" 
                v-model="diameter" 
                :min="minDiameter" 
                :max="maxDiameter" 
                step="2"
                class="slider"
                @input="syncDiameterToInput"
              />
              <div class="slider-value">{{ diameter }}см</div>
              <div class="input-with-unit">
                <input 
                  type="number" 
                  v-model="diameterInput" 
                  :min="minDiameter" 
                  :max="maxDiameter" 
                  step="2"
                  class="manual-input"
                  :class="{ 'invalid': !isDiameterValid }"
                  @input="checkDiameterValidity"
                  @blur="correctDiameterIfNeeded"
                />
                <span class="unit-label">см</span>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Материалы -->
        <div class="material-group">
          <div class="material-option">
            <input 
              type="radio" 
              id="paper" 
              value="paper" 
              v-model="material"
              class="material-radio"
            />
            <label for="paper" class="material-label">
              <span class="radio-custom"></span>
              лиц. бумага
            </label>
          </div>
          
          <div class="material-option">
            <input 
              type="radio" 
              id="velvet" 
              value="velvet" 
              v-model="material"
              class="material-radio"
            />
            <label for="velvet" class="material-label">
              <span class="radio-custom"></span>
              бархат
            </label>
          </div>
        </div>
        
        <!-- Опция с крышкой -->
        <div class="lid-option">
          <label class="switch">
            <input type="checkbox" v-model="withLid" />
            <span class="switch-slider"></span>
          </label>
          <span class="lid-label">с крышкой</span>
        </div>
        
        <!-- Тираж -->
        <div class="circulation-group">
          <label class="circulation-label">Тираж (от 300 шт)</label>
          <input 
            type="number" 
            v-model="circulation" 
            :min="300" 
            class="circulation-input"
            placeholder="300"
          />
        </div>
        
        <!-- Итоговая цена -->
        <div class="price-section">
          <div class="price-label">Итого:</div>
          <div class="price-value">{{ calculatedPrice }}</div>
        </div>
        
        <!-- Кнопка заказа -->
        <button class="order-btn" @click="handleOrder">
          Оформить заказ у менеджера
        </button>
      </div>
      
      <!-- Визуализация коробки -->
      <div class="constructor-right">
        <div class="box-visualization">
          <div 
            class="box-image" 
            :class="{ 'with-lid': withLid, [material]: true }"
            :style="boxStyle"
          >
            <div class="box-main"></div>
            <div v-if="withLid" class="box-lid"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const emit = defineEmits(['close'])

// Параметры коробки
const height = ref(25)
const diameter = ref(20)
const material = ref('paper')
const withLid = ref(false)
const circulation = ref(300)

// Отдельное значение для поля ввода диаметра
const diameterInput = ref(20)

// Состояние валидации
const isDiameterValid = ref(true)

// Ограничения
const minHeight = 3
const maxHeight = 50
const minDiameter = 12
const maxDiameter = 30

// Вычисляемые свойства
const boxStyle = computed(() => ({
  height: `${Math.max(150, height.value * 6)}px`,
  width: `${Math.max(150, diameter.value * 8)}px`,
}))

const calculatedPrice = computed(() => {
  let basePrice = 50
  
  // Базовая цена зависит от размеров (значения теперь в см)
  const sizeMultiplier = (height.value * diameter.value) / 80
  basePrice *= sizeMultiplier
  
  // Материал
  if (material.value === 'velvet') {
    basePrice *= 1.5
  }
  
  // Крышка
  if (withLid.value) {
    basePrice *= 1.3
  }
  
  // Тираж (чем больше, тем дешевле за штуку)
  const circulationDiscount = Math.max(0.7, 300 / circulation.value)
  basePrice *= circulationDiscount
  
  // Общая стоимость за весь тираж
  const totalPrice = Math.round(basePrice * circulation.value)
  
  return totalPrice.toLocaleString('ru-RU')
})

function isValidDiameter(value) {
  const num = parseInt(value)
  
  // Проверяем, что значение числовое, в диапазоне и четное
  return !isNaN(num) && 
         num >= minDiameter && 
         num <= maxDiameter && 
         num % 2 === 0
}

function checkDiameterValidity(event) {
  const value = event.target.value
  isDiameterValid.value = value === '' || isValidDiameter(value)
  
  // Обновляем основное значение diameter только если введенное значение валидно
  if (isDiameterValid.value && value !== '') {
    diameter.value = parseInt(value)
  }
}

function syncDiameterToInput() {
  // Синхронизируем поле ввода с ползунком
  diameterInput.value = diameter.value
  isDiameterValid.value = true
}

function correctDiameterIfNeeded(event) {
  const value = parseInt(event.target.value)
  
  // Если поле пустое, устанавливаем текущее значение ползунка
  if (event.target.value === '') {
    diameterInput.value = diameter.value
    isDiameterValid.value = true
    return
  }
  
  // Если значение уже валидное, ничего не делаем
  if (isValidDiameter(value)) {
    isDiameterValid.value = true
    return
  }
  
  // Корректируем невалидное значение
  let correctedValue = value
  
  // Проверяем, что значение числовое
  if (isNaN(correctedValue)) {
    correctedValue = diameter.value // Возвращаем текущее значение ползунка
  } else {
    // Ограничиваем диапазон
    if (correctedValue < minDiameter) {
      correctedValue = minDiameter
    } else if (correctedValue > maxDiameter) {
      correctedValue = maxDiameter
    }
    
    // Приводим к ближайшему четному значению (шаг 2)
    if (correctedValue % 2 !== 0) {
      const lower = Math.floor(correctedValue / 2) * 2
      const upper = lower + 2
      
      // Выбираем ближайшее
      if (Math.abs(correctedValue - lower) <= Math.abs(correctedValue - upper)) {
        correctedValue = Math.max(lower, minDiameter)
      } else {
        correctedValue = Math.min(upper, maxDiameter)
      }
    }
  }
  
  // Обновляем и поле ввода, и основное значение
  diameterInput.value = correctedValue
  diameter.value = correctedValue
  isDiameterValid.value = true
}

function handleOrder() {
  // Здесь будет логика отправки заказа менеджеру
  const orderData = {
    height: height.value,
    diameter: diameter.value,
    material: material.value,
    withLid: withLid.value,
    circulation: circulation.value,
    price: calculatedPrice.value
  }
  
  console.log('Order data:', orderData)
  alert('Заказ отправлен менеджеру! Мы свяжемся с вами в ближайшее время.')
  emit('close')
}
</script>

<style scoped>
.constructor-container {
  position: relative;
  padding: 40px;
  max-width: 1000px;
  width: 100%;
}

.close-btn {
  position: absolute;
  top: 15px;
  right: 20px;
  background: none;
  border: none;
  font-size: 2rem;
  color: #999;
  cursor: pointer;
  transition: color 0.3s;
  z-index: 10;
}

.close-btn:hover {
  color: #333;
}

.constructor-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: start;
}

.constructor-left {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.constructor-title {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin: 0 0 20px 0;
}

.parameter-group {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.parameter {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.parameter-label {
  font-size: 14px;
  color: #666;
  font-weight: 500;
}

.slider-container {
  display: flex;
  align-items: center;
  gap: 15px;
}

.slider {
  flex: 1;
  height: 6px;
  background: #e0e0e0;
  border-radius: 3px;
  outline: none;
  appearance: none;
}

.slider::-webkit-slider-thumb {
  appearance: none;
  width: 20px;
  height: 20px;
  background: #6B4C93;
  border-radius: 50%;
  cursor: pointer;
}

.slider::-moz-range-thumb {
  width: 20px;
  height: 20px;
  background: #6B4C93;
  border-radius: 50%;
  cursor: pointer;
  border: none;
}

.slider-value {
  min-width: 60px;
  font-size: 14px;
  color: #333;
  font-weight: 500;
}

.input-with-unit {
  display: flex;
  align-items: center;
  gap: 8px;
}

.manual-input {
  width: 60px;
  padding: 8px 10px;
  border: 2px solid #e0e0e0;
  border-radius: 6px;
  font-size: 14px;
  text-align: center;
  transition: border-color 0.3s;
  background: #f9f9f9;
}

.manual-input:focus {
  outline: none;
  border-color: #6B4C93;
  background: #fff;
}

.manual-input.invalid {
  border-color: #dc3545;
  background: #fff5f5;
  color: #dc3545;
}

.manual-input.invalid:focus {
  border-color: #dc3545;
  box-shadow: 0 0 0 2px rgba(220, 53, 69, 0.2);
}

.manual-input::-webkit-outer-spin-button,
.manual-input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.manual-input {
  -moz-appearance: textfield;
}

.unit-label {
  font-size: 14px;
  color: #666;
  font-weight: 500;
  user-select: none;
}

.material-group {
  display: flex;
  gap: 30px;
}

.material-option {
  display: flex;
  align-items: center;
}

.material-radio {
  display: none;
}

.material-label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  font-size: 14px;
  color: #333;
}

.radio-custom {
  width: 16px;
  height: 16px;
  border: 2px solid #ddd;
  border-radius: 50%;
  position: relative;
  transition: all 0.3s;
}

.material-radio:checked + .material-label .radio-custom {
  border-color: #6B4C93;
  background: #6B4C93;
}

.material-radio:checked + .material-label .radio-custom::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 6px;
  height: 6px;
  background: white;
  border-radius: 50%;
}

.lid-option {
  display: flex;
  align-items: center;
  gap: 12px;
}

.switch {
  position: relative;
  display: inline-block;
  width: 50px;
  height: 24px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.switch-slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: .4s;
  border-radius: 24px;
}

.switch-slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}

.switch input:checked + .switch-slider {
  background-color: #6B4C93;
}

.switch input:checked + .switch-slider:before {
  transform: translateX(26px);
}

.lid-label {
  font-size: 14px;
  color: #333;
}

.circulation-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.circulation-label {
  font-size: 14px;
  color: #666;
  font-weight: 500;
}

.circulation-input {
  padding: 12px 15px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 16px;
  max-width: 150px;
  transition: border-color 0.3s;
}

.circulation-input:focus {
  outline: none;
  border-color: #6B4C93;
}

.price-section {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 20px 0;
  border-top: 2px solid #f0f0f0;
  margin-top: 10px;
}

.price-label {
  font-size: 18px;
  color: #333;
  font-weight: 600;
}

.price-value {
  font-size: 28px;
  font-weight: bold;
  color: #6B4C93;
}

.order-btn {
  background: linear-gradient(135deg, #c8e6c9 0%, #a5d6a7 100%);
  color: #2e7d32;
  border: none;
  padding: 18px 30px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.order-btn:hover {
  background: linear-gradient(135deg, #a5d6a7 0%, #81c784 100%);
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.constructor-right {
  display: flex;
  justify-content: center;
  align-items: center;
}

.box-visualization {
  position: relative;
  width: 100%;
  height: 400px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.box-image {
  position: relative;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.box-main {
  background: linear-gradient(145deg, #e3f2fd 0%, #bbdefb 100%);
  border: 2px solid #90caf9;
  border-radius: 10px;
  width: 100%;
  height: 80%;
  position: relative;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.box-image.velvet .box-main {
  background: linear-gradient(145deg, #f3e5f5 0%, #e1bee7 100%);
  border-color: #ce93d8;
}

.box-lid {
  background: linear-gradient(145deg, #c5e1a5 0%, #aed581 100%);
  border: 2px solid #9ccc65;
  border-radius: 8px;
  width: 105%;
  height: 15%;
  margin-top: -5px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.box-image.velvet .box-lid {
  background: linear-gradient(145deg, #d1c4e9 0%, #b39ddb 100%);
  border-color: #9575cd;
}

@media (max-width: 768px) {
  .constructor-content {
    grid-template-columns: 1fr;
    gap: 30px;
  }
  
  .constructor-container {
    padding: 20px;
  }
  
  .material-group {
    flex-direction: column;
    gap: 15px;
  }
  
  .box-visualization {
    height: 300px;
  }
}
</style>