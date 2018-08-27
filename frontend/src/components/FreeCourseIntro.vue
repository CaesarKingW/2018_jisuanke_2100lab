<template>
<div class="FreeCourseIntro">
    <!-- 导航栏 -->
    <div class="navibar">
    <router-link to="/home"><a class="navi"><Icon type="ios-home" /> 网站首页</a></router-link>
    <Divider type="vertical" />
    <router-link to="/PersonalCenter"><a class="navi"><Icon type="ios-contact" /> 个人中心</a></router-link>
    </div>
    <!-- 底板 -->
    <div class="myPanel"></div>
    <!-- 课程信息 -->
    <div class="CoverDiv">
            <img id="testPic" v-bind:src="path">
            </div>
        <div id="courseTitleDiv">
        <div id="courseTitle">标题：{{ courseTitle }}</div></div>
        <div class="enterButtonDiv">
            <router-link to="/CourseShow">
            <Button id="enter" icon="md-eye" type="primary">进入课程</Button>
            </router-link>
            </div>
        <div class="shareButtonDiv">
            <Button @click="modal = true" id="share" icon="md-share" type="primary">分享课程</Button>
        </div>
        <Modal
        title="分享课程"
        v-model="modal"
        class-name="vertical-center-modal">
        <div class="urlDiv"><span id="thisURL">本页地址：{{ message }}</span>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <button id="copyButton" type="button"
        v-clipboard:copy="message"
        v-clipboard:success="onCopy"
        v-clipboard:error="onError">复制</button>
        </div>
    </Modal>
    <div class="alertButtonDiv">
        <Alert show-icon>
        <Icon type="ios-bulb-outline" slot="icon"></Icon>
        <template class="alertText" slot="desc">如果你喜欢本课程，就把它分享给朋友吧！ </template>
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
      courseid: 1,
      userphone: ''
    }
  },
  created: function() {
    this.courseid = this.$route.query.id
    console.log(this.courseid)
  },
  mounted: function() {
    this.$http
      .post(this.GLOBAL.serverSrc + 'app/get_status')
      .then(response => {
        this.userphone = response.data.list[0].pk
      })
    this.$http
      .post(
        this.GLOBAL.serverSrc + 'app/get_specified_course',
        JSON.stringify(this.courseid)
      )
      .then(response => {
        var course = []
        course = response.data.list
        this.courseTitle = course[0].fields.title
        this.path =
          this.GLOBAL.serverSrc + 'media/' + course[0].fields.Cover_picture
        this.content = course[0].fields.brief_introduction
      })
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
.FreeCourseIntro {
  text-align: center;
  margin: 0 auto;
}
.CoverDiv {
  margin: 0 auto;
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
  /* margin-top: 20px;
  margin-bottom: 20px; */
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
#courseTitleDiv {
  margin: 0 auto;
}
</style>
