<template>
<body>
<div id="CourseShow">
    <div class="navibar">
    <router-link to="/home"><a class="navi"><Icon type="ios-home" /> 网站首页</a></router-link>
    <Divider type="vertical" />
    </div>
    <br />
    <div class="title">{{ title }}</div>
    <p class="read_time">浏览量：{{ times }} 次</p>
    <div class="test_pic"><img id="changePic" v-bind:src="picpath"></div>
    <div class="playRoll"><audio id="audio" controls preload="auto" v-bind:src="aupath"  @play="Play()" @pause="Pause()" @seeked="Dragged()"></audio></div>
    <Collapse cLass="collapse" accordion v-model="value">
        <Panel>
            <Poptip trigger="hover" id="poptip" title="文字介绍信息" content="点击可展开或折叠文字介绍。">
            <div>文字介绍</div>
            </Poptip>
            <div slot="content" id="slotContent">
              <div id="scrollBar">
                 {{ content }}
              </div>
            </div>
        </Panel>
    </Collapse>
        <BackTop>
        <div>返回顶端</div>
    </BackTop>
    <div v-if="CanComment">
      <NiceMsgBoard v-bind:course_id = "courseid"></NiceMsgBoard>
    </div>
</div>
</body>
</template>
<script>
import NiceMsgBoard from './NiceMsgBoard'
export default {
  name: 'CourseShow',
  data() {
    return {
      courseid: 0,
      IsFree: true,
      userphone: '',
      IsPaid: false,
      aupath: '',
      picpath: '',
      pictures: [],
      content: '',
      title: '',
      times: null,
      last_index: 0,
      last_time: 0,
      st: '',
      CanComment: true,
      // 学习进度时间点
      studyPoint: 0,
      // 开始学习时间
      startPoint: null,
      // 是否阅后即焚
      IsDestroy: false,
      // 可阅时长
      duration: null,
      closeInterval: null
    }
  },
  created: function() {
    this.Judgestatus()
  },
  mounted: function() {
    // 判断用户是否登录，未登录则直接跳转到登录页面
    // 登录则获取课程id
  },
  components: {
    NiceMsgBoard
  },
  methods: {
    get_info: function() {
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/get_course_info',
          JSON.stringify(this.courseid)
        )
        .then(response => {
          var res = response.data
          this.title = res.course[0].title
          this.aupath = this.GLOBAL.serverSrc + res.course[0].audio
          this.content = res.course[0].context
          this.pictures = res.pictures
          this.picpath = this.GLOBAL.serverSrc + this.pictures[0].course_picture
        })
    },
    Play: function() {
      var vm = this
      vm.picpath =
        this.GLOBAL.serverSrc + vm.pictures[vm.last_index].course_picture
      var interval = (vm.pictures[vm.last_index].end_time - vm.last_time) * 1000
      vm.st = setTimeout(function() {
        vm.last_index = vm.last_index + 1
        if (vm.last_index >= vm.pictures.length) {
          vm.last_index = 0
          vm.last_time = 0
          return
        }
        vm.last_time = vm.pictures[vm.last_index].start_time
        this.studyPoint = document.getElementById('audio').currentTime
        vm.Play()
      }, interval)
    },
    Pause: function() {
      clearTimeout(this.st)
      this.last_time = document.getElementById('audio').currentTime
      this.studyPoint = this.last_time
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
        if (
          this.pictures[index].start_time <= current &&
          this.pictures[index].end_time > current
        ) {
          picindex = index
          break
        } else {
          picindex = 0
        }
      }
      this.last_time = current
      this.last_index = picindex
    },
    // 判断登录状态，防止用户强制访问
    Judgestatus: function() {
      this.$http
        .post(this.GLOBAL.serverSrc + '/app/get_status')
        .then(response => {
          var judge = response.data.is_login
          // 用户未登录状态下强制访问，跳出404 not found页面
          // 这里暂时先直接跳入登录页面
          if (!judge) {
            this.$router.push({ name: 'UserLogin' })
          } else {
            this.userphone = response.data.list[0].pk
            // 获取课程id
            this.GetCourseId()
          }
        })
    },
    GetCourseId: function() {
      // 从路由中获取课程id
      this.courseid = this.$route.query.id
      // 获取takes记录，取出课程第一次播放的时间戳
      this.createTakes()
      // 判断此门课程是否存在，不存在则直接调回home页面，
      // 是否为免费，并获取课程标题
      // 若为付费则判断订单状态
    },
    // 若是第一次观看，则加一条takes记录
    createTakes: function() {
      var now = Date.parse(new Date())
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/add_new_take',
          JSON.stringify({
            userphone: this.userphone,
            courseid: this.courseid,
            beginPoint: now
          })
        )
        .then(
          response => {
            this.startPoint = response.data.startPoint
            var breakPoint = response.data.breakPoint
            document.getElementById('audio').currentTime = breakPoint
            // 获取课程非内容属性
            this.JudgePrice()
          },
          response => {
          }
        )
    },
    // 获取课程标题和是否免费属性
    JudgePrice: function() {
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/get_specified_course',
          JSON.stringify(this.courseid)
        )
        .then(response => {
          var exist = response.data.exist
          if (exist) {
            var course = []
            course = response.data.list
            this.title = course[0].fields.title
            var price = course[0].fields.price
            this.CanComment = course[0].fields.can_comment
            this.times = course[0].fields.view_count
            this.IsDestroy = course[0].fields.Is_destroy
            this.duration = course[0].fields.distory_time
            if (this.IsDestroy) {
              this.Boom()
            }
            if (price === 0) {
              this.IsFree = true
            } else {
              this.IsFree = false
            }
            // 若是付费课程判断用户是否支付完成，未支付完成则直接跳转到主页
            if (!this.IsFree) {
              this.JudgePayment()
            } else {
              // 获取免费课程播放所需要的信息
              this.get_info()
            }
          } else {
            this.$router.push({ name: 'home' })
          }
        })
    },
    // 将用户手机号和课程id传给后端查找是否有关联两者的订单
    JudgePayment: function() {
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/get_order_payment',
          JSON.stringify({
            phone_number: this.userphone,
            course_id: this.courseid
          })
        )
        .then(response => {
          this.IsPaid = response.data.order_status
          // 如果是付费课程且未支付则直接跳转到Home页面
          if (!this.IsPaid) {
            this.$router.push({ name: 'home' })
          } else {
            // 获取课程播放所需要的信息
            this.get_info()
          }
        })
    },
    Boom: function() {
      let _this = this
      _this.closeInterval = setInterval(() => {
        var now = Date.parse(new Date())
        if (_this.startPoint !== null && _this.duration !== null) {
          var diff = now - (_this.startPoint + _this.duration * 3600000)
          if (diff > 0) {
            _this.SetBurn()
            _this.$router.push({ name: 'ReadAndBurn' })
          }
        }
      }, 1000)
    },
    SetBurn: function() {
      this.$http.post(
        this.GLOBAL.serverSrc + '/app/set_burn',
        JSON.stringify({
          userphone: this.userphone,
          courseid: this.courseid
        })
      )
    }
  },
  // vue实例销毁后记录下此次观看进度
  beforeDestroy() {
    clearInterval(this.closeInterval)
    this.$http
      .post(
        this.GLOBAL.serverSrc + '/app/add_or_update_takes',
        JSON.stringify({
          userphone: this.userphone,
          courseid: this.courseid,
          studyPoint: this.studyPoint
        })
      )
      .then(response => {}, response => {})
  }
}
</script>
<style>
#slotContent {
  text-align: left;
  font-size: 18px;
}
#poptip {
  font-size: 24px;
}
.navibar {
  z-index: 9999;
  background-color: #fff;
  position: fixed;
  width: 100%;
  height: 80px;
  top: -15px;
  opacity: 0.7;
  padding: 0px;
  /* padding: 25px; */
}
.navi {
  font-size: 18px;
  color: #022336;
  margin-left: 15px;
  margin-right: 15px;
}
.playRoll {
  margin: 0 auto;
  text-align: center;
}
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
  height: 300px;
  margin: 0 auto;
}
</style>
