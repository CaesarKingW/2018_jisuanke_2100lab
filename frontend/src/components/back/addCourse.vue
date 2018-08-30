import datetime
<template>
  <div v-if="all">
    <div v-if="start_add">
      <p id="title" class="formitem">课程标题：
        <Input id="titleInput" v-model="course_title" placeholder="" style="width: 300px" />
      </p>
      <div id="intro" class="formitem">课程简介：
        <Input id="introInput" v-model="brief_intro" type="textarea" style="width: 300px" />
      </div>
      <Button id="newCourseButton" class="formitem" @click="addCourse()">新建课程</Button>
    </div>
    <div v-if="upload_audi">
      <p class="formitem">上传音频</p>
      <p class="formitem">
        <input type="file" name="audi_upload">
        <Button @click="AudiUpload()">上传</Button>
      </p>
    </div>
    <audio controls="controls" v-if="is_show1" id="aud" class="formitem" v-bind:src="audi" @ended="audioEnded()" preload="auto"></audio>
    <div>
      <p v-if="first_notice" class="formitem">开始播放音频前，请上传课程的第一张图片</p>
      <p v-if="contin" class="formitem">继续上传课程的剩下图片</p>
      <p v-if="upload_pic" class="formitem"><input type="file" name="pic_upload">
        <button @click="PicUpload()">上传</button>
      </p>
      <div v-if="show_pic" class="formitem"><img v-bind:src="pic" id="sp" /></div>
      <p class="formitem">
        <Button v-if="set_start_time" @click="setStartTime()">将音频当前播放点设为图片开始时间</Button>
        <span v-if="start_time">图片开始时间当前被设置为：{{startTime}}</span>
      </p>
      <p v-if="set_end_time">
        <button @click="setEndTime()">将音频当前播放点设为图片结束时间</button>
        <span v-if="end_time">图片结束时间当前被设置为：{{endTime}}</span>
      </p>
      <p v-if="start_time&&end_time&&!preview">当前图片的开始时间与结束时间均已被设置好，确认提交并继续上传下一张图片吗？
        <Button @click="continu()">确认</Button>
      </p>
      <p v-if="end" class="formitem">音频已播放完，当前图片的结束时间自动被设置为音频的结束时间。</p>
      <p v-if="preview" class="formitem">所有图片的起讫时间均已被设置,去预览课程！
        <Button id="go" @click='Preview()'>
          <Icon type="ios-arrow-dropright-circle" id="arrow" />
        </Button>
      </p>
    </div>
    <div v-if="real_preview">
      <div v-if="show_real_pic" class="formitem">
        <img v-bind:src="pic_to_show" id="pts" />
      </div>
      <div class="formitem">
        <audio controls="controls" id="audio" v-bind:src="audi" @play="Play()" @pause="Pause()" preload="auto">
        </audio>
      </div>
      <Button class="formitem" :size="buttonSize" type="primary" @click="goToRest()">
        下一步
        <Icon type="ios-arrow-forward" />
      </Button>
    </div>

    <div v-if="rest">
      <h1 class="formitem">继续完善第{{course_id}}号课程的信息</h1>
      <p class="formitem">
        <Icon type="md-document" />详解：<Input type="textarea" v-model="wholeIntroduction"/></p>
      <p class="formitem">
        <Icon type="md-easel" />课程封面：<input type="file" name="course_cover"></p>
      <p class="formitem">
        <Icon type="md-flame" />是否阅后即焚：
        <i-switch v-model="Is_destroy" />
      </p>
      <p class="formitem" v-if="Is_destroy">可阅时长：
        <InputNumber :min="0" v-model="destroy_time" />小时</p>
      <p class="formitem">
        <Icon type="md-pricetag" />价格：
        <InputNumber :min="0.00" :step="0.01" v-model="price"></InputNumber>元</p>
      <p class="formitem" v-if="price>0">
        <Icon type="md-share-alt" />分销比例：
        <InputNumber :min="0" :max="100" v-model="share_rate" :formatter="value => `${value}%`" :parser="value => value.replace('%', '')"></InputNumber>
      </p>
      <p class="formitem">
        <Icon type="ios-chatbubbles" />是否允许用户留言：
        <i-switch v-model="can_comment" />
      </p>
      <p class="formitem">
        <Button @click="Submit()">提交</Button>
      </p>
    </div>
    <div v-if="finish" class="succeed">
      第{{course_id}}号课程上传成功！
    </div>
  </div>
</template>
<script>
export default {
  name: 'addCourse',
  data() {
    return {
      all: true,
      start_add: true,
      course_title: '',
      brief_intro: '',
      course_id: null,
      upload_audi: false,
      is_show1: false,
      first_notice: false,
      contin: false,
      upload_pic: false,
      show_pic: false,
      pic_uploaded: false,
      set_start_time: false,
      set_end_time: false,
      start_time: false,
      end_time: false,
      startTime: 0,
      endTime: 0,
      next: false,
      end: false,
      review: false,
      audi1: '',
      pic: '',
      pic_id: 0,
      real_preview: false,
      show_real_pic: false,
      preview: false,
      pictures: [],
      audio: '',
      pic_to_show: '',
      st: null,
      index: 0,
      last_time: 0,
      last_index: 0,
      buttonSize: 'large',
      rest: false,
      Is_destroy: false,
      destroy_time: null,
      is_free: false,
      price: null,
      share_rate: null,
      can_comment: false,
      add_course: false,
      finish: false,
      real_finished: false,
      wholeIntroduction: ''
    }
  },
  created: function() {
    this.$http
      .post('http://192.168.55.33:8000/app/get_mstatus')
      .then(response => {
        var res = response.data
        this.mis_login = res.mis_login
        if (!this.mis_login) {
          alert('还没有登录，无权访问该页面！')
          location.href = '/#/backstageLogin'
        } else {
          if (res.manager.Manage_course !== true) {
            alert('你没有权限访问该网页！')
            location.href = '/#/backstage'
          }
        }
      })
  },
  beforeDestroy: function() {
    if (this.real_finished === false) {
      this.$http
        .post('http://192.168.55.33:8000/app/half', JSON.stringify(this.course_id))
        .then(response => {})
    }
  },
  methods: {
    addCourse() {
      this.$http
        .post(
          'http://192.168.55.33:8000/app/add_course',
          JSON.stringify({
            title: this.course_title,
            brief_intro: this.brief_intro
          })
        )
        .then(response => {
          var res = response.data
          if (res['msg'] === false) {
            alert('标题和课程简介不能为空！')
          }
          if (res['msg'] === true) {
            this.course_id = res.course.id
            alert('去上传课程音频！')
            this.upload_audi = true
            this.start_add = false
          }
        })
    },
    AudiUpload() {
      var formData = new FormData()
      var str = document.querySelector('input[name ="audi_upload"]').value
      if (str.indexOf('.mp3') < 0 && str.indexOf('.MP3') < 0) {
        alert('文件类型不正确！请上传.mp3、.MP3类型的文件！')
      } else {
        var fileInfo = document.querySelector('input[name="audi_upload"]')
          .files[0]
        formData.append('file', fileInfo)
        formData.append('course_id', this.course_id)
        this.$http
          .post('http://192.168.55.33:8000/app/add_audi', formData)
          .then(response => {
            var res = response.data
            this.audi = res.audio
            this.is_show1 = true
            this.first_notice = true
            this.upload_pic = true
            this.upload_audi = false
            alert(
              '开始播放音频前，请上传课程的第一张图片，并且第一张图片的开始时间默认设为音频起点！'
            )
          })
      }
    },
    PicUpload() {
      var formData = new FormData()
      var str = document.querySelector('input[name ="pic_upload"]').value
      if (
        str.indexOf('.jpg') < 0 &&
        str.indexOf('.png') < 0 &&
        str.indexOf('.gif') < 0 &&
        str.indexOf('.JPG') < 0 &&
        str.indexOf('.PNG') < 0 &&
        str.indexOf('.GIF') < 0
      ) {
        alert(
          '文件类型不正确！请上传.jpg、.png、.gif、.JPG、.PNG、.GIF类型的文件！'
        )
      } else {
        var fileInfo = document.querySelector('input[name ="pic_upload"]')
          .files[0]
        var au = document.getElementById('aud')
        var duration = au.duration
        var st = au.currentTime
        formData.append('file', fileInfo)
        formData.append('course_id', this.course_id)
        formData.append('duration', duration)
        formData.append('count', 0)
        this.$http
          .post('http://192.168.55.33:8000/app/add_img', formData)
          .then(response => {
            var res = response.data
            this.pic = 'http://192.168.55.33:8000' + res.course_picture
            this.first_notice = false
            this.show_pic = true
            this.upload_pic = false
            alert(
              '图片上传完成，而且新上传的图片的开始时间默认设为音频当前播放点!'
            )
            this.set_end_time = true
            this.pic_id = res.id
            this.$http
              .post(
                'http://192.168.55.33:8000/app/set_start_time',
                JSON.stringify({
                  pic_id: this.pic_id,
                  start_time: st
                })
              )
              .then(response => {
                this.startTime = st
                this.start_time = true
              })
          })
      }
    },
    setStartTime() {
      var au = document.getElementById('aud')
      var st = au.currentTime
      this.$http
        .post(
          'http://192.168.55.33:8000/app/set_start_time',
          JSON.stringify({
            pic_id: this.pic_id,
            start_time: st
          })
        )
        .then(response => {
          this.start_time = true
          this.startTime = response.data.start_time
        })
    },
    setEndTime() {
      var au = document.getElementById('aud')
      var et = au.currentTime
      this.$http
        .post(
          'http://192.168.55.33:8000/app/set_end_time',
          JSON.stringify({
            pic_id: this.pic_id,
            end_time: et
          })
        )
        .then(response => {
          this.end_time = true
          this.endTime = response.data.end_time
        })
    },
    continu() {
      this.contin = true
      this.upload_pic = true
      this.set_start_time = false
      this.set_end_time = false
      this.start_time = false
      this.end_time = false
      this.show_pic = false
    },
    audioEnded() {
      alert('音频已播放完，当前图片的结束时间自动被设置为音频的结束时间!')
      var au = document.getElementById('aud')
      var et = au.currentTime
      this.$http
        .post(
          'http://192.168.55.33:8000/app/set_end_time',
          JSON.stringify({
            pic_id: this.pic_id,
            end_time: et
          })
        )
        .then(response => {
          this.end_time = true
          this.endTime = response.data.end_time
          this.preview = true
        })
    },
    Preview() {
      this.$http
        .post(
          'http://192.168.55.33:8000/app/preview',
          JSON.stringify({
            course_id: this.course_id
          })
        )
        .then(response => {
          this.start_add = false
          this.upload_audi = false
          this.is_show1 = false
          this.first_notice = false
          this.contin = false
          this.upload_pic = false
          this.upload_pic = false
          this.show_pic = false
          this.set_start_time = false
          this.start_time = false
          this.set_end_time = false
          this.end_time = false
          this.preview = false
          this.pictures = response.data.pictures
          this.audio = 'http://192.168.55.33:8000' + response.data.course.audio
          this.real_preview = true
          this.show_real_pic = true
          this.last_index = 0
          this.pic_to_show =
            'http://192.168.55.33:8000' + this.pictures[0].course_picture
        })
    },
    Play() {
      var vm = this
      vm.pic_to_show =
        'http://192.168.55.33:8000' + vm.pictures[vm.last_index].course_picture
      var interval = (vm.pictures[vm.last_index].end_time - vm.last_time) * 1000
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
    Pause() {
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
    goToRest() {
      this.rest = true
      this.add_course = false
      this.real_preview = false
    },
    Submit() {
      var formData = new FormData()
      var courseCover = document.querySelector('input[name ="course_cover"]')
        .files[0]
      formData.append('id', this.course_id)
      formData.append('whole_introduction', this.wholeIntroduction)
      formData.append('Cover_picture', courseCover)
      formData.append('Is_destroy', this.Is_destroy)
      formData.append('distroy_time', this.destroy_time)
      formData.append('price', this.price)
      formData.append('share_rate', this.share_rate)
      formData.append('can_comment', this.can_comment)
      this.$http
        .post(
          'http://192.168.55.33:8000/app/supplement_course_information',
          formData
        )
        .then(response => {
          this.rest = false
          this.finish = true
          this.real_finished = true
          var that = this
          setTimeout(function() {
            that.$router.push({ name: 'backstage' })
          }, 3000)
        })
    },
    Change(b) {
      if (b === true) {
        return 1
      } else {
        return 0
      }
    }
  }
}
</script>
<style>
#go {
  width: 50px;
  height: 30px;
}

#sp {
  width: 90px;
  height: 90px;
}

#pts {
  width: 150px;
  height: 150px;
}

#arrow {
  font-size: 20px;
}

.formitem {
  margin: 15px;
}

.succeed {
  display: table-cell;
  text-align: center;
  vertical-align: middle;
}

.width {
  width: 300px;
}
</style>
