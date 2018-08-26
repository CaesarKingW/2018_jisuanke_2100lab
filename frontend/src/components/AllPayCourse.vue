<template>
    <div id="AllPayCourse">
    <!-- 导航栏 -->
    <div class="navibar">
    <router-link to="/home"><a class="navi"><Icon type="ios-home" /> 网站首页</a></router-link>
    <Divider type="vertical" />
    <router-link to="/PersonalCenter"><a class="navi"><Icon type="ios-contact" /> 个人中心</a></router-link>
    </div>
    <!-- 底板卡片 -->
    <Card id="payCol"></Card>
    <!-- 标题 -->
    <Card id="payCol">
    <div class="allCol">
    <div class="myContent">
        <h4><Icon type="md-bookmarks" />&nbsp;所有付费内容</h4>
    </div>
    </div>
    </Card>
    <!-- 所有课程 -->
    <div v-for="item of imgs" :key="item.id">
      <router-link :to="{path:'PayCourseIntro', query:{id: item.pk}}">
      <Card class="courseCard">
        <div class="CourseInfo">
            <div class="CourseCoverDiv"><img class="courseCover" v-bind:src= 'item.fields.Cover_picture'/></div>
            <div class="CourseText">
            <div class="CourseTitle">
                <Icon type="ios-bookmarks" /> 课程标题：<span class="courseTitleContent">{{item.fields.title}}</span></div>
            <div class="CourseIntro">
                <Icon type="ios-text" /> 课程简介：<div class="courseIntroContent">
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                {{item.fields.brief_introduction}}
                    </div></div>
            <div class="CoursePrice">
                <Icon type="logo-usd" />课程价格：<span class="coursePriceContent">{{item.fields.price}} 元</span>
                </div>
            </div>
            </div>
      </Card>
      </router-link>
        </div>
    </div>
</template>
<script>
export default {
  data() {
    return {
      imgs: [],
      path: []
    }
  },
  mounted: function() {
    this.show_all_course()
  },
  methods: {
    show_all_course: function() {
      this.$http.get('http://192.168.55.33:8000/app/show_paying_course').then(
        response => {
          this.imgs = response.data.list
          console.log('success')
          for (var i = 0; i < this.imgs.length; i = i + 1) {
            var a =
              'http://192.168.55.33:8000/media/' +
              this.imgs[i].fields.Cover_picture
            this.imgs[i].fields.Cover_picture = a
          }
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
<style scoped>
.courseCard {
  width: 650px;
  /* margin-left: 150px; */
  margin: 0 auto;
  /* text-align: center; */
}
.courseTitleContent {
  font-family: 华文细黑;
}
.CourseInfo {
  display: flex;
  color: #022336;
}
/* .CourseCoverDiv {
  float: left;
}*/
.CourseText {
  float: left;
  margin-left: 5%;
  color: #022336;
}
.CoursePrice {
  font-family: 华文中宋;
  font-size: 28px;
  padding: 5px;
  color: #022336;
}
.coursePriceContent {
  font-family: 华文细黑;
}
.CourseTitle {
  font-family: 华文中宋;
  font-size: 28px;
  padding: 5px;
  color: #022336;
}
.CourseIntro {
  font-family: 华文中宋;
  font-size: 28px;
  padding: 5px;
  color: #022336;
}
.courseIntroContent {
  font-family: 华文楷体;
  font-size: 20px;
  padding: 3px;
  color: #022336;
}
.courseCover {
  width: 300px;
  height: 200px;
  border: #022336 solid 1px;
  border-radius: 4px;
}
.navibar {
  z-index: 9999;
  background-color: #fff;
  position: fixed;
  width: 100%;
  height: 80px;
  opacity: 0.4;
  padding: 25px;
}
.navi {
  font-size: 23px;
  color: #022336;
  margin-left: 15px;
  margin-right: 15px;
}
#button {
  font-size: 20px;
  color: #fff;
  margin-top: 6px;
}
.buttonText {
  color: #fff;
}
#payCol {
  background-color: #022336;
  height:80px;
  width: 100%;
  border: none;
  border-radius: 0px;
  position: fixed;
  z-index: 9998;
  opacity: 0.7;
}
.myContent {
  font-size: 40px;
  flex-grow: 3;
  text-align: center;
}
.allCol {
  display: flex;
  display: -webkit-flex;
  display: -moz-flex;
  flex-direction: row;
  height: 90px;
  margin: 0 auto;
  color: #fff;
  text-align: center;
}
</style>
