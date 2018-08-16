<template>
<div id="test">
    <!-- <span href="#" class="button" id="toggle-login">2100-LAB</span> -->
    <div id="triangle"></div>
    <h1>2100实验室</h1>
    <br>
    <h1>登录</h1>
    <form method="POST" @submit.prevent="getcode">
    手机号码：
    <input type="input" v-model="login.phone_number" />
    <input type="submit" value="获取验证码" />
    </form>
    <input type="input" placeholder="验证码" />
    <div><input type="submit" value="登录" /></div>
</div>
</template>

<script>
export default {
  data() {
    return {
      login: {
        checkCode: null,
        phone_number: null
      }
    }
  },
  methods: {
    createCode() {
      var code = ''
      var codeLength = 4 // 验证码的长度
      var random = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'
      ] // 随机数
      for (var i = 0; i < codeLength; i++) {
        // 循环操作
        var index = Math.floor(Math.random() * 36) // 取得随机数的索引（0~35）
        code += random[index] // 根据索引取得随机数加到code上
      }
      this.login.checkCode = code // 把code值赋给验证码
    },

    getcode: function() {
      var phonenumber = JSON.stringify(this.login.phone_number)
      console.log(phonenumber)
      this.createCode()
      console.log(phonenumber)
      this.$http
        .post('http://192.168.55.33:8000/app/get_code_post', phonenumber)
        .then(
          response => {
            console.log(response.data)
          },
          response => {
            console.log('error')
          }
        )
    }
  }
}
</script>
