<template>
  <div>
    <div>所购课程标题：
      <span>{{course_title}}</span>
    </div>
    <div>所购课程ID:
      <span>{{course_id}}</span>
    </div>
    <div>支付金额：
      <span>{{amount_of_money}}元</span>
    </div>
    <div>支付状态：
      <span>{{status}}</span>
    </div>
    <div>创建时间：
      <span>{{created_at}}</span>
    </div>
    <div>用户手机号：
      <span>{{phone_number}}</span>
    </div>
    <button v-show='if_refund' @click="refund()">退款</button>
  </div>
</template>
<script>
export default {
  name: 'order',
  data() {
    return {
      order_number: '',
      if_refund: null,
      course_title: '',
      course_id: 0,
      amount_of_money: 0,
      status: '',
      created_at: null,
      phone_number: ''
    }
  },
  created: function() {
    this.$http
      .post('http://192.168.55.33:8000/app/get_mstatus')
      .then(response => {
        var res = response.data
        this.mis_login = res.mis_login
        if (!this.mis_login) {
          alert('还没有登录，无权访问该页面！')
          location.href = '/#/backstageLogin'
        } else {
          if (res.manager.Manage_order !== true) {
            alert('你没有权限访问该网页！')
            location.href = '/#/backstage'
          } else {
            this.order_number = this.$route.params.order_number
            console.log(this.order_number)
            this.$http
              .post(
                'http://192.168.55.33:8000/app/search_order',
                JSON.stringify(this.order_number)
              )
              .then(response => {
                var res = response.data
                this.course_title = res.order_info.course_title
                this.course_id = res.order_info.course_id
                this.amount_of_money = res.order_info.amount_of_money
                this.status = res.order_info.status
                this.created_at = res.order_info.create_at
                this.phone_number = res.order_info.phone_number
                if (this.status === '已支付') {
                  this.if_refund = true
                } else {
                  this.if_refund = false
                }
              })
          }
        }
      })
  },
  methods: {
    refund() {
      var orderNumber = JSON.stringify(this.order_number)
      this.$http
        .post('http://192.168.55.33:8000/app/refund', orderNumber)
        .then(response => {
          alert('退款成功！')
          this.status = '已退款'
          this.if_refund = false
        })
    }
  }
}
</script>
<style>
#order {
  width: 300px;
}
</style>
