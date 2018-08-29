<template>
  <div>
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
      <FormItem>
        <Button type="primary" @click="login()">Login</Button>
      </FormItem>
      <FormItem>
        <Button type="primary" @click="register()">还没有账号？去注册</Button>
      </FormItem>
    </Form>
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
      } else {
        this.if_blank1 = false
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
</script>s
<style>
.blank {
  color: red;
}
</style>
