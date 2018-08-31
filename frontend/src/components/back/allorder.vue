<template>
    <div>
        <p><Input v-model="order_number" placeholder="输入订单号以搜索订单" id="search"/>
        <Button @click="search()">搜索</Button></p>
        <Table border stripe :columns="columns1" :data="data1"></Table>
        <Page :total="amount_of_orders" :page-size="10" :current="1" @on-change="changePage">
    </div>
</template>
<script>
export default {
  data() {
    return {
      order_number: '',
      columns1: [
        {
          title: '订单号',
          key: 'Order_number'
        },
        {
          title: '所购课程标题',
          key: 'course_title'
        },
        {
          title: '所购课程ID',
          key: 'course_id'
        },
        {
          title: '支付金额',
          key: 'amount_of_money'
        },
        {
          title: '支付状态',
          key: 'status'
        },
        {
          title: '创建时间',
          key: 'create_at'
        },
        {
          title: '用户手机号',
          key: 'phone_number'
        },
        {
          title: '操作',
          key: 'action',
          width: 150,
          align: 'center',
          render: (h, params) => {
            return h('div', [
              h(
                'Button',
                {
                  props: {
                    type: 'primary',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      this.go_to_edit(params.index)
                    }
                  }
                },
                '去管理'
              )
            ])
          }
        }
      ],
      data1: [],
      all_data: [],
      amount_of_orders: 0,
      currentPage: 1
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
            this.$http
              .post('http://192.168.55.33:8000/app/get_all_orders')
              .then(response => {
                var res = response.data
                this.all_data = res.orders
                this.amount_of_orders = this.all_data.length
                if (this.amount_of_orders <= 10) {
                  this.data1 = this.all_data
                } else {
                  for (var i = 0; i < 10; i++) {
                    this.data1.push(this.all_data[i])
                  }
                }
              })
          }
        }
      })
  },
  methods: {
    changePage(currentPage) {
      var left = this.amount_of_orders - (currentPage - 1) * 10
      var arr = []
      if (left <= 10) {
        for (var j = (currentPage - 1) * 10; j < this.amount_of_orders; j++) {
          arr.push(this.all_data[j])
        }
      } else {
        for (
          var k = (currentPage - 1) * 10;
          k < (currentPage - 1) * 10 + 10;
          k++
        ) {
          arr.push(this.all_data[k])
        }
      }
      this.data1 = arr
    },
    search() {
      var orderNumber = JSON.stringify(this.order_number)
      this.$http
        .post('http://192.168.55.33:8000/app/search_order', orderNumber)
        .then(response => {
          var res = response.data
          var arr = []
          if (res.if_order === true) {
            var order = res.order_info
            arr.push(order)
            this.amount_of_orders = 1
          } else {
            this.amount_of_orders = 0
          }
          this.all_data = arr
          this.data1 = arr
          console.log(this.data1)
        })
    },
    go_to_edit(index) {
      this.$router.push({
        name: 'order',
        params: { order_number: this.data1[index].Order_number }
      })
    }
  }
}
</script>
<style scoped>
#search {
  width: 300px;
}
</style>
