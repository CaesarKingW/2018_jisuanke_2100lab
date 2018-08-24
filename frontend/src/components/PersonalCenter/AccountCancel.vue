<template>
<div id="AccountCancel">
    <div id="card">
        <Card id="AlertColumn">
        <div slot="title" id="AlertTitle"><Icon type="md-alert" />  注销警告</div>确认注销后，您的所有个人信息
        （包括头像、昵称、已学课程及已购课程记录、奖励金等信息）将被清空，
        并且本手机号码此后将无法再次用于进行注册或登录。
        进行本操作前请慎重！
    </Card>
    <div><button id="CancelButton" v-on:click="user_destory">确认注销</button></div>
    </div>
</div>
</template>
<script>
export default {
  data() {
    return {
      // 当前登录用户手机号，现暂存为下
      user_phone: '17602284691'
    }
  },
  methods: {
    user_destory: function() {
      this.$http
        .post(
          'http://192.168.55.33:8000/app/account_destroy',
          JSON.stringify(this.user_phone)
        )
        .then(
          response => {
            console.log(response.date)
            alert('注销成功')
            // 跳转到登录页面
          },
          response => {
            console.log('error')
          }
        )
    }
  }
}
</script>
<style scoped>
#AlertColumn {
  width: 600px;
  margin-left: 280px;
  margin-top: 50px;
  background-color: brown;
  opacity: 0.9;
  color: white;
  font-size: 19px;
  border: rgba(255, 255, 255, 0.8) solid 2px;
}
#AlertTitle {
  font-size: 30px;
  text-align: center;
}
#CancelButton {
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
#CancelButton:hover {
  cursor: pointer;
  background-color: rgb(202, 53, 53);
}
</style>
