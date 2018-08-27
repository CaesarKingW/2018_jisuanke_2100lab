<template>
<body>
<div id="CourseShow">
    <div class="title">{{ title }}</div>
    <p class="read_time">浏览量：{{ times }} 次</p>
    <div class="test_pic"><img id="changePic" src="../assets/2.png"></div>
    <div id="progressRollDiv"><Progress :percent="45" status="active" /></div>
    <div id="pauseButtonDiv"><Button id="pauseButton" type="primary" shape="circle" icon="ios-play"></Button></div>
    <Collapse class="collapse" accordion v-model="value">
        <Panel>
            <Poptip trigger="hover" style="font-size: 24px;" title="文字介绍信息" content="点击可展开或折叠文字介绍。">
            <div>文字介绍</div>
            </Poptip>
            <div slot="content" style="text-align: left;font-size: 18px;">
               <div id="scrollBar">
                 除了间接是受疾病影响，疼痛不舒适时情绪就会容易变得烦躁不安。
                 主要还是老人家年纪大了，心理你缺少陪伴安全感，你应该比较少关注老人，
                 更多时间是在工作、交友、孩子和自己另一半等上面。建议你多分一些
                 注意力给老人家除了间接是受疾病影响，疼痛不舒适时情绪就会容易变得烦躁不安。
                 主要还是老人家年纪大了，心理你缺少陪伴安全感，你应该比较少关注老人，更多时间是在工作、交友、孩子和自己另一半等上面。建议你多分一些注意力给老人家除了间接是受疾病影响，疼痛不舒适时情绪就会容易变得烦躁不安。主要还是老人家年纪大了，心理你缺少陪伴安全感，你应该比较少关注老人，更多时间是在工作、交友、孩子和自己另一半等上面。建议你多分一些注意力给老人家</div>
            </div>
        </Panel>
    </Collapse>
        <BackTop>
        <div>返回顶端</div>
    </BackTop>
    <NiceMsgBoard/>
</div>
</body>
</template>
<script>
import NiceMsgBoard from './NiceMsgBoard'
export default {
  name: 'CourseShow',
  data() {
    return {
      title: '科学实验：实验室制取CO2',
      times: '9999',
      value: ''
    }
  },
  mounted: function() {
    var orderId = this.$route.query.out_trade_no
    if (typeof orderId !== 'undefined') {
      var request = JSON.stringify(orderId)
      this.$http
        .post('http://192.168.55.33:8000/app/notify', request)
        .then(response => {
          console.log(response.data)
        })
    }
  },
  components: {
    NiceMsgBoard
  }
}
</script>
<style>
#scrollBar {
  overflow-y: auto;
  overflow-x: hidden;
  height: 90px;
}
#progressRollDiv {
  width: 60%;
  text-align: center;
  margin: 0 auto;
  margin-top: 20px;
}
#pauseButtonDiv {
  text-align: center;
  margin: 20px;
}
#pauseButton {
  background-color: #fff;
  color: #000;
  border: #000 solid 2px;
  text-align: center;
  font-size: 20px;
}
.collapse {
  text-align: center;
  width: 60%;
  margin: 0 auto;
}
#CourseShow {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
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
.test_pic {
  margin: 0 auto;
  text-align: center;
}
.title {
  margin: 0 auto;
  text-align: center;
  margin-top: 20px;
  margin-bottom: 10px;
  font-size: 30px;
  font-family: 华文中宋;
}
.read_time {
  margin: 0 auto;
  margin-top: 10px;
  margin-bottom: 20px;
  text-align: center;
  font-family: 微软雅黑;
  font-size: 16px;
}
#changePic {
  border: #000 solid 5px;
  border-radius: 20px;
  width: 40%;
  height: auto;
  margin: 0 auto;
}
</style>
