import { mount } from '@vue/test-utils'
import NiceReply from '@/components/NiceReply.vue'
import Vue from 'vue'
import iview from 'iview'
import VueResource from 'vue-resource'

Vue.use(VueResource)
Vue.use(iview)

describe('新增代码展示测验', () => {
  const wrapper = mount(NiceReply)
  wrapper.setProps({user_phone: '11111111111', title: '111'})

  it('输入', () => {
    expect(wrapper.find('Input').text()).toBe('')
  })

  it('modal', () => {
    expect(wrapper.contains('Modal')).toBe(false)
  })

  wrapper.find('Input').setValue('123456789')
  expect(wrapper.find('Input').text()).toBe('')
  expect(wrapper.vm.replyContent).toEqual(null)

  const button = wrapper.find('button')
  button.trigger('click')
  expect(wrapper.vm.$message).toBe(undefined)
})
