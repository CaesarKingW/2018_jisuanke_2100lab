<template>
<div id="UserInfo">
    <img id="avatar" v-bind:src="path" class="imgDiv" /><img>
     <div id="info">
       <div id="nickname">昵称：{{nickname}}</div>
       <div id="phone">手机号码：{{user_phone}}</div>
       <div id="money">奖励金：{{amount_of_money}}</div>
     </div>
</div>
</template>
<script>
export default {
  data() {
    return {
      path: '',
      default_avator: require('../../assets/little_avatar.png'),
      nickname: '',
      amount_of_money: 0,
      user_phone: '',
      old_path: ''
    }
  },
  mounted: function() {
    this.$http.post('http://192.168.55.33:8000/app/get_status').then(
      response => {
        var obj = []
        obj = response.data.list
        this.old_path = obj[0].fields.head_protrait
        this.user_phone = obj[0].pk
        if (this.old_path === '') {
          this.path = this.default_avator
        } else {
          this.path = 'http://192.168.55.33:8000/media/' + this.old_path
          this.old_path = ''
        }
        this.nickname = obj[0].fields.user_name
        this.amount_of_money = obj[0].fields.welfare
        console.log('success')
      },
      response => {
        console.log('error')
      }
    )
  },
  method: {}
}
</script>
<style scoped>
#UserInfo {
  float: center;
}
#avatar {
  border: #666666 solid 1px;
  border-radius: 8px;
  width: 120px;
  height: 120px;
  margin-top: 30px;
  margin-left: 100px;
}
#nickname {
  font-size: 20px;
  font-family: 华文中宋;
  margin-left: 200px;
  margin-top: 5px;
}
#money {
  font-size: 20px;
  font-family: 华文中宋;
  margin-left: 200px;
  margin-top: 5px;
}
#phone {
  font-size: 20px;
  font-family: 华文中宋;
  margin-left: 200px;
  margin-top: 5px;
}
#info {
    margin-left: 100px;
}
</style>
