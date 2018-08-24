<template>
 <div id="home">
     <!-- 导航栏 -->
    <div class="NaviBar">
    <a class="navi" href="#carousel">内容展示</a>
    <Divider type="vertical" />
    <a class="navi" href="#FreeCol">免费内容</a>
    <Divider type="vertical" />
    <a class="navi" href="#PayCol">付费内容</a>
    <Divider type="vertical" />
    <a class="navi" href="#AboutUs">关于我们</a>
    <Divider type="vertical" />
    <router-link to="/ShowUserInfo" v-if="judge"><a class="navi">个人中心</a></router-link>
    <a class="navi" @click="logout" v-if="judge">用户登出</a>
    <router-link to="/UserLogin" v-else><a class="navi">用户登录</a></router-link>

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
    <div class="gengduo">
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
    <div class="item">
        <a href="/">
        <Card>
            <p class="CoverTitle" slot="title">{{ title1 }}</p>
            <p class="CoverPic"><img src="../assets/album_1.png"></p>
        </Card>
        </a>
    </div>
    <div class="item">
        <a href="/">
        <Card>
            <p class="CoverTitle" slot="title">{{ title2 }}</p>
            <p class="CoverPic"><img src="../assets/album_2.png"></p>
        </Card>
        </a>
    </div>
    <div class="item">
        <a href="/">
        <Card>
            <p class="CoverTitle" slot="title">{{ title3 }}</p>
            <p class="CoverPic"><img src="../assets/album_3.png"></p>
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
    <div class="item">
        <a href="/">
        <Card>
            <p class="CoverTitle" slot="title">{{ title1 }}</p>
            <p class="CoverPic"><img src="../assets/album_1.png"></p>
        </Card>
        </a>
    </div>
    <div class="item">
        <a href="/">
        <Card>
            <p class="CoverTitle" slot="title">{{ title2 }}</p>
            <p class="CoverPic"><img src="../assets/album_2.png"></p>
        </Card>
        </a>
    </div>
    <div class="item">
        <a href="/">
        <Card>
            <p class="CoverTitle" slot="title">{{ title3 }}</p>
            <p class="CoverPic"><img src="../assets/album_3.png"></p>
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
      judge: false,
      title1: '季节是怎么形成的',
      title2: '谁住在壳里',
      title3: '夜行性动物住在哪儿',
      value: 0,
      yourname: 'vladimir'
    }
  },
  mounted: function() {
    this.Judgestatus()
  },
  methods: {
    Judgestatus: function() {
      this.$http
        .post('http://192.168.55.33:8000/app/get_status')
        .then(
          response => {
            this.judge = response.data.is_login
          }
        )
    },
    alert_log_out() {
      this.$Message.warning(this.yourname + '已登出')
    },
    logout: function() {
      this.$http
        .post('http://192.168.55.33:8000/app/del_status')
        .then(
          response => {
            this.judge = response.data.is_login
            if (response.data.username === null) {
              this.yourname = response.data.phonenumber
            } else {
              this.yourname = response.data.username
            }
            location.href = 'http://192.168.55.33:8000/#/UserLogin'
            this.alert_log_out()
          }
        )
    }
  }
}
</script>
<style scoped>
.CoverPic {
  text-align: center;
  border:black solid 2px;
  border-radius: 3px;
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
  text-align: center;
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
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
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
