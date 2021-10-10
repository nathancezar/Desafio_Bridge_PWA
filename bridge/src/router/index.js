import Vue from 'vue';
import Router from 'vue-router';
import VueSession from 'vue-session';

Vue.use(Router);
Vue.use(VueSession, { persist: true });


export default new Router({
  routes: [
    {
        path: '/home',
        name: 'home',
        component: require('@/components/Home').default,
    },
    {
        path: '*',
        redirect: '/home',
    },
  ],
});