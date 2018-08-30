import { mount } from '@vue/test-utils'
import ModifyUserInfo from '@/components/ModifyUserInfo.vue'
import Vue from 'vue'
import iview from 'iview'
import VueResource from 'vue-resource'

Vue.use(VueResource)
Vue.use(iview)

describe('新增代码展示测验', () => {
  const wrapper = mount(ModifyUserInfo)

  it('输入', () => {
    expect(wrapper.find('Input').text()).toBe('')
  })

  it('modal', () => {
    expect(wrapper.contains('Modal')).toBe(false)
  })

  wrapper.find('Input').setValue('123456789')
  expect(wrapper.find('Input').text()).toBe('')

  const button = wrapper.find('button')
  button.trigger('click')
  expect(wrapper.vm.$message).toBe(undefined)
})
