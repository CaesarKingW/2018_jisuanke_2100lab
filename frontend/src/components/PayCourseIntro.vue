<template>
<div class="PayCourseIntro">
        <span><img id="test_pic" src="../assets/2.png"></span>
        <span><h1 id="courseTitle">标题：{{ courseTitle }}</h1></span>
        <Button @click="alipay()" id="buy" icon="logo-usd" type="primary">购买课程</Button>
        <Button @click="modal = true" id="share" icon="ios-card" type="primary">分销课程</Button>
        <Modal
        title="分销课程"
        v-model="modal"
        class-name="vertical-center-modal">
        <div style="text-align: center; padding:10px;"><span id="thisURL">本页地址：{{ message }}</span>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <button id="copy_button" type="button"
        v-clipboard:copy="message"
        v-clipboard:success="onCopy"
        v-clipboard:error="onError">复制</button>
        </div>
    </Modal>
        <Alert id="tip" show-icon>
        <Icon type="ios-trophy-outline" slot="icon"></Icon>
        <template slot="desc">分销本课程，还可额外获得{{ award }}枚奖励币哦！ </template>
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
  name: 'PayCourseInfo',
  data() {
    return {
      courseTitle: '实验室制取CO2',
      split1: 0.49,
      modal: false,
      message: window.location.href,
      award: 10,
      orderid: '',
      price: 100,
      courseid: '1',
      username: '11'
    }
  },
  methods: {
    alipay() {
      // location.href='https://openapi.alipaydev.com/gateway.do?app_id=2016091800536766&biz_content=%7B%22subject%22%3A%22%5Cu6d4b%5Cu8bd5%5Cu8ba2%5Cu5355%22%2C%22out_trade_no%22%3A%2220170233021223%22%2C%22total_amount%22%3A100%2C%22product_code%22%3A%22FAST_INSTANT_TRADE_PAY%22%7D&charset=utf-8&method=alipay.trade.page.pay&notify_url=http%3A%2F%2Fprojectsedus.com%2F&return_url=http%3A%2F%2F192.168.55.33%3A8000%2F%23%2FPayCourseIntro&sign_type=RSA2&timestamp=2018-08-23+14%3A42%3A49&version=1.0&sign=vBgAxnq%2BicQ7yn9rEi5fDU7HRelUyLYRjHdOBd8OvWJTkSvNkCR50TTJjf6LNJSPQCbe5eMQw0r7CC8gP6ow%2Bh0NfeBehkkZkK9VrYPRG4n2cWSk%2B4Gu4Rytjm1FwrW0I%2BYV5cVbm9Zqew5ltQRiFfkjp8RBSuNKsLDl3VwYKkYNgPxJkWsI2SKSfdvs76mZNSPxBJd3ZFKkcX6vShn3H0W27BanKGZV0L%2F2T2uTgPsbNnfoeUFmxwSLMYXcmqirK57lfnf9uhOMbCofqfSBkTjVhq%2FDSTmHajph8oSxRwGpkd55cyCwLgzGSiKmL8Unx1RcMR3Tth3u2ILC8YVIdw%3D%3D'
      var code = ''
      var codeLength = 16
      var random = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      for (var i = 0; i < codeLength; i++) {
        var index = Math.floor(Math.random() * 9)
        code += random[index]
      }
      this.orderid = code
      var request = {}
      request.orderid = this.orderid
      request.courseid = this.courseid
      request.username = this.username
      console.log(request)
      request = JSON.stringify(request)
      this.$http
        .post('http://192.168.55.33:8000/app/payment', request)
        .then(response => {
          console.log(response.data)
          window.location.href = response.data
        })
    }
  }
}
</script>
<style>
.PayCourseIntro {
  height: 480px;
  border: 1px solid #dcdee2;
  background-color: #c4e1ff;
}
.demo-split-pane {
  padding: 10px;
}
#test_pic {
  border: #99ccff solid 5px;
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
#buy {
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
.vertical-center-modal {
  display: flex;
  align-items: center;
  justify-content: center;
}
.ivu-modal {
  top: 0;
}
#intro {
  position: absolute;
  top: 84%;
  width: 100%;
  list-style: none;
}
#copy_button {
  width: 50px;
  height: 25px;
  margin-top: 10px;
  outline: none;
  border-radius: 4px;
  border: none;
  background-color: #2d8cf0;
  color: #fff;
  cursor: pointer;
}
#copy_button:hover {
  background: #57a3f3;
}
</style>
