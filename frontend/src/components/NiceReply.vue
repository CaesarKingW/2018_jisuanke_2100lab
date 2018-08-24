<template>
<div id="reply">
    <button id="reply_button" v-on:click="dispaly_inputfield">回复</button>
       <form v-show="IsShow" @submit.prevent="commit_reply()">
      <Input id="reply_content" placeholder="说说你对这条留言的看法吧" type="textarea" v-model="replyContent" />
      <div id="submit_area"><input id="reply_submit" type="submit" value="确定"/></div>
    </form>
    <div v-for="r of replies" :key="r.key">
      <Card id="reply_card">
        <div id="reply_user">
        &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<Icon id="reply_icon" type="md-chatboxes" /> 用户:{{r.fields.user_phone}}
        </div>
        <div id="reply_content">
        &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;{{r.fields.content}}
        </div>
      </Card>
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
  watch: {
    title: function(val, oldval) {
      this.show_reply()
    }
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
<style scoped>
#reply_icon {
  font-size: 30px;
}
#reply_card {
  border-radius: 0px;
}
#reply_content {
  width: 100%;
  color: gray;
}
#reply_submit {
  width: 8%;
  height: 28px;
  text-align: center;
  font-size: 15px;
  margin-top: 10px;
  margin-bottom: 10px;
  outline: none;
  border-radius: 4px;
  border: solid 1px;
  background-color: #fff;
  cursor: pointer;
}
#submit_area {
  text-align: center;
}
#reply_submit:hover {
  background: rgb(245, 242, 242);
  cursor: pointer;
}
#reply_button {
  width: 9%;
  text-align: center;
  height: 30px;
  font-size: 20px;
  margin-top: 10px;
  margin-bottom: 10px;
  outline: none;
  border-radius: 4px;
  border: solid 1px;
  background-color: #fff;
  cursor: pointer;
}
#reply_button:hover {
  background: rgb(245, 242, 242);
  cursor: pointer;
}
#reply_content,
reply_user {
  font-family: 华文中宋;
  font-size: 16px;
}
#reply_user {
  font-size: 16px;
  font-family: 微软雅黑;
}
</style>
