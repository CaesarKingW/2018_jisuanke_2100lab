<template>
<div id="CourseShow" style="background-color: #c4e1ff;">
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
            <div style="color: white;">文字介绍</div>
            </Poptip>
            <div slot="content" style="text-align: left;font-size: 18px;">{{content}}</div>
        </Panel>
    </Collapse>
    <BackTop>
        <div>返回顶端</div>
    </BackTop>
</div>
</template>
<script>
export default {
  name: 'ourseShow',
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
      id: 7
    }
  },
  mounted: function() {
    // get_id(),
    this.get_info()
  },
  methods: {
    get_id: function() {},
    get_info: function() {
      this.$http
        .post(
          'http://192.168.55.33:8000/app/get_course_info',
          JSON.stringify(this.id)
        )
        .then(response => {
          var res = response.data
          console.log(res)
          this.title = response.data.course[0].title
          this.aupath = 'http://192.168.55.33:8000' + response.data.course[0].audio
          console.log(this.aupath)
          this.times = response.data.course[0].view_count
          this.content = response.data.course[0].context
          this.pictures = response.data.pictures
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
      this.Play()
    }
  }
}
</script>
<style>
#CourseShow {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
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
  border: #99ccff solid 5px;
  border-radius: 20px;
}
</style>
