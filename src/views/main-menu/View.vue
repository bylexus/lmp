<template>
  <div class="main-menu">
    <h2>Main Menu</h2>
    <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
    components: {},
};
</script>

<style lang="scss" scoped>
.main-menu {
    background-color: darkblue;
    color: whitesmoke;
    position: fixed;
    top: 0;
    left: 0;
    width: 250px;
    height: 100%;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.6);
}
</style>

