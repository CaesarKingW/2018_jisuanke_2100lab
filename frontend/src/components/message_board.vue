<template>
<div id="messageboard">
  <h1>评论区</h1>
  <div v-for="(item, index) of messages" :key="item.id">
      <div>
          <h4>用户：{{item.fields.user_phone}}</h4>
          <h4>
              {{item.fields.content}}
              {{index}}
          </h4>
          <reply v-bind:title="item.pk"></reply>
      </div>
  </div>
    <form method="POST" @submit.prevent="commit_message">
    <input type="input" name="留言" v-model="message"/>
    <input type="submit" value="留言"/>
    </form>
</div>
</template>
<script>
import reply from './reply.vue'
export default {
  data() {
    return {
      message: null,
      // messages:{
      //     user_name: null,
      //     content: null
      // }
      messages: [],
      reply: [],
      replies: [],
      course_id: 1,
      user_phone: '17602284691'
    }
  },
  components: {
    reply
  },
  mounted: function() {
    this.$http
      .post(
        'http://192.168.55.33:8000/app/show_message',
        JSON.stringify(this.course_id)
      )
      .then(
        response => {
          this.messages = response.data.list
          console.log(this.messages)
          console.log('success')
        },
        response => {
          console.log('error')
        }
      )
  },
  methods: {
    commit_message: function() {
      var formDate = JSON.stringify({
        content: this.message,
        user_phone: this.user_phone,
        course_id: this.course_id
      })
      console.log(formDate)
      this.$http
        .post('http://192.168.55.33:8000/app/add_message', formDate)
        .then(
          response => {
            console.log(response.data)
          },
          response => {
            console.log('error')
          }
        )
    }
  }
}
</script>
