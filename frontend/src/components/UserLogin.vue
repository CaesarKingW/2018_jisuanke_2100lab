<template>
<div id="UserLogin">
    <Button id="lab" ghost><router-link to="/home"><div id="button_text">2100-lab <Icon type="md-log-in" /></div></router-link></Button>
    <br>
    <br>
    <div id="log_column">
    <h1>2100实验室</h1>
    <form method="POST" @submit.prevent="Is_normal_nubmer">
    <Input type="input" placeholder="请输入手机号码" size="large" icon="ios-phone-portrait" style="width: 56%;" v-model="login.phone_number"/>
    <input type="submit" id="getCodeButton" value="获取验证码" />
    </form>
    <form id="log_down" method="POST" @submit.prevent="comparecode">
    <Poptip trigger="focus" title="提示" content="注意区分大小写！">
    <Input type="input" placeholder="请输入验证码" size="large" style="width: 366px;" icon="ios-key-outline" v-model="login.usercode" />
    </Poptip>
    <br>
    <div><input v-bind:checked="isChecked" v-on:click="handleDisabled" type="checkbox" id="readAgreement" />我认真阅读并接受<span id="agreement" @click="instance('info')">本站协议</span></div>
    <input type="submit" id="login" value="登录" />
    </form>
    </div>
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
    success_login() {
      this.$Message.success('恭喜您！登录成功')
    },
    alert_input_phone() {
      this.$Message.warning('请输入您的手机号码')
    },
    alert_input_code() {
      this.$Message.warning('请输入您收到的验证码')
    },
    alert_agreement() {
      this.$Message.warning('只有同意用户协议才可以登录哦')
    },
    alert_wrong_code() {
      this.$Message.error('验证码输入错误')
    },
    alert_wrong_phone() {
      this.$Message.error('请输入正确的电话号码')
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
        this.alert_input_phone()
      } else if (
        !this.login.usercode &&
        typeof this.login.usercode !== 'undefined' &&
        this.login.usercode !== 0
      ) {
        this.alert_input_code()
      } else if (this.isDisabled === false) {
        this.alert_agreement()
      } else if (
        this.login.usercode === this.login.checkCode &&
        this.commit_phone === this.login.phone_number
      ) {
        this.success_login()
        this.Register_new_user()
        this.login.phone_number = null
        this.login.checkCode = null
        this.login.usercode = null
        this.commit_phone = null
        // 用户跳转到主页
      } else this.alert_wrong_code()
      console.log(this.login.phone_number)
    },
    Is_normal_nubmer: function() {
      if (!/^1[34578]\d{9}$/.test(this.login.phone_number)) {
        this.alert_wrong_phone()
      } else {
        this.getcode()
      }
    },
    Register_new_user: function() {
      var userphone = JSON.stringify(this.login.phone_number)
      this.$http
        .post('http://192.168.55.33:8000/app/register_new_user', userphone)
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
<style scoped>
#lab {
  margin-left: 1032px;
  font-size: 18px;
  margin-top: 28px;
  margin-bottom: 18px;
  height: 41px;
  border-radius: 4px;
  border: none;
  background-color: #075182;
}
#lab:hover {
  background: #285f83;
}
#button_text {
  color:#fff;
}
#UserLogin {
  background-image: url('../assets/BALL.jpg');
  background-repeat: no-repeat;
  background-size: 100% 100%;
  height: 583px;
  /* background-attachment: fixed; */
}
#log_column {
  width: 400px;
  margin-left: 60%;
  margin-top: 3%;
  transition: opacity 1s;
  -webkit-transition: opacity 1s;
  background-size: 100% 100%;
}
#log_column h1 {
  background: #075182;
  padding: 20px 0;
  font-size: 160%;
  font-weight: 15px;
  text-align: center;
  color: #fff;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}
form {
  background: #f0f0f0;
  padding: 4% 4%;
}
#log_down {
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
}
#getCodeButton {
  width: 43%;
  height: 33px;
  outline: none;
  border-radius: 4px;
  border: none;
  background-color: #075182;
  color: #fff;
  cursor: pointer;
}
#getCodeButton:hover {
  background: #285f83;
}
#login {
  width: 100%;
  height: 33px;
  margin-top: 10px;
  outline: none;
  border-radius: 4px;
  border: none;
  background-color: #075182;
  color: #fff;
  cursor: pointer;
}
#login:hover {
  background: #285f83;
}
#readAgreement {
  margin: 6px;
}
#agreement {
  text-decoration: underline;
  cursor: pointer;
  color: #0000d6;
}
</style>
