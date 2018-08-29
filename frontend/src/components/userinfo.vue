<template>
  <div id="userInfo">
    <div>
      <img v-bind:src="path" class="imgDiv" /><img> 昵称：{{nickname}} 奖励金数：{{amount_of_money}}
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      path: '',
      nickname: '',
      amount_of_money: 0,
      user_phone: '17602284691'
    }
  },
  mounted: function() {
    this.$http
      .post(
        this.GLOBAL.serverSrc + 'app/get_user_information',
        JSON.stringify(this.user_phone)
      )
      .then(
        response => {
          var obj = []
          obj = response.data.list
          this.path =
            this.GLOBAL.serverSrc + '/media/' + obj[0].fields.head_protrait
          this.nickname = obj[0].fields.user_name
          this.amount_of_money = obj[0].fields.welfare
        },
        response => {}
      )
  },
  methods: {}
}
</script>
