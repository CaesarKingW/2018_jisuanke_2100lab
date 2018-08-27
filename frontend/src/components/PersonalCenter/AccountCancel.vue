<template>
<div class="AccountCancel">
    <div id="card">
        <Card id="alertColumn">
        <div slot="title" id="alertTitle"><Icon type="md-alert" />  注销警告</div>确认注销后，您的所有个人信息
        （包括头像、昵称、已学课程及已购课程记录、奖励金等信息）将被清空，
        并且本手机号码此后将无法再次用于进行注册或登录。
        进行本操作前请慎重！
    </Card>
    <div id="buttonCard"><button id="cancelButton" v-on:click="userDestroy">确认注销</button></div>
    </div>
</div>
</template>
<script>
export default {
  data() {
    return {
      // 当前登录用户手机号，现暂存为下
      userPhone: ''
    }
  },
  mounted: function() {
    // 获取登录用户手机号
    this.$http.post(this.GLOBAL.serverSrc + '/app/get_status').then(response => {
      this.userPhone = response.data.list[0].pk
    })
  },
  methods: {
    userDestroy: function() {
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/account_destroy',
          JSON.stringify(this.userPhone)
        )
        .then(
          response => {
            this.getSuccessCancel()
            this.$http
              .post(this.GLOBAL.serverSrc + '/app/del_status')
              .then(response => {
                console.log('success')
                this.$router.push({ name: 'UserLogin' })
              })
          },
          response => {
            console.log('error')
          }
        )
    },
    getSuccessCancel() {
      this.$Message.warning('您的账号已永久注销！')
    }
  }
}
</script>
<style scoped>
#alertColumn {
  width: 600px;
  margin-left: 280px;
  margin-top: 50px;
  background-color: brown;
  opacity: 0.9;
  color: white;
  font-size: 19px;
  border: rgba(255, 255, 255, 0.8) solid 2px;
}
#alertTitle {
  font-size: 30px;
  text-align: center;
}
#cancelButton {
  text-align: center;
  margin-left: 325px;
  margin-top: 20px;
  width: 110px;
  height: 45px;
  background-color: brown;
  color: #fff;
  outline: none;
  border-radius: 4px;
  border: rgba(255, 255, 255, 0.8) solid 2px;
  color: #fff;
  opacity: 0.9;
  font-size: 16px;
  cursor: pointer;
}
#cancelButton:hover {
  cursor: pointer;
  background-color: rgb(202, 53, 53);
}
</style>
