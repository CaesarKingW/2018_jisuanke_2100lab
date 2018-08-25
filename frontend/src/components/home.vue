<template>
 <div id="home">
   <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no" />
     <!-- 导航栏 -->
    <div class="NaviBar">
    <router-link to="/home"><a class="navi"><Icon type="ios-home" /> 网站首页</a></router-link>
    <Divider type="vertical" />
    <router-link to="/AllFreeCourse"><a class="navi"><Icon type="md-bookmarks" /> 免费课程</a></router-link>
    <Divider type="vertical" />
    <router-link to="/AllPayCourse"><a class="navi"><Icon type="logo-usd" /> 付费课程</a></router-link>
    <Divider type="vertical" />
    <router-link to="/UserLogin"><a class="navi"><Icon type="logo-steam" /> 用户登录</a></router-link>
     </div>
     <!-- 走马灯 -->
     <div align="center" id="carousel" class="carousel">
     <Carousel autoplay v-model="value" loop>
        <CarouselItem>
            <div class="DemoCarousel"><Card>
            <div id="RollPicTag"><img class="RollPic" src="../assets/home_1.png"></div>
        </Card>
        </div>
        </CarouselItem>
        <CarouselItem>
            <div class="DemoCarousel"><img class="RollPic" src="../assets/home_2.png"></div>
        </CarouselItem>
    </Carousel>
    </div>
    <!-- 免费内容导航框 -->
    <Card id="FreeCol">
    <div class="AllCol">
    <div class="MyContent">
        <h4><Icon type="md-bookmarks" />&nbsp;免费内容</h4>
    </div>
    <div class="SeeMore">
        <Poptip trigger="hover" title="免费内容预览" content="点击查看所有免费文章。">
        <Button id="button" ghost><router-link to="/AllFreeCourse">
        <div class="ButtonText">查看更多<Icon type="md-log-in" /></div>
        </router-link></Button>
        </Poptip>
    </div>
    </div>
    </Card>
    <!-- 免费内容预览 -->
    <div class="container">
    <div class="item" v-for="item of free_course" :key="item.id">
      <a href="/">
      <Card>
         <p class="CoverTitle" slot="title">{{item.fields.title}}</p>
            <p><img class="CoverPic" v-bind:src= 'item.fields.Cover_picture'/></p>
      </Card>
      </a>
        </div>
    </div>
    <br>
    <!-- 付费内容导航框 -->
    <Card id="PayCol">
    <div class="AllCol">
    <div class="MyContent">
        <h4><Icon type="md-bookmarks" />&nbsp;付费内容</h4>
    </div>
    <div class="SeeMore">
        <Poptip trigger="hover" title="付费内容预览" content="点击查看所有付费文章。">
        <Button id="button" ghost><router-link to="/AllPayCourse">
        <div class="ButtonText">查看更多<Icon type="md-log-in" /></div>
        </router-link></Button>
        </Poptip>
    </div>
    </div>
    </Card>
    <!-- 付费内容预览 -->
    <div class="container">
    <div class="item" v-for="item of paying_course" :key="item.id">
      <a href="/">
      <Card>
         <p class="CoverTitle" slot="title">{{item.fields.title}}</p>
            <p><img class="CoverPic" v-bind:src= 'item.fields.Cover_picture'/></p>
      </Card>
      </a>
        </div>

    </div>
    <!-- 返回顶部 -->
    <BackTop>
        <div class="top">返回顶端</div>
    </BackTop>
    <!-- 关于我们卡片 -->
    <Card id="AboutUs">
    <div class="wrapper">
    <div class="left"><div><Icon size=150 type="ios-people-outline" /></div><div>团队成员</div><div>南开大学软件学院</div><div>佛组</div></div>
    <div class="middle"><div><Icon size=150 type="ios-school-outline" /></div><div>关于我们</div><div>2100实验室</div><div>专注为3~12岁儿童提供更好的科学启蒙教育</div></div>
    <div class="right"><div><Icon size=150 type="ios-eye-outline" /></div><div>联系我们</div><div>南开大学泰达学院</div><div>客服电话：15009253698</div></div>
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
      path: []
    }
  },
  mounted: function() {
    this.show_free_course()
    this.show_paying_course()
  },
  methods: {
    show_free_course: function() {
      this.$http.get('http://192.168.55.33:8000/app/show_free_course').then(
        response => {
          this.imgs = response.data.list
          console.log('success')
          for (var i = 0; i < this.imgs.length; i = i + 1) {
            var a =
              'http://192.168.55.33:8000/media/' +
              this.imgs[i].fields.Cover_picture
            this.imgs[i].fields.Cover_picture = a
          }
          var length = 0
          if (this.imgs.length > this.show_number) length = this.show_number
          else length = this.imgs.length
          this.free_course = this.imgs.slice(0, length)
          console.log('success')
        },
        response => {
          console.log('error')
        }
      )
    },
    show_paying_course: function() {
      this.$http.get('http://192.168.55.33:8000/app/show_paying_course').then(
        response => {
          this.paying_imgs = response.data.list
          console.log('success')
          for (var i = 0; i < this.paying_imgs.length; i = i + 1) {
            var a =
              'http://192.168.55.33:8000/media/' +
              this.paying_imgs[i].fields.Cover_picture
            this.paying_imgs[i].fields.Cover_picture = a
          }
          var length = 0
          if (this.paying_imgs.length > this.show_number) {
            length = this.show_number
          } else length = this.paying_imgs.length
          this.paying_course = this.paying_imgs.slice(0, length)
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
.CoverPic {
  text-align: center;
  margin-left: 12%;
  border: black solid 2px;
  border-radius: 3px;
  width: 300px;
  height: 200px;
}
.CoverTitle {
  text-align: center;
  font-size: 18px;
}
.ButtonText {
  color: #fff;
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
  font-size: 23px;
  color: #022336;
  margin-left: 15px;
  margin-right: 15px;
}
.container {
  display: flex;
  display: -webkit-flex;
  display: -moz-flex;
}
.wrapper {
  display: flex;
  display: -webkit-flex;
  display: -moz-flex;
  flex-direction: row;
  height: 270px;
  margin: 0 auto;
  color: #fff;
  text-align: center;
}
.middle {
  flex-grow: 1;
}
.left {
  flex-grow: 1;
}
.right {
  flex-grow: 1;
}
#AboutUs {
  background-color: #022336;
  height: 300px;
}
#FreeCol,
#PayCol {
  background-color: #022336;
  height: 90px;
}
.AllCol {
  display: flex;
  display: -webkit-flex;
  display: -moz-flex;
  flex-direction: row;
  height: 90px;
  margin: 0 auto;
  color: #fff;
  text-align: center;
}
.SeeMore {
  flex-grow: 1;
  text-align: center;
}
.id {
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
}
.more {
  margin-left: 65%;
}
#button {
  font-size: 20px;
  color: #fff;
  margin-top: 6px;
}
.item {
  flex-grow: 1;
  margin-top: 20px;
  margin-bottom: 20px;
}
.RollPic {
  width: 100%;
  height: 450px;
}
.MyContent {
  font-size: 40px;
  flex-grow: 3;
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
