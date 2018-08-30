<template>
  <div id="PayConfirm">
    <div id="picDiv"><img id="payPic" src="../assets/money.jpg"></div>
    <div id="paySuccess">恭喜您支付成功，请点击确认！</div>
    <input type="button" id="btn" value="确认" v-on:click="Confirm" />
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
<style scoped>
#PayConfirm {
  text-align: center;
}
#picDiv {
  margin: 0 auto;
  /* margin-left: 420px; */
}
#payPic {
  width: 31%;
  height: auto;
  /* margin: 0 auto; */
}
#paySuccess {
  color: #2c3e50;
  font-size: 30px;
}
#btn {
  background-color: #fff;
  color: #000;
  font-size: 20px;
  border: #000 solid 1px;
  border-radius: 8px;
  width: 120px;
  height: 45px;
  margin: 0 auto;
  text-align: center;
  position: static;
  margin-top: 15px;
}
#btn:hover {
  background-color: #f1f1f1;
}
</style>
