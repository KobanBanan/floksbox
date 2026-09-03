const CURRENCY_CODE = 'RUB'
const BRAND = 'Floksbox'

function ensureDataLayer() {
  if (!import.meta.client) {
    return null
  }
  window.dataLayer = window.dataLayer || []
  return window.dataLayer
}

function productToEcommerce(product, { position, list } = {}) {
  const item = {
    id: String(product.id),
    name: product.name,
    brand: BRAND,
  }

  if (product.price != null && product.price !== '') {
    item.price = Number(product.price)
  }
  if (product.category_name) {
    item.category = product.category_name
  }
  if (product.dimensions) {
    item.variant = product.dimensions
  }
  if (position != null) {
    item.position = position
  }
  if (list) {
    item.list = list
  }

  return item
}

function pushEcommerce(actionType, payload) {
  const dataLayer = ensureDataLayer()
  if (!dataLayer) {
    return
  }

  dataLayer.push({
    ecommerce: {
      currencyCode: CURRENCY_CODE,
      [actionType]: payload,
    },
  })
}

export function useYandexEcommerce() {
  const trackDetail = (product) => {
    if (!product?.id) {
      return
    }
    pushEcommerce('detail', {
      products: [productToEcommerce(product)],
    })
  }

  const trackImpressions = (products, listName) => {
    if (!products?.length) {
      return
    }
    pushEcommerce('impressions', {
      products: products.map((product, index) =>
        productToEcommerce(product, { position: index + 1, list: listName }),
      ),
    })
  }

  const trackPurchase = (orderId, products) => {
    pushEcommerce('purchase', {
      actionField: { id: String(orderId) },
      products: products.map((product) => ({
        ...productToEcommerce(product),
        quantity: product.quantity ?? 1,
      })),
    })
  }

  const trackLead = (message) => {
    trackPurchase(`lead-${Date.now()}`, [
      {
        id: 'lead',
        name: message?.slice(0, 100) || 'Заявка менеджеру',
        price: 0,
        quantity: 1,
      },
    ])
  }

  return {
    trackDetail,
    trackImpressions,
    trackPurchase,
    trackLead,
    productToEcommerce,
  }
}
