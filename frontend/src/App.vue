<template>
  <div id="app">
  <router-view />
  <div id="foot">Copyright © 2018 2100实验室-佛组 All Rights Reserved</div>
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
}
#foot {
  opacity: 0.5;
  text-align: center;
  font-size: 14px;
  position:fixed;
  bottom: 0;
  right:420px;
}
</style>
