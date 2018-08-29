<template>
  <div>
    <Input v-model="username" placeholder="请输入待搜索管理员的用户名" id="username" />
    <Button @click="search()">搜索</Button>
    <div v-if="if_show">
      <div v-if="if_exist">
        <Divider/>
        <p>课程处理
          <i-switch v-model="Manage_course" class="auth" />
        </p>
        <Divider/>
        <p>用户管理
          <i-switch v-model="Manage_user" class="auth" />
        </p>
        <Divider/>
        <p>留言管理
          <i-switch v-model="Manage_message" class="auth" />
        </p>
        <Divider/>
        <p>订单处理
          <i-switch v-model="Manage_order" class="auth" />
        </p>
        <Divider/>
        <Button @click="modify_auth()">保存</Button>
      </div>
      <div v-else>
        对不起，您搜索的管理员不存在
      </div>
    </div>
  </div>
</template>
<script>
export default {
  created: function() {
    this.$http
      .post('http://192.168.55.33:8000/app/get_mstatus')
      .then(response => {
        var res = response.data
        this.mis_login = res.mis_login
        if (!this.mis_login) {
          alert('还没有登录，无权访问该页面！')
          location.href = '/#/backstageLogin'
        } else {
          if (res.manager.Supermanager !== true) {
            alert('你没有权限访问该网页！')
            location.href = '/#/backstage'
          }
        }
      })
  },
  data() {
    return {
      username: '',
      Manage_course: null,
      Manage_user: null,
      Manage_message: null,
      Manage_order: null,
      if_show: false,
      if_exist: null
    }
  },
  methods: {
    search() {
      var username = JSON.stringify(this.username)
      this.$http
        .post('http://192.168.55.33:8000/app/search_manager', username)
        .then(response => {
          var res = response.data
          this.if_exist = res.if_exist
          if (this.if_exist) {
            this.Manage_course = res.manager.Manage_course
            this.Manage_user = res.manager.Manage_user
            this.Manage_message = res.manager.Manage_message
            this.Manage_order = res.manager.Manage_order
          }
          this.if_show = true
        })
    },
    modify_auth() {
      this.$http
        .post(
          'http://192.168.55.33:8000/app/modify',
          JSON.stringify({
            username: this.username,
            Manage_course: this.Manage_course,
            Manage_user: this.Manage_user,
            Manage_message: this.Manage_message,
            Manage_order: this.Manage_order
          })
        )
        .then(response => {
          alert('修改管理员' + this.username + '权限成功！')
          this.if_show = false
          this.username = ''
        })
    }
  }
}
</script>
<style>
.auth {
  float: right;
}

p {
  font-size: 15px;
}

#username {
  width: 300px;
}
</style>
