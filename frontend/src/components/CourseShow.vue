<template>
<div id="CourseShow">
    <Divider><h1 class="title">{{ title }}</h1></Divider>
    <Divider orientation="right"><p class="read_time" style="font-size: 24px;">浏览量：{{ times }} 次</p></Divider>
    <div class="test_pic"><img id="changePic" src="../assets/2.png"></div>
    <Divider />
    <Progress :percent="45" status="active" />
    <Divider />
    <Button type="primary" shape="circle" icon="ios-play"></Button>
    <Divider />
    <Collapse accordion v-model="value">
        <Panel style="background-color:#2d8cf0;">
            <Poptip trigger="hover" style="font-size: 24px;" title="文字介绍信息" content="点击可展开或折叠文字介绍。">
            <div style="color: white;">文字介绍</div>
            </Poptip>
            <div slot="content" style="text-align: left;font-size: 18px;">
               <div style="overflow: auto;height: 90px;">昨日太行山上,层迭峰石,突兀傲松,却静止于空洞,亿万年轮,看透了鸢飞戾天,看透了鱼翔浅底,看透了烟雨情愁,看透了日月星辰,木雕流金,将感情深深地埋在悬崖绝壁间.所以我开始彷徨,寻不到你的所藏,庆幸的是,我找到了,太行清明,你把泪已千行的岁月蕴藏在那双明镜的眼眸,雨打湿了眼眶,然后微笑的让行人用她辛辛苦苦打上来的山泉洗手,那无声的暗示,那佝偻的优雅,还有那日日的皱痕,年年倚井盼归堂的眷恋,是太行之行带给我的最美的感动.物言无情人有情,无言泪已拆两行.</div>
            </div>
        </Panel>
    </Collapse>
    <BackTop>
        <div>返回顶端</div>
    </BackTop>
</div>
</template>
<script>
export default {
  name: 'CourseShow',
  data() {
    return {
      title: '科学实验：实验室制取CO2',
      times: '9999'
    }
  },
  mounted: function() {
    var orderId = this.$route.query.out_trade_no
    if (typeof (orderId) !== 'undefined') {
      var request = JSON.stringify(orderId)
      this.$http.post('http://192.168.55.33:8000/app/notify', request)
        .then(response => {
          console.log(response.data)
        })
    }
  }
}
</script>
<style>
#CourseShow {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#title {
  color: #17233d;
}
#read_time {
  color: #808695;
  font-size: 14px;
}
.top {
  padding: 10px;
  background: #2d8cf0;
  color: #fff;
  text-align: center;
  border-radius: 2px;
}
#changePic {
    border:#000 solid 5px;
    border-radius: 20px;
}
</style>
