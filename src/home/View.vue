<template>
  <div class="home">
    <h1>Welcome to LMP!</h1>
    <div>
      <label>
        Play a song:
        <b-form-file @input="fileChosen" accept="audio/*"/>
      </label>
    </div>
    <div v-if="file">
        <div>{{file.name}}</div>
        <b-button-group>
            <b-button v-if="isPlaying !== true" @click="play" title="Play"><i class="fas fa-play"></i></b-button>
            <b-button v-if="isPlaying === true" @click="pause"><i class="fas fa-pause"></i></b-button>
            <b-button @click="stop"><i class="fas fa-stop"></i></b-button>
        </b-button-group>
    </div>
  </div>
</template>

<script>
let audio = null;

export default {
    data() {
        return {
            file: null,
            isPlaying: false
        };
    },
    methods: {
        fileChosen(file) {
            if (file){
                this.file = file;
                audio = new Audio(file.path);
            }
        },
        play() {
            if (audio) {
                audio.play();
                this.isPlaying = true;
            }
        },
        pause() {
            if (audio) {
                audio.pause();
                this.isPlaying = false;
            }
        },
        stop() {
            if (audio) {
                audio.pause();
                audio.currentTime = 0;
                this.isPlaying = false;
            }
        }
    }
};
</script>

<style lang="scss" scoped>
.home {
    margin-left: 250px;
}
</style>
