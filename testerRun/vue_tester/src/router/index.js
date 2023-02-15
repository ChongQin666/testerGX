import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import UserTest from "../components/UserTest";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'UserTest',
      component: UserTest
    }
  ]
})
