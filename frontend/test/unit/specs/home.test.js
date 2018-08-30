import { mount } from '@vue/test-utils'
import home from '@/components/home.vue'
import Vue from 'vue'
import iview from 'iview'
import VueResource from 'vue-resource'

Vue.use(VueResource)
Vue.use(iview)

describe('新增代码展示测验', () => {
  const wrapper = mount(home)

  it('div', () => {
    expect(wrapper.contains('div')).toBe(true)
  })

  it('div', () => {
    expect(wrapper.contains('button')).toBe(true)
  })

  it('div', () => {
    expect(wrapper.contains('img')).toBe(true)
  })

  wrapper.vm.mounted()
  expect(wrapper.vm.data).toBe(true)
})
