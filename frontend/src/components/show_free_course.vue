<template>
    <div id="freeCourse">
        <div v-for="item of imgs" :key="item.id">
            <img v-bind:src= 'item.fields.Cover_picture'/>
            课程标题：{{item.fields.title}}
            课程简介：{{item.fields.brief_introduction}}
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
      this.$http.get('http://192.168.55.33:8000' + '/app/show_free_course').then(
        response => {
          this.imgs = response.data.list
          for (var i = 0; i < this.imgs.length; i = i + 1) {
            var a =
              'http://192.168.55.33:8000' +
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
