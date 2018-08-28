<template>
<div id="LearntCourse">
    <div>
        <table >
            <tr>
                <th>序号</th>
                <th>课程编号</th>
                <th>课程标题</th>
                <th>开始学习时间</th>
                <th>学习进度</th>
            </tr>
            <tr v-for="(item, index) of takes" :key="item">
                <td>
                    {{index + 1}}
                </td>
                <td>
                    {{item.course_id}}
                </td>
                <td>
                    {{item.course_title}}
                </td>
                <td>
                    {{item.start_time}}
                </td>
                <td>
                    {{(item.max_study_percent/item.course_duration).toFixed(2)}}
                </td>
            </tr>
        </table>
    </div>
</div>
</template>
<script>
export default {
  data() {
    return {
      takes: [],
      userPhone: ''
    }
  },
  mounted: function() {
    this.$http.post(this.GLOBAL.serverSrc + '/app/get_status').then(response => {
      this.userPhone = response.data.list[0].pk
      this.show_takes()
    })
  },
  methods: {
    show_takes: function() {
      this.$http
        .post(
          this.GLOBAL.serverSrc + '/app/show_takes',
          JSON.stringify(this.userPhone)
        )
        .then(
          response => {
            this.takes = response.data.list
            console.log('success')
          },
          response => {
            console.log('error')
          }
        )
    }
  }
}
</script>
