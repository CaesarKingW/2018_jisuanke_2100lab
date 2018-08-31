<template>
    <div>
        <p><Input v-model="word" placeholder="请输入待搜索留言的关键字" id="search"/>
        <Button @click="search()">搜索</Button></p>
        <Table border stripe :columns="columns1" :data="data1"></Table>
        <Page :total="amount_of_users" :page-size="10" :current="1" @on-change="changePage">
    </div>
</template>
<script>
export default {
  data() {
    return {
      word: '',
      columns1: [
        {
          title: '留言ID',
          key: 'id'
        },
        {
          title: '用户手机号码',
          key: 'user_phone'
        },
        {
          title: '课程标题',
          key: 'course_title'
        },
        {
          title: '用户昵称',
          key: 'user_name'
        },
        {
          title: '课程ID',
          key: 'course_id'
        },
        {
          title: '留言内容',
          key: 'content'
        },
        {
          title: '留言时间',
          key: 'created_at'
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
      amount_of_messages: 0,
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
              .post('http://192.168.55.33:8000/app/get_all_messages')
              .then(response => {
                var res = response.data
                this.all_data = res.messages
                this.amount_of_messages = this.all_data.length
                if (this.amount_of_messages <= 10) {
                  this.data1 = this.all_data
                } else {
                  for (var i = 0; i < 10; i++) {
                    this.data1.push(this.all_data[i])
                  }
                }
              })
          }
        }
      })
  },
  methods: {
    changePage(currentPage) {
      var left = this.amount_of_messages - (currentPage - 1) * 10
      var arr = []
      if (left <= 10) {
        for (var j = (currentPage - 1) * 10; j < this.amount_of_messages; j++) {
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
      var word = JSON.stringify(this.word)
      this.$http
        .post('http://192.168.55.33:8000/app/search_comment', word)
        .then(response => {
          var res = response.data
          this.all_data = res.messages
          this.amount_of_courses = this.all_data.length
          var arr = []
          if (this.amount_of_messages <= 10) {
            arr = this.all_data
          } else {
            for (var i = 0; i < 10; i++) {
              arr.push(this.all_data[i])
            }
          }
          this.data1 = arr
        })
    },
    remove(index) {
      this.$http
        .post(
          'http://192.168.55.33:8000/app/delete_comment',
          JSON.stringify(this.data1[index].id)
        )
        .then(response => {
          alert('ID为' + this.data1[index].id + '的留言删除成功！')
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
