<template>
<div class="FreeCourseIntro">
        <span><img id="test_pic" src="../assets/1.png"></span>
        <span><h1 id="courseTitle">标题：{{ courseTitle }}</h1></span>
        <router-link to="/CourseShow"><Button id="enter" icon="md-eye" type="primary">进入课程</Button></router-link>
        <Button @click="modal = true" id="share" icon="md-share" type="primary">分享课程</Button>
        <Modal
        title="分享课程"
        v-model="modal"
        class-name="vertical-center-modal">
        <div style="text-align: center;padding:10px;"><span id="thisURL">本页地址：{{ message }}</span>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <button id="copy_button" type="button"
        v-clipboard:copy="message"
        v-clipboard:success="onCopy"
        v-clipboard:error="onError">复制</button>
        </div>
    </Modal>
        <Alert id="tip" show-icon>
        <Icon type="ios-bulb-outline" slot="icon"></Icon>
        <template slot="desc">如果你喜欢本课程，就把它分享给朋友吧！ </template>
    </Alert>
    <div id="intro"><Collapse v-model="value">
        <Panel id="intro" name="1" style="font-size: 25px;">
            课程简介
            <p slot="content">
                <ul style="font-size: 18px; list-style:none;">
                    <li>1.实验室制取二氧化碳，用大理石或石灰石与稀盐酸反应，它们的主要成分为碳酸钙，生成物有氯化钙、水和二氧化碳，方程式为：CaCO3+2HCl═CaCl2+H2O+CO2↑。</li>
                    <li>2.二氧化碳能溶于水，与水反应生成碳酸，不能用排水法收集，由于密度比空气大，可用向上排空气法收集。</li>
                    <li>3.检验二氧化碳时，利用二氧化碳与氢氧化钙反应生成碳酸钙沉淀的性质，方法是把制取的气体通入澄清的石灰水，如石灰水变浑，则气体是二氧化碳。</li>
                </ul>
                </p>
        </Panel>
    </Collapse></div>
    <br>
</div>
</template>
<script>
export default {
  name: 'FreeCourseIntro',
  data() {
    return {
      courseTitle: '实验室制取CO2',
      split1: 0.49,
      modal: false,
      message: window.location.href
    }
  }
}
</script>
<style>
.FreeCourseIntro {
  height: 480px;
  border: 1px solid #dcdee2;
  background-color: #c4e1ff;
}
.demo-split-pane {
  padding: 10px;
}
#test_pic {
    border:#99ccff solid 5px;
    position: absolute;
    left: 2%;
    top: 8%;
    border-radius: 20px;
}
#courseTitle {
    text-align: center;
    position: absolute;
    right: 8%;
    text-align: center;
    top: 20%;
    font-size: 3em;
    padding: 8px 50px;
    border: #99cccc dotted 3px;
}
#enter {
    width: 170px;
    height: 60px;
    text-align: center;
    position: absolute;
    right: 20%;
    top: 40%;
    font-size: 2em;
}
#share {
    width: 170px;
    height: 60px;
    text-align: center;
    position: absolute;
    right: 20%;
    top: 58%;
    font-size: 2em;
}
#tip {
    width: auto;
    height: 40px;
    text-align: center;
    position: absolute;
    right: 14%;
    top: 75%;
}
.vertical-center-modal{
    display: flex;
    align-items: center;
    justify-content: center;
}
.ivu-modal{
    top: 0;
}
#intro {
    position: absolute;
    top: 84%;
    width : 100%;
    list-style:none;
}
#copy_button {
    width: 50px;
    height:25px;
    margin-top:10px;
    outline:none;
    border-radius: 4px;
    border: none;
    background-color: #2d8cf0;
    color:#fff;
    cursor: pointer;
}
#copy_button:hover {
    background: #57a3f3;
}
</style>
