/* eslint-disable */
<template>
  <body>
    <navibar :username="username" />
    <leftnav/>
    <router-view/>
    <footer></footer>
  </body>
</template>

<script>
import navibar from './navibar'
import leftnav from './leftnav'

export default {
  name: 'backstage',
  data() {
    return {
      username: ''
    }
  },
  methods: {
    aa() {},
    mounted(request) {
      this.username = this.$route.params.user
    }
  },
  components: {
    navibar,
    leftnav
  }
}
</script>

<style scoped>
.fl {
  float: left;
}

.fr {
  float: right;
}
</style>
