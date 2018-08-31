<template>
  <div>
    <div class="userinfo"><img v-bind:src="head_protrait" width=80px height=80px /></div>
    <p class="userinfo">用户名：
      <span>{{username}}</span>
    </p>
    <p class="userinfo">奖励金：
      <span>{{welfare}}元</span>
    </p>
    <div class="userinfo">
      <span>是否是大V：
        <span>{{is_teacher}}</span>
      </span>
      <Button class="butt" @click="authenticate()" size="small">{{authenticate_button}}</Button>
    </div>
    <div class="userinfo">
      <span>是否被禁言：
        <span>{{can_comment}}</span>
      </span>
      <Button class="butt" @click="forbid_comment()" size="small">{{forbid_comment_button}}</Button>
    </div>
  </div>
</template>
<script>
export default {
  name: 'user',
  data() {
    return {
      phone_number: '',
      username: '',
      welfare: 0,
      head_protrait: '',
      is_teacher: null,
      can_comment: null,
      authenticate_button: '',
      forbid_comment_button: ''
    }
  },
  created: function() {
    this.phone_number = this.$route.params.phone_number
    this.$http
      .post('http://192.168.55.33:8000/app/get_mstatus')
      .then(response => {
        var res = response.data
        this.mis_login = res.mis_login
        if (!this.mis_login) {
          location.href = '/#/backstageLogin'
        } else {
          if (res.manager.Manage_user !== true) {
            alert('你没有权限访问该网页！')
            location.href = '/#/backstage'
          } else {
            this.phone_number = this.$route.params.phone_number
            var phoneNumber = JSON.stringify(this.phone_number)
            this.$http
              .post('http://192.168.55.33:8000/app/search_user', phoneNumber)
              .then(response => {
                var res = response.data
                var user = res.user_info
                this.username = user.username
                this.welfare = user.welfare
                this.head_protrait = user.head_protrait
                if (user.Is_teacher === true) {
                  this.is_teacher = '是'
                  this.authenticate_button = '取消大V身份'
                } else {
                  this.is_teacher = '否'
                  this.authenticate_button = '加V'
                }
                if (user.Can_comment === true) {
                  this.can_comment = '否'
                  this.forbid_comment_button = '禁言'
                } else {
                  this.can_comment = '是'
                  this.forbid_comment_button = '取消禁言'
                }
              })
          }
        }
      })
  },
  methods: {
    authenticate() {
      if (this.is_teacher === '是') {
        alert('取消大V身份成功！')
        this.is_teacher = '否'
        this.authenticate_button = '加V'
      } else {
        alert('加V成功！')
        this.is_teacher = '是'
        this.authenticate_button = '取消大V身份'
      }
      var phoneNumber = JSON.stringify(this.phone_number)
      this.$http
        .post('http://192.168.55.33:8000/app/authenticate', phoneNumber)
        .then(response => {})
    },
    forbid_comment() {
      if (this.can_comment === '否') {
        alert('已禁言该用户！')
        this.can_comment = '是'
        this.forbid_comment_button = '取消禁言'
      } else {
        alert('已取消对该用户的禁言！')
        this.can_comment = '否'
        this.forbid_comment_button = '禁言'
      }
      var phoneNumber = JSON.stringify(this.phone_number)
      this.$http
        .post('http://192.168.55.33:8000/app/forbid_comment', phoneNumber)
        .then(response => {})
    }
  }
}
</script>
<style>
.userinfo {
  margin: 10px;
}

.butt {
  margin-left: 5px;
  color: deepskyblue;
}
</style>
