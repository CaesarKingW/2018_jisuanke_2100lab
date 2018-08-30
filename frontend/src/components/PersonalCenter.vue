<template>
  <div class="PersonalCenter">
    <!-- <Card id="topArea">
      <div id="myCenter">个人中心
      </div>
    </Card> -->

    <div class="dropdown">
    <button class="dropbtn"><div id="dropButtonDiv"><Icon type="ios-person-outline" /> 个人中心</div></button>
    <div class="dropdown-content">
      <ul>
      <router-link to="/home" exact>
            <li class="line">
              <Icon type="ios-home" /> 回到首页
            </li>
          </router-link>
          <router-link to="/PersonalCenter/UserInfo" exact>
            <li class="line">
              <Icon type="ios-contact-outline" /> 个人信息
            </li>
          </router-link>
          <router-link to="/PersonalCenter/ModifyInfo" exact>
            <li class="line">
              <Icon type="ios-hammer-outline" /> 修改信息
            </li>
          </router-link>
          <router-link to="/PersonalCenter/LearntCourse" exact>
            <li class="line">
              <Icon type="md-bookmarks" /> 已学课程
            </li>
          </router-link>
          <router-link to="/PersonalCenter/BoughtCourse" exact>
            <li class="line">
              <Icon type="logo-usd" /> 已购课程
            </li>
          </router-link>
          <router-link to="/PersonalCenter/AccountCancel" exact>
            <li class="line">
              <Icon type="ios-trash-outline" /> 注销账户
            </li>
          </router-link>
          <router-link to="/UserLogin" exact>
            <li @click="logout" class="line">
              <Icon type="ios-log-out" /> 退出登录
            </li>
          </router-link>
          </ul>
    </div>
  </div>
    <!-- <div id="navigation">
      <nav>
        <ul>
          <router-link to="/home" exact>
            <li class="line">
              <Icon type="ios-home" /> 回到首页
            </li>
          </router-link>
          <router-link to="/PersonalCenter/UserInfo" exact>
            <li class="line">
              <Icon type="ios-contact-outline" /> 个人信息
            </li>
          </router-link>
          <router-link to="/PersonalCenter/ModifyInfo" exact>
            <li class="line">
              <Icon type="ios-hammer-outline" /> 修改信息
            </li>
          </router-link>
          <router-link to="/PersonalCenter/LearntCourse" exact>
            <li class="line">
              <Icon type="md-bookmarks" /> 已学课程
            </li>
          </router-link>
          <router-link to="/PersonalCenter/BoughtCourse" exact>
            <li class="line">
              <Icon type="logo-usd" /> 已购课程
            </li>
          </router-link>
          <router-link to="/PersonalCenter/AccountCancel" exact>
            <li class="line">
              <Icon type="ios-trash-outline" /> 注销账户
            </li>
          </router-link>
          <router-link to="/UserLogin" exact>
            <li @click="logout" class="line">
              <Icon type="ios-log-out" /> 退出登录
            </li>
          </router-link>
          <li class="blank"></li>
        </ul>
      </nav>
    </div> -->
    <router-view></router-view>
    <foot />
  </div>
</template>
<script>
export default {
  name: 'home',
  data() {
    return {
      yourname: ''
    }
  },
  created: function() {
    this.Judgestatus()
  },
  mounted: function() {},
  methods: {
    Judgestatus: function() {
      this.$http
        .post('http://192.168.55.33:8000' + '/app/get_status')
        .then(response => {
          var judge = response.data.is_login
          // 用户未登录状态下强制访问，跳出404 not found页面
          // 这里暂时先直接跳入登录页面
          if (!judge) {
            this.$router.push({ name: 'UserLogin' })
          }
        })
    },
    alert_log_out() {
      this.$Message.warning(this.yourname + '已登出')
    },
    logout: function() {
      this.$http
        .post('http://192.168.55.33:8000' + '/app/del_status')
        .then(response => {
          this.judge = response.data.is_login
          if (response.data.username === null) {
            this.yourname = response.data.phonenumber
          } else {
            this.yourname = response.data.username
          }
          location.href = 'http://192.168.55.33:8000' + '#/UserLogin'
          this.alert_log_out()
        })
    }
  }
}
</script>
<style scoped>
#dropButtonDiv {
  margin-left: -6px;
  color: #000;
  font-size: 26px;
  width: 200px;
  font-family: 华文中宋;
  padding: 10px;
}
.dropbtn {
  /* background-color: #022336; */
  color: #000;
  background-color: #fff;
  /* padding: 16px; */
  font-size: 22px;
  border: none;
  cursor: pointer;
  width: 232px;
  height: 72.3px;
  /* margin-left: 20px; */
  text-align: center;
  /* padding: 12px 16px; */
  text-decoration: none;
  display: block;
}

.dropdown {
  /* position: relative; */
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {
  background-color: #f1f1f1;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown:hover .dropbtn {
  background-color: #f1f1f1;
}

/* #topArea {
  background-color: #022336;
  width: 1270px;
  height: 90px;
  border: none;
  border-radius: 0px;
} */

.line {
  /* background-color: #022336; */
  color: #000;
  font-size: 26px;
  width: 200px;
  font-family: 华文中宋;
  padding: 10px;
  list-style: none;
}

/* .line:hover {
  background-color: #073550;
} */

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
