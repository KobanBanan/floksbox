<template>
  <div class="fallback-page">
    <HeaderSimple />
    <section class="content">
      <h1>Страница в разработке</h1>
      <p>Раздел «{{ pathLabel }}» пока недоступен.</p>
      <NuxtLink to="/" class="back-link">Вернуться на главную</NuxtLink>
    </section>
    <FooterNew />
  </div>
</template>

<script setup>
import HeaderSimple from '~/components/HeaderSimple.vue'
import FooterNew from '~/components/FooterNew.vue'

const route = useRoute()
const pathLabel = computed(() => Array.isArray(route.params.slug) ? '/' + route.params.slug.join('/') : String(route.params.slug || ''))
</script>

<style scoped>
.fallback-page { min-height: 100vh; display: flex; flex-direction: column; }
.content { max-width: 900px; margin: 80px auto; text-align: center; padding: 0 20px; }
h1 { font-family: 'Days One', cursive; color: #5e3085; margin-bottom: 12px; }
p { color: #555; margin-bottom: 20px; }
.back-link { color: #5e3085; text-decoration: none; font-weight: 600; }
.back-link:hover { text-decoration: underline; }
</style>


