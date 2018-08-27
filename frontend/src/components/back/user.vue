<template>
<div>
    <input v-model="phone_number" placeholder="请输入待搜索用户的手机号">
    <button @click="search()">搜索</button>
    <div v-show="is_show">
      <div v-if="is_null==false">
        <div><img v-bind:src="head_protrait" width=60px height=80px /></div>
        <p>用户名：<span>{{username}}</span></p>
        <p>奖励金：<span>{{welfare}}元</span></p>
        <div>
            <span>是否是大V：<span>{{is_teacher}}</span></span><button @click="authenticate()">{{authenticate_button}}</button>
        </div>
        <div>
            <span>是否被禁言：<span>{{can_comment}}</span></span><button @click="forbid_comment()">{{forbid_comment_button}}</button>
        </div>
      </div>
      <div v-else>
        对不起，您搜索的用户不存在
      </div>
    </div>
</div>
</template>
<script>
export default {
  name: 'user',
  data() {
    return {
      is_show: false,
      phone_number: '',
      is_null: null,
      username: '',
      welfare: 0,
      head_protrait: '',
      is_teacher: null,
      can_comment: null,

      authenticate_button: '',
      forbid_comment_button: ''
    }
  },
  methods: {
    search() {
      console.log(this.phone_number)
      var phoneNumber = JSON.stringify(this.phone_number)
      this.$http
        .post(this.GLOBAL.serverSrc + '/app/search_user', phoneNumber)
        .then(response => {
          var res = response.data
          console.log(res)
          this.is_null = res.is_null
          if (this.is_null === false) {
            this.username = res.user_info.user_name
            this.welfare = res.user_info.welfare
            this.head_protrait = this.GLOBAL.serverSrc + ':8000' + res.user_info.head_protrait
            if (res.user_info.Is_teacher === true) {
              this.is_teacher = '是'
              this.authenticate_button = '取消大V身份'
            } else {
              this.is_teacher = '否'
              this.authenticate_button = '加V'
            }
            if (res.user_info.Can_comment === true) {
              this.can_comment = '否'
              this.forbid_comment_button = '禁言'
            } else {
              this.can_comment = '是'
              this.forbid_comment_button = '取消禁言'
            }
          }
        })
      this.is_show = true
    },
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
        .post(this.GLOBAL.serverSrc + '/app/authenticate', phoneNumber)
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
        .post(this.GLOBAL.serverSrc + '/app/forbid_comment', phoneNumber)
        .then(response => {})
    }
  }
}
</script>
<style>
</style>
