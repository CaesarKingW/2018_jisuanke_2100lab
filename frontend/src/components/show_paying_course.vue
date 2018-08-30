<template>
  <div id="payingCourse">
    <div v-for="item of imgs" :key="item.id">
      <img v-bind:src='item.fields.Cover_picture' /> 课程标题：{{item.fields.title}} 课程简介：{{item.fields.brief_introduction}} 课程价格：{{item.fields.price}}
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      imgs: [],
      path: []
    }
  },
  mounted: function() {
    this.show_all_course()
  },
  methods: {
    show_all_course: function() {
      this.$http.get(this.GLOBAL.serverSrc + '/app/show_paying_course').then(
        response => {
          this.imgs = response.data.list
          for (var i = 0; i < this.imgs.length; i = i + 1) {
            var a =
              this.GLOBAL.serverSrc +
              '/media/' +
              this.imgs[i].fields.Cover_picture
            this.imgs[i].fields.Cover_picture = a
          }
        },
        response => {}
      )
    }
  }
}
</script>
