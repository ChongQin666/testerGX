// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
//引入axios模块
import axios from 'axios'
import VueAxios from 'vue-axios'
//引入ElementUI相关
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

//引入外部css
import '@/style/bootstrap-4.4.1.css'


Vue.use(ElementUI)

Vue.use(VueAxios,axios)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
