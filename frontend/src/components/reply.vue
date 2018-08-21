
<template>
<div id="reply">
    <button v-on:click="dispaly_inputfield">回复</button>
       <form v-show="IsShow" @submit.prevent="commit_reply()">
      <input type="text" v-model="replyContent">
      <input type="submit" value="确定"/>
    </form>
    <div v-for="r of replies" :key="r.key">
              <h5>
                 &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;{{r.fields.user_phone}}
              </h5>
              <h4>
                  &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;{{r.fields.content}}
              </h4>
          </div>
</div>
</template>
<script>
export default {
  props: ['title', 'user_phone'],
  data: function() {
    return {
      IsShow: false,
      replyContent: null,
      replies: []
    }
  },
  mounted: function() {
    this.show_reply()
  },
  methods: {
    show_reply: function() {
      this.$http
        .post(
          'http://192.168.55.33:8000/app/show_reply',
          JSON.stringify(this.title)
        )
        .then(
          response => {
            this.replies = response.data.list
            console.log('success')
          },
          response => {
            console.log('error')
          }
        )
    },
    dispaly_inputfield: function() {
      this.IsShow = !this.IsShow
    },
    commit_reply: function() {
      var formDate = JSON.stringify({
        content: this.replyContent,
        user_phone: this.user_phone,
        message_id: this.title
      })
      console.log(formDate)
      this.$http.post('http://192.168.55.33:8000/app/add_reply', formDate).then(
        response => {
          this.show_reply()
          this.IsShow = false
          this.replyContent = null
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
