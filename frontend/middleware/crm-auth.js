export default defineNuxtRouteMiddleware(async () => {
  const { loadToken, fetchMe } = useCrm()
  loadToken()
  const me = await fetchMe()
  if (!me) {
    return navigateTo('/crm/login')
  }
})
