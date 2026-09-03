<template>
  <div class="constructor-container">
    
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
           v-model.number="height" 
                :min="minHeight" 
                :max="maxHeight" 
                step="1"
                class="slider"
                :style="{ '--slider-progress': heightProgress + '%' }"
              />
              <div class="input-with-unit">
                <input 
                  type="number" 
                  v-model.number="height" 
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
            <label class="parameter-label">ширина коробки</label>
            <div class="slider-container">
              <input 
                type="range" 
                v-model.number="diameter" 
                :min="minDiameter" 
                :max="maxDiameter" 
                step="2"
                class="slider"
                :style="{ '--slider-progress': diameterProgress + '%' }"
                @input="syncDiameterToInput"
              />
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
        
        <!-- Цвет коробки -->
        <div class="color-group">
          <label class="parameter-label" for="box-color">цвет коробки</label>
          <div class="color-picker-row">
            <input
              id="box-color"
              v-model="boxColor"
              type="color"
              class="color-input"
              aria-label="Выбор цвета коробки"
            />
            <span class="color-value">{{ boxColor }}</span>
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
        
        
        
        <!-- Кнопка заказа -->
        <button class="order-btn" @click="handleOrder">
          Оформить заказ у менеджера
        </button>
      </div>
      
      <!-- Визуализация коробки: один контейнер, PNG слоями -->
      <div class="constructor-right">
        <div class="box-visualization" ref="viewportRef">
          <div class="layers-zoom" :style="zoomStyle">
            <div class="layers-container" :style="stageStyle">
              <img
                id="rb_back"
                :src="layerBackSrc"
                alt=""
                class="box-layer box-layer--back"
              />
              <img
                id="rb_bottom"
                :src="layerBottomSrc"
                alt=""
                class="box-layer box-layer--bottom"
              />
              <div
                v-if="withLid"
                class="box-layer box-layer--top-fill"
                :style="topColorFillStyle"
                aria-hidden="true"
              />
              <img
                id="rb_top"
                :src="layerTopSrc"
                alt=""
                class="box-layer box-layer--top"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount, watch, nextTick } from 'vue'

const emit = defineEmits(['close'])
const { openOrderRequest } = useOrderRequest()

// Параметры коробки
const height = ref(25) // см
const diameter = ref(20) // см (ширина)
const material = ref('paper')
const withLid = ref(true)
const circulation = ref(300)
const boxColor = ref('#5e3085')

// Отдельное значение для поля ввода диаметра
const diameterInput = ref(20)

// Состояние валидации
const isDiameterValid = ref(true)

// Ограничения
const minHeight = 3
const maxHeight = 50
const minDiameter = 12
const maxDiameter = 30

// Новая карта ширины: точные соответствия см → пиксели
function mapWidthCmToPx(cm) {
  const clamped = Math.min(Math.max(cm, minDiameter), maxDiameter)
  const even = clamped % 2 === 0 ? clamped : clamped - 1
  const widthMap = {
    12: 268,
    14: 314,
    16: 359,
    18: 405,
    20: 450,
    22: 496,
    24: 541,
    26: 587,
    28: 632,
    30: 678
  }
  return widthMap[even]
}

// Новая карта высоты: точные соответствия см → пиксели
function mapHeightCmToPx(cm) {
  const clamped = Math.min(Math.max(cm, minHeight), maxHeight)
  const heightMap = {
    3: 305,
    4: 312,
    5: 319,
    6: 325,
    7: 332,
    8: 339,
    9: 346,
    10: 352,
    11: 359,
    12: 366,
    13: 379,
    14: 392,
    15: 405,
    16: 418,
    17: 431,
    18: 444,
    19: 457,
    20: 470,
    21: 479,
    22: 488,
    23: 497,
    24: 506,
    25: 515,
    26: 524,
    27: 533,
    28: 542,
    29: 551,
    30: 560,
    31: 569,
    32: 578,
    33: 587,
    34: 596,
    35: 605,
    36: 614,
    37: 623,
    38: 632,
    39: 641,
    40: 650,
    41: 659,
    42: 668,
    43: 677,
    44: 686,
    45: 695,
    46: 704,
    47: 713,
    48: 722,
    49: 731,
    50: 740
  }
  return heightMap[clamped]
}

const stageWidthPx = computed(() => Math.round(mapWidthCmToPx(diameter.value)))
const stageHeightPx = computed(() => Math.round(mapHeightCmToPx(height.value)))

// Зум отключен: прямоугольник отображается в фактическом масштабе

// Контейнер слоёв
const viewportRef = ref(null)
const scale = ref(1)
const isScaledReady = ref(false)
const needsZoom = computed(() => height.value > 30)
const needsMinorZoom = computed(() => height.value >= 17 && height.value <= 31)

function updateScale() {
  const el = viewportRef.value
  if (!el) return
  // базовые размеры сцены
  const sceneW = stageWidthPx.value
  const sceneH = stageHeightPx.value
  // доступная область (минус небольшой паддинг безопасности)
  // Используем одинаковый паддинг для всех устройств, чтобы сохранить пропорции
  const pad = 8
  const availW = Math.max(0, el.clientWidth - pad * 2)
  const availH = Math.max(0, el.clientHeight - pad * 2)
  // единый масштаб = min по осям, чтобы сохранять пропорции
  const s = Math.min(availW / sceneW, availH / sceneH)
  if (needsZoom.value) {
    // для >30 всегда вписываем сцену
    scale.value = Math.min(1, Math.max(0.1, s))
  } else if (needsMinorZoom.value) {
    // для 17..31 уменьшаем ТОЛЬКО если вылезает за пределы
    scale.value = s < 1 ? Math.min(1, Math.max(0.1, s)) : 1
  } else {
    scale.value = 1
  }
  if (!isScaledReady.value) isScaledReady.value = true
}

let resizeObserver
onMounted(async () => {
  // Ждём отрисовку DOM, затем считаем масштаб несколько раз для надёжности
  await nextTick()
  updateScale()
  requestAnimationFrame(() => updateScale())
  window.addEventListener('load', updateScale, { once: true })
  resizeObserver = new ResizeObserver(() => updateScale())
  if (viewportRef.value) resizeObserver.observe(viewportRef.value)
})

onBeforeUnmount(() => {
  if (resizeObserver) {
    resizeObserver.disconnect()
    resizeObserver = null
  }
  window.removeEventListener('load', updateScale)
})

watch([stageWidthPx, stageHeightPx, needsZoom, needsMinorZoom], () => updateScale())

/** Размер сцены — только от слайдеров ширины/высоты */
const stageStyle = computed(() => ({
  width: `${stageWidthPx.value}px`,
  height: `${stageHeightPx.value}px`,
  backgroundColor: boxColor.value,
  visibility: isScaledReady.value ? 'visible' : 'hidden'
}))

/** Зум вьюпорта — отдельно, не меняет раскладку слоёв */
const zoomStyle = computed(() => ({
  transform: `scale(${scale.value})`,
  transformOrigin: 'center bottom'
}))

// Источники изображений слоёв (B/N/K — прозрачные, цвет под ними)
const layerBackSrc = '/assets/images/B.png'
const layerBottomSrc = '/assets/images/N.png'
const layerTopColorMaskSrc = '/assets/images/K_CVETOCHEK.png'
const layerTopSrc = computed(() => {
  if (!withLid.value) {
    const even = Math.max(minDiameter, Math.min(maxDiameter, diameter.value))
    const size = even % 2 === 0 ? even : even - 1
    return `/assets/images/top_off_${size}.png`
  }
  return '/assets/images/K.png'
})

const topColorFillStyle = computed(() => ({
  backgroundColor: boxColor.value,
  WebkitMaskImage: `url(${layerTopColorMaskSrc})`,
  maskImage: `url(${layerTopColorMaskSrc})`,
  WebkitMaskSize: '100% 100%',
  maskSize: '100% 100%',
  WebkitMaskRepeat: 'no-repeat',
  maskRepeat: 'no-repeat',
  WebkitMaskPosition: 'center top',
  maskPosition: 'center top'
}))
// Прогресс ползунков для активной области
const heightProgress = computed(() => {
  const progress = ((height.value - minHeight) / (maxHeight - minHeight)) * 100
  return Math.min(100, Math.max(0, progress))
})

const diameterProgress = computed(() => {
  const progress = ((diameter.value - minDiameter) / (maxDiameter - minDiameter)) * 100
  return Math.min(100, Math.max(0, progress))
})

// расчёт цены удалён по требованию — блок Итого скрыт

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
  // Формируем детальное сообщение для шляпной коробки
  const materialName = material.value === 'paper' ? 'дизайнерской бумаги' : 'бархата'
  const lidText = withLid.value ? 'с крышкой' : 'без крышки'
  
  const message = `Мне интересна шляпная коробка ${diameter.value}см в ширину / ${height.value}см в высоту, ${lidText}, из ${materialName}, цвет ${boxColor.value}, в количестве ${circulation.value}`
  
  openOrderRequest(message)

  emit('close')
}
</script>

<style scoped>
.constructor-container {
  position: relative;
  padding: 40px;
  max-width: 1200px;
  width: 100%;
}

@media (max-width: 768px) {
  .constructor-container {
    padding: 20px 0;
    width: 100%;
    max-width: 100%;
  }
}

@media (max-width: 480px) {
  .constructor-container {
    padding: 15px 0;
    width: 100%;
    max-width: 100%;
  }
}



.constructor-content {
  display: grid;
  grid-template-columns: 420px 1fr; /* фиксируем ширину левой колонки */
  gap: 60px;
  align-items: start;
}

.constructor-left {
  display: flex;
  flex-direction: column;
  gap: 25px;
  min-width: 420px; /* не сужать левую часть */
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
  flex: 0 0 80%; /* Уменьшаем ширину на 20% */
  height: 6px;
  background: linear-gradient(to right, #bf82f9 0%, #bf82f9 var(--slider-progress, 50%), #e9d8f9 var(--slider-progress, 50%), #e9d8f9 100%);
  border-radius: 3px;
  outline: none;
  appearance: none;
  position: relative;
}

/* Активная область ползунка для WebKit */
.slider::-webkit-slider-runnable-track {
  height: 6px;
  background: transparent;
  border-radius: 3px;
}

/* Стили для Firefox */
.slider::-moz-range-track {
  height: 6px;
  background: #e9d8f9;
  border-radius: 3px;
  border: none;
}

.slider::-moz-range-progress {
  height: 6px;
  background: #bf82f9;
  border-radius: 3px;
}

.slider::-webkit-slider-thumb {
  appearance: none;
  width: 20px;
  height: 20px;
  background: #fbf6ff;
  border: 1px solid #bf82f9;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.2s ease;
  margin-top: -7px; /* Центрируем бегунок по вертикали относительно полоски */
}

.slider::-webkit-slider-thumb:hover {
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
}

.slider::-moz-range-thumb {
  width: 20px;
  height: 20px;
  background: #fbf6ff;
  border: 1px solid #bf82f9;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.2s ease;
  margin-top: -7px; /* Центрируем бегунок по вертикали относительно полоски */
}

.slider::-moz-range-thumb:hover {
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15);
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

.color-group {
  margin-bottom: 25px;
}

.color-picker-row {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-top: 10px;
}

.color-input {
  width: 52px;
  height: 52px;
  padding: 4px;
  border: 2px solid #e9d8f9;
  border-radius: 12px;
  background: #fff;
  cursor: pointer;
}

.color-input::-webkit-color-swatch-wrapper {
  padding: 0;
}

.color-input::-webkit-color-swatch {
  border: none;
  border-radius: 8px;
}

.color-value {
  font-family: 'Montserrat', sans-serif;
  font-size: 0.95rem;
  font-weight: 600;
  color: #55376e;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.material-group {
  display: flex;
  gap: 30px;
  align-items: center;
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
  border: 2px solid #bf82f9;
  border-radius: 50%;
  position: relative;
  transition: all 0.3s;
  background: #fbf6ff;
}

.material-radio:checked + .material-label .radio-custom {
  border-color: #bf82f9;
  background: #bf82f9;
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
  background-color: #fbf6ff;
  border: 2px solid #bf82f9;
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
  background-color: #bf82f9;
  transition: .4s;
  border-radius: 50%;
}

.switch input:checked + .switch-slider {
  background-color: #bf82f9;
  border-color: #bf82f9;
}

.switch input:checked + .switch-slider:before {
  background-color: white;
  transform: translateX(26px);
}

.lid-label {
  font-size: 14px;
  color: #333;
}

.circulation-group {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 30px;
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



.order-btn {
  background: #d0ff0a;
  color: #55376e;
  border: none;
  padding: 18px 30px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  align-self: flex-start;
  width: auto;
}

.order-btn:hover {
  background: #c4f000;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(208, 255, 10, 0.3);
}

.constructor-right {
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 560px; /* гарантируем место под визуализацию */
}

.box-visualization {
  position: relative;
  width: 100%;
  height: 400px;
  display: flex;
  justify-content: center;
  align-items: flex-end;
  overflow: hidden;
}

/* Зум только здесь — не влияет на расчёт размеров слоёв */
.layers-zoom {
  position: relative;
  flex-shrink: 0;
  will-change: transform;
}

/* Один контейнер: PNG накладываются друг на друга */
.layers-container {
  position: relative;
  isolation: isolate;
  --top-h: 286px;
  --bottom-h: 87px;
}

.box-layer {
  position: absolute;
  left: 0;
  width: 100%;
  box-sizing: border-box;
  pointer-events: none;
  display: block;
}

.box-layer--back {
  top: 0;
  height: 100%;
  object-fit: fill;
  object-position: center center;
  z-index: 0;
}

.box-layer--bottom {
  bottom: 0;
  height: var(--bottom-h);
  object-fit: fill;
  object-position: center bottom;
  z-index: 1;
}

.box-layer--top-fill {
  top: 0;
  height: var(--top-h);
  z-index: 2;
}

.box-layer--top {
  top: 0;
  height: var(--top-h);
  object-fit: fill;
  object-position: center top;
  z-index: 3;
}

@media (max-width: 768px) {
  .constructor-content {
    grid-template-columns: 1fr;
    gap: 30px;
    display: flex;
    flex-direction: column;
  }
  
  .constructor-container {
    padding: 20px;
  }
  
  .constructor-left {
    min-width: auto;
    order: 2; /* Бегунки идут вторыми */
  }
  
  .constructor-right {
    min-width: auto;
    width: 100%;
    padding: 20px 0;
    order: 1; /* Визуализация коробки идет первой */
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .material-group {
    flex-direction: column;
    gap: 15px;
  }
  
  .box-visualization {
    height: 400px;
    min-height: 400px;
    width: 100%;
    max-width: 100%;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: flex-end;
  }
  
  .layers-zoom,
  .layers-container {
    position: relative;
  }

  .box-layer {
    position: absolute;
    width: 100%;
    object-fit: fill;
  }
}

@media (max-width: 480px) {
  .box-visualization {
    height: 400px;
    min-height: 400px;
    padding: 0;
  }
  
  .constructor-container {
    padding: 15px;
  }
  
  .constructor-content {
    gap: 20px;
  }
  
  .constructor-right {
    padding: 15px 0;
  }
}
</style>