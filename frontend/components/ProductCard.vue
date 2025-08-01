<template>
  <div class="product-card" @click="goToProduct">
    <div class="product-image-wrapper">
      <img 
        :src="product.image_url || '/assets/images/mainpage.png'" 
        :alt="product.name"
        class="product-image"
        @error="handleImageError"
      />
    </div>
    <div class="product-info">
      <h3 class="product-name">{{ product.name }}</h3>
      <p class="product-dimensions" v-if="product.dimensions">{{ product.dimensions }}</p>
      <div class="product-price" v-if="product.price">
        {{ formatPrice(product.price) }} ₽
      </div>
      <div class="product-category" v-if="product.category_name">
        {{ product.category_name }}
      </div>
      <button class="details-button">
        Подробно
      </button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  product: {
    type: Object,
    required: true
  }
})

const router = useRouter()

const goToProduct = () => {
  router.push(`/product/${props.product.id}`)
}

const handleImageError = (event) => {
  event.target.src = '/assets/images/mainpage.png'
}

const formatPrice = (price) => {
  return new Intl.NumberFormat('ru-RU').format(price)
}
</script>

<style scoped>
.product-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s ease;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.product-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.product-image-wrapper {
  position: relative;
  width: 100%;
  height: 160px;
  overflow: hidden;
  background: #f8f9fa;
}

.product-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.product-card:hover .product-image {
  transform: scale(1.05);
}

.product-info {
  padding: 12px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.product-name {
  font-size: 14px;
  font-weight: 600;
  color: #2d3748;
  margin: 0;
  line-height: 1.3;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.product-dimensions {
  font-size: 12px;
  color: #718096;
  margin: 0;
}

.product-price {
  font-size: 16px;
  font-weight: 700;
  color: #1a365d;
  margin-top: auto;
}

.product-category {
  font-size: 12px;
  color: #a0aec0;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.details-button {
  background: #000000;
  color: white;
  border: none;
  padding: 8px 16px;
  font-size: 12px;
  font-weight: 500;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 8px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.details-button:hover {
  background: #333333;
  transform: translateY(-1px);
}

@media (max-width: 768px) {
  .product-image-wrapper {
    height: 120px;
  }
  
  .product-info {
    padding: 10px;
  }
  
  .product-name {
    font-size: 13px;
  }
  
  .product-price {
    font-size: 15px;
  }
  
  .details-button {
    font-size: 11px;
    padding: 6px 12px;
  }
}
</style> 