<template>
  <div 
    :class="[
      'scroll-reveal',
      animationType,
      delayClass
    ]"
  >
    <slot />
  </div>
</template>

<script setup>
const props = defineProps({
  type: {
    type: String,
    default: 'fade-up',
    validator: (value) => ['fade-up', 'fade-left', 'fade-right', 'scale'].includes(value)
  },
  delay: {
    type: Number,
    default: 0,
    validator: (value) => value >= 0 && value <= 5
  }
})

const animationType = computed(() => {
  return `scroll-reveal-${props.type}`
})

const delayClass = computed(() => {
  return props.delay > 0 ? `scroll-reveal-delay-${props.delay}` : ''
})
</script>

<style scoped>
/* Стили для wrapper будут наследоваться из main.scss */
</style>
