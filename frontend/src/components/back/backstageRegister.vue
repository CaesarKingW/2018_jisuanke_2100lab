<template>
  <div >
    <Form ref="formInline" :model="formInline">
        <FormItem prop="user">
            <i-input type="text" v-model="formInline.user" placeholder="Username" @on-blur="check()">
                <Icon type="ios-person-outline" slot="prepend"></Icon>
            </i-input>
            <div v-if="blank1">
                <p v-if="if_blank1" class="blank">
                    用户名不能为空
                </p>
            </div>
            <div v-if="prompt1">
            <p v-if="if_exist" id="exist">用户名已存在</p>
            <p v-else id="notexist">该用户名可使用</p>
            </div>
        </FormItem>
        <FormItem prop="password">
            <i-input type="password" v-model="formInline.password" placeholder="Password" @on-blur="check_two()">
                <Icon type="ios-lock-outline" slot="prepend"></Icon>
            </i-input>
            <div v-if="blank2">
                <p v-if="if_blank2" class="blank">
                    密码不能为空
                </p>
            </div>
        </FormItem>
        <FormItem prop="confirm">
            <i-input type="password" v-model="formInline.confirm" placeholder="Password-comfirm" @on-blur="Confirm()">
            <Icon type="ios-eye-outline" slot="prepend"/>
            </i-input>
            <div v-if="prompt2">
            <p v-if="if_match" id="matched">两次密码一致</p>
            <p v-else id="unmatched">两次密码不一致</p>
            </div>
        </FormItem>
        <FormItem>
            <Button type="primary" @click="register()">Register</Button>
        </FormItem>
        <FormItem>
            <Button type="primary" @click="login()" v-if="can_login">使用新注册的帐号登录</Button>
        </FormItem>
    </Form>
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
      } else {
        this.if_blank1 = false
        this.blank1 = true
        console.log(this.formInline.user)
        this.$http
          .post(
            'http://192.168.55.33:8000/app/check',
            JSON.stringify({
              username: this.formInline.user
            })
          )
          .then(response => {
            var res = response.data
            console.log(res)
            this.if_exist = res['if_exist']
            this.prompt1 = true
          })
      }
    },
    check_two() {
      if (this.formInline.password === '') {
        this.if_blank2 = true
      } else {
        this.if_blank2 = false
      }
      this.blank2 = true
    },
    Confirm() {
      console.log(this.formInline.password)
      console.log(this.formInline.confirm)
      if (this.formInline.password === this.formInline.confirm) {
        this.if_match = true
      } else {
        this.if_match = false
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
            var res = response.data
            console.log(res)
            alert('注册成功！')
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
          var res = response.data
          console.log(res)
          alert('登录成功！')
          this.$router.push({ name: 'backstage' })
        })
    }
  }
}
</script>
<style>
#matched,
#notexist {
  color: green;
}
#unmatched,
#exist,
.blank {
  color: red;
}
</style>
