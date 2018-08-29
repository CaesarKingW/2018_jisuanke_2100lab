<template>
  <div id="reply">
    <button id="replyButton" v-on:click="dispaly_inputfield">回复</button>
    <form v-show="IsShow" @submit.prevent="commit_reply()">
      <Input id="replyContent" placeholder="说说你对这条留言的看法吧" type="textarea" v-model="replyContent" />
      <div id="submitArea"><input id="replySubmit" type="submit" value="确定" /></div>
    </form>
    <div v-for="r of replies" :key="r.key">
      <Card id="replyCard">
        <div id="replyUser">
          &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;
          <Icon id="replyIcon" type="md-chatboxes" /> 用户:{{r.user_name}}
        </div>
        <div id="replyContent">
          &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;{{r.content}}
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
          this.GLOBAL.serverSrc + '/app/show_reply',
          JSON.stringify(this.title)
        )
        .then(
          response => {
            this.replies = response.data.list
          },
          response => {}
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
      this.$http.post(this.GLOBAL.serverSrc + '/app/add_reply', formDate).then(
        response => {
          this.show_reply()
          this.IsShow = false
          this.replyContent = null
        },
        response => {}
      )
    }
  }
}
</script>
<style scoped>
#replyIcon {
  font-size: 30px;
}

#replyCard {
  border-radius: 0px;
}

#replySubmit {
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

#submitArea {
  text-align: center;
}

#replySubmit:hover {
  background: rgb(245, 242, 242);
  cursor: pointer;
}

#replyButton {
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

#replyButton:hover {
  background: rgb(245, 242, 242);
  cursor: pointer;
}

#replyContent,
replyUser {
  font-family: 华文中宋;
  font-size: 16px;
}

#replyContent {
  width: 100%;
  color: gray;
}

#replyUser {
  font-size: 16px;
  font-family: 微软雅黑;
}
</style>
