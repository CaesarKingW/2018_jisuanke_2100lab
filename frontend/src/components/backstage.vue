<template>
  <body>
    <navibar :username="username" @logout="aa"/>
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
    aa() {
      console.log('this.username')
      console.log(this.username)
      console.log('this.username')
    }
  },
  mounted(request) {
    this.username = this.$route.params.user
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
