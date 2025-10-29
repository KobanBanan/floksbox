// https://nuxt.com/docs/api/configuration/nuxt-config
import { defineNuxtConfig } from 'nuxt/config'

const isDev = process.env.NODE_ENV !== 'production'
const defaultBackendUrl = isDev ? 'http://localhost:8000' : 'http://backend:8000'
const backendUrl = process.env.BACKEND_URL || defaultBackendUrl
const publicApiBase = process.env.NUXT_PUBLIC_API_BASE ?? ''
const publicMediaBase = process.env.NUXT_PUBLIC_MEDIA_BASE ?? ''
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
      strictPort: false,
      // More resilient file watching on Windows/OneDrive
      watch: {
        usePolling: true,
        interval: 300,
        awaitWriteFinish: {
          stabilityThreshold: 500,
          pollInterval: 300
        }
      },
      // Stabilize HMR websocket to avoid ECONNRESET during restarts
      hmr: {
        protocol: 'ws',
        host: '127.0.0.1',
        port: 24678,
        clientPort: 24678
      },
      // Прокси для API запросов
      proxy: isDev
        ? {
            '/api': {
              target: backendUrl,
              changeOrigin: true,
              rewrite: (path) => path
            },
            '/media': {
              target: backendUrl,
              changeOrigin: true,
              rewrite: (path) => path
            }
          }
        : undefined
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
  
  // Runtime configuration
  runtimeConfig: {
    public: {
      apiBase: publicApiBase,
      mediaBase: publicMediaBase
    }
  },

  // Настройки сборки
  nitro: {
    preset: 'node-server',
    routeRules: {
      '/api/**': { proxy: `${backendUrl}/api/**` },
      '/media/**': { proxy: `${backendUrl}/media/**` },
    }
  }
})
