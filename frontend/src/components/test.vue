<template>
  <body>
    <div>
      <input type="file" name="file" id="file_upload"/>
      <input type="button" value="上传" v-on:click="FileUpload"/>
    </div>
    <img v-bind:src= path />
    <img >
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
      this.$http.get('http://192.168.55.33:8000' + '/app/show_picture').then(
        response => {
          this.img = response.data.img
          this.path =
            'http://192.168.55.33:8000' +
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
        .post('http://192.168.55.33:8000' + '/app/add_picture', formdate, config)
        .then(response => {
        })
    }
  }
}
</script>
