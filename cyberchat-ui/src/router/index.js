import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    redirect: '/chat'
  },
  {
    path: '/chat',
    name: 'Chat',
    component: () => import('../modules/chat/index.vue')
  },
  {
    path: '/contacts',
    name: 'Contacts',
    component: () => import('../modules/contacts/index.vue')
  },
  {
    path: '/discover',
    name: 'Discover',
    component: () => import('../modules/discover/index.vue')
  },
  {
    path: '/me',
    name: 'Me',
    component: () => import('../modules/me/index.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 