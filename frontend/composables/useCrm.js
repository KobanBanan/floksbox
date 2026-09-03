const TOKEN_KEY = 'floksbox_crm_token'

export function useCrm() {
  const token = useState('crm_token', () => null)
  const user = useState('crm_user', () => null)

  const apiBase = computed(() => {
    const config = useRuntimeConfig()
    return (config.public.apiBase || '').replace(/\/+$/, '')
  })

  const apiUrl = (path) => `${apiBase.value}${path}`

  const loadToken = () => {
    if (!import.meta.client) return null
    if (!token.value) {
      token.value = localStorage.getItem(TOKEN_KEY)
    }
    return token.value
  }

  const setSession = (nextToken, nextUser) => {
    token.value = nextToken
    user.value = nextUser
    if (import.meta.client) {
      localStorage.setItem(TOKEN_KEY, nextToken)
    }
  }

  const clearSession = () => {
    token.value = null
    user.value = null
    if (import.meta.client) {
      localStorage.removeItem(TOKEN_KEY)
    }
  }

  const crmFetch = async (path, options = {}) => {
    loadToken()
    const headers = {
      ...(options.headers || {}),
    }
    if (token.value) {
      headers.Authorization = `Token ${token.value}`
    }
    if (options.body && !headers['Content-Type']) {
      headers['Content-Type'] = 'application/json'
    }

    return await $fetch(apiUrl(path), {
      ...options,
      headers,
    })
  }

  const login = async (username, password) => {
    const response = await crmFetch('/api/crm/login/', {
      method: 'POST',
      body: { username, password },
    })
    if (response.success) {
      setSession(response.token, response.user)
    }
    return response
  }

  const logout = async () => {
    try {
      if (token.value) {
        await crmFetch('/api/crm/logout/', { method: 'POST' })
      }
    } catch {
      // ignore network errors on logout
    } finally {
      clearSession()
    }
  }

  const fetchMe = async () => {
    loadToken()
    if (!token.value) return null
    try {
      const me = await crmFetch('/api/crm/me/')
      user.value = me
      return me
    } catch {
      clearSession()
      return null
    }
  }

  const fetchOrders = async (params = {}) => {
    return crmFetch('/api/crm/orders/', { query: params })
  }

  const fetchOrder = async (id) => {
    return crmFetch(`/api/crm/orders/${id}/`)
  }

  const updateOrder = async (id, payload) => {
    return crmFetch(`/api/crm/orders/${id}/`, {
      method: 'PATCH',
      body: payload,
    })
  }

  return {
    token,
    user,
    login,
    logout,
    fetchMe,
    fetchOrders,
    fetchOrder,
    updateOrder,
    clearSession,
    loadToken,
  }
}
