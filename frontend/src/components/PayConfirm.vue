<template>
  <div id="PayConfirm">
    <p>您已成功支付，请点击确认</p>
    <input type="button" value="确认" v-on:click="Confirm" />
  </div>
</template>
<script>
export default {
  data() {
    return {
      courseid: null
    }
  },
  mounted() {
    this.ChangeOrderStatus()
  },
  methods: {
    ChangeOrderStatus: function() {
      var orderId = this.$route.query.out_trade_no
      if (typeof orderId !== 'undefined') {
        // 修改订单状态并获取courseid
        var request = JSON.stringify(orderId)
        this.$http
          .post('http://192.168.55.33:8000' + '/app/notify', request)
          .then(response => {
            this.courseid = response.data.course_id
          })
      }
    },
    Confirm: function() {
      this.$router.push({
        name: 'PayCourseIntro',
        query: { id: this.courseid }
      })
    }
  }
}
</script>
