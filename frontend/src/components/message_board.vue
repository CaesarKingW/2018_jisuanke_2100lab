<template>
<div id="messageboard">
  <h1>评论区</h1>
  <div v-for="item of messages" :key="item.id">
      <div>
          <h4>用户：{{item.fields.user_name}}</h4>
          <h4>
              {{item.fields.content}}
          </h4>
      </div>
  </div>
    <form method="POST" @submit.prevent="commit_message">
    <input type="input" name="留言" v-model="message"/>
    <input type="submit" value="留言"/>
    </form>
</div>
</template>
<script>
export default {
  data() {
    return {
      message: null,
      // messages:{
      //     user_name: null,
      //     content: null
      // }
      messages: []
    }
  },
  mounted: function() {
    this.$http.get('http://192.168.55.33:8000/app/show_message').then(
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
      var formDate = JSON.stringify(this.message)
      console.log(formDate)
      this.$http
        .post('http://192.168.55.33:8000/app/add_message', formDate)
        .then(
          response => {
            console.log(response.date)
          },
          response => {
            console.log('error')
          }
        )
    }
  }
}
</script>
