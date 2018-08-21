<template>
  <section>
    <div class="front">
      <form>
        用户id：
        <input type="text" name="course_name" v-model="phone_number">
        <button type="button" @click="search_user_comment">搜索</button>
      </form>
    </div>
    <div class="front">
      <Page :total="100" />
    </div>
  </section>
</template>

<script>
export default {
  name: 'comment',
  data() {
    return {
      phone_number: ''
    }
  },
  methods: {
    search_user_comment() {
      console.log(this.phone_number)
      // eslint-disable-next-line
      var phone_number = JSON.stringify(this.phone_number)
      this.$http.post('http://192.168.55.33:8000/app/user_comment', phone_number)
        .then(response => {
          console.log(response.data)
        })
    }
  }
}
</script>

<style scoped>
.front {
  position: static;
  padding-top: 50px;
  padding-bottom: 400px;
  padding-left: 400px;
  font-size: 20px;
}

</style>
