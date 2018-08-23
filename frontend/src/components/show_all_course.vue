<template>
    <div id="allCourse">
        <div v-for="item of path" :key="item.id">
            <img v-bind:src= 'item'/>
        </div>
    </div>
</template>
<script>
export default {
  data() {
    return {
      imgs: [],
      path: [],
    }
  },
  mounted: function() {
    this.show_all_course()
  },
  methods: {
    show_all_course: function() {
      this.$http.get('http://192.168.55.33:8000/app/show_all_course').then(
        response => {
          this.imgs = response.data.list
          console.log('success')

          for (var i = 0; i < this.imgs.length; i = i + 1) {
            var a =
              'http://192.168.55.33:8000/media/' +
              this.imgs[i].fields.Cover_picture
            this.path.push(a)
          }
          console.log(this.path.length)
          console.log(this.path)
        },
        response => {
          console.log('error')
        }
      )
    }
  }
}
</script>
