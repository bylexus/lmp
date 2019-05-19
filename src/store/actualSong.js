import Vue from 'vue';
import Vuex from 'vuex';
import types from './mutation-types';

const actualSong = {
    state: {
        file: null,
        isPlaying: false,
        currentTime: 0,
        totalTime: 0,
    },
    mutations: {
        [types.PLAY_SONG](state, songFile) {
            state.file = songFile;
        },
        [types.SET_PLAYING](state, isPlaying) {
            if (state.file) {
                state.isPlaying = isPlaying === true;
            }
        },
        [types.SET_PAUSE](state) {
            if (state.file) {
                state.isPlaying = false;
            }
        },
        [types.SET_STOP](state) {
            if (state.file) {
                state.isPlaying = false;
            }
        },
        [types.SET_CURRENT_TIME](state, currentTime) {
            state.currentTime = currentTime;
        },
        [types.SET_DURATION](state, totalTime) {
            state.totalTime = totalTime;
        },
        [types.SEEK_POSITION](state, seekToTime) {
            state.currentTime = seekToTime;
        },
    },
};
export default actualSong;
