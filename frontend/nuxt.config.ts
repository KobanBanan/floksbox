// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  
  // CSS конфигурация
  css: ['~/assets/styles/main.scss'],
  
  // Настройки сервера разработки
  devServer: {
    host: '0.0.0.0',
    port: 3000
  },
  
  // Vite конфигурация для разработки
  vite: {
    server: {
      allowedHosts: [
        'localhost',
        '127.0.0.1', 
        '415cb6b1a367.ngrok-free.app',
        '.ngrok-free.app',
        'all'
      ],
      host: '0.0.0.0',
      port: 3000,
      strictPort: false
    }
  },
  
  // SEO оптимизация
  app: {
    head: {
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      title: 'Floksbox',
      meta: [
        { name: 'description', content: 'Floksbox - ваш надежный партнер' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Days+One&display=swap' }
      ]
    }
  },
  
  // Настройки сборки
  nitro: {
    preset: 'node-server',
    devServer: {
      watch: true
    }
  }
})
