import datetime
<template>
<div>
<h1>添加课程</h1>
<div v-if="start_add"><p>标题：<input v-model="course_title"></p><div>课程简介：<textarea v-model="brief_intro"></textarea></div><button @click="addCourse()">新建课程</button></div>
<div v-if="upload_audi"><h2>上传音频</h2><input type="file" name="audi_upload">
<input type="button" value="上传" @click="AudiUpload()"></div>
<audio controls="controls" v-if="is_show1"  @ended='audioEnded()' id="aud">
  <source v-bind:src="audi" type="audio/mpeg">
</audio>
<div><h2 v-if="first_notice">开始播放音频前，请上传课程的第一张图片</h2>
<h2 v-if="contin">继续上传课程的剩下图片</h2>
<p v-if="upload_pic"><input type="file" name="pic_upload"><button @click="PicUpload()">上传</button></p>
<p v-if="show_pic"><img v-bind:src="pic" id="sp"/></p>
<p><button v-if="set_start_time" @click="setStartTime()">将音频当前播放点设为图片开始时间</button><span v-if="start_time">图片开始时间当前被设置为：{{startTime}}</span></p>
<p v-if="set_end_time"><button @click="setEndTime()">将音频当前播放点设为图片结束时间</button><span v-if="end_time">图片结束时间当前被设置为：{{endTime}}</span></p>
<p v-if="start_time&&end_time&&!preview">当前图片的开始时间与结束时间均已被设置好，确认提交并继续上传下一张图片吗？<button @click="continu()">确认</button></p>
<p v-if="end">音频已播放完，当前图片的结束时间自动被设置为音频的结束时间。</p>
<p v-if="preview">所有图片的起讫时间均已被设置,去预览课程！<button id="go" @click='Preview()'></button></p>
</div>
<div v-if="real_preview">
  <div v-if="show_real_pic" >
    <img v-bind:src="pic_to_show" id="pts"/>
  </div>
  <audio controls="controls" id="audio" @play="Play()" @pause="Pause()" @ended="Ended()">
  <source v-bind:src="audio" type="audio/mpeg">
  </audio>
</div>
</div>
</template>
<script>
export default {
  name: 'addCourse',
  data() {
    return {
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
      last_index: 0
    }
  },
  methods: {
    addCourse() {
      console.log(this.course_title)
      console.log(this.brief_intro)
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/add_course',
          JSON.stringify({
            title: this.course_title,
            brief_intro: this.brief_intro
          })
        )
        .then(response => {
          var res = response.data
          console.log(res)
          this.course_id = res.id
          alert('新建课程成功！去上传课程音频！')
          this.upload_audi = true
          this.start_add = false
        })
    },
    AudiUpload() {
      var formData = new FormData()
      var fileInfo = document.querySelector('input[name ="audi_upload"]')
        .files[0]
      formData.append('file', fileInfo)
      formData.append('course_id', this.course_id)
      this.$http
        .post(this.GLOBAL.serverSrc + '/app/add_audi', formData)
        .then(response => {
          var res = response.data
          console.log(res)
          this.audi = this.GLOBAL.serverSrc + ':8000' + res.audio
          console.log(this.audi)
          this.is_show1 = true
          this.first_notice = true
          this.upload_pic = true
          this.upload_audi = false
          alert(
            '开始播放音频前，请上传课程的第一张图片，并且第一张图片的开始时间默认设为音频起点！'
          )
        })
    },
    PicUpload() {
      var formData = new FormData()
      var fileInfo = document.querySelector('input[name ="pic_upload"]')
        .files[0]
      formData.append('file', fileInfo)
      formData.append('course_id', this.course_id)
      this.$http
        .post(this.GLOBAL.serverSrc + '/app/add_img', formData)
        .then(response => {
          var res = response.data
          console.log(res)
          this.pic = this.GLOBAL.serverSrc + ':8000' + res.course_picture
          console.log(this.pic)
          this.first_notice = false
          this.show_pic = true
          this.upload_pic = false
          alert(
            '图片上传完成，而且新上传的图片的开始时间默认设为音频当前播放点!'
          )
          // this.set_start_time = true
          var au = document.getElementById('aud')
          var st = au.currentTime
          this.set_end_time = true
          this.pic_id = res.id
          this.$http
            .post(
              this.GLOBAL.serverSrc + '/app/set_start_time',
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
    },
    setStartTime() {
      var au = document.getElementById('aud')
      console.log(au.currentTime)
      var st = au.currentTime
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/set_start_time',
          JSON.stringify({
            pic_id: this.pic_id,
            start_time: st
          })
        )
        .then(response => {
          console.log(response.data)
          this.start_time = true
          this.startTime = response.data.start_time
        })
    },
    setEndTime() {
      var au = document.getElementById('aud')
      console.log(au.currentTime)
      var et = au.currentTime
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/set_end_time',
          JSON.stringify({
            pic_id: this.pic_id,
            end_time: et
          })
        )
        .then(response => {
          console.log(response.data)
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
      console.log(au.currentTime)
      var et = au.currentTime
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/set_end_time',
          JSON.stringify({
            pic_id: this.pic_id,
            end_time: et
          })
        )
        .then(response => {
          console.log(response.data)
          this.end_time = true
          this.endTime = response.data.end_time
          this.preview = true
        })
    },
    Preview() {
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/preview',
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
          console.log(response.data)
          this.pictures = response.data.pictures
          this.audio = this.GLOBAL.serverSrc + ':8000' + response.data.course.audio
          this.real_preview = true
          this.show_real_pic = true
          this.last_index = 0
          this.pic_to_show =
            this.GLOBAL.serverSrc + ':8000' + this.pictures[0].course_picture
          console.log(this.pic_to_show)
        })
    },
    Play() {
      var vm = this
      console.log(vm)
      vm.pic_to_show =
        this.GLOBAL.serverSrc + ':8000' + vm.pictures[vm.last_index].course_picture
      var interval = (vm.pictures[vm.last_index].end_time - vm.last_time) * 1000
      vm.st = setTimeout(function() {
        vm.last_index = vm.last_index + 1
        if (vm.last_index === vm.pictures.length) {
          vm.last_index = 0
          vm.last_time = 0
        }
        vm.last_time = vm.pictures[vm.last_index].start_time
        vm.Play()
      }, interval)
    },
    Pause() {
      clearTimeout(this.st)
      this.last_time = document.getElementById('audio').currentTime
    },
    Ended() {
      clearTimeout(this.st)
    }
  }
}
</script>
<style>
#go {
  background-image: 'url(../assets/jiantou.jpg)';
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
</style>
