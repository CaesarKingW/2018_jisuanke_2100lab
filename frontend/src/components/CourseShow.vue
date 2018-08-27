<template>
<body>
<div id="CourseShow">
    <Divider><h1 class="title">{{ title }}</h1></Divider>
    <Divider orientation="right"><p class="read_time" style="font-size: 24px;">浏览量：{{ times }} 次</p></Divider>
    <div class="test_pic"><img id="changePic" v-bind:src="picpath" width=500px height=350px></div>
    <Divider />
    <!-- <Progress :percent="45" status="active" /> -->
    <audio id="audio" controls preload="auto" v-bind:src="aupath"  @play="Play()" @pause="Pause()" @seeked="Dragged()"></audio>
    <Divider />
    <Button type="primary" shape="circle" icon="ios-play"></Button>
    <Divider />
    <Collapse accordion v-model="value">
        <Panel style="background-color:#2d8cf0;">
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
      aupath: '',
      picpath: '',
      pictures: [],
      content: '',
      title: '',
      times: 0,
      last_index: 0,
      last_time: 0,
      st: '',
      id: 1
    }
  },
  mounted: function() {
    this.get_info()
  },
  methods: {
    get_info: function() {
      this.$http
        .post(
          'http://192.168.55.33:8000/app/get_course_info',
          JSON.stringify(this.id)
        )
        .then(response => {
          var res = response.data
          console.log(res)
          this.title = res.course[0].title
          this.aupath = 'http://192.168.55.33:8000' + res.course[0].audio
          console.log(this.aupath)
          this.times = res.course[0].view_count
          this.content = res.course[0].context
          this.pictures = res.pictures
          this.picpath =
            'http://192.168.55.33:8000' + this.pictures[0].course_picture
        })
    },
    Play: function() {
      console.log(this.last_time)
      console.log(this.last_index)
      var vm = this
      vm.picpath =
        'http://192.168.55.33:8000' +
        vm.pictures[vm.last_index].course_picture
      var interval = (
        vm.pictures[vm.last_index].end_time - vm.last_time) * 1000
      vm.st = setTimeout(function() {
        vm.last_index = vm.last_index + 1
        if (vm.last_index >= vm.pictures.length) {
          vm.last_index = 0
          vm.last_time = 0
          return
        }
        vm.last_time = vm.pictures[vm.last_index].start_time
        vm.Play()
      }, interval)
    },
    Pause: function() {
      clearTimeout(this.st)
      this.last_time = document.getElementById('audio').currentTime
      if (
        document.getElementById('audio').currentTime ===
        document.getElementById('audio').duration
      ) {
        this.last_time = 0
        this.last_index = 0
      }
    },
    Dragged: function() {
      var current = document.getElementById('audio').currentTime
      var picindex
      for (let index = 0; index < this.pictures.length; index++) {
        if (this.pictures[index].start_time <= current && this.pictures[index].end_time > current) {
          picindex = index
          break
        } else {
          picindex = 0
        }
      }
      this.last_time = current
      this.last_index = picindex
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
