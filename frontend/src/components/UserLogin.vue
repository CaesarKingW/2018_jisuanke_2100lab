<template>
<div id="UserLogin">
    <!-- <span href="#" class="button" id="toggle-login">2100-LAB</span> -->
    <div id="triangle"></div>
    <h1>2100实验室</h1>
    <br>
    <h1>登录</h1>
    <form>
    <input type="phone" placeholder="手机号码" />
    <input type="id_code" placeholder="验证码" />
    <div><input type="submit" value="获取验证码" /></div>
    <div><input type="submit" value="登录" /></div>
    </form>
</div>
</template>
<style scoped>
#log_column {
  text-align: center;
}
.button{
  width:100px;
  background:#3399cc;
  display:block;
  margin:0 auto;
  margin-top:1%;
  padding:10px;
  text-align:center;
  text-decoration:none;
  color:#fff;
  cursor:pointer;
  transition:background .3s;
  -webkit-transition:background .3s;
}
.button:hover{
  background:#2288bb;
}
#UserLogin{
  width:400px;
  margin:0 auto;
  margin-top:8px;
  margin-bottom:2%;
  transition:opacity 1s;
  -webkit-transition:opacity 1s;
}
#triangle{
  width:0;
  border-top:12x solid transparent;
  border-right:12px solid transparent;
  border-bottom:12px solid #3399cc;
  border-left:12px solid transparent;
  margin:0 auto;
}
#UserLogin h1{
  background:#3399cc;
  padding:20px 0;
  font-size:140%;
  font-weight:300;
  text-align:center;
  color:#fff;
}
form{
  background:#f0f0f0;
  padding:6% 4%;
}
input[type="phone"],input[type="id_code"]{
  width:92%;
  background:#fff;
  margin-bottom:4%;
  border:1px solid #ccc;
  padding:4%;
  font-family:'Open Sans',sans-serif;
  font-size:95%;
  color:#555;
}
input[type="submit"]{
  margin-top: 1%;
  width:100%;
  background:#3399cc;
  border:0;
  padding:4%;
  font-family:'Open Sans',sans-serif;
  font-size:100%;
  color:#fff;
  cursor:pointer;
  transition:background .3s;
  -webkit-transition:background .3s;
}
input[type="submit"]:hover{
  background:#2288bb;
}
</style>
