<template>
  <div id="useModify">
    <div>
      <img v-bind:src="path" class="imgDiv" /><img>
      <input type='file' name='head' id='head' class="none" accept="image/*" v-on:change="Upload_head" />
      <input type='button' value='上传头像' v-on:click="click_file">
    </div>
    <div>
      昵称：{{oldname}}
      <form @submit.prevent="modify_nickname">
        <input type="text" v-model="nickname">
        <input type="submit" value="确认修改" />
      </form>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      // 应该为获取当前用户的头像，无头像则为一张默认头像，现暂设为一张默认图片
      path: '',
      default_avator: require('../assets/little_avatar.png'),
      // 应为当前登录用户的手机号，现暂时设置为一名已存在的用户的手机号
      user_phone: '17602284691',
      nickname: '',
      oldname: '',
      oldpath: ''
    }
  },
  mounted: function() {
    this.get_old_avator()
  },
  methods: {
    get_old_avator: function() {
      this.$http
        .post(
          'http://192.168.55.33:8000' + '/app/get_old_avator',
          JSON.stringify(this.user_phone)
        )
        .then(response => {
          this.oldpath = response.data.oldpath[0].fields.head_protrait
          this.oldname = response.data.oldpath[0].fields.user_name
          if (this.oldpath === '') {
            this.path = this.default_avator
          } else {
            this.path = 'http://192.168.55.33:8000' + '/media/' + this.oldpath
            this.oldpath = ''
          }
        })
    },
    click_file: function() {
      document.getElementById('head').click()
    },
    Upload_head: function(e) {
      // 上传图片到后端
      var formdate = new FormData()
      var fileinfo = document.querySelector('input[type=file]').files[0]
      // 获取上传的第一份文件event.targer.files[0];//t.target.file["0"]
      formdate.append('file', fileinfo)
      formdate.append('user_phone', this.user_phone)
      let config = { headers: { 'Content-Type': 'multipart/form-data' } }
      this.$http
        .post('http://192.168.55.33:8000' + '/app/update_avator', formdate, config)
        .then(response => {})

      //  前端读取图片进行预览
      let _this = this
      let fr = new FileReader()
      fr.onload = function() {
        _this.path = fr.result
      }
      fr.readAsDataURL(fileinfo)
    },
    modify_nickname: function() {
      // 判断输入的昵称是否符合规范
      var nickname = this.nickname
      if (!nickname.match(/^[(\u4e00-\u9fa5)|(0-9)|(A-Z|(a-z))]+$/)) {
        alert('只能含有汉字字母和数字')
        return 0
      } else {
        alert('昵称符合规范')
      }
      this.$http
        .post(
          'http://192.168.55.33:8000' + '/app/update_nickname',
          JSON.stringify({
            phone_number: this.user_phone,
            nickname: this.nickname
          })
        )
        .then(
          response => {
            this.get_old_avator()
          },
          response => {}
        )
    }
  }
}
</script>

<style scoped>
.none {
  display: none;
}
</style>
