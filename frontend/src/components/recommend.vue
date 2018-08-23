<template>
    <div id="recommendCourse">
        <!-- 免费推荐课程 -->
        <div v-for="item of free_course" :key="item.id">
            <img v-bind:src= 'item.fields.Cover_picture'/>
            课程标题：{{item.fields.title}}
        </div>
        <!-- 付费推荐课程 -->
        <div v-for="item of paying_course" :key="item.id">
            <img v-bind:src= 'item.fields.Cover_picture'/>
            课程标题：{{item.fields.title}}
        </div>
    </div>
</template>
<script>
export default {
  data() {
    return {
      imgs: [],
      free_course: [],
      paying_imgs: [],
      paying_course: [],
      show_number: 3,// 设定主页要显示的图片数量
      path: []
    }
  },
  mounted: function() {
    this.show_free_course()
    this.show_paying_course()
  },
  methods: {
    show_free_course: function() {
      this.$http.get('http://192.168.55.33:8000/app/show_free_course').then(
        response => {
          this.imgs = response.data.list
          console.log('success')
          for (var i = 0; i < this.imgs.length; i = i + 1) {
            var a =
              'http://192.168.55.33:8000/media/' +
              this.imgs[i].fields.Cover_picture
            this.imgs[i].fields.Cover_picture = a
          }
          var length = 0
          if (this.imgs.length > this.show_number) length = this.show_number
          else length = this.imgs.length
          this.free_course = this.imgs.slice(0, length)
          console.log('success')
        },
        response => {
          console.log('error')
        }
      )
    },
    show_paying_course: function() {
      this.$http.get('http://192.168.55.33:8000/app/show_paying_course').then(
        response => {
          this.paying_imgs = response.data.list
          console.log('success')
          for (var i = 0; i < this.paying_imgs.length; i = i + 1) {
            var a =
              'http://192.168.55.33:8000/media/' +
              this.paying_imgs[i].fields.Cover_picture
            this.paying_imgs[i].fields.Cover_picture = a
          }
          var length = 0
          if (this.paying_imgs.length > this.show_number) length = this.show_number
          else length = this.paying_imgs.length
          this.paying_course = this.paying_imgs.slice(0, length)
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
