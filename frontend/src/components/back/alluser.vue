<template>
    <div>
        <Input v-model="phone_number" placeholder="请输入待搜索用户的手机号" id="search" />
        <Button @click="search()">搜索</Button>
        <Table border stripe :columns="columns1" :data="data1"></Table>
        <Page :total="amount_of_users" :page-size="10" :current="1" @on-change="changePage">
    </div>
</template>
<script>
export default {
  data() {
    return {
      phone_number: '',
      columns1: [
        {
          title: '手机号',
          key: 'phone_number'
        },
        {
          title: '昵称',
          key: 'user_name'
        },
        {
          title: '奖励金',
          key: 'welfare'
        },
        {
          title: '是否能发言',
          key: 'Can_comment'
        },
        {
          title: '是否为大V',
          key: 'Is_teacher'
        },
        {
          title: '操作',
          key: 'action',
          width: 150,
          align: 'center',
          render: (h, params) => {
            return h('div', [
              h(
                'Button',
                {
                  props: {
                    type: 'primary',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      this.go_to_edit(params.index)
                    }
                  }
                },
                '去管理'
              ),
              h(
                'Button',
                {
                  props: {
                    type: 'error',
                    size: 'small'
                  },
                  on: {
                    click: () => {
                      this.remove(params.index)
                    }
                  }
                },
                '删除'
              )
            ])
          }
        }
      ],
      data1: [],
      all_data: [],
      amount_of_users: 0,
      currentPage: 1
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
          if (res.manager.Manage_user !== true) {
            alert('你没有权限访问该网页！')
            location.href = '/#/backstage'
          } else {
            this.$http
              .post('http://192.168.55.33:8000/app/get_all_users')
              .then(response => {
                var res = response.data
                this.all_data = res.users
                this.amount_of_users = this.all_data.length
                console.log(this.amount_of_users)
                if (this.amount_of_users <= 10) {
                  this.data1 = this.all_data
                } else {
                  for (var i = 0; i < 10; i++) {
                    this.data1.push(this.all_data[i])
                  }
                }
                console.log(this.data1)
              })
          }
        }
      })
  },
  methods: {
    changePage(currentPage) {
      var left = this.amount_of_users - (currentPage - 1) * 10
      var arr = []
      if (left <= 10) {
        for (var j = (currentPage - 1) * 10; j < this.amount_of_users; j++) {
          arr.push(this.all_data[j])
        }
      } else {
        for (
          var k = (currentPage - 1) * 10;
          k < (currentPage - 1) * 10 + 10;
          k++
        ) {
          arr.push(this.all_data[k])
        }
      }
      this.data1 = arr
      console.log(this.data1)
    },
    search() {
      var phoneNumber = JSON.stringify(this.phone_number)
      this.$http
        .post('http://192.168.55.33:8000/app/search_user', phoneNumber)
        .then(response => {
          var res = response.data
          var arr = []
          if (res.is_null === false) {
            var user = res.user_info
            arr.push(user)
            this.amount_of_users = 1
          } else {
            this.amount_of_users = 0
          }
          this.all_data = arr
          this.data1 = arr
        })
    },
    go_to_edit(index) {
      this.$router.push({
        name: 'user',
        params: { phone_number: this.data1[index].phone_number }
      })
    },
    remove(index) {
      this.$http
        .post(
          'http://192.168.55.33:8000/app/delete_user',
          JSON.stringify(this.data1[index].phone_number)
        )
        .then(response => {
          alert('删除手机号为' + this.data1[index].phone_number + '的用户！')
        })
      this.data1.splice(index, 1)
    }
  }
}
</script>
<style scoped>
#search {
  width: 300px;
}
</style>
