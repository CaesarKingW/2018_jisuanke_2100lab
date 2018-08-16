import Vue from 'vue'
import Router from 'vue-router'
import UserLogin from '@/components/UserLogin'
import A from '@/components/A'
import test from '@/components/test'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/A',
      name: 'A',
      component: A
    },
    {
      path: '/login',
      name: 'UserLogin',
      component: UserLogin
    },
    {
      path: '/test',
      name: 'test',
      component: test
    }
  ]
})
