<template>
  <div>
    <Table stripe :columns="columns1" :data="data1"></Table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      username: '',
      columns1: [
        {
          title: '操作类型',
          key: 'operate_type'
        },
        {
          title: '操作对象',
          key: 'object_type'
        },
        {
          title: '操作时间',
          key: 'created_at'
        }
      ],
      data1: []
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
          this.$http
            .post('http://192.168.55.33:8000/app/search_history')
            .then(response => {
              var resp = response.data
              this.data1 = resp.history
            })
        }
      })
  }
}
</script>
