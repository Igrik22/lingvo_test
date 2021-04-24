import Login from '@/components/Login'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/Login',
    name: 'Login',
    component: Login
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
