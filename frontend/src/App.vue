<template>
  <div id="app">
    <span><router-link to="/home"><Button type="primary" id="lab">2100-lab</Button></router-link></span>
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
  background-color: #c4e1ff
}
#lab {
  margin-left: 15%;
  font-size: 18px;
  float: left;
}
</style>
