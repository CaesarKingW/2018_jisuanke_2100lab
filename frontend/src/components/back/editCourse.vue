<template>
  <div>
    <Input v-model="word" placeholder="输入课程标题关键字以搜索课程" id="word" />
    <Button @click="search()">搜索</Button>
    <Table border stripe :columns="columns1" :data="data1"></Table>
    <Page :total="amount_of_courses" :page-size="10" :current="1" @on-change="changePage">
  </div>
</template>
<script>
export default {
  name: 'editCourse',
  data() {
    return {
      word: '',
      columns1: [
        {
          title: '课程id',
          key: 'id'
        },
        {
          title: '标题',
          key: 'title'
        },
        {
          title: '简介',
          key: 'brief_introduction'
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
                '去编辑'
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
      amount_of_courses: 0,
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
          if (res.manager.Manage_course !== true) {
            alert('你没有权限访问该网页！')
            location.href = '/#/backstage'
          } else {
            this.$http
              .post('http://192.168.55.33:8000/app/get_all_courses')
              .then(response => {
                var res = response.data
                this.all_data = res.courses
                this.amount_of_courses = this.all_data.length
                console.log(this.amount_of_courses)
                if (this.amount_of_courses <= 10) {
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
      var left = this.amount_of_courses - (currentPage - 1) * 10
      var arr = []
      if (left <= 10) {
        for (var j = (currentPage - 1) * 10; j < this.amount_of_courses; j++) {
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
        .post('http://192.168.55.33:8000/app/search_course', word)
        .then(response => {
          var res = response.data
          this.all_data = res.courses
          this.amount_of_courses = this.all_data.length
          var arr = []
          if (this.amount_of_courses <= 10) {
            arr = this.all_data
          } else {
            for (var i = 0; i < 10; i++) {
              arr.push(this.all_data[i])
            }
          }
          this.data1 = arr
        })
    },
    go_to_edit(index) {
      this.$router.push({
        name: 'realEdit',
        params: { id: this.data1[index].id }
      })
    },
    remove(index) {
      this.$http
        .post(
          'http://192.168.55.33:8000/app/delete_course',
          JSON.stringify(this.data1[index].id)
        )
        .then(response => {
          alert('删除第' + this.data1[index].id + '号课程！')
        })
      this.data1.splice(index, 1)
    }
  }
}
</script>
<style scoped>
#word {
  width: 300px;
}
</style>
