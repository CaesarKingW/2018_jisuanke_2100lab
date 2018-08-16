<template>
<div id="test">
    <div id="triangle"></div>
    <h1>2100实验室</h1>
    <br>
    <h1>登录</h1>
    <form method="POST" @submit.prevent="Is_normal_nubmer">
    手机号码：
    <input type="input" name="手机号码" v-model="login.phone_number"/>
    <input type="submit" value="获取验证码"/>
    </form>
    <form method="POST" @submit.prevent="comparecode">
        验证码： <input type="input" v-model="login.usercode"/>
        <input type="submit" value="登录"/>
    </form>
</div>
</template>

<script>
export default {
  data() {
    return {
      commit_phone: null,
      login: {
        checkCode: null,
        phone_number: null,
        usercode: null
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
      this.commit_phone = this.login.phone_number
      this.createCode()
      var phonenumber = JSON.stringify(this.login)
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
    },

    comparecode: function() {
      if (
        !this.login.phone_number &&
        typeof this.login.phone_number !== 'undefined' &&
        this.login.phone_number !== 0
      ) {
        alert('请输入手机号')
      } else if (
        !this.login.usercode &&
        typeof this.login.usercode !== 'undefined' &&
        this.login.usercode !== 0
      ) {
        alert('请输入验证码')
      } else if (
        this.login.usercode === this.login.checkCode &&
        this.commit_phone === this.login.phone_number
      ) {
        alert('登录成功')
        this.login.phone_number = null
        this.login.checkCode = null
        this.login.usercode = null
        this.commit_phone = null
      } else alert('登录失败')
      console.log(this.login.phone_number)
    },

    Is_normal_nubmer: function() {
      if (!/^1[34578]\d{9}$/.test(this.login.phone_number)) {
        alert('手机号码有误，请重填')
      } else {
        this.getcode()
      }
    }
  }
}
</script>
