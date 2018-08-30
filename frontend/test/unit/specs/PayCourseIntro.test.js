import { mount } from '@vue/test-utils'
import PayCourseIntro from '@/components/PayCourseIntro.vue'
import Vue from 'vue'
import iview from 'iview'
import VueResource from 'vue-resource'

Vue.use(VueResource)
Vue.use(iview)

describe('新增代码展示测验', () => {
  const wrapper = mount(PayCourseIntro)

  it('主体', () => {
    expect(wrapper.find('.navi').text()).toBe(undefined)
  })

  it('路由', () => {
    expect(wrapper.contains('router-link')).toBe(true)
  })

  it('路由', () => {
    expect(wrapper.contains('Card')).toBe(true)
  })

  it('courseid', () => {
    expect(wrapper.vm.data).toBe(undefined)
  })

  wrapper.vm.userphone = '11111111111'
  wrapper.vm.GetUserPhone()
  it('电话', () => {
    expect(wrapper.vm.userphone).toBe(undefined)
  })

  const button = wrapper.findAll('button')
  expect(button.length()).toBe(undefined)
})
