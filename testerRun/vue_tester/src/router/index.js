import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import UserTest from "../components/UserTest";
import testRunner from "../components/testRunner";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'UserTest',
      component: UserTest
    },
    {
      path: '/testRunner',
      name: 'testRunner',
      component: testRunner
    },
  ]
})
