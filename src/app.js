import 'app.scss';

import Vue from 'vue';
import VueRouter from 'vue-router';
import BootstrapVue from 'bootstrap-vue';

import Main from 'views/Main.vue';

import store from 'store/Store';
import router from 'routes/router';
import playerService from 'services/PlayerService.js';

Vue.use(VueRouter);
Vue.use(BootstrapVue);

playerService.init(store);

new Vue({
    el: '#app',
    store,
    router,
    components: { Main },
    render(h) {
        return h('Main');
    },
});
