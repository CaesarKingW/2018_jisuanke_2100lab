<template>
  <div>
    <Input v-model="order_number" placeholder="请输入待搜索的订单号" style="width: 300px" />
    <Button @click="search()">搜索</Button>
    <div v-show='is_show'>
      <div v-if='if_order'>
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
      <div v-else>
        对不起，您搜索的订单不存在
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'order',
  data() {
    return {
      order_number: '',
      is_show: false,
      if_order: null,
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
          }
        }
      })
  },
  methods: {
    search() {
      var orderNumber = JSON.stringify(this.order_number)
      this.$http
        .post('http://192.168.55.33:8000/app/search_order', orderNumber)
        .then(response => {
          var res = response.data
          this.if_order = res.if_order
          if (this.if_order === true) {
            this.course_title = res.order_info.course_title
            this.course_id = res.order_info.course_id
            this.amount_of_money = res.order_info.amount_of_money
            this.status = res.order_info.status
            if (this.status !== '已支付') {
              this.if_refund = false
            } else {
              this.if_refund = true
            }
            this.created_at = res.order_info.create_at
            this.phone_number = res.order_info.user_phone
          }
        })
      this.is_show = true
    },
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
</style>
