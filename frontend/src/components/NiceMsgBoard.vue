<template>
  <div class="NiceMsgBoard">
    <div id="commentAlert">
      <Alert show-icon>
        <div id="commentTitle">留言区</div>
        <Icon id="textIcon" type="md-text" slot="icon"></Icon>
      </Alert>
    </div>
    <form method="POST" @submit.prevent="commit_message">
      <div id="postFont">
        <Input v-model="message" type="textarea" :rows="4" align=c enter id="postColumn" placeholder="请在此畅所欲言……" />
      </div>
      <div id="postButton_area"><input id="postButton" type="submit" value="发送留言" /></div>
    </form>
    <div v-for="(item, index) of messages" :key="item.id">
      <Divider />
      <Card class="oneCommentCard">
        <div class="one_comment_div">
          <div id="userName" v-if="IsTeacher">
            <Icon id="commentIcon" type="md-person" />
            <Icon type="logo-vimeo" id="V" />用户：{{item.user_name}}</div>
          <div id="userName" v-else>
            <Icon id="commentIcon" type="md-person" />用户：{{item.user_name}}</div>
          <div class="oneContentDiv">
            {{item.content}}
          </div>
          <button id="likeButton" v-on:click="praise(item.id, index)"><span id="loveIcon"><Icon type="md-heart" /></span> ：{{item.praise_count}}</button>
          <NiceReply v-bind:title="item.id" v-bind:user_phone="user_phone"></NiceReply>
        </div>
      </Card>
    </div>
  </div>
</template>
<script>
import NiceReply from './NiceReply.vue'
export default {
  props: ['course_id'],
  data() {
    return {
      message: null,
      messages: [],
      NiceReply: [],
      NiceReplies: [],
      user_phone: '',
      IsTeacher: false,
      CanComment: true
    }
  },
  components: {
    NiceReply
  },
  mounted: function() {
    this.$http
      .post('http://192.168.55.33:8000' + '/app/get_status')
      .then(response => {
        this.user_phone = response.data.list[0].pk
        this.CanComment = response.data.list[0].fields.Can_comment
        this.IsTeacher = response.data.list[0].fields.Is_teacher
      })
    this.show_message()
  },
  watch: {
    course_id: function(val, oldval) {
      this.show_message()
    }
  },
  methods: {
    show_message: function() {
      this.$http
        .post(
          'http://192.168.55.33:8000' + '/app/show_message',
          JSON.stringify(this.course_id)
        )
        .then(
          response => {
            this.messages = response.data.list
          },
          response => {}
        )
    },
    commit_message: function() {
      if (this.CanComment) {
        var formDate = JSON.stringify({
          content: this.message,
          user_phone: this.user_phone,
          course_id: this.course_id
        })
        this.$http
          .post(this.GLOBAL.serverSrc + '/app/add_message', formDate)
          .then(
            response => {
              this.show_message()
              this.message = null
            },
            response => {}
          )
      }
    },
    praise: function(messageid, index) {
      if (this.CanComment) {
        var formDate = JSON.stringify({
          message_id: messageid,
          user_phone: this.user_phone
        })
        this.$http.post(this.GLOBAL.serverSrc + '/app/praise', formDate).then(
          response => {
            this.show_message()
          },
          response => {}
        )
      }
    }
  }
}
</script>
<style scoped>
#loveIcon {
  color: red;
  margin-left: -2px;
}

#userName {
  font-size: 18px;
  font-family: 微软雅黑;
}

#commentIcon {
  font-size: 35px;
}

#postFont {
  font-size: 25px;
  margin: 0 auto;
}

#commentAlert {
  text-align: center;
  padding: 20px;
  width: 940px;
  margin-left: 180px;
}

#commentTitle {
  font-size: 40px;
  font-family: 华文中宋;
  padding: 20px;
}

#textIcon {
  font-size: 60px;
  padding-top: 2px;
}

.oneCommentCard {
  /* text-align: center; */
  margin-left: 200px;
  width: 900px;
}

.oneContentDiv {
  font-family: 华文中宋;
  font-size: 20px;
  color: #666666;
}

#postColumn {
  width: 900px;
  font-family: 华文中宋;
  font-size: 25px;
  margin-left: 200px;
  margin-bottom: 30px;
}

#postButton {
  width: 22%;
  height: 40px;
  font-size: 20px;
  margin-top: 10px;
  margin: 0 auto;
  margin-left: 520px;
  text-align: center;
  border-radius: 4px;
  border: solid 1px;
  background-color: #fff;
  cursor: pointer;
}

#postButton:hover {
  background: rgb(245, 242, 242);
  cursor: pointer;
}

#likeButton {
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

#likeButton:hover {
  background: rgb(245, 242, 242);
  cursor: pointer;
}
#V {
  color: lightgreen;
}
@media screen and (max-width: 500px) {
  #commentTitle {
    font-size: 30px;
    font-family: 华文中宋;
    padding: 10px;
  }
  #textIcon {
    font-size: 40px;
    padding-top: 2px;
  }
  #postButton {
    width: 18%;
    height: 30px;
    font-size: 15px;
    margin-top: 5px;
    margin-left: 160px;
    border-radius: 4px;
    border: solid 1px;
    background-color: #fff;
    cursor: pointer;
  }
  #postColumn {
    width: 340px;
    font-family: 华文中宋;
    font-size: 25px;
    margin-left: 25px;
    margin-bottom: 30px;
  }
  #commentAlert {
    width: 340px;
    margin-left: 25px;
  }
  .oneCommentCard {
    /* text-align: center; */
    margin-left: 25px;
    width: 340px;
  }
  #commentIcon {
    font-size: 20px;
  }
  .oneContentDiv {
    font-family: 华文中宋;
    font-size: 18px;
    color: #666666;
  }
  #likeButton {
    width: 20%;
    height: 30px;
    font-size: 15px;
    margin-top: 10px;
    background-color: #fff;
    border-radius: 4px;
    border: solid 1px;
    cursor: pointer;
    margin-left: 230px;
  }

  #likeButton:hover {
    background: rgb(245, 242, 242);
    cursor: pointer;
  }
}
</style>
