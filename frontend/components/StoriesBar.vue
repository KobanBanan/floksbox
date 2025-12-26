<template>
  <section class="stories-bar">
    <div class="container">
      <div v-if="stories.length > 0" class="stories-list">
        <div
          v-for="(story, index) in stories"
          :key="index"
          class="story-item"
          @click="openStory(index)"
        >
          <div class="story-image-wrapper">
            <img
              :src="story.icon"
              :alt="story.title"
              class="story-image"
            />
          </div>
          <div class="story-text">
            <div class="story-title">{{ story.title }}</div>
            <div class="story-subtitle">{{ story.subtitle }}</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Stories Viewer -->
    <Teleport to="body">
      <StoriesViewer
        v-if="isViewerOpen"
        :stories="stories"
        :initial-index="currentStoryIndex"
        @close="closeViewer"
      />
    </Teleport>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import StoriesViewer from './StoriesViewer.vue'

const stories = [
  {
    icon: '/stories/st_1/ico.png',
    title: 'Как заказать?',
    subtitle: 'Проведем от задумки до заказа',
    slides: [
      { type: 'image', src: '/stories/st_1/st1_1.jpg' },
      { type: 'image', src: '/stories/st_1/st1_2.jpg' },
      { type: 'image', src: '/stories/st_1/st1_3.jpg' },
      { type: 'image', src: '/stories/st_1/st1_4.jpg' },
      { type: 'image', src: '/stories/st_1/st1_5.jpg' }
    ]
  },
  {
    icon: '/stories/st_2/ico.png',
    title: 'Каталог FEFCO',
    subtitle: 'Выбираем готовые чертежи для печати',
    slides: [
      { type: 'image', src: '/stories/st_2/st2_1.jpg' },
      { type: 'image', src: '/stories/st_2/st2_2.jpg' },
      { type: 'image', src: '/stories/st_2/st2_3.jpg' },
      { type: 'image', src: '/stories/st_2/st2_4.jpg' },
      { type: 'image', src: '/stories/st_2/st2_5.jpg' },
      { type: 'image', src: '/stories/st_2/st2_6.jpg' }
    ]
  }
]

const isViewerOpen = ref(false)
const currentStoryIndex = ref(0)

const openStory = (index) => {
  currentStoryIndex.value = index
  isViewerOpen.value = true
}

const closeViewer = () => {
  isViewerOpen.value = false
}
</script>

<style lang="scss" scoped>
.stories-bar {
  padding: 20px 0;
  background: transparent;
  width: 100%;
  max-width: 100%;
  overflow-x: hidden;
}

.container {
  max-width: 990px; /* выравниваем с шириной hero */
  margin: 0 auto;
  padding: 0 20px 0 10px; /* уменьшаем левый отступ для выравнивания с баннером */
}

.stories-list {
  display: flex;
  gap: 20px;
  justify-content: flex-start;
  flex-wrap: wrap;
  align-items: flex-start;
}

.story-item {
  display: flex;
  flex-direction: column;
  cursor: pointer;
  transition: opacity 0.3s ease, box-shadow 0.3s ease;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  overflow: visible;
  opacity: 0.8;
  width: 130px; /* компактнее, как в макете */
  flex-shrink: 0;
  min-height: 220px; /* единая высота */
  
  &:hover {
    opacity: 1;
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
  }
}

.story-image-wrapper {
  position: relative;
  overflow: visible;
  background: transparent;
  flex-shrink: 0;
  margin: -21px 0 0 0; /* поднимаем ещё на 5px */
  z-index: 1;
}

.story-image {
  display: block;
  max-width: 100%;
  height: auto;
  object-fit: contain; /* не растягиваем, сохраняем пропорции */
  display: block;
}

.story-text {
  padding: 12px 16px;
  font-family: 'Montserrat', sans-serif;
  position: relative;
  z-index: 2;
  background: #ffffff;
  border-radius: 0 0 12px 12px;
}

.story-title {
  font-weight: 700;
  font-size: 16px;
  color: #000;
  margin-bottom: 4px;
  line-height: 1.2;
}

.story-subtitle {
  font-weight: 400;
  font-style: italic;
  font-size: 14px;
  color: #666;
  line-height: 1.3;
}

@media (max-width: 768px) {
  .stories-list {
    gap: 15px;
  }
  
  .story-item {
    width: 120px;
    min-height: 190px;
  }
  
  .story-image-wrapper {
    margin-top: -19px;
  }
  
  .story-title {
    font-size: 14px;
  }
  
  .story-subtitle {
    font-size: 12px;
  }
  
  .story-text {
    padding: 10px 12px;
  }
}

@media (max-width: 480px) {
  .stories-list {
    gap: 12px;
  }
  
  .story-item {
    width: 110px;
    min-height: 175px;
  }
  
  .story-image-wrapper {
    margin-top: -15px;
  }
  
  .story-title {
    font-size: 12px;
  }
  
  .story-subtitle {
    font-size: 11px;
  }
  
  .story-text {
    padding: 8px 10px;
  }
}
</style>
