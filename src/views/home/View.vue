<template>
  <b-container fluid class="home">
    <b-row>
      <b-col>
        <Player/>
      </b-col>
    </b-row>
    <h1>Welcome to LMP!</h1>
    <div>
      <label>
        Play a song:
        <b-form-file @input="fileChosen" accept="audio/*"/>
      </label>
    </div>
  </b-container>
</template>

<script>
import types from 'store/mutation-types';
import Player from 'components/Player.vue';

export default {
    data() {
        return {};
    },
    methods: {
        fileChosen(file) {
            if (file) {
                this.$store.commit(types.PLAY_SONG, file);
            }
        },
    },
    components: {
        Player,
    },
};
</script>

<style lang="scss" scoped>
.home {
    // margin-left: 250px;
}
</style>
