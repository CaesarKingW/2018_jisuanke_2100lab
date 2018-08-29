import Vue from 'vue'
import App from './App'
import router from './router'
import VueResource from 'vue-resource'
import iView from 'iview'
import 'iview/dist/styles/iview.css'
import global_ from '@/components/Global'
// 引用文件
Vue.prototype.GLOBAL = global_
// 挂载到Vue实例上面
Vue.use(VueResource)
Vue.config.productionTip = false
Vue.use(iView)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
