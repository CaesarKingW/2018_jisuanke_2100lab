<template>
<div id = "destroy">
    <button v-on:click="user_destory">确认注销</button>
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

// 请提示用户，注销之后再也无法登录
