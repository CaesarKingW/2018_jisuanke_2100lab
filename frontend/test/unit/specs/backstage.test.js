import { shallowMount } from '@vue/test-utils'
import backstage from '@/components/backstage.vue'
import Vue from 'vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'

Vue.use(VueResource)
Vue.use(VueRouter)

describe('后台单元测验', () => {
  const wrapper = shallowMount(backstage)

  it('主体', () => {
    expect(wrapper.find('body').exists()).toBeTruthy()
  })

  it('存在页脚', () => {
    expect(wrapper.find('footer').exists()).toBeTruthy()
  })
})
