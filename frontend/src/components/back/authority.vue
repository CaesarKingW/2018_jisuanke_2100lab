<template>
  <section class="front">
    <div >
      <Form>
        <FormItem>
          管理员账号:
          <Input v-model="managername" style="width: 200px;"/>
          <Button type="primary" @click="search_auth()">搜索</Button>
        </FormItem>
      </Form>
    </div>
    <Form :model="arrtibute" v-if="auth_page">
      <Divider orientation="left" style="width: 400px;">管理员{{arrtibute.managername}}的权限</Divider>
      <FormItem>
        <Checkbox v-model="arrtibute.super"></Checkbox>
        <span>权限赋予权限</span>
        <br>
        <Checkbox v-model="arrtibute.course"></Checkbox>
        <span>课程处理权限</span>
        <br>
        <Checkbox v-model="arrtibute.message"></Checkbox>
        <span>留言管理权限</span>
        <br>
        <Checkbox v-model="arrtibute.user"></Checkbox>
        <span>用户管理权限</span>
        <br>
        <Checkbox v-model="arrtibute.order"></Checkbox>
        <span>订单处理权限</span>
        <br>
      </FormItem>
      <br>
      <Button type="primary" @click="change_manager()">确定</Button>
      <Modal
        v-model="modal1"
        title="提示">
        <p>管理员权限修改完成！</p>
    </Modal>
    </Form>
    <div v-else>
      <p>无此用户</p>
    </div>
  </section>
</template>

<script>
export default {
  name: 'authority',
  data() {
    return {
      modal1: false,
      auth_page: false,
      managername: '',
      arrtibute: {
        managername: '',
        super: false,
        course: false,
        message: false,
        user: false,
        order: false
      }
    }
  },
  methods: {
    search_auth() {
      this.arrtibute.managername = this.managername
      // eslint-disable-next-line
      var managername = JSON.stringify(this.managername)
      this.$http
        .post('http://192.168.55.33:8000/app/manager_search', managername)
        .then(response => {
          console.log(response.data)
          if (response.data['data'] !== 'false') {
            this.auth_page = true
            this.arrtibute.managername = response.data.username
            this.arrtibute.super = response.data.Supermanager
            this.arrtibute.course = response.data.Manage_course
            this.arrtibute.message = response.data.Manage_message
            this.arrtibute.user = response.data.Manage_user
            this.arrtibute.order = response.data.Manage_order
          } else {
            this.auth_page = false
          }
        })
    },
    change_manager() {
      var managerprops = JSON.stringify(this.arrtibute)
      this.$http
        .post('http://192.168.55.33:8000/app/manager_change', managerprops)
        .then(response => {
          console.log(response.data)
        })
      this.modal1 = true
    }
  }
}
</script>

<style scoped>
.front {
  float: left;
  padding-top: 5%;
  padding-bottom: 10px;
  padding-left: 10%;
  font-size: 20px;
}
</style>
