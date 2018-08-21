<template>
 <div id="home">
     <router-link to="/home">
     <Button type="primary" id="lab">2100-lab</Button>
     </router-link>
     <router-link to="/UserLogin">
     <Button type="primary" id="log_but">用户登录</Button>
     </router-link>
     <Divider />
     <br>
     <!-- 600px * 400px -->
     <div align="center">
     <Carousel autoplay height="400px" v-model="value" loop>
        <CarouselItem>
            <div class="demo-carousel"><img class="roll_pic" src="../assets/1.png"></div>
        </CarouselItem>
        <CarouselItem>
            <div class="demo-carousel"><img class="roll_pic" src="../assets/2.png"></div>
        </CarouselItem>
        <CarouselItem>
            <div class="demo-carousel"><img class="roll_pic" src="../assets/3.png"></div>
        </CarouselItem>
        <CarouselItem>
            <div class="demo-carousel"><img class="roll_pic" src="../assets/4.png"></div>
        </CarouselItem>
    </Carousel>
    </div>
    <div id="col_bg">
    <Divider id="divider" orientation="left">
        <Poptip trigger="hover" title="免费内容预览" content="点击更多查看所有免费文章。">
        <div class="myContent"><Alert style="font-size: 20px;text-align: center;"><Icon type="md-bookmarks" />&nbsp;免费内容</Alert></div>
        </Poptip>
    </Divider>
    <Divider id="divider" orientation="right"><Button id="button" shape="circle">更多</Button></Divider>
    </div>
    <Row>
        <div style="padding: 20px;">
        <Card :bordered="false">
            <p style="text-align:center;" class="album_title" slot="title">{{ free_title1 }}</p>
            <p style="text-align:center;"><img class="album" src="../assets/album_1.png"></p>
        </Card>
        </div>
        <div style="padding: 20px;">
        <Card :bordered="false">
            <p style="text-align:center;" class="album_title" slot="title">{{ free_title2 }}</p>
            <p style="text-align:center;"><img class="album" src="../assets/album_2.png"></p>
        </Card>
        </div>
    </Row>
    <br>
    <div id="col_bg">
    <Divider id="divider" orientation="left">
        <Poptip trigger="hover" title="付费内容预览" content="点击更多查看所有付费文章。">
        <div class="myContent"><Alert style="font-size: 20px;text-align: center;"><Icon type="logo-usd" />&nbsp;付费内容</Alert></div>
        </Poptip>
    </Divider>
    <Divider id="divider" orientation="right"><Button id="button" shape="circle">更多</Button></Divider>
    </div>
    <Row>
        <div style="padding: 20px;">
        <Card :bordered="false">
            <p style="text-align:center;" class="album_title" slot="title">{{ pay_title1 }}</p>
            <p style="text-align:center;"><img class="album" src="../assets/album_3.png"></p>
        </Card>
        </div>
        <div style="padding: 20px;">
        <Card :bordered="false">
            <p style="text-align:center;" class="album_title" slot="title">{{ pay_title2 }}</p>
            <p style="text-align:center;"><img class="album" src="../assets/album_4.png"></p>
        </Card>
        </div>
    </Row>
    <BackTop>
        <div class="top">返回顶端</div>
    </BackTop>
 </div>
</template>
<script>
export default {
  name: 'home',
  data() {
    return {
      free_title1: '季节是怎么形成的',
      free_title2: '谁住在壳里',
      pay_title1: '夜行性动物住在哪儿',
      pay_title2: '如果我们不睡觉'
    }
  }
}
</script>

<style scoped>
.id {
  font-family:
    "Helvetica Neue",
    Helvetica,
    "PingFang SC",
    "Hiragino Sans GB",
    "Microsoft YaHei",
    "微软雅黑",
    Arial,
    sans-serif;
}

.content-text {
  margin-left: 10%;
}

.more {
  margin-left: 65%;
}

.content {
  width: 80%;
  height: 20%;
}

#button {
  font-size: 14px;
  color: #515a6e;
}

#col_bg {
  background-color: #0072e3;
}
.top {
  padding: 10px;
  background: rgba(0, 153, 229, 0.7);
  color: #fff;
  text-align: center;
  border-radius: 2px;
}
#log_but {
  margin-left: 90%;
  float: left;
}
#lab {
  margin-left: 15%;
  font-size: 18px;
  float: left;
}
.roll_pic {
    border:#99ccff solid 5px;
    border-radius: 20px;
}
.myContent {
    font-size: 63px;
}
.album {
    border:#99ccff solid 5px;
    border-radius: 20px;
}
.album_title {
    font-size: 20px;
}
</style>
