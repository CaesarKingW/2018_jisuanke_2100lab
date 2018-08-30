<template>
  <div id="messageboard">
    <h1>评论区</h1>
    <div v-for="(item, index) of messages" :key="item.id">
      <div>
        <h4>用户：{{item.user_phone}}</h4>
        <h4>
          {{item.content}}
        </h4>
        <button v-on:click="praise(item.pk, index)">👍 :{{item.praise_count}}</button>
        <!-- #v-bind将"  "内内容解释为表达式 -->
        <reply v-bind:title="item.pk" v-bind:user_phone="user_phone"></reply>
      </div>
    </div>
    <form method="POST" @submit.prevent="commit_message">
      <input type="input" name="留言" v-model="message" />
      <input type="submit" value="留言" />
    </form>
  </div>
</template>
<script>
import reply from './reply.vue'
export default {
  data() {
    return {
      message: null,
      messages: [],
      reply: [],
      replies: [],
      // 先假定当前课程为1，用户手机号为17602284691
      course_id: 1,
      user_phone: '17602284691'
    }
  },
  components: {
    reply
  },
  mounted: function() {
    this.show_message()
  },
  methods: {
    show_message: function() {
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/show_message',
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
          },
          response => {}
        )
    },
    praise: function(messageid, index) {
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
</script>
