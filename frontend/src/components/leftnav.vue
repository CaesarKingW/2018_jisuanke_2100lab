<template>
  <div  class="leftnav">
      <nav>
        <ul>
          <li class="line">课程处理</li>
          <li class="line">留言管理</li>
          <li class="line">用户管理</li>
          <li class="line">订单处理</li>
          <li class="line">数据统计</li>
          <li class="line">权限等级</li>
          <li class="line">后台操作历史查看</li>
        </ul>
      </nav>
  </div>
</template>

<script>

export default {
  name: 'leftnav',
  data() {
    return {

    }
  }
}
</script>

<style scopeds>
.leftnav {
  float: left;
  width: 231px;
  height: 410px;
  background-color: #5cadff;
}

.line {
  position: relative;
  height: 59px;
  font-size: 16px;
  line-height: 59px;
  color: #fff;
  border-bottom: 1px solid #fff;
}
</style>
