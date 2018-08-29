<template>
  <div id="AllPayCourse">
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
    <!-- <div class="myPanel"></div> -->
    <br />
    <br />
    <br />
    <br />
    <br />
    <div id="blank"></div>
    <div v-for="item of imgs" :key="item.id">
      <router-link :to="{path:'PayCourseIntro', query:{id: item.pk}}">
        <Card class="courseCard">
          <div class="CourseInfo">
            <div class="CourseCoverDiv"><img class="courseCover" v-bind:src='item.fields.Cover_picture' /></div>
            <div class="CourseText">
            <div class="CourseTitle">
                <Icon type="ios-bookmarks" /> 课程标题：<span class="courseTitleContent">{{item.fields.title}}</span></div>
            <div class="CourseIntro">
                <Icon type="ios-text" /> 课程简介：
                <div class="courseIntroContent">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                {{item.fields.brief_introduction}}</div></div>
            <div class="CoursePrice">
                <Icon type="logo-usd" /> 课程价格：<span class="coursePriceContent">{{item.fields.price}} 元</span>
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
      this.$http.get(this.GLOBAL.serverSrc + '/app/show_paying_course').then(
        response => {
          this.imgs = response.data.list
          for (var i = 0; i < this.imgs.length; i = i + 1) {
            var a =
              this.GLOBAL.serverSrc +
              '/media/' +
              this.imgs[i].fields.Cover_picture
            this.imgs[i].fields.Cover_picture = a
          }
        },
        response => {}
      )
    }
  }
}
</script>
<style scoped>
.courseCard {
  width: 650px;
  margin: 0 auto;
}

.courseTitleContent {
  font-family: 华文细黑;
}

.CourseInfo {
  display: flex;
  color: #022336;
}
.CourseText {
  float: left;
  margin-left: 5%;
  color: #022336;
}

.CoursePrice {
  font-family: 华文中宋;
  font-size: 25px;
  padding: 5px;
  color: #022336;
}

.coursePriceContent {
  font-family: 华文细黑;
}

.CourseTitle {
  font-family: 华文中宋;
  font-size: 25px;
  padding: 5px;
  color: #022336;
}

.CourseIntro {
  font-family: 华文中宋;
  font-size: 25px;
  padding: 5px;
  color: #022336;
}

.courseIntroContent {
  font-family: 华文楷体;
  font-size: 20px;
  padding: 3px;
  width: 250px;
  color: #022336;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
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
  opacity: 0.9;
  padding: 25px;
}

.navi {
  font-size: 18px;
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
  height: 80px;
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
.myPanel {
  background-color: red;
  position: fixed;
  width: 100%;
  height: 160px;
  opacity: 1;
  padding: 25px;
}

@media screen and (max-width: 500px) {
  .navi {
    display: block;
  }
  #blank {
    margin-top: 105px;
  }
  .courseCard {
    width: 100%;
    height: 160px;
    margin: 0 auto;
  }
  .courseCover {
    width: 180px;
    height: 130px;
    border: #022336 solid 1px;
    border-radius: 4px;
  }
  .courseTitleContent {
    font-family: 华文细黑;
  }
  .CourseInfo {
    display: flex;
    color: #022336;
    /* width: 30%; */
  }
  .CourseText {
    float: left;
    margin-left: 2%;
    color: #022336;
    width: 40%;
  }
  .CourseTitle {
    font-family: 华文中宋;
    font-size: 14px;
    /* padding: 1px; */
    color: #022336;
  }
  .CourseIntro {
    font-family: 华文中宋;
    font-size: 14px;
    /* padding: 1px; */
    color: #022336;
  }
  .courseIntroContent {
    font-family: 华文楷体;
    font-size: 12px;
    /* padding: 1px; */
    color: #022336;
    width: 90px;
    color: #022336;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .CoursePrice {
    font-family: 华文中宋;
    font-size: 14px;
    /* padding: 1px; */
    color: #022336;
  }
  .coursePriceContent {
    font-family: 华文细黑;
  }
}
</style>
