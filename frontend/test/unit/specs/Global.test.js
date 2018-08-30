import { mount } from '@vue/test-utils'
import Global from '@/components/Global.vue'
import Vue from 'vue'
import iview from 'iview'
import VueResource from 'vue-resource'

Vue.use(VueResource)
Vue.use(iview)

describe('新增代码展示测验', () => {
  const wrapper = mount(Global)

  it('头像', () => {
    expect(wrapper.vm.serverSrc).toBe(undefined)
  })

  it('modal', () => {
    expect(wrapper.contains('div')).toBe(false)
  })
})
