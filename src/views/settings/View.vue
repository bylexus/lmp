<template>
  <b-container fluid class="settings">
    <b-row>
      <b-col>
        <h1>Settings</h1>
      </b-col>
    </b-row>

    <h2>Music locations</h2>
    <label>
      Choose music folder location:
      <b-form-file @input="folderChosen" directory/>
    </label>

    <b-row>
      <b-col>
        <b-button @click="goBack" variant="primary">
          <i class="fas fa-arrow-left"></i>
        </b-button>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import types from 'store/mutation-types';

// use electron require for node modules, by accessing global window.require here:
const walkdir = window.require('walkdir');
const mime = window.require('mime');
const NodeId3 = window.require('node-id3');

export default {
    data() {
        return {};
    },
    methods: {
        goBack() {
            this.$router.go(-1);
        },
        folderChosen(dir) {
            let emitter = walkdir(dir.path, { no_return: true });
            emitter.on('file', (path, stat) => {
                let type = mime.getType(path);
                if (type && type.match(/^audio\//)) {
                    NodeId3.read(path, (err, tags) => {
                        if (!err) {
                            console.log('ID3 tags for ', path, tags);
                        }
                    });
                    // console.log('found: ', type, path, stat);
                }
            });
            emitter.on('end', () => {
                console.log('End!');
            });
        },
    },
    components: {},
};
</script>

<style lang="scss" scoped>
.settings {
}
</style>
