<style scoped>
.layout {
  position: relative;
  overflow: hidden;
  background: #f5f7f9;
  border: 1px solid #d7dde4;
  border-radius: 4px;
}

#text {
  margin-bottom: 5px;
  margin-left: 5px;
  color: white;
}

.layout-nav {
  float: right;
  color: white;
}
</style>
<template>
  <div class="layout">
    <Layout>
      <Header>
        <span id="text">2100实验室</span>
        <span class="layout-nav">{{username}}/
          <Button @click="logout()" type="text" ghost>登出</span>
      </Header>
      <Layout>
        <Sider hide-trigger :style="{background: '#fff'}">
          <Menu active-name="1-2" theme="light" width="auto" :open-names="['1']">
            <Submenu name="1" v-if="course">
              <template slot="title">
                <Icon type="ios-navigate"></Icon>
                课程处理
              </template>
              <MenuItem name="1-1" to="/backstage/addCourse">新建课程</MenuItem>
              <MenuItem name="1-2" to="/backstage/editCourse">编辑课程</MenuItem>
            </Submenu>
            <MenuItem name="2" to="/backstage/user" v-if="user">
            <Icon type="md-contact" /> 用户管理
            </MenuItem>
            <MenuItem name="3" to="/backstage/comment" v-if="message">
            <Icon type="ios-chatboxes" /> 留言管理
            </MenuItem>
            <MenuItem name="4" to="/backstage/order" v-if="order">
            <Icon type="ios-keypad"></Icon>
            订单处理
            </MenuItem>
            <MenuItem name="5" to="/backstage/data">
            <Icon type="md-analytics" /> 数据统计
            </MenuItem>
            <MenuItem name="6" to="/backstage/authority" v-if="authority">
            <Icon type="md-bookmark" /> 权限设置
            </MenuItem>
            <MenuItem name="7" to="/backstage/operatingHistory">
            <Icon type="ios-time" /> 操作历史
            </MenuItem>
          </Menu>
        </Sider>
        <Layout :style="{padding: '0 24px 24px'}">
          <Content :style="{padding: '24px', minHeight: '280px', background: '#fff'}">
            <router-view/>
          </Content>
        </Layout>
      </Layout>
    </Layout>
  </div>
</template>
<script>
export default {
  data() {
    return {
      mis_login: false,
      username: null,
      course: false,
      user: false,
      order: false,
      message: false,
      authority: false
    }
  },
  created: function() {
    this.$http
      .post('http://192.168.55.33:8000/app/get_mstatus')
      .then(response => {
        var res = response.data
        this.mis_login = res.mis_login
        if (!this.mis_login) {
          alert('还没有登录，无权访问该页面！')
          location.href = '/#/backstageLogin'
        } else {
          this.username = res.manager.username
          this.course = res.manager.Manage_course
          this.user = res.manager.Manage_user
          this.order = res.manager.Manage_order
          this.message = res.manager.Manage_message
          this.authority = res.manager.Supermanager
        }
      })
  },
  methods: {
    logout() {
      this.$http
        .post('http://192.168.55.33:8000/app/backstage_logout')
        .then(response => {
          alert('登出成功！')
          location.href = '/#/backstageLogin'
        })
    }
  }
}
</script>
