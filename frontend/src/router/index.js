import Vue from 'vue'
import Router from 'vue-router'
import UserLogin from '@/components/UserLogin'
import backstage from '@/components/backstage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/UserLogin',
      name: 'UserLogin',
      component: UserLogin
    },
    {
      path: '/backstage',
      name: 'backstage',
      component: backstage
    }
  ]
})
