import VueRouter from 'vue-router';
import Home from 'views/home/View.vue';
import Settings from 'views/settings/View.vue';

const router = new VueRouter({
    routes: [{ path: '/', component: Home }, { path: '/settings', component: Settings }],
});

export default router;
