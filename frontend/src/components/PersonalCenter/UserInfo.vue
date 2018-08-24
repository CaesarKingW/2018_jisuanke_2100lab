<template>
<div id="UserInfo">
    <img id="avatar" v-bind:src="path" class="imgDiv" /><img>
    <div>
        <h1 id="nick">昵称：{{nickname}}</h1>
        <h1 id="nick">奖励金：{{amount_of_money}}</h1>
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
        this.user_phone = obj[0].fields.phone_number
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
  float: left;
}
#avatar {
  border: #666666 solid 1px;
  border-radius: 8px;
  width: 120px;
  height: 120px;
  margin: 30px;
  margin-left: 300px;
}
#nick {
  width: 120px;
  height: 40px;
  margin: 30px;
  margin-left: 300px;
}
</style>
