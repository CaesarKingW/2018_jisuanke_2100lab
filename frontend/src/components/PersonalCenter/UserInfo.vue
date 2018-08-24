<template>
    <div id="UserInfo">
        <img id="avatar" src="../../assets/little_avatar.png">
    <div id="nickname_div">{{ nickname }}</div>
    <div id="phone_div">手机号码：{{ phone }}</div>
    <div id="award_div">奖励金数：<Icon type="logo-usd" />{{ award }}</div>
    <router-link to="/ModifyUserInfo"><Button style="margin: 10px;" size="large" type="primary">修改个人信息</Button></router-link>
    <div id="course">
    </div>
    </div>
</template>
