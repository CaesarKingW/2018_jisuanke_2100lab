<template>
<body>
<div id="CourseShow">
    <Divider><h1 class="title">{{ title }}</h1></Divider>
    <Divider orientation="right"><p class="read_time" style="font-size: 24px;">浏览量：{{ times }} 次</p></Divider>
    <div class="test_pic"><img id="changePic" src="../assets/2.png"></div>
    <Divider />
    <Progress :percent="45" status="active" />
    <Divider />
    <Button type="primary" shape="circle" icon="ios-play"></Button>
    <Divider />
    <Collapse accordion v-model="value">
        <Panel style="background-color:#2d8cf0;">
            <Poptip trigger="hover" style="font-size: 24px;" title="文字介绍信息" content="点击可展开或折叠文字介绍。">
            <div style="color: white;">文字介绍</div>
            </Poptip>
            <div slot="content" style="text-align: left;font-size: 18px;">
               <div style="overflow: auto;height: 90px;">content</div>
            </div>
        </Panel>
    </Collapse>
        <BackTop>
        <div>返回顶端</div>
    </BackTop>
    <NiceMsgBoard/>
</div>
</body>
</template>
<script>
import NiceMsgBoard from './NiceMsgBoard'
export default {
  name: 'CourseShow',
  data() {
    return {
      courseid: 0,
      IsFree: true,
      userphone: '',
      IsPaid: false,
      title: '科学实验：实验室制取CO2',
      times: '9999'
    }
  },
  created: function() {
    // 从路由中获取课程id
    this.courseid = this.$route.query.id
    // 判断用户是否登录，未登录则直接跳转到登录页面
    this.Judgestatus()
    // 判断此门课程是否存在，不存在则直接调回home页面，
    // 是否为免费，并获取课程标题
    this.JudgePrice()
  },
  mounted: function() {
    var orderId = this.$route.query.out_trade_no
    if (typeof orderId !== 'undefined') {
      var request = JSON.stringify(orderId)
      this.$http
        .post(this.GLOBAL.serverSrc + 'app/notify', request)
        .then(response => {
          console.log(response.data)
        })
    }
  },
  components: {
    NiceMsgBoard
  },
  methods: {
    Judgestatus: function() {
      this.$http
        .post(this.GLOBAL.serverSrc + 'app/get_status')
        .then(response => {
          var judge = response.data.is_login
          // 用户未登录状态下强制访问，跳出404 not found页面
          // 这里暂时先直接跳入登录页面
          if (!judge) {
            this.$router.push({ name: 'UserLogin' })
          }
        })
    },
    // 获取课程标题和是否免费属性
    JudgePrice: function() {
      this.$http
        .post(
          this.GLOBAL.serverSrc + 'app/get_specified_course',
          JSON.stringify(this.courseid)
        )
        .then(response => {
          var exist = response.data.exist
          if (exist) {
            var course = []
            course = response.data.list
            this.title = course[0].fields.title
            var price = course[0].fields.price
            if (price === 0) {
              this.IsFree = true
            } else {
              this.IsFree = false
            }
            // 若是付费课程判断用户是否支付完成，未支付完成则直接跳转到主页
            if (!this.IsFree) {
              this.JudgePayment()
            }
          } else {
            // alert('您无权访问此网址')
            this.$router.push({ name: 'home' })
          }
        })
    },
    // 将用户手机号和课程id传给后端查找是否有关联两者的订单
    JudgePayment: function() {
      this.$http
        .post(
          this.GLOBAL.serverSrc + 'app/get_order_payment',
          JSON.stringify({
            phone_number: this.userphone,
            course_id: this.courseid
          })
        )
        .then(response => {
          this.IsPaid = response.data.order_status
          // 如果是付费课程且未支付则直接跳转到Home页面
          if (!this.IsPaid) {
            // alert('您必须先购买才能访问此页面')
            this.$router.push({ name: 'home' })
          }
        })
    }
  }
}
</script>
<style>
#CourseShow {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#title {
  color: #17233d;
}
#read_time {
  color: #808695;
  font-size: 14px;
}
.top {
  padding: 10px;
  background: #2d8cf0;
  color: #fff;
  text-align: center;
  border-radius: 2px;
}
#changePic {
  border: #000 solid 5px;
  border-radius: 20px;
}
</style>
