import { mount } from '@vue/test-utils'
import CourseShow from '@/components/CourseShow.vue'
import Vue from 'vue'
import iview from 'iview'
import VueResource from 'vue-resource'

Vue.use(VueResource)
Vue.use(iview)

describe('新增代码展示测验', () => {
  const wrapper = mount(CourseShow)

  it('主体', () => {
    expect(wrapper.contains('div')).toBe(true)
  })

  it('courseid', () => {
    expect(wrapper.vm.data).toBe(undefined)
  })

  it('音频', () => {
    expect(wrapper.contains('#audio')).toBe(true)
  })

  it('碰撞', () => {
    expect(wrapper.find('.playRoll').exists()).toBeTruthy()
  })

  wrapper.vm.get_info()
  expect(wrapper.vm.data).toBe(undefined)
})
