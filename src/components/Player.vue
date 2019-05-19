<template>
  <b-container fluid class="player">
    <b-row class="song-info">
      <b-col>
        <div v-if="file">
          <div>{{file.name}}</div>
        </div>
        <div v-if="!file">no file</div>
      </b-col>
    </b-row>
    <b-row class="song-controls">
      <b-col>
        <b-button-group>
          <b-button v-if="isPlaying !== true" @click="play" title="Play">
            <i class="fas fa-play"></i>
          </b-button>
          <b-button v-if="isPlaying === true" @click="pause">
            <i class="fas fa-pause"></i>
          </b-button>
          <b-button @click="stop">
            <i class="fas fa-stop"></i>
          </b-button>
        </b-button-group>
        <span v-html="'&nbsp;'"></span>
        <span>{{String(Math.floor(currentTime/60)).padStart(2,'0')}}:{{String(Number(currentTime%60).toFixed(0)).padStart(2,'0')}}</span> /
        <span>{{String(Math.floor(totalTime/60)).padStart(2,'0')}}:{{String(Number(totalTime%60).toFixed(0)).padStart(2,'0')}}</span>
      </b-col>
    </b-row>
    <b-row class="song-progress">
        <b-col><input type="range" @mousedown="onRangeInputStart" @mouseup="onRangeInputEnd" min="0" v-bind:max="totalTime" v-model="currentTime" /></b-col>
    </b-row>
  </b-container>
</template>

<script>
import { mapState } from 'vuex';
import types from 'store/mutation-types';

let audio = new Audio();

export default {
    data() {
        return {};
    },
    methods: {
        play() {
            this.$store.commit(types.SET_PLAYING, true);
        },
        pause() {
            this.$store.commit(types.SET_PAUSE);
        },
        stop() {
            this.$store.commit(types.SET_STOP);
        },
        onRangeInputStart() {

        },
        onRangeInputEnd() {

        }
    },
    computed: {
        ...mapState({
            file: state => state.actualSong.file,
            isPlaying: state => state.actualSong.isPlaying,
            totalTime: state => state.actualSong.totalTime,
        }),
        currentTime: {
            get: function() {
                return this.$store.state.actualSong.currentTime;
            },
            set: function(newValue) {
                this.$store.commit(types.SEEK_POSITION, newValue);
            }
        }
    },
};
</script>

<style lang="scss" scoped>
</style>
