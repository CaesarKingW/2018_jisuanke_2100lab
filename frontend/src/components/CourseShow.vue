<template>
<div id="CourseShow" style="background-color: #c4e1ff;">
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
                实验室用大理石和稀盐酸来反应制取二氧化碳，可我们知道，能产生二氧化碳的反应有很多，为什么却选此反应呢？
                该反应最大的优点是反应速度适中，便于实验室收集气体。能否用稀硫酸代替稀盐酸呢？回答是不可以。因为稀硫酸会和大理石中的碳酸钙反应生成微溶于水的硫酸钙，覆盖在大理石表面，使酸与大理石脱离接触，反应自行停止。看到的现象是刚开始有气泡冒出，很快就没有了。
                那么碳酸钠也能和稀盐酸反应放出二氧化碳，用碳酸钠是否可以代替大理石呢？回答也是不可以，因为碳酸钠是粉末性固体，能与盐酸充分接触，反应速度太快，不便于收集气体。
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
      this.$http.post('http://192.168.55.33:8000/app/return_url', request)
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
    border:#99ccff solid 5px;
    border-radius: 20px;
}
</style>
