import { defineConfig } from 'vite'

export default defineConfig({
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
}) 