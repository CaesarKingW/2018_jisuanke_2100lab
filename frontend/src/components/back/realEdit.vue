<template>
<Tabs value="name1">
        <TabPane label="音画同步" name="name1">
            音画同步
        </TabPane>
        <TabPane label="其他" name="name2">
            <Form :model="formItem" :label-width="150">
                <FormItem label="标题"><Input v-model="formItem.title"/></FormItem>
                <FormItem label="简介"><Input v-model="formItem.brief_introduction" type="textarea"/></FormItem>
                <FormItem label="详解"><div><p>当前：<a :href="formItem.oldWI" target="_blank">（当前详解）</a></p><p>修改：<input type=file id="newWI"/></p></div></FormItem>
                <FormItem label="课程封面："><p>当前：<a :href=formItem.oldCP target="_blank">（当前封面）</a></p><p>修改：<input type=file id="newCP"/></p></FormItem>
                <FormItem label="是否阅后即焚:"><i-switch v-model="formItem.Is_destroy"></i-switch></FormItem>
                <FormItem label="可阅时长：" v-if="this.formItem.Is_destroy"><InputNumber v-model="formItem.distroy_time"/>小时</FormItem>
                <FormItem label="价格"><InputNumber v-model="formItem.price"/>元</FormItem>
                <FormItem label="分销比例" v-if="formItem.price>0"><InputNumber :max="100" v-model="formItem.share_rate" :formatter="value => `${value}%`" :parser="value => value.replace('%', '')"/></FormItem>
                <FormItem label="允许用户留言"><i-switch v-model="formItem.can_comment"></i-switch></FormItem>
                <FormItem><Button type="primary" @click="save_modify()">保存修改</Button></FormItem>
            </Form>
        </TabPane>
</Tabs>
</template>
<script>
export default {
  data() {
    return {
      id: null,
      formItem: {
        title: '',
        brief_introduction: '',
        oldCP: '',
        oldWI: '',
        Is_destroy: null,
        distroy_time: null,
        price: null,
        share_rate: null,
        can_comment: null
      }
    }
  },
  created: function() {
    this.id = this.$route.params.id
    console.log(this.id)
    this.$http
      .post(
        'http://192.168.55.33:8000/app/search_one_course',
        JSON.stringify(this.id)
      )
      .then(response => {
        var res = response.data
        console.log(response.data)
        this.formItem.title = res.course['title']
        this.formItem.brief_introduction = res.course['brief_introduction']
        this.formItem.oldCP =
          'http://192.168.55.33:8000' + res.course['Cover_picture']
        this.formItem.oldWI =
          'http://192.168.55.33:8000' + res.course['whole_introduction']
        this.formItem.Is_destroy = res.course['Is_destroy']
        this.formItem.distroy_time = res.course['distory_time']
        this.formItem.price = res.course['price']
        this.formItem.share_rate = res.course['share_rate'] * 100
        this.formItem.can_comment = res.course['can_comment']
      })
  },
  methods: {
    save_modify() {
      var formData = new FormData()
      formData.append('id', this.id)
      formData.append('title', this.formItem.title)
      formData.append('brief_introduction', this.formItem.brief_introduction)
      formData.append(
        'whole_introduction',
        document.getElementById('newWI').files[0]
      )
      formData.append(
        'Cover_picture',
        document.getElementById('newCP').files[0]
      )
      formData.append('Is_destroy', this.formItem.Is_destroy)
      if (this.formItem.Is_destroy === true) {
        formData.append('distroy_time', this.formItem.distroy_time)
      }
      formData.append('price', this.formItem.price)
      if (this.formItem.price > 0) {
        formData.append('share_rate', this.formItem.share_rate)
      }
      formData.append('can_comment', this.formItem.can_comment)
      this.$http
        .post('http://192.168.55.33:8000/app/editCourse', formData)
        .then(response => {
          console.log(response.data)
        })
    }
  }
}
</script>
<style>
</style>
