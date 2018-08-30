<template>
  <div id="backstageLogin">
    <div id="logColumn">
      <div id="mobilePanel"></div>
      <div id="title"><h1>2100实验室后台</h1></div>
    <Form ref="formInline" :model="formInline">
      <FormItem prop="user">
        <div id="userInputDiv"><i-input type="text" v-model="formInline.user" placeholder="请输入用户名" @on-blur="check()">
          <Icon type="ios-person-outline" slot="prepend"></Icon>
        </i-input>
        </div>
        <!-- <div id="ifBlank1" v-if="blank1">
          <p v-if="if_blank1" class="blank">
            <Icon size=16 type="ios-alert-outline" /> 用户名不能为空
          </p>
        </div> -->
      </FormItem>
      <FormItem prop="password">
        <div id="pwdInputDiv"><i-input type="password" v-model="formInline.password" placeholder="请输入密码" @on-blur="check_two()">
          <Icon type="ios-lock-outline" slot="prepend"></Icon>
        </i-input>
        </div>
        <!-- <div v-if="blank2">
          <p v-if="if_blank2" class="blank">
            <Icon size=16 type="ios-alert-outline" /> 密码不能为空
          </p>
        </div> -->
      </FormItem>
      <FormItem>
        <Button id="loginButton" type="primary" @click="login()">立刻登录</Button>
      </FormItem>
      <FormItem>
        <Button id="regButton" type="primary" @click="register()">注册账号</Button>
      </FormItem>
    </Form>
      </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      blank1: false,
      if_blank1: null,
      blank2: false,
      if_blank2: null,
      formInline: {
        user: '',
        password: ''
      }
    }
  },
  methods: {
    check() {
      if (this.formInline.user === '') {
        this.if_blank1 = true
        this.blank1 = true
        this.$Message.warning('用户名不能为空！')
      } else {
        this.if_blank1 = false
      }
    },
    check_two() {
      if (this.formInline.password === '') {
        this.if_blank2 = true
        this.$Message.warning('密码不能为空！')
      } else {
        this.if_blank2 = false
      }
      this.blank2 = true
    },
    login() {
      if (this.if_blank1 === false && this.if_blank2 === false) {
        this.$http
          .post(
            'http://192.168.55.33:8000/app/backstage_login',
            JSON.stringify({
              username: this.formInline.user,
              password: this.formInline.password
            })
          )
          .then(response => {
            alert('登录成功！')
            this.$router.push({ name: 'backstage' })
          })
      }
    },
    register() {
      this.$router.push({ name: 'backstageRegister' })
    }
  }
}
</script>
<style scoped>
#logColumn {
  width: 35%;
  margin-top: 6%;
  margin-left: 32%;
  transition: opacity 1s;
  -webkit-transition: opacity 1s;
  background-size: 100% 100%;
  border: #f1f1f1 solid 1px;
  border-radius: 8px;
}
#logColumn:hover {
  box-shadow: 5px 5px 2px #888888;
}

#logColumn h1 {
  background: #075182;
  padding: 20px 0;
  font-size: 160%;
  font-weight: 15px;
  text-align: center;
  color: #fff;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}
.blank {
  color: red;
  font-size: 13px;
}
#backstageLogin {
  text-align: center;
}
#userInputDiv {
  margin-top: 5%;
  width: 95%;
  margin-left: 2.5%;
}
#pwdInputDiv {
  width: 95%;
  margin-left: 2.5%;
}
#loginButton {
  background-color: #fff;
  color: #000;
  font-size: 15px;
  border: #000 solid 1px;
  border-radius: 8px;
  width: 90px;
  height: 35px;
  /* margin: 0 auto; */
  text-align: center;
  position: static;
}
#regButton {
  background-color: #fff;
  color: #000;
  font-size: 15px;
  border: #000 solid 1px;
  border-radius: 8px;
  width: 90px;
  height: 35px;
  /* margin: 0 auto; */
  text-align: center;
  position: static;
}
@media screen and (max-width: 500px) {
  #backstageLogin {
    width: 100%;
    height: 700px;
  }
  #logColumn {
    background-color: #fff;
    width: 95%;
    margin-top: 25%;
    margin-left: 2%;
    transition: opacity 1s;
    -webkit-transition: opacity 1s;
    background-size: 100% 100%;
    border: #022336 solid 1px;
    border-radius: 8px;
  }
  #logColumn:hover {
    box-shadow: 5px 5px 2px #888888;
  }

  #logColumn h1 {
    background: #075182;
    padding: 20px 0;
    font-size: 160%;
    font-weight: 15px;
    text-align: center;
    color: #fff;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
  }
  .blank {
    color: red;
    font-size: 13px;
  }
  #backstageLogin {
    text-align: center;
  }
  #userInputDiv {
    margin-top: 5%;
    width: 95%;
    margin-left: 2.5%;
  }
  #pwdInputDiv {
    width: 95%;
    margin-left: 2.5%;
  }
  #loginButton {
    background-color: #fff;
    color: #000;
    font-size: 15px;
    border: #000 solid 1px;
    border-radius: 8px;
    width: 90px;
    height: 35px;
    /* margin: 0 auto; */
    text-align: center;
    position: static;
  }
  #regButton {
    background-color: #fff;
    color: #000;
    font-size: 15px;
    border: #000 solid 1px;
    border-radius: 8px;
    width: 90px;
    height: 35px;
    /* margin: 0 auto; */
    text-align: center;
    position: static;
  }
}
</style>
