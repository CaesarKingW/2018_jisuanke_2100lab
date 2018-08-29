<template>
<div class="ReadAndBurn">
    <img src="../assets/flame.png">
    <h1>您查看的内容已经被焚毁了哦(´∩ω∩｀)</h1>
    <router-link to="/home">
    <Button id="backHome"><Icon type="ios-home" size=20 /> 回到主页</Button>
    </router-link>
</div>
</template>
<style>
#backHome {
  width: 120px;
  height: 40px;
  font-size: 16px;
  border: #000 solid 1px;
}
#backHome:hover {
  border: rgba(0, 0, 0, 0.459) solid 1px;
  color: #ff9966;
}
.ReadAndBurn {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 50px;
}

.ReadAndBurn h1 {
  color: #ff9966;
  font-size: 40px;
  margin: 20px;
  font-family: 幼圆;
}
.navibar {
  z-index: 9999;
  background-color: #fff;
  position: fixed;
  width: 100%;
  opacity: 0.9;
  padding: 25px;
}
.navi {
  font-size: 18px;
  color: #022336;
  margin-left: 15px;
  margin-right: 15px;
}
</style>
