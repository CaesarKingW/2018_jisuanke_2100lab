<template>
  <div id="backstageRegister">
    <div id="regColumn">
      <div id="mobilePanel"></div>
      <div id="title"><h1>2100实验室后台注册</h1></div>
    <Form ref="formInline" :model="formInline">
      <FormItem prop="user">
        <div id="userInputDiv"><i-input type="text" id="userInput" v-model="formInline.user" placeholder="请输入用户名" @on-blur="check()">
          <Icon type="ios-person-outline" slot="prepend"></Icon>
        </i-input>
        </div>
      </FormItem>
      <FormItem prop="password">
        <div id="pwdOneDiv"><i-input type="password" id="pwdOneInput" v-model="formInline.password" placeholder="请输入密码" @on-blur="check_two()">
          <Icon type="ios-lock-outline" slot="prepend"></Icon>
        </i-input>
        </div>
      </FormItem>
      <FormItem prop="confirm">
        <div id="pwdTwoDiv">
        <i-input type="password" id="pwdTwoInput" v-model="formInline.confirm" placeholder="请确认密码" @on-blur="Confirm()">
          <Icon type="ios-eye-outline" slot="prepend" />
        </i-input>
        </div>
      </FormItem>
      <FormItem>
       <div id="regBtnDiv"><Button type="primary" id="regButton" @click="register()">立刻注册</Button></div>
      </FormItem>
      <FormItem>
        <div id="logBtnDiv"><Button type="primary" id="logButton" @click="login()" v-if="can_login">立刻登录</Button></div>
      </FormItem>
    </Form>
  </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      prompt1: false,
      if_exist: null,
      prompt2: false,
      if_match: null,
      blank1: false,
      if_blank1: null,
      blank2: false,
      if_blank2: null,
      can_login: false,
      formInline: {
        user: '',
        password: '',
        confirm: ''
      }
    }
  },
  methods: {
    check() {
      if (this.formInline.user === '') {
        this.if_blank1 = true
        this.blank1 = true
        this.$Message.warning('用户名不可为空！')
      } else {
        this.if_blank1 = false
        this.blank1 = true
        this.$http
          .post(
            'http://192.168.55.33:8000/app/check',
            JSON.stringify({
              username: this.formInline.user
            })
          )
          .then(response => {
            var res = response.data
            this.if_exist = res['if_exist']
            if (res['if_exist'] === true) {
              this.$Message.error('用户名已存在！')
            } else {
              this.$Message.success('用户名可用！')
            }
            this.prompt1 = true
          })
      }
    },
    check_two() {
      if (this.formInline.password === '') {
        this.if_blank2 = true
        this.$Message.warning('密码不可为空！')
      } else {
        this.if_blank2 = false
      }
      this.blank2 = true
    },
    Confirm() {
      if (this.formInline.password === this.formInline.confirm) {
        this.if_match = true
        this.$Message.success('两次输入密码一致！')
      } else {
        this.if_match = false
        this.$Message.error('两次输入密码不一致！')
      }
      this.prompt2 = true
    },
    register() {
      if (
        this.if_blank1 === false &&
        this.if_blank2 === false &&
        this.if_exist === false &&
        this.if_match === true
      ) {
        this.$http
          .post(
            'http://192.168.55.33:8000/app/backstage_register',
            JSON.stringify({
              username: this.formInline.user,
              password: this.formInline.password
            })
          )
          .then(response => {
            this.$Message.success('注册成功！')
            this.can_login = true
          })
      }
    },
    login() {
      this.$http
        .post(
          'http://192.168.55.33:8000/app/backstage_login',
          JSON.stringify({
            username: this.formInline.user,
            password: this.formInline.password
          })
        )
        .then(response => {
          this.$Message.success('登录成功！')
          this.$router.push({ name: 'backstage' })
        })
    }
  }
}
</script>
<style scoped>
#regColumn {
  width: 35%;
  margin-top: 6%;
  margin-left: 32%;
  transition: opacity 1s;
  -webkit-transition: opacity 1s;
  background-size: 100% 100%;
  border: #f1f1f1 solid 1px;
  border-radius: 8px;
}
#regColumn:hover {
  box-shadow: 5px 5px 2px #888888;
}
#regColumn h1 {
  background: #075182;
  padding: 20px 0;
  font-size: 160%;
  font-weight: 15px;
  text-align: center;
  color: #fff;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}
#userInputDiv,
#pwdOneDiv,
#pwdTwoDiv {
  margin-top: 5%;
  width: 95%;
  margin-left: 2.5%;
  margin: 0 auto;
}
#userInputDiv {
  margin-top: 5%;
}
#regButton,
#logButton {
  background-color: #fff;
  color: #000;
  font-size: 15px;
  border: #000 solid 1px;
  border-radius: 8px;
  width: 90px;
  height: 35px;
  margin: 0 auto;
  text-align: center;
  position: static;
}
#regBtnDiv,
#logBtnDiv {
  margin-left: 40%;
}
@media screen and (max-width: 500px) {
  #regColumn {
    width: 95%;
    margin-top: 6%;
    margin-left: 2.5%;
    transition: opacity 1s;
    -webkit-transition: opacity 1s;
    background-size: 100% 100%;
    border: #f1f1f1 solid 1px;
    border-radius: 8px;
    margin-top: 120px;
  }
  #regColumn:hover {
    box-shadow: 5px 5px 2px #888888;
  }
  #regColumn h1 {
    background: #075182;
    padding: 20px 0;
    font-size: 160%;
    font-weight: 15px;
    text-align: center;
    color: #fff;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
  }
  #userInputDiv,
  #pwdOneDiv,
  #pwdTwoDiv {
    margin-top: 5%;
    width: 95%;
    margin-left: 2.5%;
    margin: 0 auto;
  }
  #userInputDiv {
    margin-top: 5%;
  }
  #regButton,
  #logButton {
    background-color: #fff;
    color: #000;
    font-size: 15px;
    border: #000 solid 1px;
    border-radius: 8px;
    width: 90px;
    height: 35px;
    margin: 0 auto;
    text-align: center;
    position: static;
  }
  #regBtnDiv,
  #logBtnDiv {
    margin-left: 38%;
  }
}
</style>
