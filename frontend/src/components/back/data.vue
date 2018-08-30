<template>
  <section class="fl">
    <Dropdown>
      <a href="javascript:void(0)">
        <p class='choose'>{{droptext_user}}</p>
        <Icon type="ios-arrow-down"></Icon>
      </a>
      <DropdownMenu slot="list">
        <DropdownItem disabled>
          <p @click='time_to_now("week")'>本周</p>
        </DropdownItem>
        <DropdownItem disabled>
          <p @click='time_to_now("month")'>本月</p>
        </DropdownItem>
        <DropdownItem disabled>
          <p @click='time_to_now("season")'>季度</p>
        </DropdownItem>
        <DropdownItem disabled>
          <p @click='time_to_now("semi_year")'>半年</p>
        </DropdownItem>
        <DropdownItem disabled>
          <p @click='time_to_now("year")'>全年</p>
        </DropdownItem>
        <DropdownItem>
          <p @click='time_to_now("all")'>全部</p>
        </DropdownItem>
      </DropdownMenu>
    </Dropdown>
    <p class='choose'>注册的用户总数为{{user_amount}}.</p>
    <br>
    <Dropdown>
      <a href="javascript:void(0)">
        <p class='choose'>{{droptext_order}}</p>
        <Icon type="ios-arrow-down"></Icon>
      </a>
      <DropdownMenu slot="list">
        <DropdownItem>
          <p @click='order_to_now("week")'>本周</p>
        </DropdownItem>
        <DropdownItem>
          <p @click='order_to_now("month")'>本月</p>
        </DropdownItem>
        <DropdownItem>
          <p @click='order_to_now("season")'>季度</p>
        </DropdownItem>
        <DropdownItem>
          <p @click='order_to_now("semi_year")'>半年</p>
        </DropdownItem>
        <DropdownItem>
          <p @click='order_to_now("year")'>全年</p>
        </DropdownItem>
        <DropdownItem>
          <p @click='order_to_now("all")'>全部</p>
        </DropdownItem>
      </DropdownMenu>
    </Dropdown>
    <p class='choose'>的订单总数为{{order_amount}}.</p>
    <br>
    <Dropdown>
      <a href="javascript:void(0)">
        <p class='choose'>{{droptext_money}}</p>
        <Icon type="ios-arrow-down"></Icon>
      </a>
      <DropdownMenu slot="list">
        <DropdownItem>
          <p @click='money_to_now("week")'>本周</p>
        </DropdownItem>
        <DropdownItem>
          <p @click='money_to_now("month")'>本月</p>
        </DropdownItem>
        <DropdownItem>
          <p @click='money_to_now("season")'>季度</p>
        </DropdownItem>
        <DropdownItem>
          <p @click='money_to_now("semi_year")'>半年</p>
        </DropdownItem>
        <DropdownItem>
          <p @click='money_to_now("year")'>全年</p>
        </DropdownItem>
        <DropdownItem>
          <p @click='money_to_now("all")'>全部</p>
        </DropdownItem>
      </DropdownMenu>
    </Dropdown>
    <p class='choose'>的订单总金额为{{money_amount}}.</p>
    <div id="free_watch" class="chart"></div>
    <div id="pay_watch" class="chart"></div>
    <div id="pay_sale" class="chart"></div>
  </section>
</template>

<script>
import echarts from 'echarts'

export default {
  name: 'data',
  data() {
    return {
      free_watch1: [],
      free_watch2: [],
      pay_watch1: [],
      pay_watch2: [],
      pay_sale1: [],
      pay_sale2: [],
      droptext_user: '选择时间范围',
      user_amount: '',
      user_time: {
        week: Number,
        month: Number,
        season: Number,
        semi_year: Number,
        year: Number,
        all: Number
      },
      droptext_order: '选择时间范围',
      order_amount: '',
      order_time: {
        week: Number,
        month: Number,
        season: Number,
        semi_year: Number,
        year: Number,
        all: Number
      },
      droptext_money: '选择时间范围',
      money_amount: '',
      money_time: {
        week: Number,
        month: Number,
        season: Number,
        semi_year: Number,
        year: Number,
        all: Number
      }
    }
  },
  methods: {
    time_to_now(_time) {
      switch (_time) {
        case 'week':
          this.droptext_user = '本周'
          this.user_amount = 1
          break
        case 'month':
          this.droptext_user = '本月'
          this.user_amount = 10
          break
        case 'season':
          this.droptext_user = '季度'
          this.user_amount = 100
          break
        case 'semi_year':
          this.droptext_user = '半年'
          this.user_amount = 1000
          break
        case 'year':
          this.droptext_user = '全年'
          this.user_amount = 10000
          break
        case 'all':
          this.droptext_user = '全部'
          this.user_amount = this.user_time.all
          break
      }
    },
    order_to_now(_time) {
      switch (_time) {
        case 'week':
          this.droptext_order = '本周'
          this.order_amount = this.order_time.week
          break
        case 'month':
          this.droptext_order = '本月'
          this.order_amount = this.order_time.month
          break
        case 'season':
          this.droptext_order = '季度'
          this.order_amount = this.order_time.season
          break
        case 'semi_year':
          this.droptext_order = '半年'
          this.order_amount = this.order_time.semi_year
          break
        case 'year':
          this.droptext_order = '全年'
          this.order_amount = this.order_time.year
          break
        case 'all':
          this.droptext_order = '全部'
          this.order_amount = this.order_time.all
          break
      }
    },
    money_to_now(_time) {
      switch (_time) {
        case 'week':
          this.droptext_money = '本周'
          this.money_amount = this.money_time.week
          break
        case 'month':
          this.droptext_money = '本月'
          this.money_amount = this.money_time.month
          break
        case 'season':
          this.droptext_money = '季度'
          this.money_amount = this.money_time.season
          break
        case 'semi_year':
          this.droptext_money = '半年'
          this.money_amount = this.money_time.semi_year
          break
        case 'year':
          this.droptext_money = '全年'
          this.money_amount = this.money_time.year
          break
        case 'all':
          this.droptext_money = '全部'
          this.money_amount = this.money_time.all
          break
      }
    },
    get_user_amount() {
      this.$http
        .post('http://192.168.55.33:8000' + '/app/user_amount')
        .then(response => {
          this.user_time.all = response.data
        })
    },
    get_order_amount() {
      this.$http
        .post('http://192.168.55.33:8000' + '/app/order_amount')
        .then(response => {
          this.order_time.week = response.body['week'] + ''
          this.order_time.month = response.body['month'] + ''
          this.order_time.season = response.body['season'] + ''
          this.order_time.semi_year = response.body['semi_year'] + ''
          this.order_time.year = response.body['year'] + ''
          this.order_time.all = response.body['all'] + ''
        })
    },
    get_money_amount() {
      this.$http
        .post('http://192.168.55.33:8000' + '/app/money_amount')
        .then(response => {
          this.money_time.week = response.body['week']
          this.money_time.month = response.body['month']
          this.money_time.season = response.body['season']
          this.money_time.semi_year = response.body['semi_year']
          this.money_time.year = response.body['year']
          this.money_time.all = response.body['all']
        })
    },
    get_free_watch() {
      this.$http
        .post('http://192.168.55.33:8000' + '/app/free_watch')
        .then(response => {
          this.free_watch1 = response.data['title']
          this.free_watch2 = response.data['count']
          this.draw_free_watch('free_watch')
        })
    },
    draw_free_watch(id) {
      this.free_watch_chart = echarts.init(document.getElementById(id))
      this.free_watch_chart.setOption({
        title: {
          text: '免费课程观看数TOP10'
        },
        tooltip: {},
        legend: {
          data: ['销量']
        },
        xAxis: {
          data: this.free_watch1
        },
        yAxis: {},
        series: [
          {
            name: '销量',
            type: 'bar',
            data: this.free_watch2
          }
        ]
      })
    },
    get_pay_watch() {
      this.$http
        .post('http://192.168.55.33:8000' + '/app/pay_watch')
        .then(response => {
          this.pay_watch1 = response.data['title']
          this.pay_watch2 = response.data['count']
          this.draw_pay_watch('pay_watch')
        })
    },
    draw_pay_watch(id) {
      this.pay_watch_chart = echarts.init(document.getElementById(id))
      this.pay_watch_chart.setOption({
        title: {
          text: '付费课程观看数TOP10'
        },
        tooltip: {},
        legend: {
          data: ['销量']
        },
        xAxis: {
          data: this.pay_watch1
        },
        yAxis: {},
        series: [
          {
            name: '销量',
            type: 'bar',
            data: this.pay_watch2
          }
        ]
      })
    },
    get_pay_sale() {
      this.$http
        .post('http://192.168.55.33:8000' + '/app/pay_sale')
        .then(response => {
          this.pay_sale1 = response.data['title']
          this.pay_sale2 = response.data['count']
          this.draw_pay_sale('pay_sale')
        })
    },
    draw_pay_sale(id) {
      this.pay_sale_chart = echarts.init(document.getElementById(id))
      this.pay_sale_chart.setOption({
        title: {
          text: '付费课程观看数TOP10'
        },
        tooltip: {},
        legend: {
          data: ['销量']
        },
        xAxis: {
          data: this.pay_sale1
        },
        yAxis: {},
        series: [
          {
            name: '销量',
            type: 'bar',
            data: this.pay_sale2
          }
        ]
      })
    }
  },
  //  调用
  mounted() {
    this.$nextTick(function() {
      this.get_user_amount()
      this.get_order_amount()
      this.get_money_amount()
      this.get_free_watch()
      this.get_pay_watch()
      this.get_pay_sale()
    })
  }
}
</script>

<style scoped>
.choose {
  display: inline;
}

.fl {
  margin-left: 20%;
}

.chart {
  float: left;
  width: 600px;
  height: 400px;
  padding: 0;
  margin: 0;
  list-style: none;
}
</style>
