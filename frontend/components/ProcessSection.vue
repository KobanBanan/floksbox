<template>
  <section class="process-section">
    <div class="process-container">
      <img
        class="process-image"
        src="/assets/process/process.png"
        alt="Процесс работы Floksbox"
        loading="lazy"
      />
    </div>
  </section>
</template>

<script setup>
// No script logic required for static image section
</script>

<style scoped>
.process-section {
  width: 100%;
}

.process-container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 8px 16px; /* уменьшили вертикальные отступы с 16px до 8px */
}

.process-image {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 12px;
}

@media (min-width: 1024px) {
  .process-container {
    padding: 12px 16px; /* уменьшили с 24px до 12px */
  }
}
</style>


