<template>
    <div class="PersonalCenter">
        <Card id="topArea">
            <div>
                <Divider id="myCenter">个人中心</Divider>
            </div>
        </Card>
        <div id="navigation">
        <nav>
        <ul>
          <router-link to ="/home" exact>
          <li class="line">
              <Icon type="ios-home" /> 回到首页
        </li>
              </router-link>
          <router-link to ="/PersonalCenter/UserInfo" exact>
          <li class="line">
              <Icon type="ios-contact-outline" /> 个人信息
        </li>
              </router-link>
          <router-link to ="/PersonalCenter/ModifyInfo" exact>
          <li class="line">
              <Icon type="ios-hammer-outline" /> 修改信息
        </li>
              </router-link>
          <router-link to ="/PersonalCenter/LearntCourse" exact>
          <li class="line">
              <Icon type="md-bookmarks" /> 已学课程
        </li>
              </router-link>
          <router-link to ="/PersonalCenter/BoughtCourse" exact>
          <li class="line">
              <Icon type="logo-usd" /> 已购课程
        </li>
        </router-link>
          <router-link to ="/PersonalCenter/AccountCancel" exact>
          <li class="line">
              <Icon type="ios-trash-outline" /> 注销账户
        </li>
        </router-link>
        <router-link to ="/UserLogin" exact>
          <li  @click="logout" v-if="judge" class="line">
              <Icon type="ios-log-out" /> 退出登录
        </li>
        </router-link>
          <li class="blank"></li>
        </ul>
      </nav>
        </div>
      <router-view></router-view>
      <foot />
    </div>
</template>
<script>
export default {
  name: 'home',
  data() {
    return {
      value: 0,
      imgs: [],
      free_course: [],
      paying_imgs: [],
      paying_course: [],
      show_number: 3,
      path: [],
      judge: false,
      yourname: ''
    }
  },
  mounted: function() {
    this.show_free_course()
    this.show_paying_course()
    this.Judgestatus()
  },
  methods: {
    show_free_course: function() {
      this.$http.get('http://192.168.55.33:8000/app/show_free_course').then(
        response => {
          this.imgs = response.data.list
          console.log('success')
          for (var i = 0; i < this.imgs.length; i = i + 1) {
            var a =
              'http://192.168.55.33:8000/media/' +
              this.imgs[i].fields.Cover_picture
            this.imgs[i].fields.Cover_picture = a
          }
          var length = 0
          if (this.imgs.length > this.show_number) length = this.show_number
          else length = this.imgs.length
          this.free_course = this.imgs.slice(0, length)
          console.log('success')
        },
        response => {
          console.log('error')
        }
      )
    },
    show_paying_course: function() {
      this.$http.get('http://192.168.55.33:8000/app/show_paying_course').then(
        response => {
          this.paying_imgs = response.data.list
          console.log('success')
          for (var i = 0; i < this.paying_imgs.length; i = i + 1) {
            var a =
              'http://192.168.55.33:8000/media/' +
              this.paying_imgs[i].fields.Cover_picture
            this.paying_imgs[i].fields.Cover_picture = a
          }
          var length = 0
          if (this.paying_imgs.length > this.show_number) {
            length = this.show_number
          } else length = this.paying_imgs.length
          this.paying_course = this.paying_imgs.slice(0, length)
          console.log('success')
        },
        response => {
          console.log('error')
        }
      )
    },
    Judgestatus: function() {
      this.$http
        .post('http://192.168.55.33:8000/app/get_status')
        .then(response => {
          this.judge = response.data.is_login
        })
    },
    alert_log_out() {
      this.$Message.warning(this.yourname + '已登出')
    },
    logout: function() {
      this.$http
        .post('http://192.168.55.33:8000/app/del_status')
        .then(response => {
          this.judge = response.data.is_login
          if (response.data.username === null) {
            this.yourname = response.data.phonenumber
          } else {
            this.yourname = response.data.username
          }
          location.href = 'http://192.168.55.33:8000/#/UserLogin'
          this.alert_log_out()
        })
    }
  }
}
</script>
<style scoped>
#topArea {
  background-color: #022336;
  width: 1270px;
  height: 90px;
  border: none;
  border-radius: 0px;
}
.line {
  background-color: #022336;
  color: #fff;
  font-size: 26px;
  width: 200px;
  font-family: 华文中宋;
  padding: 10px;
}
.line:hover {
  background-color: #073550;
}
.blank {
  background-color: #022336;
  width: 200px;
  height: 600px;
  font-family: 华文中宋;
  padding: 10px;
}
#navigation {
  float: left;
}
#myCenter {
  text-align: center;
  font-size: 28px;
  font-family: 华文中宋;
  color: #fff;
}
</style>
