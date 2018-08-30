import { shallowMount } from '@vue/test-utils'
import AllFreeCourse from '@/components/AllFreeCourse.vue'
import Vue from 'vue'
import VueResource from 'vue-resource'

Vue.use(VueResource)

describe('新增课程模块单元测验', () => {
  const wrapper = shallowMount(AllFreeCourse)

  it('标题是"新增课程"', () => {
    expect(wrapper.find('.navi').text()).toEqual('网站首页')
  })

  it('存在Divider', () => {
    expect(wrapper.find('div').exists()).toBeTruthy()
  })
})
