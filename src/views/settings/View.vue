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
    <div v-if="syncing">Inspecting dir, please stand by ...</div>
  </b-container>
</template>

<script>
import types from 'store/mutation-types';

// use electron require for node modules, by accessing global window.require here:
// const walkdir = window.require('walkdir');
// const mime = window.require('mime');
// const NodeId3 = window.require('node-id3');
// const { ipcRenderer } = window.require('electron');
import { ipcRendererCall as ipcCall } from 'services/ipcRendererCall';

export default {
    data() {
        return {
            syncing: false,
        };
    },
    methods: {
        goBack() {
            this.$router.go(-1);
        },
        async folderChosen(dir) {
            this.syncing = true;
            try {
                let data = await ipcCall('inspect-dir', {
                    dir: dir.path,
                });
                console.log('inspection done:', data);
            } catch (e) {
                console.log('ERROR:', e);
            } finally {
                this.syncing = false;
            }
        },
    },
    components: {},
};
</script>

<style lang="scss" scoped>
.settings {
}
</style>
