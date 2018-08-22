<template>
  <div id="app">
  <router-view />
  <Layout>
  <Footer><div id="foot">Copyright © 2018 2100实验室-佛组 All Rights Reserved.</div></Footer>
  </Layout>
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
  opacity: 1;
  text-align: center;
}
</style>
