import Login from '@/components/Login'
import register from '@/components/register'
import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home'
import HomeWork from '@/components/HomeWork'
import FinishedHomeWork from '@/components/FinishedHomeWork'

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
  },
  {
    path: '/homework',
    name: 'HomeWork',
    component: HomeWork
  },
  {
    path: '/finishedhomework',
    name: 'FinishedHomeWork',
    component: FinishedHomeWork
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
