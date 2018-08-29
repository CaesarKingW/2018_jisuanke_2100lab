<template>

  <body>
    <!-- <form action="http://192.168.55.33/app/add_picture" method="post" enctype="multipart/form-data">
        <input type="file" name="fafafa">
        <input type="submit">
    </form> -->
    <div>
      <input type="file" name="file" id="file_upload" />
      <input type="button" value="上传" v-on:click="FileUpload" />
    </div>
    <img v-bind:src=p ath />
    <img>
  </body>
</template>
<script>
export default {
  data() {
    return {
      img: [],
      path: ''
    }
  },
  mounted: function() {
    this.show_picture()
  },
  methods: {
    show_picture: function() {
      this.$http.get(this.GLOBAL.serverSrc + '/app/show_picture').then(
        response => {
          this.img = response.data.img
          this.path =
            this.GLOBAL.serverSrc +
            '/media/' +
            this.img[0].fields.course_picture
        },
        response => {}
      )
    },
    FileUpload: function() {
      var formdate = new FormData()
      var fileinfo = document.querySelector('input[type=file]').files[0]
      formdate.append('file', fileinfo)
      let config = { headers: { 'Content-Type': 'multipart/form-data' } }
      this.$http
        .post(this.GLOBAL.serverSrc + '/app/add_picture', formdate, config)
        .then(response => {})
    }
  }
}
</script>
