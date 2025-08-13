<template>
  <section class="menu-section">
    <div class="menu-grid">
      <div
        v-for="(item, index) in menuItems"
        :key="index"
        class="menu-item"
        @mouseenter="setHover(index, true)"
        @mouseleave="setHover(index, false)"
      >
        <div
          class="item-frame"
          :style="{ '--bg-image': `url(${itemBackgrounds[index]})` }"
        >
          <div class="item-image-container">
            <img
              :src="hoveredItems[index] ? item.iconOn : item.iconOff"
              :alt="plainText(item.name)"
              class="item-image"
              :class="{ lifted: hoveredItems[index] }"
            />
          </div>
          <div class="item-text" :class="{ active: hoveredItems[index] }" v-html="item.name"></div>
        </div>
      </div>
    </div>
  </section>
  
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'

// 9 пунктов меню согласно ТЗ
const menuItems = [
  {
    name: 'Четырехклапанные<br>коробки',
    iconOn: '/assets/menu/for_on.png',
    iconOff: '/assets/menu/for_off.png'
  },
  {
    name: 'Гофролисты<br>',
    iconOn: '/assets/menu/blk_on.png',
    iconOff: '/assets/menu/blk_off.png'
  },
  {
    name: 'Сложная высечка<br>',
    iconOn: '/assets/menu/clp_on.png',
    iconOff: '/assets/menu/clp_off.png'
  },
  {
    name: 'Офсетная печать<br>',
    iconOn: '/assets/menu/plg_on.png',
    iconOff: '/assets/menu/plg_off.png'
  },
  {
    name: 'Подарочные<br>пакеты',
    iconOn: '/assets/menu/pkt_on.png',
    iconOff: '/assets/menu/pkt_off.png'
  },
  {
    name: 'Шляпные&nbsp;коробки<br>',
    iconOn: '/assets/menu/rnd_on.png',
    iconOff: '/assets/menu/rnd_off.png'
  },
  {
    name: 'Дизайнерская<br>упаковка',
    iconOn: '/assets/menu/dsg_on.png',
    iconOff: '/assets/menu/dsg_off.png'
  },
  {
    name: 'Кашированная<br>гофроупаковка',
    iconOn: '/assets/menu/klp_on.png',
    iconOff: '/assets/menu/klp_off.png'
  },
  {
    name: 'Гофроупаковка<br>с флексопечатью',
    iconOn: '/assets/menu/dvj_on.png',
    iconOff: '/assets/menu/dvj_off.png'
  }
]

// Состояние hover для каждого элемента (массив булевых значений)
const hoveredItems = ref(Array.from({ length: menuItems.length }, () => false))

const setHover = (index, isHovered) => {
  hoveredItems.value[index] = isHovered
}

// Случайный фон back_1..4 для каждой ячейки
const itemBackgrounds = reactive([])
onMounted(() => {
  const bgPool = ['/assets/menu/back_1.png', '/assets/menu/back_2.png', '/assets/menu/back_3.png', '/assets/menu/back_4.png']
  for (let i = 0; i < menuItems.length; i += 1) {
    const randomBg = bgPool[Math.floor(Math.random() * bgPool.length)]
    itemBackgrounds[i] = randomBg
  }
})

const plainText = (htmlText) => htmlText.replace(/<br\s*\/?>/gi, ' ')
</script>

<style lang="scss" scoped>
.menu-section {
  padding: 30px 0;
  background-color: transparent;
}

.menu-grid {
  width: 100%;
  max-width: 1200px; /* единая ширина */
  margin: 0 auto;
  padding: 0 20px; /* внутренние отступы */
  display: grid;
  grid-template-columns: repeat(5, minmax(200px, 1fr)); /* адаптируем под меньшую ширину */
  grid-template-rows: repeat(2, 1fr);
  gap: 50px 10px; /* еще больше увеличено с 30px до 50px */
  justify-items: center;
}

.menu-item {
  width: 100%;
  height: 250px; /* фиксированная высота для всех карточек */
  max-width: 220px; /* фиксированная ширина для всех карточек */
}

/* Позиционирование элементов нижнего ряда по центру */
.menu-item:nth-child(6) {
  grid-column: 1;
  grid-row: 2;
}

.menu-item:nth-child(7) {
  grid-column: 2;
  grid-row: 2;
}

.menu-item:nth-child(8) {
  grid-column: 3;
  grid-row: 2;
}

.menu-item:nth-child(9) {
  grid-column: 4;
  grid-row: 2;
}

.item-frame {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 8px;
  overflow: visible; /* изменено с hidden чтобы текст мог быть вне */
  cursor: pointer;
  outline: none;
  transition: transform 0.3s ease;
  display: flex;
  flex-direction: column;
  min-height: 250px; /* минимальная высота для одинаковости */

  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 200px; /* фиксированная высота для области фона */
    background-image: var(--bg-image);
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    opacity: 0.9; /* 90% видимость по умолчанию */
    transition: opacity 0.2s ease;
    border-radius: 8px 8px 0 0; /* скругление только сверху */
  }

  &:hover::before {
    opacity: 1; /* 100% при наведении */
  }

  &:hover {
    transform: translateY(-4px);
  }
}

.item-image-container {
  position: relative;
  height: 200px; /* фиксированная высота для области изображения */
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1; /* над фоном */
  padding: 15px;
}

.item-image {
  width: 150px; /* уменьшено для лучшего размещения */
  height: 150px;
  object-fit: contain;
  transition: transform 0.3s ease;

  &.lifted {
    transform: translateY(-5px); /* небольшой подъем при ховере */
  }
}

.item-text {
  position: relative;
  background: rgba(255, 255, 255, 0.95); /* полупрозрачный белый фон */
  margin: 0 0 0 0; /* убрали отрицательные отступы */
  border-radius: 0 0 8px 8px; /* скругление только снизу */
  z-index: 2;
  font-family: 'Days', sans-serif;
  font-weight: 400;
  font-size: 13px; /* слегка уменьшено для лучшего размещения */
  line-height: 1.2;
  color: #000000;
  text-align: center;
  user-select: none;
  padding: 12px 8px; /* увеличенные вертикальные отступы */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* легкая тень */
  transition: all 0.3s ease;
  height: 50px; /* фиксированная высота для текстовой области */
  display: flex;
  align-items: center;
  justify-content: center;

  &.active {
    background: rgba(255, 255, 255, 1); /* полностью белый при ховере */
    transform: translateY(-2px);
  }
}

/* Адаптивность */
@media (max-width: 1440px) {
  .menu-item { 
    max-width: 200px; 
    height: 230px; /* слегка уменьшено для больших экранов */
  }
  .item-frame { min-height: 230px; }
  .item-image-container { height: 180px; }
}

@media (max-width: 1200px) {
  .menu-grid { 
    width: 95%; 
    grid-template-columns: repeat(4, minmax(200px, 1fr)); 
    gap: 40px 16px; /* еще больше увеличено с 25px до 40px */
  }
  .menu-item { 
    max-width: 180px; 
    height: 210px; 
  }
  .item-frame { min-height: 210px; }
  .item-image-container { height: 160px; }
}

@media (max-width: 992px) {
  .menu-grid { 
    width: 95%; 
    grid-template-columns: repeat(3, minmax(180px, 1fr)); 
    gap: 35px 14px; /* еще больше увеличено с 22px до 35px */
  }
  .menu-item { 
    max-width: 200px; 
    height: 220px; 
  }
  .item-frame { min-height: 220px; }
  .item-image-container { height: 170px; }
}

@media (max-width: 768px) {
  .menu-grid { 
    width: 90%; 
    grid-template-columns: repeat(2, 1fr); 
    gap: 30px 12px; /* еще больше увеличено с 20px до 30px */
  }
  .menu-item { 
    max-width: 160px; 
    height: 180px; 
  }
  .item-frame { min-height: 180px; }
  .item-image-container { height: 130px; }
  .item-image { width: 80px; height: 80px; } /* адаптировано под новую структуру */
  .item-text { 
    font-size: 10px; /* уменьшено для лучшего размещения */
    height: 50px;
    padding: 8px 4px;
  }
}

@media (max-width: 480px) {
  .menu-grid { 
    width: 95%; 
    grid-template-columns: 1fr; 
    gap: 25px; /* еще больше увеличено с 18px до 25px */
  }
  .menu-section { padding: 20px 0; }
  .menu-item { 
    max-width: 250px; 
    height: 200px;
    margin: 0 auto; /* центрирование для одноколоночного макета */
  }
  .item-frame { min-height: 200px; }
  .item-image-container { height: 150px; }
  .item-image { width: 100px; height: 100px; } /* больше для одноколоночного макета */
  .item-text { 
    font-size: 11px; /* увеличено для лучшей читаемости */
    height: 50px;
    padding: 10px 8px;
  }
}
</style>