<template>
  <div id="ModifyInfo">
    <img id="avatar" v-bind:src="path" class="imgDiv" /><img>
    <div>
      <input type='file' name='head' id='head' class="none" accept="image/*" v-on:change="Upload_head" />
      <input id="avatarUploadButton" type='button' value='修改头像' v-on:click="click_file">
    </div>
    <div>
      <div id="nickname">当前昵称：<br>{{oldname}}</div>
      <form @submit.prevent="modify_nickname">
        <div>
          <Input id="nameUploadText" type="text" v-model="nickname" />
        </div>
        <div><input id="nameUploadButton" type="submit" value="确认修改" /></div>
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
      user_phone: '',
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
      this.$http.post(this.GLOBAL.serverSrc + '/app/get_status').then(
        response => {
          var obj = []
          obj = response.data.list
          this.oldpath = obj[0].fields.head_protrait
          this.user_phone = obj[0].pk
          this.oldname = obj[0].fields.user_name
          if (this.oldpath === '') {
            this.path = this.default_avator
          } else {
            this.path = this.GLOBAL.serverSrc + '/media/' + this.oldpath
            this.oldpath = ''
          }
        },
        response => {}
      )
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
      let config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      this.$http
        .post(this.GLOBAL.serverSrc + '/app/update_avator', formdate, config)
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
        this.$Message.warning(
          '昵称修改失败！注意:昵称只能使用汉字、字母和数字哦！'
        )
        return 0
      } else {
        this.$Message.success('恭喜您，昵称修改成功！')
      }
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/update_nickname',
          JSON.stringify({
            phone_number: this.user_phone,
            nickname: this.nickname
          })
        )
        .then(
          response => {
            this.get_old_avator()
            this.nickname = ''
          },
          response => {}
        )
    }
  }
}
</script>

<style scoped>
#nameUploadText {
  width: 120px;
  margin-left: 100px;
}

#ModifyInfo {
  float: left;
}

#nickname {
  margin-top: 5px;
  margin-left: 100px;
  font-family: 华文中宋;
  font-size: 20px;
}

#avatar {
  width: 120px;
  height: 120px;
  margin: 30px;
  margin-left: 100px;
  border: #666 solid 1px;
  border-radius: 8px;
}

#avatarUploadButton {
  width: 120px;
  height: 40px;
  font-size: 20px;
  margin-left: 100px;
  outline: none;
  border-radius: 4px;
  border: #666666 solid 1px;
  background-color: #fff;
  cursor: pointer;
  text-align: center;
}

#avatarUploadButton:hover {
  cursor: pointer;
  background: rgb(245, 242, 242);
}

#nameUploadButton {
  width: 120px;
  height: 40px;
  font-size: 20px;
  margin-left: 100px;
  margin-top: 30px;
  outline: none;
  border-radius: 4px;
  border: #666666 solid 1px;
  background-color: #fff;
  cursor: pointer;
  text-align: center;
}

#nameUploadButton:hover {
  cursor: pointer;
  background: rgb(245, 242, 242);
}

.none {
  display: none;
}
</style>
