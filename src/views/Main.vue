<template>
  <div>
    <b-container fluid>
      <MainMenu/>
      <router-view class="main"></router-view>
    </b-container>
  </div>
</template>

<script>
import MainMenu from 'views/main-menu/View.vue';

export default {
    data() {
        return {
            date: new Date(),
        };
    },
    components: {
        MainMenu,
    },
};
</script>

<style lang="scss" scoped>
.main {
    margin-left: 250px;
    width: auto;
}
</style>


