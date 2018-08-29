<template>
  <div id="home">
    <meta name="viewport" content="width=device-width, initial-scale=1.0,
   maximum-scale=1.0, minimum-scale=1.0, user-scalable=no" />
    <div class="NaviBar">
      <router-link to="/home">
        <a class="navi">
          <Icon type="md-home" /> 网站首页
        </a>
      </router-link>
      <Divider type="vertical" />
      <router-link to="/AllFreeCourse">
        <a class="navi">
          <Icon type="md-bookmarks" /> 免费课程</a>
      </router-link>
      <Divider type="vertical" />
      <router-link to="/AllPayCourse">
        <a class="navi">
          <Icon type="logo-usd" /> 付费课程</a>
      </router-link>
      <Divider type="vertical" />
      <router-link to="/PersonalCenter" v-if="judge">
        <a class="navi">
          <Icon type="ios-contact" /> 个人中心</a>
      </router-link>
      <a class="navi" @click="logout" v-if="judge">
        <Icon type="md-log-out" /> 退出登录</a>
      <router-link to="/UserLogin" v-else>
        <a class="navi">
          <Icon type="md-log-in" /> 用户登录</a>
      </router-link>
    </div>
    <div align="center" id="carousel" class="carousel">
      <Carousel autoplay v-model="value" loop>
        <CarouselItem>
          <div class="DemoCarousel">
            <Card>
              <div id="RollPicTag"><img class="RollPic" src="../assets/home_1.png">
              </div>
            </Card>
          </div>
        </CarouselItem>
        <CarouselItem>
          <div class="DemoCarousel"><img class="RollPic" src="../assets/home_2.png"></div>
        </CarouselItem>
      </Carousel>
    </div>
    <Card id="FreeCol">
      <div class="AllCol">
        <div class="MyContent">
          <div>
            <Icon type="md-bookmarks" />&nbsp;免费内容</div>
        </div>
        <div class="SeeMore">
          <Button id="button" ghost>
            <router-link to="/AllFreeCourse">
              <span class="ButtonText">查看更多
                <Icon type="md-log-in" />
              </span>
            </router-link>
          </Button>
        </div>
      </div>
    </Card>
    <div class="container">
      <div class="item" v-for="item of free_course" :key="item.id">
        <router-link :to="{path:'FreeCourseIntro', query:{id: item.pk}}">
          <Card class="courseCard">
            <p class="CoverTitle" slot="title">{{item.fields.title}}</p>
            <p><img class="CoverPic" v-bind:src='item.fields.Cover_picture' /></p>
          </Card>
        </router-link>
      </div>
    </div>
    <br>
    <Card id="PayCol">
      <div class="AllCol">
        <div class="MyContent">
          <div>
            <Icon type="md-bookmarks" />&nbsp;付费内容</div>
        </div>
        <div class="SeeMore">
          <Button id="button" ghost>
            <router-link to="/AllPayCourse">
              <span class="ButtonText">查看更多
                <Icon type="md-log-in" />
              </span>
            </router-link>
          </Button>
        </div>
      </div>
    </Card>
    <div class="container">
      <div class="item" v-for="item of paying_course" :key="item.id">
        <router-link :to="{path:'PayCourseIntro', query:{id: item.pk}}">
          <Card class="courseCard">
            <p class="CoverTitle" slot="title">{{item.fields.title}}</p>
            <p><img class="CoverPic" v-bind:src='item.fields.Cover_picture' /></p>
          </Card>
        </router-link>
      </div>
    </div>
    <BackTop>
      <div class="top">返回顶端</div>
    </BackTop>
    <Card id="AboutUs">
      <div class="wrapper">
        <div class="left">
          <div>
            <Icon size=100 type="ios-people-outline" />
          </div>
          <div>团队成员</div>
          <div>南开大学软件学院</div>
          <div>佛组</div>
        </div>
        <div class="middle">
          <div>
            <Icon size=100 type="ios-school-outline" />
          </div>
          <div>关于我们</div>
          <div>2100实验室</div>
          <div>专注为3~12岁儿童提供更好的科学启蒙教育</div>
        </div>
        <div class="right">
          <div>
            <Icon size=100 type="ios-eye-outline" />
          </div>
          <div>联系我们</div>
          <div>南开大学泰达学院</div>
          <div>客服电话：15009253698</div>
        </div>
      </div>
    </Card>
  </div>
</template>
<script>
export default {
  name: 'home',
  data() {
    return {
      value: 0,
      imgs: [],
      free_course: [],
      paying_imgs: [],
      paying_course: [],
      show_number: 3,
      path: [],
      judge: false,
      yourname: ''
    }
  },
  mounted: function() {
    this.show_free_course()
    this.show_paying_course()
    this.Judgestatus()
  },
  methods: {
    show_free_course: function() {
      this.$http.get(this.GLOBAL.serverSrc + '/app/show_free_course').then(
        response => {
          this.imgs = response.data.list
          for (var i = 0; i < this.imgs.length; i = i + 1) {
            var a =
              this.GLOBAL.serverSrc +
              '/media/' +
              this.imgs[i].fields.Cover_picture
            this.imgs[i].fields.Cover_picture = a
          }
          var length = 0
          if (this.imgs.length > this.show_number) length = this.show_number
          else length = this.imgs.length
          this.free_course = this.imgs.slice(0, length)
        },
        response => {}
      )
    },
    show_paying_course: function() {
      this.$http.get(this.GLOBAL.serverSrc + '/app/show_paying_course').then(
        response => {
          this.paying_imgs = response.data.list
          for (var i = 0; i < this.paying_imgs.length; i = i + 1) {
            var a =
              this.GLOBAL.serverSrc +
              '/media/' +
              this.paying_imgs[i].fields.Cover_picture
            this.paying_imgs[i].fields.Cover_picture = a
          }
          var length = 0
          if (this.paying_imgs.length > this.show_number) {
            length = this.show_number
          } else length = this.paying_imgs.length
          this.paying_course = this.paying_imgs.slice(0, length)
        },
        response => {}
      )
    },
    Judgestatus: function() {
      this.$http
        .post(this.GLOBAL.serverSrc + '/app/get_status')
        .then(response => {
          this.judge = response.data.is_login
        })
    },
    alert_log_out() {
      this.$Message.warning(this.yourname + '已登出')
    },
    logout: function() {
      this.$http
        .post(this.GLOBAL.serverSrc + '/app/del_status')
        .then(response => {
          this.judge = response.data.is_login
          if (response.data.username === null) {
            this.yourname = response.data.phonenumber
          } else {
            this.yourname = response.data.username
          }
          location.href = this.GLOBAL.serverSrc + '#/UserLogin'
          this.alert_log_out()
        })
    }
  }
}
</script>
<style scoped>
.home {
  margin: 0 auto;
}

.CoverPic {
  text-align: center;
  border: black solid 2px;
  border-radius: 3px;
  width: 270px;
  height: 200px;
  margin: auto;
}

.CoverTitle {
  text-align: center;
  font-size: 18px;
}

.ButtonText {
  color: #fff;
  float: right;
}

.NaviBar {
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

.container {
  width: 85%;
  display: flex;
  display: -webkit-flex;
  display: -moz-flex;
  margin: 0 auto;
  justify-content: space-around;
}

.wrapper {
  display: flex;
  display: -webkit-flex;
  display: -moz-flex;
  flex-direction: row;
  height: 200px;
  margin: 0 auto;
  color: #fff;
}

.middle {
  flex-grow: 1;
  flex-shrink: 1;
  margin: 0 auto;
}

.left {
  flex-grow: 1;
  flex-shrink: 1;
  margin: 0 auto;
  text-align: center;
}

.right {
  flex-grow: 1;
  flex-shrink: 1;
  margin: 0 auto;
  text-align: center;
}

#AboutUs {
  background-color: #022336;
  height: 220px;
  width: 85%;
  margin: 0 auto;
  text-align: center;
}

#FreeCol,
#PayCol {
  background-color: #022336;
  height: 60px;
  width: 85%;
  text-align: center;
  margin: 0 auto;
}

.AllCol {
  display: flex;
  display: -webkit-flex;
  display: -moz-flex;
  flex-direction: row;
  height: 40px;
  margin: 0 auto;
  color: #fff;
  text-align: center;
}

.SeeMore {
  position: static;
}

.id {
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
}
#button {
  position: static;
  font-size: 15px;
  margin-left: 797px;
  color: #fff;
  border: none;
}

.item {
  flex-grow: 1;
  flex-shrink: 1;
  margin-top: 20px;
  margin-bottom: 20px;
  text-align: center;
}

.RollPic {
  width: 100%;
  height: 450px;
}

.carousel {
  width: 85%;
  margin: 0 auto;
}

.MyContent {
  font-size: 18px;
  margin-left: 27px;
  text-align: center;
}

.top {
  padding: 12px;
  background: rgba(13, 102, 146, 0.9);
  color: #fff;
  text-align: center;
  border-radius: 2px;
}
</style>
