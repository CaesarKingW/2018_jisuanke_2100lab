<template>
<div class="ShowUserInfo">
    <img id="avatar" src="../assets/little_avatar.png">
    <div id="nickname_div">{{ nickname }}</div>
    <div id="phone_div">手机号码：{{ phone }}</div>
    <div id="award_div">奖励金数：<Icon type="logo-usd" />{{ award }}</div>
    <Button style="margin: 10px;" size="large" type="primary">修改个人信息</Button>
    <div id="course">
    <div style="background:#eee;padding: 20px">
        <Card :bordered="false">
            <p slot="title">已学课程</p>
            <ul style="list-style:none;">
                <li>实验室制取CO2</li>
            </ul>
        </Card>
    </div>
    <div style="background:#eee; padding: 20px">
        <Card :bordered="false">
            <p slot="title">已购课程</p>
            <ul style="list-style:none;">
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
      phone: '15009253698',
      nickname: '2100实验室用户',
      award: 10
    }
  }
}
</script>
<style scoped>
.ShowUserInfo {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#phone_div, #award_div {
    font-size: 30px;
    margin: 15px;
}
#nickname_div {
    font-size: 22px;
}
#avatar {
    border:#99ccff solid 5px;
    border-radius: 20px;
    margin: 10px;
}
#learnt, #bought {
    font-size: 30px;
    margin: 15px;
}
#course {
    font-size: 25px;
}
</style>
