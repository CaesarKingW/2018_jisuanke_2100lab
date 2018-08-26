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
               <div style="overflow: auto;height: 90px;">content</div>
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
