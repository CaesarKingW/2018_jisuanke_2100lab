<template>
  <div class="FreeCourseIntro">
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
    <div class="myPanel"></div>
    <div id="blank"></div>
    <div class="CoverDiv">
            <img id="testPic" v-bind:src="path">
            </div>
        <div id="courseTitleDiv">
        <div id="courseTitle">标题：{{ courseTitle }}</div></div>
        <div class="enterButtonDiv">
        <div v-if="judge"><Button id="enter" icon="md-eye" type="primary" v-on:click="IsBurn">进入课程</Button></div>
        <div v-else><Button id="enter" icon="md-eye" type="primary" v-on:click="modall = true">进入课程</Button></div>
            <Modal v-model="modall" title="温馨提示" @on-ok="ok"
        @on-cancel="cancel">
              <p>您必须先登录才能学习课程</p>
            </Modal>
            </div>
        <div class="shareButtonDiv">
            <Button @click="modal = true" id="share" icon="md-share" type="primary">分享课程</Button>
        </div>
        <Modal
        title="分享课程"
        v-model="modal"
        class-name="vertical-center-modal">
        <div class="urlDiv"><span id="thisURL">请将此链接分享给他人：{{ message }}</span>
        </div>
    </Modal>
    <div v-if="isBurn" class="burnDiv">
      <Alert type="error" show-icon>
        <Icon type="ios-bulb-outline" slot="icon"></Icon>
        <template class="burnText" slot="desc">本文为阅后即焚类文章，在初次阅读后{{ burnTime }}小时无法再查看，请注意及时阅读哦！</template>
      </Alert>
    </div>
    <div class="alertButtonDiv">
      <Alert show-icon>
        <Icon type="ios-alert" slot="icon"></Icon>
        <template class="alertText" slot="desc">如果你喜欢本课程，就把它分享给朋友吧！ </template>
      </Alert>
    </div>
    <div class="introDiv">
      <Card class="intro">
        <p id="title" slot="title">课程简介</p>
        <p class="introContent">{{content}}</p>
      </Card>
    </div>
  </div>
</template>
<script>
export default {
  name: 'FreeCourseIntro',
  data() {
    return {
      path: '',
      courseTitle: '',
      content: '',
      split1: 0.49,
      modal: false,
      message: window.location.href,
      courseid: 0,
      userphone: '',
      judge: false,
      modall: false,
      burnTime: null,
      isBurn: false
    }
  },
  created: function() {
    this.courseid = this.$route.query.id
  },
  mounted: function() {
    this.Judgestatus()
    this.GetUserPhone()
    this.GetSpecifiedCourse()
    this.$Message.config({
      top: 120
    })
  },
  methods: {
    Judgestatus: function() {
      this.$http
        .post('http://192.168.55.33:8000' + '/app/get_status')
        .then(response => {
          this.judge = response.data.is_login
          if (!this.judge) {
            this.$Message.warning('请您先登录')
          }
        })
    },
    GetSpecifiedCourse: function() {
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
              'http://192.168.55.33:8000' + '/media/' + course[0].fields.Cover_picture
            this.content = course[0].fields.brief_introduction
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
          this.userphone = response.data.list[0].pk
        })
    },
    ok: function() {
      this.$router.push({ name: 'UserLogin' })
    },
    cancel: function() {},
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
    }
  }
}
</script>
<style>
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

.navi:hover {
  color: #022336;
}

.intro {
  font-size: 19px;
  font-family: 华文中宋;
}

.introContent {
  font-size: 17px;
  position: static;
  font-family: 华文中宋;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.myPanel {
  margin: 0 auto;
  height: 90px;
  border: none;
  border-radius: 0px;
}

.alertText,
.burnText {
  text-align: center;
  color: #fff;
}

.CoverDiv {
  margin: 0 auto;
  text-align: center;
}

.ivu-modal {
  top: 0;
}

.urlDiv {
  text-align: center;
  padding: 10px;
}

#share,
#enter {
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

.vertical-center-modal {
  display: flex;
  align-items: center;
  justify-content: center;
}

.ivu-modal {
  top: 0;
}

.enterButtonDiv,
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
  color: #fff;
  cursor: pointer;
}

#title {
  font-size: 19px;
}

#testPic {
  width: 360px;
  height: 250px;
  border: #cccccc solid 2px;
  border-radius: 8px;
  margin: 0 auto;
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

#courseTitleDiv {
  margin: 0 auto;
}
@media screen and (max-width: 500px) {
  .navi {
    display: block;
  }
  #blank {
    margin-top: 125px;
  }
  .navibar {
    z-index: 9999;
    position: fixed;
    width: 100%;
    opacity: 0;
    padding: 25px;
  }
}
</style>
