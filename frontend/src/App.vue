<template>
  <div id="app">
<<<<<<< HEAD
    <router-link to="UserLogin/"><button id="log_but">用户登录</button></router-link>
    <hr width="90%" style="height: 1.5px;" color="#99cccc"/>
   <router-view></router-view>
=======
    <span><router-link to="/home"><Button type="primary" id="lab">2100-lab</Button></router-link></span>
    <router-view/>
>>>>>>> e26123e89fbe241638fc91582bfa50f059d8639f
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
#lab {
  margin-left: 15%;
  font-size: 18px;
  float: left;
}
</style>
