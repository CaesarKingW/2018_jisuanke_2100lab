import { mount } from '@vue/test-utils'
import NiceUserModify from '@/components/NiceUserModify.vue'
import Vue from 'vue'
import iview from 'iview'
import VueResource from 'vue-resource'

Vue.use(VueResource)
Vue.use(iview)

describe('新增代码展示测验', () => {
  const wrapper = mount(NiceUserModify)

  it('头像', () => {
    expect(wrapper.find('img').exists()).toBe(true)
  })

  it('modal', () => {
    expect(wrapper.contains('input')).toBe(true)
  })

  const button = wrapper.find('#uploadButton')
  button.trigger('click')
  expect(wrapper.vm.$message).toBe(undefined)
})
