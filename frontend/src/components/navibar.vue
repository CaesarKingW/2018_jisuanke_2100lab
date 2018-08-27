<template>
    <header class="header">
      <div>
        <div class="fl img">
          <img src="../assets/scienceCaptain.jpg">
        </div>
        <div class="fl menutext">
          <p>2100实验室后台</p>
        </div>
      </div>
      <div class="fr">
        <div class="fl menutext">
          <p>{{username}},您好！</p>
        </div>
        <div class="fl menutext">
          <Button @click="logout">登出</Button>
        </div>
      </div>
    </header>
</template>

<script>
export default {
  name: 'navibar',
  props: {
    username: String
  },
  data() {
    return {

    }
  },
  methods: {
    logout() {
      var request = {}
      this.$http.post(this.GLOBAL.serverSrc + 'app/back_log_out', request)
        .then(response => {
          console.log(response.data)
          this.$router.push({path: '/backlogin'})
        })
    }
  }
}
</script>

<style scopeds>
.header {
  position: static;
  height: 100px;
  padding-top: 20px;
  background-color: #2b85e4;
}

.img {
  margin-right: 40px;
}

.menutext {
  padding-top: 20px;
  margin-right: 40px;
  font-size: 20px;
  text-align: center;
}

.fl {
  float: left;
}

.fr {
  float: right;
}
</style>
