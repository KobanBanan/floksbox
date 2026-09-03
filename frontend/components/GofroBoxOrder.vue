<template>
  <div class="gofro-order">
    <h2 class="gofro-order__title">Закажите индивидуальный размер</h2>
    <p class="gofro-order__hint">Укажите размеры в миллиметрах (от {{ MIN }} до {{ MAX }})</p>

    <div class="gofro-order__fields">
      <div class="gofro-order__field">
        <label class="gofro-order__label" for="gofro-length">Длина</label>
        <div class="gofro-order__input-row">
          <input
            id="gofro-length"
            type="number"
            v-model.number="length"
            :min="MIN"
            :max="MAX"
            class="gofro-order__input"
            @blur="clampField('length')"
          />
          <span class="gofro-order__unit">мм</span>
        </div>
      </div>

      <div class="gofro-order__field">
        <label class="gofro-order__label" for="gofro-height">Высота</label>
        <div class="gofro-order__input-row">
          <input
            id="gofro-height"
            type="number"
            v-model.number="height"
            :min="MIN"
            :max="MAX"
            class="gofro-order__input"
            @blur="clampField('height')"
          />
          <span class="gofro-order__unit">мм</span>
        </div>
      </div>

      <div class="gofro-order__field">
        <label class="gofro-order__label" for="gofro-width">Ширина</label>
        <div class="gofro-order__input-row">
          <input
            id="gofro-width"
            type="number"
            v-model.number="width"
            :min="MIN"
            :max="MAX"
            class="gofro-order__input"
            @blur="clampField('width')"
          />
          <span class="gofro-order__unit">мм</span>
        </div>
      </div>
    </div>

    <button type="button" class="gofro-order__btn" @click="handleOrder">
      заказать у менеджера
    </button>
  </div>
</template>

<script setup>
const { openOrderRequest } = useOrderRequest()

const MIN = 30
const MAX = 1500

const length = ref(400)
const height = ref(200)
const width = ref(300)

const fields = { length, height, width }

function clampValue(value) {
  const n = Number(value)
  if (Number.isNaN(n)) return MIN
  return Math.min(MAX, Math.max(MIN, Math.round(n)))
}

function clampField(name) {
  const field = fields[name]
  if (field) field.value = clampValue(field.value)
}

function handleOrder() {
  clampField('length')
  clampField('height')
  clampField('width')

  const message = `Мне нужен гофрокороб индивидуального размера: длина ${length.value} мм, высота ${height.value} мм, ширина ${width.value} мм`
  openOrderRequest(message)
}
</script>

<style scoped>
.gofro-order {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 720px;
  margin: 0 auto;
  padding: 36px 40px;
  background: #fff;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  transform: none;
  writing-mode: horizontal-tb;
  direction: ltr;
  text-align: left;
  box-sizing: border-box;
}

.gofro-order * {
  transform: none;
  writing-mode: horizontal-tb;
}

.gofro-order__btn:hover {
  transform: translateY(-2px);
}

.gofro-order__title {
  font-family: 'Days One', cursive;
  font-size: 1.75rem;
  font-weight: 400;
  color: #5e3085;
  text-align: center;
  margin: 0 0 10px;
  line-height: 1.2;
}

.gofro-order__hint {
  font-family: 'Montserrat', sans-serif;
  font-size: 0.95rem;
  color: #666;
  text-align: center;
  margin: 0 0 28px;
  line-height: 1.5;
}

.gofro-order__fields {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
  margin-bottom: 28px;
}

.gofro-order__field {
  display: flex;
  flex-direction: column;
  gap: 8px;
  min-width: 0;
}

.gofro-order__label {
  font-family: 'Montserrat', sans-serif;
  font-size: 0.85rem;
  font-weight: 600;
  color: #333;
  text-transform: uppercase;
  letter-spacing: 0.4px;
}

.gofro-order__input-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.gofro-order__input {
  width: 100%;
  min-width: 0;
  padding: 12px 14px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 16px;
  font-family: 'Montserrat', sans-serif;
  text-align: center;
  box-sizing: border-box;
}

.gofro-order__input:focus {
  outline: none;
  border-color: #6b4c93;
}

.gofro-order__unit {
  flex-shrink: 0;
  font-size: 14px;
  color: #666;
  font-family: 'Montserrat', sans-serif;
}

.gofro-order__btn {
  display: block;
  width: 100%;
  max-width: 360px;
  margin: 0 auto;
  background: #d0ff0a;
  color: #55376e;
  border: none;
  padding: 18px 28px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 700;
  font-family: 'Montserrat', sans-serif;
  cursor: pointer;
  transition: background 0.3s, box-shadow 0.3s, transform 0.3s;
}

.gofro-order__btn:hover {
  background: #c4f000;
  box-shadow: 0 5px 15px rgba(208, 255, 10, 0.3);
}

@media (max-width: 768px) {
  .gofro-order {
    padding: 24px 18px;
    border-radius: 16px;
  }

  .gofro-order__fields {
    grid-template-columns: 1fr;
    gap: 16px;
  }
}
</style>
