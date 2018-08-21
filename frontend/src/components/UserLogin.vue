<template>
<div id="UserLogin">
    <router-link to="/home"><Button type="primary" id="lab">2100-lab</Button></router-link>
    <router-link to="/home"><Button type="primary" id="home_but">前往首页</Button></router-link>
    <Divider />
    <h1>2100实验室</h1>
    <form method="POST" @submit.prevent="Is_normal_nubmer">
    <span><Input type="input" placeholder="请输入手机号码" size="large" icon="ios-phone-portrait" style="width: 56%;" name="手机号码" v-model="login.phone_number"/></span>
    <span><input type="submit" id="getCodeButton" value="获取验证码" /></span>
    </form>
    <form method="POST" @submit.prevent="comparecode">
    <Poptip trigger="focus" title="提示" content="注意区分大小写！">
    <Input type="input" placeholder="请输入验证码"  style="width: 168%;" size="large" icon="ios-key-outline" v-model="login.usercode" />
    </Poptip>
    <br>
    <div><input v-bind:checked="isChecked" v-on:click="handleDisabled" type="checkbox" id="readAgreement" />我认真阅读并接受<span id="agreement" @click="instance('info')">本站协议</span></div>
    <input type="submit" id="login" value="登录" />
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
      },
      isDisabled: false,
      isChecked: false
    }
  },
  methods: {
    instance(type) {
      const title = '2100实验室用户协议'
      const content =
        '<p><ul style="list-style: none;"><li>第一，绝不意气用事。</li><li>第二，绝不漏判任何一件坏事。</li><li>第三，绝对裁判的公正漂亮。</li></ul></p>'
      switch (type) {
        case 'info':
          this.$Modal.info({
            title: title,
            content: content
          })
          break
      }
    },
    handleDisabled: function() {
      this.isChecked = !this.isChecked
      if (this.isChecked === true) {
        this.isDisabled = true
      } else {
        this.isDisabled = false
      }
    },
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
      } else if (this.isDisabled === false) {
        alert('必须同意协议才可进行登录')
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
#home_but {
  margin-left: 130%;
  float: left;
  font-size: 18px;
}
#lab {
  margin-left: -60%;
  font-size: 18px;
  float: left;
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
#UserLogin h1 {
  background: #2d8cf0;
  padding: 20px 0;
  font-size: 160%;
  font-weight: 300;
  text-align: center;
  color: #fff;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
}
form {
  background: #f0f0f0;
  padding: 6% 4%;
}
#home_but {
  margin-left: 170%;
  float: left;
}
#getCodeButton {
  width: 43%;
  height: 33px;
  outline: none;
  border-radius: 4px;
  border: none;
  background-color: #2d8cf0;
  color: #fff;
  cursor: pointer;
}
#getCodeButton:hover {
  background: #57a3f3;
}
#login {
  width: 100%;
  height: 33px;
  margin-top: 10px;
  outline: none;
  border-radius: 4px;
  border: none;
  background-color: #2d8cf0;
  color: #fff;
  cursor: pointer;
}
#login:hover {
  background: #57a3f3;
}
#readAgreement {
  margin: 8px;
}
#agreement {
  text-decoration: underline;
  cursor: pointer;
  color: #0000d6;
}
</style>
