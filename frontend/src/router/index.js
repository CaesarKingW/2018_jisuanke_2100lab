import Vue from 'vue'
import Router from 'vue-router'
import UserLogin from '@/components/UserLogin'
import A from '@/components/A'
import test from '@/components/test'
import messageboard from '@/components/message_board'
import home from '@/components/home'
import backstage from '@/components/backstage'
import course from '@/components/back/course'
import comment from '@/components/back/comment'
import user from '@/components/back/user'
import order from '@/components/back/order'
import data from '@/components/back/data'
import authority from '@/components/back/authority'
import log from '@/components/back/log'

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
    },
    {
      path: '/message',
      name: 'message',
      component: messageboard
    },
    {
      path: '/home',
      name: 'home',
      component: home
    },
    {
      path: '/backstage',
      name: 'backstage',
      component: backstage,
      children: [{
        path: 'course',
        name: 'course',
        component: course
      },
      {
        path: 'comment',
        name: 'comment',
        component: comment
      },
      {
        path: 'user',
        name: 'user',
        component: user
      },
      {
        path: 'order',
        name: 'order',
        component: order
      },
      {
        path: 'data',
        name: 'data',
        component: data
      },
      {
        path: 'authority',
        name: 'authority',
        component: authority
      },
      {
        path: 'log',
        name: 'log',
        component: log
      }
      ]
    }
  ]
})
