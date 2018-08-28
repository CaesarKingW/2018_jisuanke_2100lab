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
            <div v-if="judge">
              <router-link :to="{path:'CourseShow', query:{id: courseid}}" v-if="IsPaid"><Button  id="buy" type="primary">
                <Icon type="logo-usd" /> 进入课程</Button></router-link>
              <div v-else><Button  id="buy" type="primary" v-on:click="alipay()">
                <Icon type="logo-usd" /> 购买课程</Button></div>
            </div>
            <div v-else><Button  id="buy" type="primary" v-on:click="modall = true">
            <Icon type="logo-usd" /> 购买课程</Button></div>
            <Modal v-model="modall" title="温馨提示" @on-ok="ok"
            @on-cancel="cancel">
              <p>您必须先登录才能学习课程</p>
            </Modal>
            </div>
        <div class="shareButtonDiv">
          <Button @click="modal = true" id="share" type="primary">
            <Icon type="ios-card" /> 分销课程</Button>
            </div>
        <div class="alertButtonDiv">
          <Alert class="alertButton" show-icon>
        <Icon type="ios-trophy-outline" slot="icon"></Icon>
        <template class="alertText" slot="desc">分销本课程，还可额外获得 {{ award }} 枚奖励币哦！</template>
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
      modall: false,
      message: window.location.href,
      award: 0,
      orderid: '',
      price: 100,
      courseid: 1,
      userphone: '',
      value: '1',
      // 判断用户是否登录
      judge: false,
      // 判断用户是否支付成功
      IsPaid: false
    }
  },
  created: function() {
    // 从路由获取课程id
    this.courseid = this.$route.query.id
    // 判断是否登录
    this.Judgestatus()
    // 获取用户手机号并判断是否已经支付完成
    this.GetUserPhone()
  },
  mounted: function() {
    this.get_specified_course()
  },
  methods: {
    Judgestatus: function() {
      this.$http
        .post(this.GLOBAL.serverSrc + '/app/get_status')
        .then(response => {
          this.judge = response.data.is_login
          if (this.judge !== true) {
            this.$Message.warning('请您先登录')
          }
        })
    },
    get_specified_course: function() {
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/get_specified_course',
          JSON.stringify(this.courseid)
        )
        .then(response => {
          var exist = response.data.exist
          if (exist) {
            var course = []
            course = response.data.list
            this.courseTitle = course[0].fields.title
            this.path =
              this.GLOBAL.serverSrc + '/media/' + course[0].fields.Cover_picture
            this.content = course[0].fields.brief_introduction
            this.price = course[0].fields.price
            this.award = Math.floor(course[0].fields.share_rate * this.price)
          } else {
            this.$router.push({ name: 'home' })
          }
        })
    },
    GetUserPhone: function() {
      this.$http
        .post(this.GLOBAL.serverSrc + '/app/get_status')
        .then(response => {
          this.userphone = response.data.list[0].pk
          // 判断支付状态
          this.JudgePayment()
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
        .post(this.GLOBAL.serverSrc + '/app/payment', request)
        .then(response => {
          window.location.href = response.data
        })
    },
    ok: function() {
      this.$router.push({ name: 'UserLogin' })
    },
    cancel: function() {},
    JudgePayment: function() {
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/get_order_payment',
          JSON.stringify({
            phone_number: this.userphone,
            course_id: this.courseid
          })
        )
        .then(response => {
          this.IsPaid = response.data.order_status
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
.vertical-center-modal {
  display: flex;
  align-items: center;
  justify-content: center;
}
.ivu-modal {
  top: 0;
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
}
.alertButtonDiv {
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
.contentText {
  font-family: 华文中宋;
  font-size: 17px;
  position: static;
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
</style>
