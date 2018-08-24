<template>
    <div class="PersonalCenter">
        <Card id="top_area">
            <div>
                <Divider id="MyCenter">个人中心</Divider>
            </div>
        </Card>
        <div id="navigation">
        <nav>
        <ul>
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
          <li class="blank"></li>
        </ul>
      </nav>
        </div>
      <router-view></router-view>
      <foot />
    </div>
</template>
<style scoped>
#top_area {
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
#MyCenter {
  text-align: center;
  font-size: 28px;
  font-family: 华文中宋;
  color: #fff;
}
</style>
