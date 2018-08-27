<template>
<div class="FreeCourseIntro">
    <div class="flexDiv">
        <div class="introPic"><img id="test_pic" v-bind:src="path"></div>
        <div class="courseInfoText">
        <div class="courseTitle">标题：{{ courseTitle }}</div>
        <div class="enterCourse"><router-link to="/CourseShow"><Button id="enter" icon="md-eye" type="primary">进入课程</Button></router-link></div>
        <div class="shareCourse">
            <Button @click="modal = true" id="share" icon="md-share" type="primary">分享课程</Button>
        </div>
        </div>
        <Modal
        title="分享课程"
        v-model="modal"
        class-name="vertical-center-modal">
        <div style="text-align: center;padding:10px;"><span id="thisURL">本页地址：{{ message }}</span>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <button id="copy_button" type="button"
        v-clipboard:copy="message"
        v-clipboard:success="onCopy"
        v-clipboard:error="onError">复制</button>
        </div>
    </Modal>
    <div class="alertColumn">
        <Alert id="tip" show-icon>
        <Icon type="ios-bulb-outline" slot="icon"></Icon>
        <template slot="desc">如果你喜欢本课程，就把它分享给朋友吧！ </template>
    </Alert>
    </div>
    </div>
    <div class="introText">
        <Collapse v-model="value">
        <Panel id="introText" name="1" style="font-size: 25px;">
            课程简介
            <p slot="content">
                <ul style="font-size: 18px; list-style:none;">
                    {{content}}
                </ul>
                </p>
        </Panel>
    </Collapse>
    </div>
    <br>
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
.FreeCourseIntro {
  height: 480px;
  border: 1px solid #dcdee2;
  /* background-color: #c4e1ff; */
}
.demo-split-pane {
  padding: 10px;
}
.flexDiv {
    display:flex;
}
.introPic {
    flex-grow: 3;
}
.courseIntroText {
    flex-grow: 1;
}
#test_pic {
  border: #99ccff solid 5px;
  position: absolute;
  left: 2%;
  top: 8%;
  border-radius: 20px;
}
#courseTitle {
  text-align: center;
  position: absolute;
  right: 8%;
  text-align: center;
  top: 20%;
  font-size: 3em;
  padding: 8px 50px;
  border: #99cccc dotted 3px;
}
#enter {
  width: 170px;
  height: 60px;
  text-align: center;
  position: absolute;
  right: 20%;
  top: 40%;
  font-size: 2em;
}
#share {
  width: 170px;
  height: 60px;
  text-align: center;
  position: absolute;
  right: 20%;
  top: 58%;
  font-size: 2em;
}
#tip {
  width: auto;
  height: 40px;
  text-align: center;
  position: absolute;
  right: 14%;
  top: 75%;
}
.vertical-center-modal {
  display: flex;
  align-items: center;
  justify-content: center;
}
.ivu-modal {
  top: 0;
}
#intro {
  position: absolute;
  top: 84%;
  width: 100%;
  list-style: none;
}
#copy_button {
  width: 50px;
  height: 25px;
  margin-top: 10px;
  outline: none;
  border-radius: 4px;
  border: none;
  background-color: #2d8cf0;
  color: #fff;
  cursor: pointer;
}
#copy_button:hover {
  background: #57a3f3;
}
</style>
