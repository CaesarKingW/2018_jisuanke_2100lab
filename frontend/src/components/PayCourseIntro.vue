<template>
  <div class="PayCourseIntro">
    <!-- 导航栏 -->
    <div class="navibar">
    <router-link to="/home"><a class="navi"><Icon type="ios-home" /> 网站首页</a></router-link>
    <Divider type="vertical" />
    <router-link to="/AllFreeCourse">
    <a class="navi"><Icon type="md-bookmarks" /> 免费课程</a>
    </router-link>
    <Divider type="vertical" />
    <router-link to="/AllPayCourse">
    <a class="navi"><Icon type="logo-usd" /> 付费课程</a>
    </router-link>
    <Divider type="vertical" />
    <router-link to="/PersonalCenter"><a class="navi"><Icon type="ios-contact" /> 个人中心</a></router-link>
    </div>
    <!-- 课程信息 -->
  <div class="myPanel"></div>
  <div id="blank"></div>
        <div class="coverDiv">
          <img id="testPic" v-bind:src="path">
        </div>
        <div class="courseTitleDiv"><div id="courseTitle">标题：{{ courseTitle }}</div></div>
        <div class="buyButtonDiv">
            <div v-if="judge">
              <div v-if="IsPaid"><Button  id="buy" type="primary" v-on:click="IsBurn">进入课程</Button>
              </div>
              <div v-else>
                <Poptip placement="right" v-model="visible">
                <a><Button  id="buy" type="primary">
                <Icon type="logo-usd" />{{ price }} 购买课程</Button></a>
                <div slot="title">
                  <i>
                  <Button id="aliPayButton" v-on:click="alipay()"><Icon type="logo-usd" />支付宝支付</Button>
                  <Button id="wxPayButton" v-on:click="wxpay()"><Icon type="logo-usd" />微信支付</Button>
                  <Button id="awardButton" v-on:click="awardpay()"><Icon type="logo-usd" />奖励金支付</Button>
                  </i>
                </div>
                <div slot="content">
                <a @click="close">放弃购买</a>
                </div>
                </Poptip>
               </div>
             </div>
            <div v-else>
              <Button id="buy" v-on:click="modall = true" type="primary">
              <Icon type="logo-usd" /><span>{{ price }}</span>购买课程
              </Button>
              <Modal v-model="modall" title="温馨提示" @on-ok="ok"
              @on-cancel="cancel">
              <p>您必须先登录才能学习课程</p>
              </Modal>
            </div>
          </div>
        <div class="shareButtonDiv">
          <Button @click="modal = true" id="share" type="primary">
            <Icon type="ios-card" /> 分享课程</Button>
            </div>
            <div v-if="isBurn" class="burnDiv">
        <Alert type="warning" show-icon>
        <Icon type="ios-alert" slot="icon"></Icon>
        <template class="burnText" slot="desc">本文为阅后即焚类文章，在初次阅读后{{ burnTime }}小时无法再查看，请注意及时阅读哦！</template>
      </Alert>
    </div>
    <div class="alertButtonDiv">
      <Alert class="alertButton" show-icon>
        <Icon type="ios-trophy-outline" slot="icon"></Icon>
        <template class="alertText" slot="desc">分享本课程给他人，他人购买后，你还可以额外获得 {{ award }} 枚奖励币哦！</template>
          </Alert>
        </div>
        <div class="introDiv">
          <Card>
            <p class="intro" slot="title">课程简介</p>
            <p class="introContent">{{content}}</p>
        </Card>
        </div>
   <Modal
        title="分销课程"
        v-model="modal"
        class-name="vertical-center-modal">
        <div id="urlDiv"><span id="thisURL">请将此链接分享给他人：{{ message }}</span>
        </div>
        </Modal>
    <br />
  </div>
</template>
<script>
export default {
  name: 'PayCourseInfo',
  data() {
    return {
      path: '',
      courseTitle: '',
      content: '',
      split1: 0.49,
      modal: false,
      modall: false,
      message: window.location.href,
      // 分享课程可得奖励金
      award: 0,
      orderid: '',
      price: 55,
      courseid: 1,
      userphone: '',
      value: '1',
      visible: false,
      // 判断用户是否登录
      judge: false,
      // 判断用户是否支付成功
      IsPaid: false,
      burnTime: null,
      isBurn: false,
      // 用户奖励金余额
      AwardOfUser: 0
    }
  },
  created: function() {
    // 从路由获取课程id
    this.courseid = this.$route.query.id
    // 判断是否登录
    this.Judgestatus()
  },
  mounted: function() {
    this.get_specified_course()
    this.$Message.config({
      top: 120
    })
  },
  methods: {
    close() {
      this.visible = false
    },
    Judgestatus: function() {
      this.$http
        .post('http://192.168.55.33:8000' + '/app/get_status')
        .then(response => {
          this.judge = response.data.is_login
          if (this.judge !== true) {
            this.$Message.warning('请您先登录')
          } else {
            // 获取用户手机号并判断是否已经支付完成
            this.GetUserPhone()
          }
        })
    },
    get_specified_course: function() {
      this.$http
        .post(
          'http://192.168.55.33:8000' + '/app/get_specified_course',
          JSON.stringify(this.courseid)
        )
        .then(response => {
          var exist = response.data.exist
          if (exist) {
            var course = []
            course = response.data.list
            this.courseTitle = course[0].fields.title
            this.path =
              'http://192.168.55.33:8000' +
              '/media/' +
              course[0].fields.Cover_picture
            this.content = course[0].fields.brief_introduction
            this.price = course[0].fields.price
            this.award = Math.floor(course[0].fields.share_rate * this.price)
            this.isBurn = course[0].fields.Is_destroy
            this.burnTime = course[0].fields.distory_time
          } else {
            this.$router.push({ name: 'home' })
          }
        })
    },
    GetUserPhone: function() {
      this.$http
        .post('http://192.168.55.33:8000' + '/app/get_status')
        .then(response => {
          // 获取手机号
          this.userphone = response.data.list[0].pk
          // 获取用户账户奖励金
          this.AwardOfUser = response.data.list[0].fields.welfare
          // 判断支付状态
          this.JudgePayment()
          // 生成专属邀请链接
          this.ShareEncode()
          // 判断是否为分享链接
          this.IsShare()
        })
    },
    alipay() {
      var code = ''
      var codeLength = 16
      var random = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      for (var i = 0; i < codeLength; i++) {
        var index = Math.floor(Math.random() * 9)
        code += random[index]
      }
      this.orderid = code
      var request = {}
      request.orderid = this.orderid
      request.courseid = this.courseid
      request.userphone = this.userphone
      request = JSON.stringify(request)
      this.$http
        .post('http://192.168.55.33:8000' + '/app/payment', request)
        .then(response => {
          window.location.href = response.data
        })
    },
    wxpay: function() {
      this.$Message.warning('抱歉，暂不支持微信支付')
    },
    awardpay: function() {
      if (this.AwardOfUser > this.price) {
        var r = confirm('确认使用奖励金支付？')
        if (r) {
          var left = this.AwardOfUser - this.price
          this.$http
            .post(
              this.GLOBAL.serverSrc + '/app/awardpay',
              JSON.stringify({
                userphone: this.userphone,
                courseid: this.courseid,
                userAward: left,
                price: this.price
              })
            )
            .then(response => {
              this.AwardOfUser = left
              this.$Message.success(
                '支付' +
                  this.price +
                  '元，您的奖励金余额为:' +
                  this.AwardOfUser +
                  '元'
              )
              this.$router.push({
                name: 'CourseShow',
                query: { id: this.courseid }
              })
            })
        } else {
          // 取消支付
        }
      } else {
        this.$Message.warning(
          '抱歉，您的奖励金不足以支付，请您选择其它支付方式'
        )
      }
    },
    ok: function() {
      this.$router.push({ name: 'UserLogin' })
    },
    cancel: function() {},
    JudgePayment: function() {
      this.$http
        .post(
          'http://192.168.55.33:8000' + '/app/get_order_payment',
          JSON.stringify({
            phone_number: this.userphone,
            course_id: this.courseid
          })
        )
        .then(response => {
          this.IsPaid = response.data.order_status
        })
    },
    IsBurn: function() {
      this.$http
        .post(
          'http://192.168.55.33:8000' + '/app/get_burn_status',
          JSON.stringify({
            userphone: this.userphone,
            courseid: this.courseid
          })
        )
        .then(response => {
          var isBurn = response.data.status
          if (isBurn) {
            this.$router.push({ name: 'ReadAndBurn' })
          } else {
            this.$router.push({
              name: 'CourseShow',
              query: { id: this.courseid }
            })
          }
        })
    },
    // 对用户手机号进行简单编码
    ShareEncode: function() {
      var refer = ['*', '^', '@', '(', '!', ')', '%', '#', '&', '$']
      var code = ''
      var temp = this.userphone
      for (var i = 0; i < 11; i++) {
        var index = temp % 10
        temp = (temp - index) / 10
        code += refer[index]
      }
      var shareCode = escape(code)
      this.message =
        this.GLOBAL.serverSrc +
        '/#/PayCourseIntro?id=' +
        this.courseid +
        '&code=' +
        shareCode
    },
    IsShare: function() {
      var code = this.$route.query.code
      // 判断是否为分享链接
      if (typeof code !== 'undefined') {
        // 对code进行译码
        var decode = unescape(code)
        var str = decode.split('')
        var presenter = 0
        var refer = ['*', '^', '@', '(', '!', ')', '%', '#', '&', '$']
        for (var i = 0; i < str.length; i++) {
          var temp = refer.indexOf(str[i])
          presenter += temp * Math.pow(10, i)
        }
        if (presenter !== this.userphone) {
          // 将分享记录插入表中
          // 如果presenter不存在，插入失败，弹出邀请链接错误
          this.$http
            .post(
              this.GLOBAL.serverSrc + '/app/add_share',
              JSON.stringify({
                presenter: presenter,
                courseid: this.courseid,
                receiver: this.userphone
              })
            )
            .then(response => {
              var status = response.data.status
              if (!status) {
                this.$Message.error('邀请链接错误，请重新进入')
              }
            })
        } else {
          this.$Message.warning('抱歉，您不可以自己分享给自己的！')
        }
      }
    }
  }
}
</script>
<style scoped>
#urlDiv {
  text-align: center;
  padding: 10px;
}

#buttons {
  margin: 0 auto;
  text-align: center;
}

.navibar {
  z-index: 9999;
  background-color: #fff;
  position: fixed;
  width: 100%;
  opacity: 0.9;
  padding: 25px;
}

.navi {
  font-size: 18px;
  color: #022336;
  margin-left: 15px;
  margin-right: 15px;
}

.myPanel {
  margin: 0 auto;
  height: 90px;
  border: none;
  border-radius: 0px;
}

.vertical-center-modal {
  display: flex;
  align-items: center;
  justify-content: center;
}

.ivu-modal {
  top: 0;
}

.alertText,
.burnText {
  text-align: center;
  color: #fff;
}

.coverDiv {
  margin: 0 auto;
  text-align: center;
}

.ivu-modal {
  top: 0;
}

#share,
#buy {
  background-color: #fff;
  color: #000;
  font-size: 20px;
  border: #000 solid 1px;
  border-radius: 8px;
  width: 130px;
  height: 45px;
  margin: 0 auto;
  text-align: center;
  position: static;
}

.buyButtonDiv,
.shareButtonDiv {
  margin: 0 auto;
  text-align: center;
  margin-top: 15px;
  margin-bottom: 25px;
  position: static;
}

#copyButton {
  width: 50px;
  height: 25px;
  outline: none;
  border-radius: 4px;
  border: none;
  background-color: #2d8cf0;
  color: #fff;
  cursor: pointer;
}

#copyButton:hover {
  background: #57a3f3;
}

#testPic {
  width: 360px;
  height: 250px;
  border: #cccccc solid 2px;
  border-radius: 8px;
  margin: 0 auto;
  text-align: center;
}

.alertButtonDiv,
.burnDiv {
  margin: 0 auto;
  text-align: center;
  width: 60%;
  height: 5%;
  margin-top: 10px;
}

.introDiv {
  width: 60%;
  margin: 0 auto;
  text-align: left;
  margin-top: 20px;
}

.intro {
  font-size: 19px;
  font-family: 华文中宋;
}

.introContent {
  font-size: 17px;
  font-size: 17px;
  position: static;
  font-family: 华文中宋;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

#courseTitle {
  color: #000;
  font-family: 华文中宋;
  font-size: 28px;
  border: none;
  margin-top: 20px;
  margin: 0 auto;
  text-align: center;
  position: static;
}

.courseTitleDiv {
  margin: 0 auto;
}

@media screen and (max-width: 500px) {
  .navi {
    display: block;
    color: #000;
  }
  #blank {
    margin-top: 125px;
  }
  .navibar {
    z-index: 9999;
    position: fixed;
    color: #000;
    width: 100%;
    opacity: 0.9;
    padding: 25px;
  }
}
</style>
