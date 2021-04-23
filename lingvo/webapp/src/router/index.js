import Login from '@/components/Login'
import register from '@/components/register'
import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: register
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
