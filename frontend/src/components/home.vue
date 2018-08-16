<template>
 <div id="home">
     <!-- 600px * 400px -->
     <Carousel autoplay height="400px" v-model="value" loop>
        <CarouselItem>
            <div class="demo-carousel"><img src="../assets/1.png"></div>
        </CarouselItem>
        <CarouselItem>
            <div class="demo-carousel"><img src="../assets/2.png"></div>
        </CarouselItem>
        <CarouselItem>
            <div class="demo-carousel"><img src="../assets/3.png"></div>
        </CarouselItem>
        <CarouselItem>
            <div class="demo-carousel"><img src="../assets/4.png"></div>
        </CarouselItem>
    </Carousel>
    <div id="col_bg">
    <Divider id="divider" orientation="left">
        <Poptip trigger="hover" title="免费内容预览" content="点击更多查看所有免费文章。">
        <Button :size="large" icon="md-bookmarks">免费内容</Button>
        </Poptip>
    </Divider>
    <Divider id="divider" orientation="right"><Button id="button" shape="circle">更多</Button></Divider>
    </div>
    <Row>
        <div style="padding: 20px">
        <Card :bordered="false">
            <p slot="title">title</p>
            <p><img src="../assets/logo.png"></p>
        </Card>
        </div>
    </Row>
    <div id="col_bg">
    <Divider id="divider" orientation="left">
        <Poptip trigger="hover" title="付费内容预览" content="点击更多查看所有付费文章。">
        <Button :size="large" icon="md-bookmarks">付费内容</Button>
        </Poptip>
    </Divider>
    <Divider id="divider" orientation="right"><Button id="button" shape="circle">更多</Button></Divider>
    </div>
    <Row>
        <div style="padding: 20px">
        <Card :bordered="false">
            <p slot="title">title</p>
            <p><img src="../assets/logo.png"></p>
        </Card>
        </div>
    </Row>
    <BackTop>
        <div class="top">返回顶端</div>
    </BackTop>
 </div>
</template>
<style scoped>
.id {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
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
  color: #515a6e;
  font-size: 14px;
}
.demo-carousel {
  margin-left: 30%;
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
</style>
