<template>
  <div class="ModifyUserInfo" style="background-color: #c4e1ff;">
    <div><img id="avatar" src="../assets/little_avatar.png"></div>
    <div>
      <Button style="margin: 10px;" size="large" type="primary">上传头像</Button>
    </div>
    <div id="nickname">昵称：
      <Input prefix="ios-contact" placeholder="请输入昵称" style="width: auto" />
    </div>
    <Button type="primary" style="margin: 10px;" size="large" @click="modal = true">确认修改</Button>
    <Modal v-model="modal" title="修改信息" @on-ok="ok" @on-cancel="cancel">
      <p>恭喜你，个人信息修改成功！</p>
    </Modal>
  </div>
</template>
<script>
export default {
  data() {
    return {
      modal: false
    }
  },
  methods: {
    ok() {
      this.$Message.info('Clicked ok')
    },
    cancel() {
      this.$Message.info('Clicked cancel')
    }
  }
}
</script>
<style scoped>
.ModifyUserInfo {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#avatar {
  border: #9cf solid 5px;
  border-radius: 20px;
  margin: 10px;
}

#nickname {
  font-size: 20px;
  margin: 30px;
}
</style>
