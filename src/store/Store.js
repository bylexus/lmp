import Vue from 'vue';
import Vuex from 'vuex';
import types from './mutation-types';

import actualSong from 'store/actualSong';

Vue.use(Vuex);

const store = new Vuex.Store({
    modules: {
        actualSong
    },
    state: {
    },
    mutations: {
    },
});

export default store;
