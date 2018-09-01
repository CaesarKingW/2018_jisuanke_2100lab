<template>
  <div>
    <Tabs value="name1" v-if="all">
      <TabPane label="音画同步" name="name1">
        <div v-if="upload_audi">
          <p>上传音频</p>
          <p>
            <input type="file" name="audi_upload">
            <Button @click="AudiUpload()">上传</Button>
          </p>
        </div>
        <audio controls="controls" v-if="is_show1" id="aud" class="formitem" v-bind:src="audi" @ended="audioEnded()" preload="auto"></audio>
        <div>
          <p v-if="first_notice">开始播放音频前，请上传课程的第一张图片</p>
          <p v-if="contin">继续上传课程的剩下图片</p>
          <p v-if="upload_pic">
            <input type="file" name="pic_upload">
            <button @click="PicUpload()">上传</button>
          </p>
          <div v-if="show_pic"><img v-bind:src="pic" id="sp" /></div>
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
          <div v-if="show_real_pic">
            <img v-bind:src="pic_to_show" id="pts" />
          </div>
          <div>
            <audio controls="controls" id="audio" v-bind:src="audi" @play="Play()" @pause="Pause()" preload="auto">
            </audio>
          </div>
        </div>
      </TabPane>
      <TabPane label="其他" name="name2">
        <Form :model="formItem" :label-width="150">
          <FormItem label="标题">
            <Input v-model="formItem.title" />
          </FormItem>
          <FormItem label="简介">
            <Input v-model="formItem.brief_introduction" type="textarea" />
          </FormItem>
          <FormItem label="详解">
            <Input type="textarea" v-model="formItem.whole_introduction" />
          </FormItem>
          <FormItem label="课程封面：">
            <p>当前：
              <a :href=formItem.oldCP target="_blank">（当前封面）</a>
            </p>
            <p>修改：<input type=file id="newCP" /></p>
          </FormItem>
          <FormItem label="是否阅后即焚:">
            <i-switch v-model="formItem.Is_destroy"></i-switch>
          </FormItem>
          <FormItem label="可阅时长：" v-if="this.formItem.Is_destroy">
            <InputNumber v-model="formItem.distroy_time" />小时</FormItem>
          <FormItem label="价格">
            <InputNumber v-model="formItem.price" />元</FormItem>
          <FormItem label="分销比例" v-if="formItem.price>0">
            <InputNumber :max="100" v-model="formItem.share_rate" :formatter="value => `${value}%`" :parser="value => value.replace('%', '')" />
          </FormItem>
          <FormItem label="允许用户留言">
            <i-switch v-model="formItem.can_comment"></i-switch>
          </FormItem>
          <FormItem>
            <Button type="primary" @click="save_modify()">保存修改</Button>
          </FormItem>
        </Form>
      </TabPane>
    </Tabs>
    <div v-if="finish">第{{id}}号课程编辑成功！</div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      id: null,
      all: true,
      upload_audi: true,
      if_show1: false,
      first_notice: false,
      contin: false,
      upload_pic: false,
      show_pic: false,
      pic: null,
      set_start_time: false,
      start_time: false,
      startTime: null,
      set_end_time: false,
      end_time: false,
      endTime: null,
      end: false,
      preview: false,
      real_preview: false,
      pic_to_show: null,
      audi: null,
      count: 0,
      finish: false,
      formItem: {
        title: '',
        brief_introduction: '',
        oldCP: '',
        Is_destroy: null,
        distroy_time: null,
        price: null,
        share_rate: null,
        can_comment: null,
        whole_introduction: ''
      }
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
          } else {
            this.id = this.$route.params.id
            this.$http
              .post(
                'http://192.168.55.33:8000/app/search_one_course',
                JSON.stringify(this.id)
              )
              .then(response => {
                var res = response.data
                this.formItem.title = res.course['title']
                this.formItem.brief_introduction =
                  res.course['brief_introduction']
                this.formItem.oldCP =
                  'http://192.168.55.33:8000' + res.course['Cover_picture']
                this.formItem.whole_introduction =
                  res.course['whole_introduction']
                this.formItem.Is_destroy = res.course['Is_destroy']
                this.formItem.distroy_time = res.course['distory_time']
                this.formItem.price = res.course['price']
                this.formItem.share_rate = res.course['share_rate'] * 100
                this.formItem.can_comment = res.course['can_comment']
              })
          }
        }
      })
  },
  methods: {
    AudiUpload() {
      var formData = new FormData()
      var str = document.querySelector('input[name ="audi_upload"]').value
      if (str.indexOf('.mp3') < 0 && str.indexOf('.MP3') < 0) {
        alert('文件类型不正确！请上传.mp3、.MP3类型的文件！')
      } else {
        var fileInfo = document.querySelector('input[name="audi_upload"]')
          .files[0]
        formData.append('file', fileInfo)
        formData.append('course_id', this.id)
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
      this.count = this.count + 1
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
        formData.append('course_id', this.id)
        formData.append('duration', duration)
        formData.append('count', this.count)
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
            course_id: this.id
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
    save_modify() {
      var formData = new FormData()
      formData.append('id', this.id)
      formData.append('title', this.formItem.title)
      formData.append('brief_introduction', this.formItem.brief_introduction)
      formData.append('whole_introduction', this.formItem.whole_introduction)
      formData.append(
        'Cover_picture',
        document.getElementById('newCP').files[0]
      )
      formData.append('Is_destroy', this.formItem.Is_destroy)
      if (this.formItem.Is_destroy === true) {
        formData.append('distroy_time', this.formItem.distroy_time)
      }
      formData.append('price', this.formItem.price)
      if (this.formItem.price > 0) {
        formData.append('share_rate', this.formItem.share_rate)
      }
      formData.append('can_comment', this.formItem.can_comment)
      this.$http
        .post('http://192.168.55.33:8000/app/editCourse', formData)
        .then(response => {
          this.all = false
          var that = this
          that.finish = true
          setTimeout(function() {
            that.$router.push({ name: 'backstage' })
          }, 3000)
        })
    }
  }
}
</script>
