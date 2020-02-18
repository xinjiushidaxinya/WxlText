import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/login'
import house from '../components/house.vue'
import houtai from '../components/houtai.vue'
import housemessege from '../components/housemessege.vue'
import housedata from '../components/housedata.vue'
import dingdan from '../components/dingdan.vue'
import xiugai from '../components/xiugai.vue'


Vue.use(Router)
export default new Router({
  mode:'history',
  routes: [
	  {
	    path: '/',
	    name: 'login',
	    component: Login
	  },
    {
      path: '/house',
      name: 'house',
      component: house
    },
    {
      path: '/houtai',
      name: 'houtai',
      component: houtai
    },
    {
      path: '/HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld,
      children:[
		    {
		            name : "housemessege",
		            path : "housemessege",
		            component : housemessege
		          },
        {
                 name : "housedata",
                 path : "housedata",
                 component : housedata
               },
        {
                 name : "dingdan",
                 path : "dingdan",
                 component : dingdan
               },
          {
                         name : "xiugai",
                         path : "xiugai",
                         component : xiugai
                       }
	  ]
    }
  ]
})
