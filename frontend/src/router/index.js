import Vue from 'vue'
import Router from 'vue-router'
import UserLogin from '@/components/UserLogin'
import test from '@/components/test'
import messageboard from '@/components/message_board'
import home from '@/components/home'
import backlogin from '@/components/backlogin'
import backstage from '@/components/backstage'
import course from '@/components/back/course'
import comment from '@/components/back/comment'
import user from '@/components/back/user'
import order from '@/components/back/order'
import data from '@/components/back/data'
import authority from '@/components/back/authority'
import log from '@/components/back/log'
import deny from '@/components/back/deny'
import CourseShow from '@/components/CourseShow'
import FreeCourseIntro from '@/components/FreeCourseIntro'
import PayCourseIntro from '@/components/PayCourseIntro'
import ShowUserInfo from '@/components/ShowUserInfo'
import ModifyUserInfo from '@/components/ModifyUserInfo'
import ReadAndBurn from '@/components/ReadAndBurn'
import useModify from '@/components/use_modify'
import NiceMsgBoard from '@/components/NiceMsgBoard'
import editCourse from '@/components/back/editCourse'
import addCourse from '@/components/back/addCourse'
import destroy from '@/components/account_cancellation'
import AllFreeCourse from '@/components/AllFreeCourse'
import AllPayCourse from '@/components/AllPayCourse'
import NiceUserModify from '@/components/NiceUserModify'
import freeCourse from '@/components/show_free_course'
import payingCourse from '@/components/show_paying_course'
import recommendCourse from '@/components/recommend'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/UserLogin',
      name: 'UserLogin',
      component: UserLogin
    },
    // 测试用
    {
      path: '/test',
      name: 'test',
      component: test
    },
    //
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
      path: '/CourseShow',
      name: 'CourseShow',
      component: CourseShow
    },
    {
      path: '/FreeCourseIntro',
      name: 'FreeCourseIntro',
      component: FreeCourseIntro
    },
    {
      path: '/PayCourseIntro',
      name: 'PayCourseIntro',
      component: PayCourseIntro
    },
    {
      path: '/ShowUserInfo',
      name: 'ShowUserInfo',
      component: ShowUserInfo
    },
    {
      path: '/ModifyUserInfo',
      name: 'ModifyUserInfo',
      component: ModifyUserInfo
    },
    {
      path: '/user_modify',
      name: 'user_modify',
      component: useModify
    },
    {
      path: '/ReadAndBurn',
      name: 'ReadAndBurn',
      component: ReadAndBurn
    },
    {
      path: '/NiceMsgBoard',
      name: 'NiceMsgBoard',
      component: NiceMsgBoard
    },
    {
      path: '/AllFreeCourse',
      name: 'AllFreeCourse',
      component: AllFreeCourse
    },
    {
      path: '/AllPayCourse',
      name: 'AllPayCourse',
      component: AllPayCourse
    },
    {
      path: '/message_board',
      name: 'message_board',
      component: messageboard
    },
    {
      path: '/NiceUserModify',
      name: 'NiceUserModify',
      component: NiceUserModify
    },
    {
      path: '/backlogin',
      name: 'backlogin',
      component: backlogin
    },
    {
      // path: '/backstage/:user',
      path: '/backstage',
      name: 'backstage',
      component: backstage,
      children: [{
        path: 'course',
        name: 'course',
        component: course
      },
      {
        path: 'editCourse',
        name: 'editCourse',
        component: editCourse
      },
      {
        path: 'addCourse',
        name: 'addCourse',
        component: addCourse
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
      },
      {
        path: 'deny',
        name: 'deny',
        component: deny
      }
      ]
    },
    {
      path: '/account_destroy',
      name: 'account_destroy',
      component: destroy
    },
    {
      path: '/free_course',
      name: 'free_course',
      component: freeCourse
    },
    {
      path: '/paying_course',
      name: 'paying_course',
      component: payingCourse
    },
    {
      path: '/recommend_course',
      name: 'recommend_course',
      component: recommendCourse
    }
  ]
})
