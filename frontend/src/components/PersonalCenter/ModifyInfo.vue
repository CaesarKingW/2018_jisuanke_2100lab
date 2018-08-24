<template>
<div id="ModifyInfo">
    <img id="avatar" v-bind:src="path" class="imgDiv" /><img>
    <div>
      <input type='file' name='head' id='head' style="display:none" accept="image/*" v-on:change="Upload_head"/>
      <input id="upload_button" type='button' value='修改头像' v-on:click="click_file">
    </div>
    <div>
      <h1 id="nickname">昵称：{{oldname}}</h1>
        <form @submit.prevent="modify_nickname">
            <input id="upload_button" type="text" v-model="nickname">
            <br>
            <input id="upload_button" type="submit" value="确认修改"/>
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
      default_avator: require('../../assets/little_avatar.png'),
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
          'http://192.168.55.33:8000/app/get_old_avator',
          JSON.stringify(this.user_phone)
        )
        .then(response => {
          this.oldpath = response.data.oldpath[0].fields.head_protrait
          this.oldname = response.data.oldpath[0].fields.user_name
          console.log(this.oldname)
          console.log(this.oldpath)
          if (this.oldpath === '') {
            this.path = this.default_avator
          } else {
            this.path = 'http://192.168.55.33:8000/media/' + this.oldpath
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
        .post('http://192.168.55.33:8000/app/update_avator', formdate, config)
        .then(response => {
          console.log(response.data)
        })

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
          'http://192.168.55.33:8000/app/update_nickname',
          JSON.stringify({
            phone_number: this.user_phone,
            nickname: this.nickname
          })
        )
        .then(
          response => {
            console.log(response.date)
            console.log('success')
            this.get_old_avator()
            this.nickname = ''
          },
          response => {
            console.log('error')
          }
        )
    }
  }
}
</script>

<style scoped>
#ModifyInfo {
  float: left;
}
#nickname {
  width: 120px;
  height: 40px;
  margin: 30px;
  margin-left: 300px;
}
#avatar {
  border: #666666 solid 1px;
  border-radius: 8px;
  width: 120px;
  height: 120px;
  margin: 30px;
  margin-left: 300px;
}
#upload_button {
  width: 120px;
  height: 40px;
  font-size: 20px;
  margin-left: 300px;
  outline: none;
  border-radius: 4px;
  border: #666666 solid 1px;
  background-color: #fff;
  cursor: pointer;
  text-align: center;
}
#upload_button:hover {
  background: rgb(245, 242, 242);
  cursor: pointer;
}
</style>
