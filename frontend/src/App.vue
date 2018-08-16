<template>
  <div id="app">
    <router-link to="UserLogin/"><button id="log_but">用户登录</button></router-link>
    <hr width="90%" style="height: 1.5px;" color="#99cccc"/>
   <router-view></router-view>
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
#log_but {
  background-color: #3399cc;
  color: #ffffff;
  text-align:center;
  margin-left: 80%;
  width: 90px;
  height: 40px;
  cursor:pointer;
}
</style>
