<template>
  <body>
    <navibar/>
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
      username: 'hasaki'
    }
  },
  components: {
    navibar,
    leftnav
  }
}
</script>

<style scopeds>
.fl {
  float: left;
}

.fr {
  float: right;
}
</style>
