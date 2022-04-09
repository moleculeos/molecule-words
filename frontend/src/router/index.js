import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import StatisticsView from '../views/StatisticsView.vue'
import RefreshWordsView from '../views/RefreshWordsView.vue'
import AddNewWordsView from '../views/AddNewWordView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/addnew',
    name: 'AddNew',

    component: AddNewWordsView
  },
  {
    path: '/statistics',
    name: 'Statistics',

    component: StatisticsView
  },
  {
    path: '/refresh',
    name: 'RefreshWords',
    component: RefreshWordsView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
