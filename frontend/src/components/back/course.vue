<template>
  <section>
    <div class="front">
      <form>
        课程名：
        <input type="text" name="course_name">
        <button type="primary">搜索</button>
      <Button type="primary" @click="modal1 = true">创建课程</Button>
      <Modal
        v-model="modal1"
        title="课程添加"
        @on-ok="ok"
        @on-cancel="cancel">
        <Form>
          <FormItem label="标题">
            <Input/>
          </FormItem>
          <FormItem label="简介">
            <Input/>
          </FormItem>
          <FormItem label="添加图片">
            <Button type="primary">浏览..</Button>
          </FormItem>
          <FormItem label="添加音频">
            <Button type="primary">浏览..</Button>
          </FormItem>
          <FormItem label="添加介绍">
            <Input type="textarea" :autosize="true" />
          </FormItem>
          <FormItem label="课程属性"/>
          <FormItem>
            <Radio label="apple">
            <span>阅后即焚</span>
            <span>时间</span>
            <Input/>
            </Radio>
          </FormItem>
          <FormItem>
            <Radio label="apple">
            <span>是否付费</span>
            <span>价格</span>
            <Input/>
            </Radio>
          </FormItem>
          <FormItem>
            <Radio label="是否允许留言">
            <span>是否允许留言</span>
            </Radio>
          </FormItem>
        </Form>
      </Modal>
      </form>
    </div>
    <div class="front">
      <Page :total="100" />
    </div>
  </section>
</template>

<script>
import courseblock from './courseblock'

export default {
  name: 'course',
  data() {
    return {
      course: [],
      block: 5,
      modal1: false
    }
  },
  components: {
    courseblock
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
