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
  width: 90%;
  max-width: 1600px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(5, minmax(260px, 1fr));
  grid-template-rows: repeat(2, 1fr);
  gap: 10px;
  justify-items: center;
}

.menu-item {
  width: 100%;
  max-width: 340px;
  aspect-ratio: 340 / 210;
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
  overflow: hidden;
  cursor: pointer;
  outline: none;
  transition: transform 0.3s ease;

  &::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: var(--bg-image);
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    opacity: 0.9; /* 90% видимость по умолчанию */
    transition: opacity 0.2s ease;
  }

  &:hover::before {
    opacity: 1; /* 100% при наведении */
  }

  &:hover {
    transform: translateY(-4px);
  }
}

.item-image-container {
  position: absolute;
  top: 5%;
  left: 50%;
  transform: translateX(-50%);
  width: auto;
  height: auto;
  z-index: 1; /* над фоном */
}

.item-image {
  width: 200px;
  height: 200px;
  object-fit: contain;
  transition: transform 0.3s ease;
  transform: translateY(-37px);

  &.lifted {
    transform: translateY(-44px);
  }
}

.item-text {
  position: absolute;
  bottom: 15px; /* поднимаем выше для наложения на изображение */
  left: 0;
  right: 0;
  transform: none;
  z-index: 2; /* над изображением */
  font-family: 'Days', sans-serif;
  font-weight: 400;
  font-size: 18px;
  line-height: 1.2;
  color: #000000;
  text-align: center;
  user-select: none;
  padding: 0 8px;
  text-shadow: 0 0 2px rgba(255, 255, 255, 1), 
               0 0 4px rgba(255, 255, 255, 0.9), 
               0 0 8px rgba(255, 255, 255, 0.8),
               0 0 12px rgba(255, 255, 255, 0.6),
               0 0 16px rgba(255, 255, 255, 0.4);
}

/* Адаптивность */
@media (max-width: 1440px) {
  .menu-item { max-width: 260px; }
}

@media (max-width: 1200px) {
  .menu-grid { 
    width: 95%; 
    grid-template-columns: repeat(4, minmax(240px, 1fr)); 
    gap: 16px; 
  }
  .menu-item { max-width: 320px; }
}

@media (max-width: 992px) {
  .menu-grid { 
    width: 95%; 
    grid-template-columns: repeat(3, minmax(220px, 1fr)); 
    gap: 14px; 
  }
  .menu-item { max-width: 280px; }
}

@media (max-width: 768px) {
  .menu-grid { 
    width: 90%; 
    grid-template-columns: repeat(2, 1fr); 
    gap: 12px; 
  }
  .menu-item { max-width: 200px; }
  .item-image { width: 120px; height: 120px; }
  .item-text { font-size: 10px; }
}

@media (max-width: 480px) {
  .menu-grid { 
    width: 95%; 
    grid-template-columns: 1fr; 
    gap: 15px; 
  }
  .menu-section { padding: 20px 0; }
  .menu-item { max-width: 300px; }
  .item-text { font-size: 11px; }
}
</style>