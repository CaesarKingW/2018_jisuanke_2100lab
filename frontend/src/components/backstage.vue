<template>
  <body>
    <header>
      <div >
        <div class="fl">
          <img src="../assets/scienceCaptain.jpg" style="margin-right: 40px;">
        </div>
        <div class="fl" style="text-align: center; font-size: 20px">
          <p>2100实验室后台</p>
        </div>
      </div>
      <div class="fr">
        <div class="fl" style="margin-right: 40px;">
          <p>{{username}},您好！</p>
        </div>
        <div class="fl">
          <p>登出</p>
        </div>
      </div>
    </header>
    <div style="width: 231px; margin-top: 30px">
      <nav>
        <ul>
          <li>课程处理</li>
          <li>留言管理</li>
          <li>用户管理</li>
          <li>订单处理</li>
          <li>数据统计</li>
          <li>权限等级</li>
          <li>后台操作历史查看</li>
        </ul>
      </nav>

    </div>
    <footer></footer>
  </body>
</template>

<script>
export default {
  name: 'backstage',
  data() {
    return {
      username: 'hasaki'
    }
  }
}
</script>

<style scopeds>
.fl {
  float: left;
}

.fr {
  float: right;
}
</style>
