<template>
  <section class="menu-section" ref="sectionRef">
    <div class="menu-inner">
      <div class="parallax-box parallax-center">
        <img ref="bgImgRef" src="/assets/menu/kb1.png" alt="Фоновая графика" class="parallax-img" />
      </div>
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
    </div>
  </section>
  
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted, nextTick } from 'vue'

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

// Простой кастомный параллакс, чтобы точно двигалось
const sectionRef = ref(null)
const bgImgRef = ref(null)
let rafId = 0

const updateParallax = () => {
  const sectionEl = sectionRef.value
  const bgEl = bgImgRef.value
  if (!sectionEl || !bgEl) return
  const rect = sectionEl.getBoundingClientRect()
  const viewportH = window.innerHeight || 800
  const t = Math.max(-1, Math.min(1, (rect.top + rect.height / 2 - viewportH / 2) / viewportH))
  const amplitude = Math.min(200, Math.max(120, rect.height * 0.2))
  bgEl.style.transform = `translate3d(0, ${t * amplitude}px, 0) scale(1.35)`
}

const onScrollResize = () => {
  if (rafId) cancelAnimationFrame(rafId)
  rafId = requestAnimationFrame(updateParallax)
}

onMounted(async () => {
  const bgPool = ['/assets/menu/back_1.png', '/assets/menu/back_2.png', '/assets/menu/back_3.png', '/assets/menu/back_4.png']
  for (let i = 0; i < menuItems.length; i += 1) {
    const randomBg = bgPool[Math.floor(Math.random() * bgPool.length)]
    itemBackgrounds[i] = randomBg
  }
  if (process.client) {
    await nextTick()
    const imgs = [bgImgRef.value].filter(Boolean)
    await Promise.all(imgs.map(img => (img.complete ? Promise.resolve() : new Promise(res => img.addEventListener('load', res, { once: true })))) )
    updateParallax()
    window.addEventListener('scroll', onScrollResize, { passive: true })
    window.addEventListener('resize', onScrollResize)
  }
})

onUnmounted(() => {
  if (process.client) {
    window.removeEventListener('scroll', onScrollResize)
    window.removeEventListener('resize', onScrollResize)
  }
})

const plainText = (htmlText) => htmlText.replace(/<br\s*\/?>/gi, ' ')
</script>

<style lang="scss" scoped>
.menu-section {
  position: relative;
  padding: 30px 0;
  background-color: transparent;
  overflow: visible;
}

.menu-inner {
  position: relative;
  max-width: 1400px;
  margin: 0 auto;
}

.parallax-box {
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  transform: translateY(-50%);
  width: 1200px;
  height: auto;
  pointer-events: none;
  z-index: -1; /* ниже всей сетки */
}

.parallax-center { margin: 0 auto; }

.parallax-img {
  display: block;
  width: 100%;
  height: auto;
}

.menu-grid {
  width: 100%;
  max-width: 1200px; /* единая ширина */
  margin: 0 auto;
  padding: 0 20px; /* внутренние отступы */
  display: grid;
  grid-template-columns: repeat(3, 180px); /* 3 колонки по 180px каждая */
  grid-template-rows: repeat(3, 1fr); /* 3 ряда для сетки 3x3 */
  gap: 40px 100px; /* 40px между горизонтальными рядами, 100px между вертикальными столбцами */
  justify-items: center;
  justify-content: center;
  position: relative;
  z-index: 1; /* поверх параллакса */
}

.menu-item {
  width: 100%;
  height: 220px; /* уменьшенная высота для более компактного вида */
  max-width: 180px; /* ширина 180px */
}

/* Элементы автоматически располагаются в сетке 3x3 */

.item-frame {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 8px;
  overflow: visible;
  cursor: pointer;
  outline: none;
  transition: transform 0.3s ease;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  min-height: 220px;

  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 170px;
    background-image: var(--bg-image);
    background-size: 100% 100%;
    background-position: center;
    background-repeat: no-repeat;
    opacity: 0.9;
    transition: opacity 0.2s ease;
    border-radius: 8px 8px 0 0;
    z-index: 0; /* фон ниже контента карточки и ниже параллакса */
  }

  &:hover::before {
    opacity: 1;
  }

  &:hover {
    transform: translateY(-4px);
  }
}

.item-image-container {
  position: relative;
  height: 170px;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1;
  padding: 15px;
  flex-shrink: 0; /* не позволяем сжиматься */
}

.item-image {
  width: 165px; /* увеличено на 10% (150px + 15px) */
  height: 165px;
  object-fit: contain;
  transition: transform 0.3s ease;

  &.lifted {
    transform: translateY(-20px); /* подъем на 20px при ховере */
  }
}

.item-text {
  position: relative;
  width: 100%;
  background: transparent;
  border-radius: 0 0 8px 8px;
  z-index: 10; /* высокий z-index чтобы быть поверх всего */
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
  flex-shrink: 0;
  margin-top: 0; /* убираем любые отступы */

  &.active {
    background: transparent;
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
    grid-template-columns: repeat(3, 1fr); /* сохраняем 3 колонки */
    gap: 25px 15px;
  }
  .parallax-box { width: 900px; }
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
    grid-template-columns: repeat(3, 1fr); /* сохраняем 3 колонки */
    gap: 20px 12px;
  }
  .parallax-box { width: 800px; }
  .menu-item { 
    max-width: 180px; 
    height: 200px; 
  }
  .item-frame { min-height: 200px; }
  .item-image-container { height: 150px; }
}

@media (max-width: 768px) {
  .menu-grid { 
    width: 90%; 
    grid-template-columns: repeat(2, 1fr); 
    gap: 30px 12px; /* еще больше увеличено с 20px до 30px */
  }
  .parallax-box { display: none; }
  .menu-item { 
    max-width: 160px; 
    height: 180px; 
  }
  .item-frame { min-height: 180px; }
  .item-image-container { height: 130px; }
  .item-image { width: 88px; height: 88px; } /* увеличено на 10% (80px + 8px) */
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
  .item-image { width: 110px; height: 110px; } /* увеличено на 10% (100px + 10px) */
  .item-text { 
    font-size: 11px; /* увеличено для лучшей читаемости */
    height: 50px;
    padding: 10px 8px;
  }
}
</style>