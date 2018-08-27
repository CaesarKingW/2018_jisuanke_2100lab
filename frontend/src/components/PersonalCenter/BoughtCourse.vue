<template>
<div id="BoughtCourse">
    <div>
        <table >
            <tr>
                <th>序号</th>
                <th>订单编号</th>
                <th>课程编号</th>
                <th>课程标题</th>
                <th>支付金额</th>
                <th>订单状态</th>
                <th>发起订单时间</th>
            </tr>
            <tr v-for="(item, index) of orders" :key="item">
                <td>
                    {{index + 1}}
                </td>
                <td>
                    {{item.Order_number}}
                </td>
                <td>
                    {{item.course_id}}
                </td>
                <td>
                    {{item.course_title}}
                </td>
                <td>
                    {{item.amount_of_money}}
                </td>
                <td>
                    {{item.status}}
                </td>
                <td>
                    {{item.create_at}}
                </td>
            </tr>
        </table>
    </div>
</div>
</template>
<script>
export default {
  data() {
    return {
      orders: [],
      userPhone: ''
    }
  },
  mounted: function() {
    this.$http.post(this.GLOBAL.serverSrc + '/app/get_status').then(response => {
      this.userPhone = response.data.list[0].pk
      this.show_orders()
    })
  },
  methods: {
    show_orders: function() {
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/show_orders',
          JSON.stringify(this.userPhone)
        )
        .then(
          response => {
            this.orders = response.data.list
            console.log('success')
          },
          response => {
            console.log('error')
          }
        )
    }
  }
}
</script>
