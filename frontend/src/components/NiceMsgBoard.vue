<template>
<div id="NiceMsgBoard">
  <div id="comment_alert">
  <Alert show-icon>
        <div id="comment_title">留言区</div>
        <Icon id="text_icon" type="md-text" slot="icon"></Icon>
  </Alert>
  </div>
  <form method="POST" @submit.prevent="commit_message">
    <div id="post_font"><Input v-model="message" type="textarea" :rows="4" id="post_column" placeholder="请在此畅所欲言……" /></div>
    <div id="post_button_area"><input id="post_button" type="submit" value="发送留言 (ゝ∀･)"/></div>
    </form>
  <div v-for="(item, index) of messages" :key="item.id">
    <Divider />
    <Card class="one_comment_card">
      <div class="one_comment_div">
          <div id="user_name"><Icon id="comment_icon" type="md-person" /> 用户：{{item.user_name}}</div>
          <div class="one_content_div">
              {{item.content}}
          </div>
          <button id="like_button" v-on:click="praise(item.id, index)"><span style="color: red">❤</span> ：{{item.praise_count}}</button>
          <NiceReply v-bind:title="item.id" v-bind:user_phone="user_phone"></NiceReply>
      </div>
    </Card>
  </div>
</div>
</template>
<script>
import NiceReply from './NiceReply.vue'
export default {
  data() {
    return {
      message: null,
      messages: [],
      NiceReply: [],
      NiceReplies: [],
      // 先假定当前课程为1，用户手机号为17602284691
      course_id: 1,
      user_phone: ''
    }
  },
  components: {
    NiceReply
  },
  mounted: function() {
    this.$http
      .post('http://192.168.55.33:8000/app/get_status')
      .then(response => {
        this.user_phone = response.data.list[0].pk
        console.log(this.user_phone)
      })
    this.show_message()
  },
  methods: {
    show_message: function() {
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
            this.show_message()
            this.message = null
            console.log(response.data)
          },
          response => {
            console.log('error')
          }
        )
    },
    praise: function(messageid, index) {
      var formDate = JSON.stringify({
        message_id: messageid,
        user_phone: this.user_phone
      })
      this.$http.post('http://192.168.55.33:8000/app/praise', formDate).then(
        response => {
          var hasPraise = response.data.has_praise
          this.show_message()
          console.log(response.data)
          console.log(hasPraise)
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
#user_name {
  font-size: 18px;
  font-family: 微软雅黑;
}
#comment_icon {
  font-size: 35px;
}
#post_font {
  font-size: 25px;
}
#comment_alert {
  text-align: center;
  padding: 20px;
  width: 940px;
  margin-left: 180px;
}
#comment_title {
  font-size: 40px;
  font-family: 华文中宋;
  padding: 20px;
}
#text_icon {
  font-size: 60px;
  padding-top: 2px;
}
.one_comment_card {
  /* text-align: center; */
  margin-left: 200px;
  width: 900px;
}
.one_content_div {
  font-family: 华文中宋;
  font-size: 20px;
  color: #666666;
}
#post_column {
  width: 900px;
  font-family: 华文中宋;
  font-size: 25px;
  margin-left: 200px;
  margin-bottom: 30px;
}
#post_button_area {
  text-align: center;
  margin-bottom: 30px;
}
#post_button {
  width: 15%;
  height: 40px;
  margin-left: -100px;
  font-size: 20px;
  margin-top: 10px;
  outline: none;
  border-radius: 4px;
  border: solid 1px;
  background-color: #fff;
  cursor: pointer;
}
#post_button:hover {
  background: rgb(245, 242, 242);
  cursor: pointer;
}
#like_button {
  width: 8%;
  height: 30px;
  font-size: 20px;
  margin-top: 10px;
  background-color: #fff;
  border-radius: 4px;
  border: solid 1px;
  cursor: pointer;
  margin-left: 720px;
}
#like_button:hover {
  background: rgb(245, 242, 242);
  cursor: pointer;
}
</style>
