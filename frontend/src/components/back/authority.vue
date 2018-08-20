<template>
  <section>
    <div class="front">
      <form>
        用户id：
        <input type="text" name="course_name">
        <button type="button">搜索</button>
      </form>
    </div>
    <div class="front">
      <input type="checkbox" id="jack" value="Jack">
      <label for="jack">课程处理权限</label>
      <br>
      <input type="checkbox" id="john" value="John">
      <label for="john">留言管理权限</label>
      <br>
      <input type="checkbox" id="mike" value="Mike">
      <label for="mike">用户管理权限</label>
      <br>
      <input type="checkbox" id="1" value="1">
      <label for="1">订单处理权限</label>
      <br>
      <input type="checkbox" id="2" value="2">
      <label for="2">后台操作历史权限</label>
      <br>
      <br>
      <br>
      <Button type="primary" @click="modal1 = true">确定</Button>
      <Modal
        v-model="modal1"
        title="提示"
        @on-ok="ok"
        @on-cancel="cancel">
        <p>管理员权限修改完成！</p>
    </Modal>
    </div>
  </section>
</template>

<script>

export default {
  name: 'authority',
  data() {
    return {
      modal1: false
    }
  },
  methods: {
    ok () {
      this.$Message.info('Clicked ok')
    },
    cancel () {
      this.$Message.info('Clicked cancel')
    }
  }
}
</script>

<style scoped>
.front {
  position: static;
  padding-top: 50px;
  padding-bottom: 10px;
  padding-left: 400px;
  font-size: 20px;
}

</style>
