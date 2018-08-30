import { shallowMount } from '@vue/test-utils'
import AllPayCourse from '@/components/AllPayCourse.vue'
import Vue from 'vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'

Vue.use(VueResource)
Vue.use(VueRouter)

describe('新增付费课程模块单元测验', () => {
  const wrapper = shallowMount(AllPayCourse)

  it('标题是"新增课程"', () => {
    expect(wrapper.find('.navi').text()).toEqual('网站首页')
  })

  it('存在Divider', () => {
    expect(wrapper.find('Divider').exists()).toBeTruthy()
  })

  it('存在Card', () => {
    expect(wrapper.find('Card').exists()).toBeFalsy()
  })
})
