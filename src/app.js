import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
import Main from './Main.vue';

import './app.scss';

Vue.use(BootstrapVue);

new Vue({
    el: '#app',
    components: { Main },
    render(h) {
        return h('Main');
    }
});
