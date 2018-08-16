// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
<<<<<<< HEAD
import VueResource from 'vue-resource'
=======
import iView from 'iview'
import 'iview/dist/styles/iview.css'
>>>>>>> e26123e89fbe241638fc91582bfa50f059d8639f

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
