<template>
  <div class="ShowUserInfo">
    <img id="avatar" src="../assets/little_avatar.png">
    <div id="nickname_div">{{ nickname }}</div>
    <div id="phone_div">手机号码：{{ phone }}</div>
    <div id="award_div">奖励金数：<Icon type="logo-usd" />{{ award }}</div>
    <router-link to="/ModifyUserInfo"><Button class="button" size="large" type="primary">修改个人信息</Button></router-link>
    <div id="course">
    <div class="box">
        <Card :bordered="false">
            <p slot="title">已学课程</p>
            <ul class="none">
                <li>实验室制取CO2</li>
            </ul>
        </Card>
    </div>
    <div class="box">
        <Card :bordered="false">
            <p slot="title">已购课程</p>
            <ul class="none">
                <li>自由落体运动</li>
            </ul>
        </Card>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'ShowUserInfo',
  data() {
    return {
      phone: '',
      nickname: '',
      award: 0
    }
  },
  mounted: function() {
    this.$http
      .post(this.GLOBAL.serverSrc + '/app/get_status')
      .then(response => {
        this.phone = response.data.phonenumber
        this.nickname = response.data.username
        this.award = response.data.award
      })
  }
}
</script>
<style scoped>
.ShowUserInfo {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#phone_div,
#award_div {
  font-size: 30px;
  margin: 15px;
}

#nickname_div {
  font-size: 22px;
}

#avatar {
  border: #99ccff solid 5px;
  border-radius: 20px;
  margin: 10px;
}

#learnt,
#bought {
  font-size: 30px;
  margin: 15px;
}

#course {
  font-size: 25px;
}

.box {
  background:#eee;
  padding: 20px;
}

.none{
  list-style:none;
}

.button {
  margin: 10px;
}
</style>
