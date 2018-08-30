import { shallowMount } from '@vue/test-utils'
import backlogin from '@/components/backlogin.vue'
import Vue from 'vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'

Vue.use(VueResource)
Vue.use(VueRouter)

describe('单元测验', () => {
  const wrapper = shallowMount(backlogin)

  it('2100lab后台管理员登陆"', () => {
    expect(wrapper.find('p').text()).toEqual('2100lab后台管理员登陆')
  })

  it('存在button', () => {
    expect(wrapper.find('Button').exists()).toBeTruthy()
  })

  it('存在div', () => {
    expect(wrapper.find('div').exists()).toBeTruthy()
  })

  it('存在form', () => {
    expect(wrapper.find('form').exists()).toBeTruthy()
  })

  const button = wrapper.find('button')
  button.trigger('click')
  expect(wrapper.vm.count).toBe(undefined)
})
