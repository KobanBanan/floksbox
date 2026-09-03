<template>
  <section class="menu-section" :class="{ 'menu-section--catalog': catalogLayout }" ref="sectionRef">
    <div class="menu-inner">
      <div class="parallax-box parallax-center" />
      <div class="menu-grid" :class="{ 'menu-grid--catalog': catalogLayout }">
        <div
          v-for="(item, index) in menuItems"
          :key="index"
          class="menu-item"
          @mouseenter="setHover(index, true)"
          @mouseleave="setHover(index, false)"
          @click="navigateToCategory(item.route)"
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
            <div class="item-content">
              <div class="item-text" :class="{ active: hoveredItems[index] }" v-html="item.name" />
              <p v-if="catalogLayout" class="item-description">{{ item.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive, onMounted, nextTick } from 'vue'
import { catalogMenuItems } from '../composables/useCatalogMenuItems'

const props = defineProps({
  catalogLayout: {
    type: Boolean,
    default: false,
  },
})

const menuItems = catalogMenuItems.filter((item) => item.route !== '/fefco')

const hoveredItems = ref(Array.from({ length: menuItems.length }, () => false))

const setHover = (index, isHovered) => {
  hoveredItems.value[index] = isHovered
}

const itemBackgrounds = reactive([])
const sectionRef = ref(null)

onMounted(async () => {
  const bgPool = [
    '/assets/menu/back_1.png',
    '/assets/menu/back_2.png',
    '/assets/menu/back_3.png',
    '/assets/menu/back_4.png',
  ]
  for (let i = 0; i < menuItems.length; i += 1) {
    const randomBg = bgPool[Math.floor(Math.random() * bgPool.length)]
    itemBackgrounds[i] = randomBg
  }
  if (process.client) {
    await nextTick()
  }
})

const plainText = (htmlText) => htmlText.replace(/<br\s*\/?>/gi, ' ')

const navigateToCategory = (route) => {
  if (route) {
    navigateTo(route)
  }
}
</script>

<style lang="scss" scoped>
.menu-section {
  position: relative;
  padding: 15px 0;
  background-color: transparent;
  overflow: hidden;
  width: 100vw;
  margin-left: calc(-50vw + 50%);
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
  width: 100%;
  height: auto;
  pointer-events: none;
  z-index: -1;
}

.parallax-center {
  margin: 0 auto;
  width: 100%;
}

.menu-grid {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: grid;
  grid-template-columns: repeat(3, 180px);
  grid-template-rows: repeat(3, 1fr);
  gap: 40px 100px;
  justify-items: center;
  justify-content: center;
  position: relative;
  z-index: 1;
}

.menu-item {
  width: 100%;
  height: 220px;
  max-width: 180px;
}

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
    z-index: 0;
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
  flex-shrink: 0;
}

.item-image {
  width: 165px;
  height: 165px;
  object-fit: contain;
  transition: transform 0.3s ease;

  &.lifted {
    transform: translateY(-20px);
  }
}

.item-content {
  position: relative;
  width: 100%;
  z-index: 10;
}

.item-text {
  position: relative;
  width: 100%;
  background: transparent;
  border-radius: 0 0 8px 8px;
  font-family: 'Days One', cursive;
  font-weight: 400;
  font-size: 13px;
  line-height: 1.2;
  color: #000000;
  text-align: center;
  user-select: none;
  padding: 12px 8px;
  transition: all 0.3s ease;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  margin-top: 0;

  &.active {
    background: transparent;
    transform: translateY(-2px);
  }
}

.item-description {
  display: none;
}

@media (min-width: 993px) {
  .menu-section--catalog {
    width: 100%;
    margin-left: 0;
    padding: 24px 0 10px;
    overflow: visible;
  }

  .menu-section--catalog .menu-inner {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 40px;
    overflow: visible;
  }

  .menu-grid--catalog {
    width: calc(100% + 48px);
    max-width: none;
    margin-left: -24px;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    grid-template-rows: repeat(3, auto);
    gap: 22px 20px;
    padding: 0;
    justify-items: stretch;
    justify-content: stretch;
  }

  .menu-grid--catalog .menu-item {
    max-width: none;
    height: auto;
    width: 100%;
  }

  .menu-grid--catalog .item-frame {
    flex-direction: row;
    align-items: center;
    gap: 18px;
    min-height: 156px;
    height: 100%;
    padding: 8px 18px 8px 0;
    background: transparent;
    border-radius: 8px;
    box-shadow: none;
    overflow: visible;

    &::before {
      display: block;
      top: 0;
      left: 0;
      right: 0;
      height: 100%;
      border-radius: 8px;
      opacity: 1;
      background-size: 100% 100%;
    }

    &:hover {
      transform: translateY(-4px);
      box-shadow: none;
    }
  }

  .menu-grid--catalog .item-image-container {
    flex: 0 0 165px;
    width: 165px;
    height: 165px;
    min-height: 165px;
    padding: 0;
    margin-left: -16px;
    background: transparent;
    border-radius: 0;
    overflow: visible;
    z-index: 2;
    justify-content: center;
    align-items: flex-end;
  }

  .menu-grid--catalog .item-image {
    display: block;
    width: 165px;
    height: 165px;
    min-width: 165px;
    min-height: 165px;
    max-width: none;
    max-height: none;
    object-fit: contain;
    flex-shrink: 0;

    &.lifted {
      transform: translateY(-20px);
    }
  }

  .menu-grid--catalog .item-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-width: 0;
    padding: 4px 0 4px 0;
    margin-left: 0;
    z-index: 1;
  }

  .menu-grid--catalog .item-text {
    height: auto;
    min-height: 0;
    padding: 0 0 8px;
    text-align: left;
    justify-content: flex-start;
    font-size: 0.95rem;
    line-height: 1.25;

    &.active {
      transform: translateY(-2px);
    }
  }

  .menu-grid--catalog .item-description {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    margin: 0;
    font-family: 'Montserrat', sans-serif;
    font-size: 0.78rem;
    line-height: 1.45;
    color: #5a6478;
    text-align: left;
  }
}

@media (min-width: 993px) and (max-width: 1024px) {
  .menu-section--catalog .menu-inner {
    padding: 0 20px;
  }
}

@media (max-width: 1440px) {
  .menu-item {
    max-width: 200px;
    height: 230px;
  }
  .item-frame {
    min-height: 230px;
  }
  .item-image-container {
    height: 180px;
  }
}

@media (max-width: 1200px) {
  .menu-grid {
    width: 95%;
    grid-template-columns: repeat(3, 1fr);
    gap: 25px 15px;
  }
  .parallax-box {
    width: 100%;
  }
  .menu-item {
    max-width: 180px;
    height: 210px;
  }
  .item-frame {
    min-height: 210px;
  }
  .item-image-container {
    height: 160px;
  }
}

@media (max-width: 992px) {
  .menu-grid {
    width: 95%;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px 12px;
  }
  .parallax-box {
    width: 100%;
  }
  .menu-item {
    max-width: 180px;
    height: 200px;
  }
  .item-frame {
    min-height: 200px;
  }
  .item-image-container {
    height: 150px;
  }

  .menu-grid--catalog {
    grid-template-columns: repeat(3, 1fr);
    gap: 20px 12px;
    padding: 0 20px;
  }

  .menu-grid--catalog .menu-item {
    max-width: 180px;
    height: 200px;
  }

  .menu-grid--catalog .item-frame {
    flex-direction: column;
    align-items: center;
    min-height: 200px;
    padding: 0;
    background: transparent;
    border-radius: 8px;
    box-shadow: none;

    &::before {
      display: block;
      height: 170px;
    }

    &:hover {
      transform: translateY(-4px);
      box-shadow: none;
    }
  }

  .menu-grid--catalog .item-image-container {
    flex: none;
    width: 100%;
    height: 150px;
    min-height: 0;
    padding: 15px;
    margin-left: 0;
    background: transparent;
    border-radius: 0;
  }

  .menu-grid--catalog .item-image {
    display: block;
    width: 165px;
    height: 165px;
    min-width: 0;
    min-height: 0;
  }

  .menu-grid--catalog .item-content {
    padding: 0;
  }

  .menu-grid--catalog .item-text {
    text-align: center;
    justify-content: center;
    height: 50px;
    padding: 12px 8px;
    font-size: 13px;
  }

  .menu-grid--catalog .item-description {
    display: none;
  }
}

@media (max-width: 768px) {
  .menu-grid {
    width: 95%;
    grid-template-columns: repeat(3, minmax(90px, 1fr));
    gap: 18px 10px;
  }
  .parallax-box {
    display: none;
  }
  .menu-item {
    max-width: 140px;
    height: 160px;
  }
  .item-frame {
    min-height: 160px;
  }
  .item-image-container {
    height: 110px;
  }
  .item-image {
    width: 82px;
    height: 82px;
  }
  .item-text {
    font-size: 10px;
    height: 46px;
    padding: 6px 4px;
  }

  .menu-grid--catalog .menu-item {
    max-width: 140px;
    height: 160px;
  }

  .menu-grid--catalog .item-frame {
    min-height: 160px;
  }

  .menu-grid--catalog .item-image-container {
    height: 110px;
  }

  .menu-grid--catalog .item-image {
    width: 82px;
    height: 82px;
  }

  .menu-grid--catalog .item-text {
    font-size: 10px;
    height: 46px;
    padding: 6px 4px;
  }
}

@media (max-width: 480px) {
  .menu-grid {
    width: 95%;
    grid-template-columns: repeat(3, minmax(90px, 1fr));
    gap: 16px 8px;
  }
  .menu-section {
    padding: 20px 0;
  }
  .menu-item {
    max-width: 130px;
    height: 150px;
    margin: 0 auto;
  }
  .item-frame {
    min-height: 150px;
  }
  .item-image-container {
    height: 100px;
  }
  .item-image {
    width: 76px;
    height: 76px;
  }
  .item-text {
    font-size: 10px;
    height: 44px;
    padding: 6px 4px;
  }

  .menu-grid--catalog .menu-item {
    max-width: 130px;
    height: 150px;
  }

  .menu-grid--catalog .item-frame {
    min-height: 150px;
  }

  .menu-grid--catalog .item-image-container {
    height: 100px;
  }

  .menu-grid--catalog .item-image {
    width: 76px;
    height: 76px;
  }

  .menu-grid--catalog .item-text {
    font-size: 10px;
    height: 44px;
    padding: 6px 4px;
  }
}
</style>
