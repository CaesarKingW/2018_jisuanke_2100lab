<template>
  <section>
    <div class="front">
      <form>
        订单号：
        <input type="text" name="course_name">
        <button type="button">搜索</button>
      </form>
    </div>
    <div class="front">
      <Page :total="100" />
    </div>
  </section>
</template>

<script>

export default {
  name: 'order',
  data() {
    return {
      course: [],
      block: 5
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
