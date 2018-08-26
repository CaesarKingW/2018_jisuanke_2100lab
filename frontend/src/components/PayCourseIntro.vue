<template>
<div class="PayCourseIntro">
  <!-- 导航栏 -->
    <div class="navibar">
    <router-link to="/home"><a class="navi"><Icon type="ios-home" /> 网站首页</a></router-link>
    <Divider type="vertical" />
    <router-link to="/PersonalCenter"><a class="navi"><Icon type="ios-contact" /> 个人中心</a></router-link>
    </div>
    <!-- 课程信息 -->
  <div class="myPanel"></div>
        <div class="coverDiv">
          <img id="testPic" v-bind:src="path">
        </div>
        <div class="courseTitleDiv"><div id="courseTitle">标题：{{ courseTitle }}</div></div>
        <div class="buyButtonDiv">
          <Button @click="alipay()" id="buy" type="primary">
            <Icon type="logo-usd" /> 购买课程
            </Button></div>
        <div class="shareButtonDiv">
          <Button @click="modal = true" id="share" type="primary">
            <Icon type="ios-card" /> 分销课程</Button>
            </div>
        <div class="alertButtonDiv">
          <Alert class="alertButton" show-icon>
        <Icon type="ios-trophy-outline" slot="icon"></Icon>
        <template class="alertText1" slot="desc">分销本课程，还可额外获得 {{ award }} 枚奖励币哦！</template>
          </Alert>
        </div>
        <div class="introDiv">
          <Collapse v-model="value">
            <Panel class="intro">
            课程简介
            <p slot="content" class="contentText">
                  {{content}}
                </p>
            </Panel>
          </Collapse>
        </div>
   <Modal
        title="分销课程"
        v-model="modal"
        class-name="vertical-center-modal">
        <div style="text-align: center; padding:10px;"><span id="thisURL">本页地址：{{ message }}</span>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <button id="copyButton" type="button"
        v-clipboard:copy="message"
        v-clipboard:success="onCopy"
        v-clipboard:error="onError">复制</button>
        </div>
        </Modal>
    <br>
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
      message: window.location.href,
      award: 0,
      orderid: '',
      price: 100,
      courseid: 1,
      userphone: '',
      value: '1'
    }
  },
  created: function() {
    this.courseid = this.$route.query.id
    console.log(this.courseid)
  },
  mounted: function() {
    this.$http
      .post('http://192.168.55.33:8000/app/get_status')
      .then(response => {
        this.userphone = response.data.list[0].pk
        console.log(this.user_phone)
      })
    this.$http
      .post(
        'http://192.168.55.33:8000/app/get_specified_course',
        JSON.stringify(this.courseid)
      )
      .then(response => {
        var course = []
        course = response.data.list
        this.courseTitle = course[0].fields.title
        this.path =
          'http://192.168.55.33:8000/media/' + course[0].fields.Cover_picture
        this.content = course[0].fields.brief_introduction
        this.price = course[0].fields.price
        this.award = course[0].fields.share_rate * this.price
      })
  },
  methods: {
    alipay() {
      // location.href='https://openapi.alipaydev.com/gateway.do?app_id=2016091800536766&biz_content=%7B%22subject%22%3A%22%5Cu6d4b%5Cu8bd5%5Cu8ba2%5Cu5355%22%2C%22out_trade_no%22%3A%2220170233021223%22%2C%22total_amount%22%3A100%2C%22product_code%22%3A%22FAST_INSTANT_TRADE_PAY%22%7D&charset=utf-8&method=alipay.trade.page.pay&notify_url=http%3A%2F%2Fprojectsedus.com%2F&return_url=http%3A%2F%2F192.168.55.33%3A8000%2F%23%2FPayCourseIntro&sign_type=RSA2&timestamp=2018-08-23+14%3A42%3A49&version=1.0&sign=vBgAxnq%2BicQ7yn9rEi5fDU7HRelUyLYRjHdOBd8OvWJTkSvNkCR50TTJjf6LNJSPQCbe5eMQw0r7CC8gP6ow%2Bh0NfeBehkkZkK9VrYPRG4n2cWSk%2B4Gu4Rytjm1FwrW0I%2BYV5cVbm9Zqew5ltQRiFfkjp8RBSuNKsLDl3VwYKkYNgPxJkWsI2SKSfdvs76mZNSPxBJd3ZFKkcX6vShn3H0W27BanKGZV0L%2F2T2uTgPsbNnfoeUFmxwSLMYXcmqirK57lfnf9uhOMbCofqfSBkTjVhq%2FDSTmHajph8oSxRwGpkd55cyCwLgzGSiKmL8Unx1RcMR3Tth3u2ILC8YVIdw%3D%3D'
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
      console.log(request)
      request = JSON.stringify(request)
      this.$http
        .post('http://192.168.55.33:8000/app/payment', request)
        .then(response => {
          console.log(response.data)
          window.location.href = response.data
        })
    }
  }
}
</script>
<style scoped>
.navibar {
  z-index: 9999;
  background-color: #fff;
  position: fixed;
  width: 100%;
  opacity: 0.9;
  padding: 25px;
}
.navi {
  font-size: 23px;
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
.alertText {
  text-align: center;
  color: #fff;
}
.PayCourseIntro {
  text-align: center;
  margin: 0 auto;
}
.CoverDiv {
  margin: 0 auto;
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
  /* margin-top: 20px;
  margin-bottom: 20px; */
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
.alertButtonDiv {
  margin-top: 10px;
}
#testPic {
  width: 360px;
  height: 250px;
  border: #cccccc solid 2px;
  border-radius: 8px;
  margin: 0 auto;
}
.alertButton {
  margin: 0 auto;
  text-align: center;
  width: 60%;
  height: 5%;
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
.contentText {
  font-family: 华文中宋;
  font-size: 17px;
  position: static;
}
#courseTitle {
  color: #fff;
  font-family: 华文中宋;
  font-size: 28px;
  border: none;
  margin-top: 20px;
  margin: 0 auto;
  text-align: center;
  position: static;
}
#courseTitleDiv {
  margin: 0 auto;
}
</style>
