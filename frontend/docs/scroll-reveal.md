# Scroll Reveal Анимации

Система scroll reveal анимаций позволяет элементам появляться плавно при прокрутке страницы.

## Использование

### Базовые классы

```html
<!-- Базовый класс для всех scroll reveal элементов -->
<div class="scroll-reveal">
  Содержимое появится при прокрутке
</div>
```

### Типы анимаций

```html
<!-- Появление снизу вверх (по умолчанию) -->
<div class="scroll-reveal scroll-reveal-fade-up">
  Появляется снизу
</div>

<!-- Появление слева -->
<div class="scroll-reveal scroll-reveal-fade-left">
  Появляется слева
</div>

<!-- Появление справа -->
<div class="scroll-reveal scroll-reveal-fade-right">
  Появляется справа
</div>

<!-- Масштабирование -->
<div class="scroll-reveal scroll-reveal-scale">
  Увеличивается при появлении
</div>
```

### Задержки

```html
<!-- Задержка 0.1s -->
<div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-1">
  Появляется с задержкой 0.1s
</div>

<!-- Задержка 0.2s -->
<div class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-2">
  Появляется с задержкой 0.2s
</div>

<!-- Доступны задержки от 1 до 5 (0.1s - 0.5s) -->
```

### Компонент-обертка

Для удобства можно использовать компонент `ScrollRevealWrapper`:

```vue
<template>
  <ScrollRevealWrapper type="fade-up" :delay="1">
    <MyComponent />
  </ScrollRevealWrapper>
</template>
```

## Настройки

### CSS переменные

Анимации можно настроить через CSS:

```scss
.scroll-reveal-visible {
  animation-duration: 0.8s; // длительность анимации
  animation-timing-function: cubic-bezier(0.25, 0.46, 0.45, 0.94); // easing
}
```

### Accessibility

Система автоматически отключает анимации для пользователей с `prefers-reduced-motion: reduce`.

### Мобильные устройства

На мобильных устройствах анимации ускоряются для лучшей производительности.

## Примеры использования

### Последовательное появление секций

```vue
<template>
  <div>
    <section class="scroll-reveal scroll-reveal-fade-up">
      Первая секция
    </section>
    
    <section class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-1">
      Вторая секция (с задержкой)
    </section>
    
    <section class="scroll-reveal scroll-reveal-fade-up scroll-reveal-delay-2">
      Третья секция (с большей задержкой)
    </section>
  </div>
</template>
```

### Карточки с разными направлениями

```vue
<template>
  <div class="cards-grid">
    <div class="scroll-reveal scroll-reveal-fade-left">
      Карточка слева
    </div>
    
    <div class="scroll-reveal scroll-reveal-scale scroll-reveal-delay-1">
      Карточка в центре
    </div>
    
    <div class="scroll-reveal scroll-reveal-fade-right scroll-reveal-delay-2">
      Карточка справа
    </div>
  </div>
</template>
```

## Производительность

- Использует Intersection Observer API для эффективного отслеживания видимости
- Автоматически прекращает наблюдение за элементами после их появления
- Минимальное влияние на производительность
- Работает корректно при навигации между страницами в SPA
