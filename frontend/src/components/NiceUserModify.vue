<template>
<div id="useModify">
    <img  id="avatar" v-bind:src="path" class="imgDiv" /><img>
    <input type='file' name='head' id='head' style="display:none" accept="image/*" v-on:change="Upload_head"/>
    <div><input id="upload_button" type='button' value='上传头像' v-on:click="click_file"></div>
</div>
</template>
<script>
export default {
  data() {
    return {
      // 应该为获取当前用户的头像，无头像则为一张默认头像，现暂设为一张默认图片
      path: require('../assets/little_avatar.png'),
      // 应为当前登录用户的手机号，现暂时设置为一名已存在的用户的手机号
      user_phone: '17602284691'
    }
  },
  methods: {
    click_file: function() {
      document.getElementById('head').click()
    },
    Upload_head: function(e) {
      // 上传当前手机号到后端
      this.$http.post(
        this.GLOBAL.serverSrc + 'app/get_user_phone',
        JSON.stringify({ user_phone: this.user_phone })
      )

      // 上传图片到后端
      var formdate = new FormData()
      var fileinfo = document.querySelector('input[type=file]').files[0]
      // event.targer.files[0];//t.target.file["0"]
      formdate.append('file', fileinfo)
      let config = { headers: { 'Content-Type': 'multipart/form-data' } }
      this.$http
        .post(this.GLOBAL.serverSrc + 'app/update_avator', formdate, config)
        .then(response => {
          console.log(response.data)
          // var resultobj = response.data
          // this.result = resultobj.msg
        })

      //  前端读取图片进行预览
      let _this = this
      //   _this.imgObj = e.target.files['0']
      let fr = new FileReader()
      fr.onload = function() {
        _this.path = fr.result
      }
      fr.readAsDataURL(fileinfo)
    }
  }
}
</script>
<style scoped>
#useModify {
  text-align: center;
}
#avatar {
  border: #666666 solid 1px;
  border-radius: 8px;
  width: 170px;
  height: 170px;
  margin: 30px;
}
#upload_button {
  width: 170px;
  height: 40px;
  font-size: 20px;
  margin-top: 10px;
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
