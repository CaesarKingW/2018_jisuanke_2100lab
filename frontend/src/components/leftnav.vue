<template>
  <div class="leftnav">
    <nav>
      <ul>
        <router-link to="/backstage/course" exact>
          <li class="line">课程处理</li>
        </router-link>
        <router-link to="/backstage/comment" exact>
          <li class="line">留言管理</li>
        </router-link>
        <router-link to="/backstage/user" exact>
          <li class="line">用户管理</li>
        </router-link>
        <router-link to="/backstage/order" exact>
          <li class="line">订单处理</li>
        </router-link>
        <router-link to="/backstage/data" exact>
          <li class="line">数据统计</li>
        </router-link>
        <router-link to="/backstage/authority" exact>
          <li class="line">权限等级</li>
        </router-link>
        <router-link to="/backstage/log" exact>
          <li class="line">后台操作历史查看</li>
        </router-link>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'leftnav',
  data() {
    return {}
  }
}
</script>

<style scoped>
.router-link-active {
  font-size: 20px;
}

.leftnav {
  float: left;
  width: 231px;
  height: 410px;
  font-size: 16px;
  color: #fff;
  background-color: #5cadff;
}

.line {
  position: relative;
  height: 59px;
  line-height: 59px;
  color: #fff;
  border-bottom: 1px solid #fff;
}
</style>
