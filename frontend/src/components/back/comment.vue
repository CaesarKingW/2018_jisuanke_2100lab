<template>
<div>
    <div>
        <input v-model="phone_number" placeholder='请输入用户手机号以搜索其留言'> <button @click="search()">搜索</button>
    </div>
    <div v-show='is_show'>
    <div v-if = 'if_user===false'>
        对不起，您搜索的用户不存在
    </div>
    <div v-else-if='if_comment===false'>
        对不起，不存在您所搜索的用户的留言
    </div>
    <div v-else>
        <ul><li v-for="message in messages" :key="message.id">用户{{phone_number}}在{{message.created_at}}时对第{{message.course_id}}号课程《{{message.course_title}}》发表评论“{{message.content}}”。<button @click="delete_comment(message.id)">删除</button></li></ul>
    </div>
    </div>
</div>
</template>

<script>
export default {
  name: 'comment',
  data() {
    return {
      is_show: false,
      phone_number: '',
      if_user: null,
      if_comment: null,
      messages: []
    }
  },
  methods: {
    search() {
      var phoneNumber = JSON.stringify(this.phone_number)
      this.$http
        .post(this.GLOBAL.serverSrc + '/app/search_comment', phoneNumber)
        .then(response => {
          var res = response.data
          console.log(res)
          if (res.if_user === false) {
            this.if_user = false
          } else {
            if (res.if_comment === false) {
              this.if_comment = false
            } else {
              this.if_user = true
              this.if_comment = true
              this.messages = res.messages
              console.log(this.messages)
            }
          }
        })
      this.is_show = true
    },
    delete_comment(messageId) {
      alert('删除成功！')
      console.log(this.phone_number)
      console.log(messageId)
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/delete_comment',
          JSON.stringify({
            message_id: messageId,
            phone_number: this.phone_number
          })
        )
        .then(response => {
          var res = response.data
          console.log(res)
          if (res.if_user === false) {
            this.if_user = false
          } else {
            if (res.if_comment === false) {
              this.if_comment = false
            } else {
              this.if_user = true
              this.if_comment = true
              this.messages = res.messages
              console.log(this.messages)
            }
          }
        })
    }
  }
}
</script>

<style>
</style>
