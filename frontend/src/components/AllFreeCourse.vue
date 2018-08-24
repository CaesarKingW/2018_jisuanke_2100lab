<template>
    <div id="AllFreeCourse">
    <!-- 导航栏 -->
    <div class="navibar">
    <router-link to="/home"><a class="navi">网站首页</a></router-link>
    <Divider type="vertical" />
    <a class="navi" href="#free_col">免费内容</a>
    <Divider type="vertical" />
    <router-link to="/PersonalCenter"><a class="navi">个人中心</a></router-link>
    </div>
    <!-- 底板卡片 -->
    <Card id="free_col"></Card>
    <!-- 标题 -->
    <Card id="free_col">
    <div class="all_col">
    <div class="myContent">
        <h4><Icon type="md-bookmarks" />&nbsp;所有免费内容</h4>
    </div>
    </div>
    </Card>
    <!-- 所有课程 -->
    <div class="container">
    <div class="item">
        <a href="/">
        <Card>
            <p style="text-align:center;" slot="title">{{ title1 }}</p>
            <p style="text-align:center;"><img src="../assets/album_1.png"></p>
        </Card>
        </a>
    </div>
    <div class="item">
        <a href="/">
        <Card>
            <p style="text-align:center;" slot="title">{{ title2 }}</p>
            <p style="text-align:center;"><img src="../assets/album_2.png"></p>
        </Card>
        </a>
    </div>
    </div>
    </div>
</template>
<script>
export default {
  data() {
    return {
      title1: '季节是怎么形成的',
      title2: '谁住在壳里',
      title3: '夜行性动物住在哪儿'
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  display: -webkit-flex;
  display: -moz-flex;
}
.item {
  flex-grow: 1;
  margin-top: 20px;
  margin-bottom: 20px;
}
.one_course {
  display: flex;
  display: -webkit-flex;
  display: -moz-flex;
  flex-direction: row;
  height: 270px;
  margin: 0 auto;
  color: #fff;
  text-align: center;
}
.cover_item {
  flex-grow: 2;
}
#cover {
  border: #022336 solid 2px;
  border-radius: 8px;
  width: 350px;
  height: 250px;
}
.course_title {
  flex-grow: 1;
}
.navibar {
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
#button {
  font-size: 20px;
  color: #fff;
  margin-top: 6px;
}
.button_text {
  color: #fff;
}
#free_col {
  background-color: #022336;
  height: 90px;
  border: none;
  border-radius: 0px;
}
.myContent {
  font-size: 40px;
  flex-grow: 3;
  text-align: center;
}
.all_col {
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
