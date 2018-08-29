<template>
<div id="UserLogin">
    <br>
    <br>
    <div class="logColumn">
    <router-link to="/home"><h1>2100实验室</h1></router-link>
    <form method="POST" @submit.prevent="Is_normal_nubmer">
    <Input id="inputPhone" type="text" placeholder="请输入手机号码" size="large" icon="ios-phone-portrait" v-model="phone_number"/>
    <input type="submit" id="getCodeButton" value="获取验证码" />
    </form>
    <form id="logDown" method="POST" @submit.prevent="comparecode">
    <div class="caseSensitive"><Icon type="ios-alert" />&nbsp;&nbsp;请注意区分验证码大小写！</div>
    <Input type="text" placeholder="请输入验证码" size="large" icon="ios-key-outline" v-model="usercode"/>
    <div><input v-bind:checked="isChecked" v-on:click="handleDisabled" type="checkbox" id="readAgreement"/> 我认真阅读并接受<span id="agreement" @click="instance('info')">本站协议</span></div>
    <input type="submit" id="login" value="登录" />
    </form>
    </div>
</div>
</template>
<script>
export default {
  data() {
    return {
      phone_number: null,
      usercode: null,
      isDisabled: false,
      isChecked: false,
      status: false,
      is_login: false,
      count: 60
    }
  },
  mounted: function() {
    this.$Message.config({
      top: 120
    })
    this.$http
      .post(this.GLOBAL.serverSrc + '/app/get_status')
      .then(response => {
        this.is_login = response.data.is_login
        if (this.is_login) {
          this.alert_wrong_status()
          location.href = '/#/home'
        }
      })
  },
  methods: {
    timedCount: function() {
      document.getElementById('getCodeButton').disabled = true
      document.getElementById('getCodeButton').value =
        this.count + 's后重新获取验证码'
      this.count = this.count - 1
      if (this.count !== 0) {
        let _this = this
        setTimeout(() => {
          _this.timedCount()
        }, 1000)
      } else {
        this.count = 60
        document.getElementById('getCodeButton').disabled = false
        document.getElementById('getCodeButton').value = '获取验证码'
      }
    },
    instance(type) {
      const title = '2100实验室用户协议'
      const content = '<p>在此处输入用户协议。</p>'
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
    alert_wrong_status() {
      this.$Message.error('您已经登录了')
    },
    alert_wrong_user() {
      this.$Message.error('您的手机号已被注销，请更换手机号')
    },
    handleDisabled: function() {
      this.isChecked = !this.isChecked
      if (this.isChecked === true) {
        this.isDisabled = true
      } else {
        this.isDisabled = false
      }
    },
    getcode: function() {
      var phonenumber = JSON.stringify(this.phone_number)
      this.$http
        .post(this.GLOBAL.serverSrc + '/app/get_code_post', phonenumber)
        .then(
          response => {
            var Isexists = response.data.Is_exists
            if (Isexists === false) {
              this.alert_wrong_user()
              this.phone_number = null
            }
          },
          response => {}
        )
    },
    comparecode: function() {
      if (
        !this.phone_number &&
        typeof this.phone_number !== 'undefined' &&
        this.phone_number !== 0
      ) {
        this.alert_input_phone()
      } else if (
        !this.usercode &&
        typeof this.usercode !== 'undefined' &&
        this.usercode !== 0
      ) {
        this.alert_input_code()
      } else if (this.isDisabled === false) {
        this.alert_agreement()
      } else {
        this.verify_the_login()
      }
    },
    Is_normal_nubmer: function() {
      if (!/^1[34578]\d{9}$/.test(this.phone_number)) {
        this.alert_wrong_phone()
      } else {
        this.getcode()
        this.timedCount()
      }
    },
    Register_new_user: function() {
      var userphone = JSON.stringify(this.phone_number)
      this.$http
        .post(this.GLOBAL.serverSrc + '/app/register_new_user', userphone)
        .then(response => {}, response => {})
    },
    verify_the_login: function() {
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/get_user_code',
          JSON.stringify({
            phone_number: this.phone_number,
            code: this.usercode
          })
        )
        .then(
          response => {
            this.status = response.data.status
            if (this.status) {
              this.success_login()
              this.Register_new_user()
              this.phone_number = null
              this.usercode = null
              this.commit_phone = null
              // 用户跳转到主页
              location.href = '/#/home'
            } else {
              this.alert_wrong_code()
            }
          },
          response => {}
        )
    }
  }
}
</script>
<style scoped>
#inputPhone {
  width: 60%;
}

.caseSensitive {
  font-size: 13px;
  margin-bottom: 5px;
}

#codeInput {
  width: 160%;
}

#lab {
  margin-left: 25%;
  font-size: 18px;
  margin-top: 18.5%;
  margin-bottom: 18px;
  height: 41px;
  position: fixed;
  border-radius: 4px;
}

#buttonText {
  color: #000;
}

#UserLogin {
  margin: 0 auto;
  background-image: url('../assets/BALL.jpg');
  background-repeat: no-repeat;
  background-size: cover;
  background-color: #022336;
  width: 100%;
  height: 100%;
  height: 585px;
  background-size: cover;
}

.logColumn {
  width: 45%;
  margin-left: 52%;
  margin-top: 6%;
  transition: opacity 1s;
  -webkit-transition: opacity 1s;
  background-size: 100% 100%;
}

.logColumn h1 {
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
  background: #fff;
  padding: 2% 3%;
}

#logDown {
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
}

#getCodeButton {
  width: 39%;
  height: 33px;
  margin-top: 10px;
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
  margin-top: 8px;
  margin-bottom: 6px;
}

#agreement {
  text-decoration: underline;
  cursor: pointer;
  color: #0000d6;
}
</style>
