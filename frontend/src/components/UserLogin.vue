<template>
<div id="UserLogin">
    <span><router-link to="/home"><Button type="primary" id="home_but">前往首页</Button></router-link></span>
     <Divider />
    <div id="triangle"></div>
    <h1>2100实验室</h1>
    <br>
    <h1>登录</h1>
    <form method="POST" @submit.prevent="Is_normal_nubmer">
    <Input type="input" placeholder="请输入手机号码" size="large" icon="ios-phone-portrait" name="手机号码" v-model="login.phone_number"/>
    <input type="submit" value="获取验证码"/>
    </form>
    <form method="POST" @submit.prevent="comparecode">
    <Input type="input" placeholder="请输入验证码"  size="large" icon="ios-key-outline" v-model="login.usercode"/>
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
      } else alert('验证码错误')
      console.log(this.login.phone_number)
    },

    Is_normal_nubmer: function() {
      if (!/^1[34578]\d{9}$/.test(this.login.phone_number)) {
        alert('请输入正确的手机号码')
      } else {
        this.getcode()
      }
    }
  }
}
</script>
<style scoped>
#log_column {
  text-align: center;
}
.button {
  width: 100px;
  background: #3399cc;
  display: block;
  margin: 0 auto;
  margin-top: 1%;
  padding: 10px;
  text-align: center;
  text-decoration: none;
  color: #fff;
  cursor: pointer;
  transition: background 0.3s;
  -webkit-transition: background 0.3s;
}
.button:hover {
  background: #2288bb;
}
#UserLogin {
  width: 400px;
  margin: 0 auto;
  margin-top: 8px;
  margin-bottom: 2%;
  transition: opacity 1s;
  -webkit-transition: opacity 1s;
  background-size: 100% 100%;
}
#triangle {
  width: 0;
  border-top: 12x solid transparent;
  border-right: 12px solid transparent;
  border-bottom: 12px solid #3399cc;
  border-left: 12px solid transparent;
  margin: 0 auto;
}
#UserLogin h1 {
  background: #3399cc;
  padding: 20px 0;
  font-size: 160%;
  font-weight: 300;
  text-align: center;
  color: #fff;
}
form {
  background: #f0f0f0;
  padding: 6% 4%;
}
input[type="phone"],
input[type="id_code"] {
  width: 92%;
  background: #fff;
  margin-bottom: 4%;
  border: 1px solid #ccc;
  padding: 4%;
  font-family: "Open Sans", sans-serif;
  font-size: 100%;
  color: #555;
}
input[type="submit"] {
  margin-top: 1%;
  width: 100%;
  background: #3399cc;
  border: 0;
  padding: 4%;
  font-family: "Open Sans", sans-serif;
  font-size: 100%;
  color: #fff;
  cursor: pointer;
  transition: background 0.3s;
  -webkit-transition: background 0.3s;
}
input[type="submit"]:hover {
  background: #2288bb;
}
#home_but {
  margin-left: 170%;
  float: left;
}
</style>
