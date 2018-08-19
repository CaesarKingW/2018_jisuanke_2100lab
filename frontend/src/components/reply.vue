
<template>
<div id="reply">
    <div v-for="r of replies" :key="r.key">
              <h5>
                 &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;{{r.fields.user_phone}}
              </h5>
              <h4>
                  &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;{{r.fields.content}}
              </h4>
          </div>
</div>
</template>
<script>
export default {
  props: ['title'],
  data: function() {
    return {
      replies: []
    }
  },
  mounted: function() {
    this.$http
      .post(
        'http://192.168.55.33:8000/app/show_reply',
        JSON.stringify(this.title)
      )
      .then(
        response => {
          this.replies = response.data.list
          console.log('success')
        },
        response => {
          console.log('error')
        }
      )
  }
}
</script>
