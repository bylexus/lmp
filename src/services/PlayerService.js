import types from 'store/mutation-types';

class PlayerService {
    constructor(vueStore) {
        this.vueStore = vueStore;
        this.audio = new Audio();
        this.audio.addEventListener('timeupdate', this.onTimeupdate.bind(this));

        this.startAfterLoad = this.startAfterLoad.bind(this);

        vueStore.subscribe((mutation, state) => {
            this.onMutation(mutation, state);
        });
    }

    onMutation(mutation, state) {
        switch (mutation.type) {
            case types.PLAY_SONG:
                this.playNewFile(state.actualSong.file);
                break;
            case types.SET_PLAYING:
                this.playSong();
                break;
            case types.SET_PAUSE:
                this.pauseSong();
                break;
            case types.SET_STOP:
                this.stopSong();
                break;
            case types.SEEK_POSITION:
                this.seekTo(state.actualSong.currentTime);
                break;
        }
    }

    playNewFile(file) {
        this.audio.src = file.path;
        this.audio.pause();
        this.audio.load();
        this.audio.addEventListener('canplay', this.startAfterLoad, {once: true});
    }

    startAfterLoad() {
        this.vueStore.commit(types.SET_PLAYING, true);
        this.vueStore.commit(types.SET_DURATION, this.audio.duration);
    }

    playSong() {
        this.audio.play();
    }

    pauseSong() {
        this.audio.pause();
    }

    stopSong() {
        this.audio.pause();
        this.audio.currentTime = 0;
    }

    onTimeupdate(event) {
        const currentTime = Math.trunc(this.audio.currentTime);
        if (Math.trunc(this.vueStore.state.actualSong.currentTime) !== currentTime) {
            this.vueStore.commit(types.SET_CURRENT_TIME, currentTime);
        }
    }

    seekTo(time) {
        this.audio.currentTime = time;
    }
}

let instance = null;

function init(vueStore) {
    instance = new PlayerService(vueStore);
}

function getInstance() {
    return instance;
}

export default {
    init,
    getInstance
};
