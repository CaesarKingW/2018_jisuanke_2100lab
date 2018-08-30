import { mount } from '@vue/test-utils'
import PayConfirm from '@/components/PayConfirm.vue'
import Vue from 'vue'
import iview from 'iview'
import VueResource from 'vue-resource'

Vue.use(VueResource)
Vue.use(iview)

const $route = {
  path: '/app/notify',
  query: {'id': '111', 'out_trade_no': '111'}
}

describe('新增代码展示测验', () => {
  const wrapper = mount(PayConfirm, {
    mocks: {
      $route
    }
  })

  it('头像', () => {
    expect(wrapper.find('p').text()).toBe('您已成功支付，请点击确认')
  })

  it('modal', () => {
    expect(wrapper.contains('div')).toBe(true)
  })

  wrapper.vm.ChangeOrderStatus()
  it('courseid', () => {
    expect(wrapper.vm.courseid).toBe(null)
  })
})
