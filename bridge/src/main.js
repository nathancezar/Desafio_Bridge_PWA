import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { BootstrapVue } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)

Vue.config.productionTip = false

const backend = process.env.NODE_ENV === 'development' ? 'http://localhost:8888' : 'http://192.168.0.70:8888';

Vue.mixin({
  data() {
      return {
          get backend() {
              return backend;
          }
      }
  }
});

new Vue({
  components: { App },
  router,
  render: h => h(App),
}).$mount('#app')
