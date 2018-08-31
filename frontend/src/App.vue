<template>
  <div id="app">
  <router-view />
  </div>
</template>
<script>
export default {
  name: 'App'
}
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #f8f8f9;
}

#foot {
  opacity: 1;
  text-align: center;
  font-size: 14px;
  position: fixed;
  bottom: 0;
  right: 420px;
}
</style>
