<template>
  <div>
    <b-container fluid>
      <MainMenu/>
      <Home/>
    </b-container>
  </div>
</template>

<script>
import MainMenu from './main-menu/View.vue';
import Home from './home/View.vue';

export default {
    data() {
        return {
            date: new Date()
        };
    },
    components: {
        MainMenu,
        Home
    }
};
</script>

<style lang="scss" scoped>
.main {
}
</style>


