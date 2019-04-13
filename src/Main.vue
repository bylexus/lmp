<template>
  <div>
    <b-container fluid>
      <MainMenu/>
      <div class="main">
        <h1>Hello to lmp!</h1>
      </div>
    </b-container>
  </div>
</template>

<script>
import MainMenu from './main-menu/View.vue';

export default {
    data() {
        return {
            date: new Date()
        };
    },
    components: {
        MainMenu
    }
};
</script>

<style lang="scss" scoped>
.main {
    margin-left: 250px;
}
</style>


