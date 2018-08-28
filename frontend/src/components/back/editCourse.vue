<template>
<div>
<Input v-model="word" placeholder="输入课程标题关键字以搜索课程" style="width: 300px" />
<Button @click="search()">搜索</Button>
<Table border stripe :columns="columns1" :data="data1"></Table>
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
      data1: []
    }
  },
  methods: {
    search() {
      var word = JSON.stringify(this.word)
      this.$http
        .post('http://192.168.55.33:8000/app/search_course', word)
        .then(response => {
          var res = response.data
          this.data1 = res.courses
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
          var res = response.data
        })
      this.data1.splice(index, 1)
    }
  }
}
</script>
<style>
</style>
