<template>
  <div class="main">
    <p class="text">2100lab后台管理员登陆</p>
    <Form ref="formInline" :model="formInline" :rules="ruleInline" label-position="centre" :label-width="100">
      <FormItem prop="user" label="用户名：">
        <Input type="text" v-model="formInline.user" placeholder="Username" class="input" />
        <Icon type="ios-person-outline" slot="prepend"></Icon>
      </FormItem>
      <FormItem prop="password" label="密码：">
        <Input type="password" v-model="formInline.password" placeholder="Password" class="input" />
        <Icon type="ios-lock-outline" slot="prepend"></Icon>
      </FormItem>
      <FormItem>
        <Button type="primary" @click="handleSubmit()">登录</Button>
      </FormItem>
    </Form>
  </div>
</template>

<script>
export default {
  name: 'backlogin',
  data() {
    return {
      formInline: {
        user: '',
        password: ''
      },
      ruleInline: {
        user: [{ required: true, message: '请输入账号', trigger: 'blur' }],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          {
            type: 'string',
            min: 6,
            message: '密码不能短于6位！',
            trigger: 'blur'
          }
        ]
      }
    }
  },
  methods: {
    handleSubmit() {
      var managerlogin = JSON.stringify(this.formInline)
      this.$http
        .post('http://192.168.55.33:8000' + '/app/manager_login', managerlogin)
        .then(response => {
          if (response.data.data === 'true') {
            this.$router.push({
              path: '/backstage',
              name: 'backstage',
              params: {
                user: this.formInline.user
              }
            })
          } else {
            this.$Message.error('用户名或密码错误！')
          }
        })
    }
  }
}
</script>

<style scoped>
.main {
  margin: 15% 30%;
}

.text {
  position: center;
  margin-bottom: 20px;
  font-size: 40px;
}

.input {
  width: 300px;
  margin-bottom: 20px;
}
</style>
