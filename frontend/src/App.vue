<template>
  <div id="app">
    <router-link to="UserLogin/"><Button type="primary" id="log_but">用户登录</Button></router-link>
    <Divider />
    <router-view/>
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
  background-color: #c4e1ff;
}

#log_but {
  margin-top: 2%;
  margin-left: 90%;
}
</style>
