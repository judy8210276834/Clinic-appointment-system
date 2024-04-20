import { createRouter, createWebHistory } from 'vue-router';
import BackBookingRecordPage from '../pages/BackBookingRecordPage.vue';
import BackChooseDatePage from '../pages/BackChooseDatePage.vue';
import BookingPage from '../pages/BookingPage.vue';
import BookingRecordPage from '../pages/BookingRecordPage.vue';
import ChooseDatePage from '../pages/ChooseDatePage.vue';
import ChooseTimePage from '../pages/ChooseTimePage.vue';
import HistoricalAmountPage from '../pages/HistoricalAmountPage.vue';
import LoginPage from '../pages/LoginPage.vue';
import ReportPage from '../pages/ReportPage.vue';
import SettingPage from '../pages/SettingPage.vue';

const routes = [
  // {
  //   path: '/',
  //   name: 'home',
  //   component: HomeView
  // },
  {
    path: '/back_booking_record',
    name: 'back_booking_record',
    component: BackBookingRecordPage
  },
  {
    path: '/back_choose_date',
    name: 'back_choose_date',
    component: BackChooseDatePage
  },
  {
    path: '/booking',
    name: 'booking',
    component: BookingPage
  },
  {
    path: '/booking_record',
    name: 'booking_record',
    component: BookingRecordPage
  },
  {
    path: '/',
    name: 'choose_date',
    component: ChooseDatePage
  },
  {
    path: '/choose_time',
    name: 'choose_time',
    component: ChooseTimePage
  },
  {
    path: '/historical_amount',
    name: 'historical_amount',
    component: HistoricalAmountPage
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage
  },
  {
    path: '/report',
    name: 'report',
    component: ReportPage
  },
  {
    path: '/setting',
    name: 'setting',
    component: SettingPage
  },

  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
